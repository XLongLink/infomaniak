# xinfomaniak

[![PyPI version](https://img.shields.io/pypi/v/xinfomaniak)](https://pypi.org/project/xinfomaniak/)
[![Tests](https://github.com/XLongLink/infomaniak/actions/workflows/test.yml/badge.svg)](https://github.com/XLongLink/infomaniak/actions/workflows/test.yml)
[![Python versions](https://img.shields.io/pypi/pyversions/xinfomaniak)](https://pypi.org/project/xinfomaniak/)
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
pip install xinfomaniak
```

## Library usage

```python
from infomaniak import Client

client = Client(token="your-token")
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
