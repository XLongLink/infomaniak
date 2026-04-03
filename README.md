# infomaniak

[![PyPI version](https://img.shields.io/pypi/v/infomaniak)](https://pypi.org/project/infomaniak/)
[![Tests](https://github.com/peaktwilight/infomaniak-cli/actions/workflows/test.yml/badge.svg)](https://github.com/peaktwilight/infomaniak-cli/actions/workflows/test.yml)
[![Python versions](https://img.shields.io/pypi/pyversions/infomaniak)](https://pypi.org/project/infomaniak/)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

Python client library for the [Infomaniak](https://www.infomaniak.com) API.

The package now focuses on the library surface. The only remaining CLI entrypoint is:

```bash
infomaniak
```

Running it opens the Infomaniak token creation page in your browser:

`https://manager.infomaniak.com/v3/infomaniak-api`

## Install

```bash
pip install infomaniak
```

## Library usage

```python
from infomaniak import Client, DNSClient

client = Client(token="your-token")
dns = DNSClient(token="your-token", zone="example.com")
```

You can also provide `INFOMANIAK_API_TOKEN` via environment variables or a local `.env` file.

## Token helper CLI

```bash
infomaniak
infomaniak --help
infomaniak --version
```

## License

MIT
