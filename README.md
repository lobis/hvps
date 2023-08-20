# [HVPS](https://github.com/lobis/hvps)

<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-2-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->

[![PyPI version](https://badge.fury.io/py/hvps.svg)](https://badge.fury.io/py/hvps)
[![node.js bindings](https://badge.fury.io/js/hvps.svg)](https://badge.fury.io/js/hvps)
[![node-red node](https://badge.fury.io/js/hvps-node-red.svg)](https://www.npmjs.com/package/hvps-node-red)

[![PyPI downloads](https://img.shields.io/pypi/dm/hvps.svg)](https://pypi.org/project/hvps/)
![Python Version](https://img.shields.io/badge/python-3.8-blue.svg)

[![Build and Test](https://github.com/lobis/hvps/actions/workflows/build-test.yml/badge.svg)](https://github.com/lobis/hvps/actions/workflows/build-test.yml)
[![Upload Python Package to PyPI and nodejs bindings to npm](https://github.com/lobis/hvps/actions/workflows/publish.yml/badge.svg)](https://github.com/lobis/hvps/actions/workflows/publish.yml)

## What is this? 🤔

This is a Python package for controlling high voltage power supplies (HVPS) over serial port.
The aim is to provide a unified pythonic interface for different HVPS models.

Along with the Python package, a minimal set of bindings for Node.js is also provided. A nodered node is also available.
They both rely on the Python package to be installed in order to work.

Currently only **CAEN** and **iseg** brands are supported.

## Installation ⚙️

Installation via `pip` is supported.
To install the latest [published version](https://github.com/lobis/hvps/releases), run:

```bash
pip install hvps
```

To install the package from source, including development dependencies, clone the repository and run:

```bash
pip install .[dev]
```

## Usage 👨‍💻

There is a hierarchy of objects that represent the HVPS and its components:

- `HVPS`: represents the HVPS itself and handles the connection to the serial port. The classes `Caen` and `Iseg` are
  available for the respective brands.
- `Module`: represents a module of the HVPS. Some HVPS support multiple modules over the same connection
- `Channel`: represents a channel of the HVPS

### Connection

```python
from hvps import Caen, Iseg
import logging

# connection interface is common to all HVPS
# if no serial port is specified, the first available port will be used
# if no baudrate is specified, the default baudrate will be used
# if logging_level is specified, the logger will be configured accordingly
with Caen(port="/dev/ttyUSB0", baudrate=115200, logging_level=logging.DEBUG) as hvps:
    # using context manager (with) is recommended, but not required.
    # If not used, the connection must be opened and closed manually (hvps.open() and hvps.close())
    # connection settings can be accessed
    print(f"port: {hvps.port}")
    print(f"baudrate: {hvps.baudrate}")
```

### Module

```python
from hvps import Caen

# default connection settings
with Caen() as caen:
    module = caen.module()  # get the first module (module 0)
    # if multiple modules are present, they can be accessed by index e.g. caen.module(1)

    # get the module's name
    print(f"module name: {module.name}")
```

### Channel

```python
from hvps import Caen

with Caen() as caen:
    module = caen.module(0)

    print(f"number of channels: {module.number_of_channels}")

    channel = module.channel(2)  # get channel number 2

    # get monitoring parameters
    print(f"vmon: {channel.vmon}")
    print(f"vset: {channel.vset}")

    # set values (remote mode must be enabled)
    # turn on channel
    channel.turn_on()

    channel.vset = 300.0  # 300 V
```

## Disclaimer ⚠️

The development of this package is mostly based on documentation with access to only a few models of HVPS.

If you use this package, it is very possible you find a bug or some oversight.
You are encouraged to make a [pull request](https://github.com/lobis/hvps/pulls) or to create
an [issue](https://github.com/lobis/hvps/issues) to report a bug, to request additional features or to suggest
improvements.

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tbody>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/lobis"><img src="https://avatars.githubusercontent.com/u/35803280?v=4?s=100" width="100px;" alt="Luis Antonio Obis Aparicio"/><br /><sub><b>Luis Antonio Obis Aparicio</b></sub></a><br /><a href="https://github.com/lobis/hvps/commits?author=lobis" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/AlonsoDRDLV"><img src="https://avatars.githubusercontent.com/u/71894461?v=4?s=100" width="100px;" alt="AlonsoDRDLV"/><br /><sub><b>AlonsoDRDLV</b></sub></a><br /><a href="https://github.com/lobis/hvps/commits?author=AlonsoDRDLV" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/jherkenhoff"><img src="https://avatars.githubusercontent.com/u/22686781?v=4?s=100" width="100px;" alt="jherkenhoff"/><br /><sub><b>jherkenhoff</b></sub></a><br /><a href="https://github.com/lobis/hvps/commits?author=jherkenhoff" title="Code">💻</a></td>
    </tr>
  </tbody>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification.
Contributions of any kind welcome!
