General
-------

- Drop all uses of `optional` (is this part of `proto2->proto3`?)

`datastore.proto`
-----------------

- Rename `DatastoreService` as `Datastore`
- URI changes
  -           Lookup: `/v1beta3/projects/{project_id}:lookup`
  -         RunQuery: `/v1beta3/projects/{project_id}:runQuery`
  - BeginTransaction: `/v1beta3/projects/{project_id}:beginTransaction`
  -           Commit: `/v1beta3/projects/{project_id}:commit`
  -         Rollback: `/v1beta3/projects/{project_id}:rollback`
  -      AllocateIds: `/v1beta3/projects/{project_id}:allocateIds`
- `project_id` field added to
  - `LookupRequest`
  - `RunQueryRequest`
  - `BeginTransactionRequest`
  - `CommitRequest`
  - `RollbackRequest`
  - `AllocateIdsRequest`

  This isn't required over HTTP(S) since it comes through the URI.
- Rename `LookupRequest.key` to `LookupRequest.keys` (was and
  still is `repeated`)
- Grouped `RunQueryRequest.query|gql_query` into a `oneof` block
  (`oneof` is new to `proto3`)
- Added `RunQueryResponse.query` which gives back the parsed
  `GqlQuery` if it was set in the request
- Removed `BeginTransactionRequest.IsolationLevel|isolation_level`
- Removed `[default=**];` syntax (`proto2->proto3`?)
- Removed reference to `/* serialized Transaction */` in
  `BeginTransactionResponse.transaction`, `RollbackRequest.transaction`,
  `CommitRequest.transaction` and `ReadOptions.transaction`
- Adding `CommitRequest.Mode.MODE_UNSPECIFIED` enum value
- Rename `CommitRequest.mutation` to `CommitRequest.mutations`,
  was `optional` and now is `repeated`
- Added `CommitResponse.index_updates`. This was moved from `MutationResult`
  which used to hold a list of `insert_auto_id_key`s but now a
  `MutationResult` is a singular entry in `CommitRequest.mutations`
- Rename `AllocateIdsRequest.key` to `AllocateIdsRequest.keys` (was and
  still is `repeated`)
- Rename `AllocateIdsResponse.key` to `AllocateIdsResponse.keys` (was and
  still is `repeated`)
- Grouped `Mutation.insert|update|upsert|delete` into a `oneof` block
  (`oneof` is new to `proto3`) called `operation`
- Removed `Mutation.insert_auto_id` and `Mutation.force`
- As mentioned `MutationResult` goes from being a "plural" container
  to a "singular" container and loses `index_updates`
- Rename `ReadOptions.ReadConsistency.DEFAULT` to
  `ReadOptions.ReadConsistency.READ_CONSISTENCY_UNSPECIFIED`
- Grouped `ReadOptions.read_consistency|transaction` into a `oneof` block
  (`oneof` is new to `proto3`) called `consistency_type`

`entity.proto`
--------------

- Rename `PartitionId.dataset_id` to `PartitionId.project_id`
- Rename `PartitionId.namespace` to `PartitionId.namespace_id`
- Grouped `Key.PathElement.id|name` into a `oneof` block
  (`oneof` is new to `proto3`) called `id_type`
- Rename `Key.path_element` to `Key.path` (`repeated` in both)
- Added `ArrayValue` message class, which has a single field
  containing repeated `Value` (called `values`)
- Changes to `Value`:
  - Added `google.protobuf.NullValue null_value`
  - Changed `int64 timestamp_microseconds_value` to
    `google.protobuf.Timestamp timestamp_value`
  - Dropped `string blob_key_value`
  - Added `google.type.LatLng geo_point_value`
  - Renamed the (`repeated`) `Value list_value` as
    `ArrayValue array_value` (no longer repeated)
  - Rename `indexed` as `exclude_from_indexes` (still
    a `bool`)
  - Grouped `null_value`, `boolean_value`, `integer_value`,
    `double_value`, `timestamp_value`, `key_value`, `string_value`,
    `blob_value`, `geo_point_value`, `entity_value`,
    and `array_value` into a `oneof` called `value_type`
- Changed the (`repeated`) `Entity.property` (of message type
  `Property`) for a map: `map<string, Value>` called `Entity.properties`
- Dropped `Property` and `PropertyExpression` message types. The first
  (`Property`) has been obsoleted by the `map` (new to `proto3`) and
  the second (`PropertyExpression`) was only used as a projection in
  queries, so has been re-purposed elsewhere.

`query.proto`
-------------

- TBD
- `int32 index_updates` vs. `google.protobuf.Int32Value limit`?
