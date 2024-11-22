.PHONY: install generate run clean

# Virtual environment directory name
VENV_DIR = venv

install:
	python3 -m venv $(VENV_DIR)
	$(VENV_DIR)/bin/pip install --upgrade pip
	$(VENV_DIR)/bin/pip install -r requirements.txt

generate:
	$(VENV_DIR)/bin/python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. grpc_tools.proto

run: install generate
	$(VENV_DIR)/bin/python client.py

clean:
	rm -rf $(VENV_DIR)
	rm -f grpc_tools_pb2.py grpc_tools_pb2_grpc.py
