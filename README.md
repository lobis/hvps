# HVPS

[![PyPI version](https://badge.fury.io/py/hvps.svg)](https://badge.fury.io/py/hvps)
[![node.js bindings](https://badge.fury.io/js/hvps.svg)](https://badge.fury.io/js/hvps)
[![node-red node](https://badge.fury.io/js/hvps-node-red.svg)](https://www.npmjs.com/package/hvps-node-red)

[![PyPI downloads](https://img.shields.io/pypi/dm/hvps.svg)](https://pypi.org/project/hvps/)
![Python Version](https://img.shields.io/badge/python-3.8-blue.svg)

[![Build and Test](https://github.com/lobis/hvps/actions/workflows/build-test.yml/badge.svg)](https://github.com/lobis/hvps/actions/workflows/build-test.yml)
[![Upload Python Package to PyPI and nodejs bindings to npm](https://github.com/lobis/hvps/actions/workflows/publish.yml/badge.svg)](https://github.com/lobis/hvps/actions/workflows/publish.yml)

## 🤔 What is this?

This is a Python package for controlling high voltage power supplies (HVPS) over serial port.
The aim is to provide a unified pythonic interface for different HVPS models.

Along with the Python package, a minimal set of bindings for Node.js is also provided. A nodered node is also available.
They both rely on the Python package to be installed in order to work.

Currently only **CAEN** and **iseg** brands are supported.

## ⚙️ Installation

Installation via `pip` is supported.
To install the latest [published version](https://github.com/lobis/hvps/releases), run:

```bash
pip install hvps
```

To install the package from source, including development dependencies, clone the repository and run:

```bash
pip install .[dev]
```

## 👨‍💻 Usage

There is a hierarchy of objects that represent the HVPS and its components:

- `HVPS`: represents the HVPS itself and handles the connection to the serial port
- `Module`: represents a module of the HVPS. Some HVPS support multiple modules over the same connection
- `Channel`: represents a channel of the HVPS

### Connection

```python
from hvps import Caen, Iseg
import logging

# connection interface is common to all HVPS
# if no serial port is specified, the first available port will be used
# if no baudrate is specified, the default baudrate will be used
# if connect=False, the connection will not be established (useful for testing)
# if logging_level is specified, the logger will be configured accordingly
hvps = Caen(port="/dev/ttyUSB0", baudrate=115200, connect=True, logging_level=logging.DEBUG)

# connection settings can be accessed
print(f"port: {hvps.port}")
print(f"baudrate: {hvps.baudrate}")
```

### Module

```python
from hvps import Caen

# default connection settings
caen = Caen()

module = caen.module()  # get the first module (module 0)
# if multiple modules are present, they can be accessed by index e.g. caen.module(1)

# get the module's name
print(f"module name: {module.name}")
```

### Channel

```python
from hvps import Caen

caen = Caen()
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

## ⚠️ Disclaimer

The development of this package is mostly based on documentation with access to only a few models of HVPS.

If you use this package, it is very possible you find a bug or some oversight.
You are encouraged to make a [pull request](https://github.com/lobis/hvps/pulls) or to create
an [issue](https://github.com/lobis/hvps/issues) to report a bug, to request additional features or to suggest
improvements.
