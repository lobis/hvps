# HVPS

[![PyPI version](https://badge.fury.io/py/hvps.svg)](https://badge.fury.io/py/hvps)
[![npm version](https://badge.fury.io/js/hvps.svg)](https://badge.fury.io/js/hvps)

[![PyPI downloads](https://img.shields.io/pypi/dm/hvps.svg)](https://pypi.org/project/hvps/)
![Python Version](https://img.shields.io/badge/python-3.8-blue.svg)

[![Build and Test](https://github.com/lobis/hvps/actions/workflows/build-test.yml/badge.svg)](https://github.com/lobis/hvps/actions/workflows/build-test.yml)
[![Upload Python Package to PyPI and nodejs bindings to npm](https://github.com/lobis/hvps/actions/workflows/publish.yml/badge.svg)](https://github.com/lobis/hvps/actions/workflows/publish.yml)

## 🤔 What is this?

The goal of this Python package is to interface with different brands of high voltage power supplies in a uniform way.
Currently only CAEN and iseg brands are supported. Communication is performed via serial port (over USB).

## ⚠️ Disclaimer

The features of this package are based on my needs at the time of writing.
I have done very limited testing on a single model (DT1471ET) but it should also work for other CAEN power supplies also
supporting RS232.

If you use this package, it is very possible you find a bug or some oversight.
You are encouraged to make a [pull request](https://github.com/lobis/hvps/pulls) or to create
an [issue](https://github.com/lobis/hvps/issues) to report a bug, to request additional features or to suggest
improvements.

## ⚙️ Installation

Installation via `pip` is supported.
To install the latest [published version](https://github.com/lobis/lecroy-scope/releases), run:

```bash
pip install hvps
```

To install the package from source, including development dependencies, clone the repository and run:

```bash
pip install .[dev]
```

## 👨‍💻 Usage

### CAEN

```python
from hvps import Caen

# automatically detect serial port and baudrate (can be manually set)
caen = Caen()
# get the first module. CAEN supports multiple modules over the same connection
# typically only one module will be present
module = caen.module(0)

# get channel number 2
channel = module.channel(2)

# print current 'vset' and 'vmon' values
print(f"vset: {channel.vset}")
print(f"vmon: {channel.vmon}")

# switch channel off and on
channel.turn_off()
channel.turn_on()

# set a new value of 'vset'
channel.vset = 300.0  # 300 V
```
