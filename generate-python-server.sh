#!/bin/sh

PACKAGE_NAME="pi_control_hub_api"
PACKAGE_VERSION="10.1.0"

openapi-generator generate \
    -i pi_control_hub_api.yaml \
    -g python-fastapi \
    -t ./python-fastapi-async-template \
    -o . \
    -p packageName=$PACKAGE_NAME \
    -p packageVersion=$PACKAGE_VERSION
