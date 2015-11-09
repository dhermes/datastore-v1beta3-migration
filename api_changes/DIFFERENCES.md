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
- Drop all uses of `optional` (is this part of `proto2->proto3`?)
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

- TBD

`query.proto`
-------------

- TBD
- `int32 index_updates` vs. `google.protobuf.Int32Value limit`?
