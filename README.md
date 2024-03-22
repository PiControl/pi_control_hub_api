# pi_control_hub_api

This repostory contains the OpenAPI definition for PiControl. As of now it
provides the server API for Python FastAPI and the clöient API for Swift.

## Generating the Python server API

The Python server API needs to be generated and the generated sources need to be
committed and pushed such that the repo can be installed directly from GitHub.

### Install the OpenAPI Generator

#### Linux

For Linux node and npm is required. Install the generator by executing the
following shell command:

```bash
npm install @openapitools/openapi-generator-cli -g
```

Add the following alias to your shell profile:

```bash
alias openapi-generator="npx @openapitools/openapi-generator-cli"
```

Afterwards restart your shell and you're good to go.

### macOS

For macOS [Homebrew](https://brew.sh) is required. Install the generator by
executing the following shell command:

```bash
brew install openapi-generator
```

Afterwards you're good to go.

### Generate the Python server API

Execute the shell script

```bash
./generate-python-server.sh
```

Afterwards you can commit and push the changes or install it by executing

```bash
pip install .
```
