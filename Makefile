GENERATED_DIR=$(shell pwd)/generated_python
FINAL_DIR=datastore_deps/_generated

help:
	@echo 'Makefile for generating pb2 modules from proto files    '
	@echo '                                                        '
	@echo '   make generate         Generates the protobuf modules '
	@echo '   make check_generate   Checks that generate succeeded '

generate: rewrite_imports.py
	mkdir -p $(GENERATED_DIR)
	# Datastore API Files
	protoc --python_out=$(GENERATED_DIR) google/datastore/v1beta3/*.proto
	mv $(GENERATED_DIR)/google/datastore/v1beta3/* $(FINAL_DIR)
	# Auxiliary API Files
	protoc --python_out=$(GENERATED_DIR) google/api/*.proto
	mv $(GENERATED_DIR)/google/api/* $(FINAL_DIR)
	protoc --python_out=$(GENERATED_DIR) google/protobuf/*.proto
	mv $(GENERATED_DIR)/google/protobuf/* $(FINAL_DIR)
	protoc --python_out=$(GENERATED_DIR) google/type/*.proto
	mv $(GENERATED_DIR)/google/type/* $(FINAL_DIR)
	python rewrite_imports.py

check_generate: check_generate.py
	python check_generate.py

.PHONY: generate check_generate
