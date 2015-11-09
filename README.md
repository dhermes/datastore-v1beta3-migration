# Datastore `v1beta3` Migration Notes

Retrieving `.proto` Files
-------------------------

```bash
mkdir -p google/api
mkdir -p google/datastore/v1beta3
mkdir -p google/protobuf
mkdir -p google/type

cd google/api
wget https://raw.githubusercontent.com/google/googleapis/f66e425a93ca60ee49764bf97cbc3dd2efa97058/google/api/annotations.proto
wget https://raw.githubusercontent.com/google/googleapis/f66e425a93ca60ee49764bf97cbc3dd2efa97058/google/api/http.proto

cd ../../google/datastore/v1beta3
wget https://raw.githubusercontent.com/google/googleapis/f66e425a93ca60ee49764bf97cbc3dd2efa97058/google/datastore/v1beta3/datastore.proto
wget https://raw.githubusercontent.com/google/googleapis/f66e425a93ca60ee49764bf97cbc3dd2efa97058/google/datastore/v1beta3/entity.proto
wget https://raw.githubusercontent.com/google/googleapis/f66e425a93ca60ee49764bf97cbc3dd2efa97058/google/datastore/v1beta3/query.proto

cd ../../../google/protobuf
wget https://raw.githubusercontent.com/google/protobuf/a663afb23bfc7b7f34abfd0ae86b16e128c428ce/src/google/protobuf/struct.proto
wget https://raw.githubusercontent.com/google/protobuf/a663afb23bfc7b7f34abfd0ae86b16e128c428ce/src/google/protobuf/timestamp.proto
wget https://raw.githubusercontent.com/google/protobuf/a663afb23bfc7b7f34abfd0ae86b16e128c428ce/src/google/protobuf/wrappers.proto

cd ../../google/type
wget https://raw.githubusercontent.com/google/googleapis/f66e425a93ca60ee49764bf97cbc3dd2efa97058/google/type/latlng.proto
```
