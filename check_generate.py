"""Checking that protobuf generated modules import correctly."""

from __future__ import print_function

import glob
import os


def main():
    """Import all PB2 files."""
    print('>>> import datastore_deps._generated')
    _ = __import__('datastore_deps._generated')
    pb2_files = sorted(glob.glob('datastore_deps/_generated/*pb2.py'))
    for filename in pb2_files:
        basename = os.path.basename(filename)
        module_name, _ = os.path.splitext(basename)

        print('>>> from datastore_deps._generated import ' + module_name)
        _ = __import__('datastore_deps._generated', fromlist=[module_name])


if __name__ == '__main__':
    main()
