"""Build script for rewriting imports for protobuf generated modules.

Intended to be used for Datastore protos (google/datastore/v1beta3)
and the dependent modules (google/ap, google/protobuf, and google/type).
"""

import glob


IMPORT_TEMPLATE = 'import %s'
IMPORT_FROM_TEMPLATE = 'from %s import '
PROTOBUF_IMPORT_TEMPLATE = 'from google.protobuf import %s '
REPLACE_PROTOBUF_IMPORT_TEMPLATE = 'from datastore_deps._generated import %s '
REPLACEMENTS = {
    'google.api': 'datastore_deps._generated',
    'google.datastore.v1beta3': 'datastore_deps._generated',
    'google.type': 'datastore_deps._generated',
}
GOOGLE_PROTOBUF_CUSTOM = (
    'struct_pb2',
    'timestamp_pb2',
    'wrappers_pb2',
)


def transform_old_to_new(line, old_module, new_module,
                         ignore_import_from=False):
    """Transforms from an old module to a new one.

    First checks if a line starts with
        "from {old_module} import ..."
    then checks if the line contains
        "import {old_module} ..."
    and finally checks if the line starts with (ignoring whitespace)
        "{old_module} ..."

    In any of these cases, "{old_module}" is replaced with "{new_module}".
    If none match, nothing is returned.

    :type line: str
    :param line: The line to be transformed.

    :type old_module: str
    :param old_module: The import to be re-written.

    :type new_module: str
    :param new_module: The new location of the re-written import.

    :type ignore_import_from: bool
    :param ignore_import_from: Flag to determine if the "from * import"
                               statements should be ignored.

    :rtype: :class:`str` or :data:`NoneType <types.NoneType>`
    :returns: The transformed line if the old module was found, otherwise
              does nothing.
    """
    if not ignore_import_from:
        import_from_statement = IMPORT_FROM_TEMPLATE % (old_module,)
        if line.startswith(import_from_statement):
            new_import_from_statement = IMPORT_FROM_TEMPLATE % (new_module,)
            # Only replace the first instance of the import statement.
            return line.replace(import_from_statement,
                                new_import_from_statement, 1)

    # If the line doesn't start with a "from * import *" statement, it
    # may still contain a "import * ..." statement.
    import_statement = IMPORT_TEMPLATE % (old_module,)
    if import_statement in line:
        new_import_statement = IMPORT_TEMPLATE % (new_module,)
        # Only replace the first instance of the import statement.
        return line.replace(import_statement,
                            new_import_statement, 1)

    # Also need to change references to the standalone imports. As a
    # stop-gap we fix references to them at the beginning of a line
    # (ignoring whitespace).
    if line.lstrip().startswith(old_module):
        # Only replace the first instance of the old_module.
        return line.replace(old_module, new_module, 1)


def transform_line(line):
    """Transforms an import line in a PB2 module.

    If the line is not an import of one of the packages in
    ``REPLACEMENTS`` or ``GOOGLE_PROTOBUF_CUSTOM``, does nothing and returns
    the original. Otherwise it replaces the package matched with our local
    package or directly rewrites the custom ``google.protobuf`` import
    statement.

    :type line: str
    :param line: The line to be transformed.

    :rtype: str
    :returns: The transformed line.
    """
    for old_module, new_module in REPLACEMENTS.iteritems():
        result = transform_old_to_new(line, old_module, new_module)
        if result is not None:
            return result

    for custom_protobuf_module in GOOGLE_PROTOBUF_CUSTOM:
        # We don't use the "from * import" check in transform_old_to_new
        # because part of `google.protobuf` comes from the installed
        # `protobuf` library.
        import_from_statement = PROTOBUF_IMPORT_TEMPLATE % (
            custom_protobuf_module,)
        if line.startswith(import_from_statement):
            new_import_from_statement = REPLACE_PROTOBUF_IMPORT_TEMPLATE % (
                custom_protobuf_module,)
            # Only replace the first instance of the import statement.
            return line.replace(import_from_statement,
                                new_import_from_statement, 1)

        old_module = 'google.protobuf.' + custom_protobuf_module
        new_module = 'datastore_deps._generated.' + custom_protobuf_module
        result = transform_old_to_new(line, old_module, new_module,
                                      ignore_import_from=True)
        if result is not None:
            return result

    # If no matches, there is nothing to transform.
    return line


def rewrite_file(filename):
    """Rewrites a given PB2 modules.

    :type filename: str
    :param filename: The name of the file to be rewritten.
    """
    with open(filename, 'rU') as file_obj:
        content_lines = file_obj.read().split('\n')

    new_content = []
    for line in content_lines:
        new_content.append(transform_line(line))

    with open(filename, 'w') as file_obj:
        file_obj.write('\n'.join(new_content))


def main():
    """Rewrites all PB2 files."""
    pb2_files = glob.glob('datastore_deps/_generated/*pb2.py')
    for filename in pb2_files:
        rewrite_file(filename)


if __name__ == '__main__':
    main()
