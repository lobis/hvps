# caenhv

## 🤔 What is this?

This is an unofficial Python package to interface with CAEN high voltage power supplies over USB (RS232 protocol).


## ⚠️ Disclaimer

The features of this package are based on my needs at the time of writing.
I have done very limited testing on a single model (DT1471ET) but it should also work for other CAEN power supplies also supporting RS232.

If you use this package, it is very possible you find a bug or some oversight.
You are encouraged to make a [pull request](https://github.com/lobis/caen-hv/pulls) or to create
an [issue](https://github.com/lobis/caen-hv/issues) to report a bug, to request additional features or to suggest
improvements.

## 👨‍💻 Usage

```python
from caenhv import CaenHV

# automatically detect serial port and baudrate (can be manually set)
caen = CaenHV()
# get the first module. CAEN supports multiple modules over the same connection
# typically only one module should be present
module = caen[0]

# get channel number 2
channel = module.channel(2)

# print current 'vset' and 'vmon' values
print(f"vset: {channel.vset}")
print(f"vmon: {channel.vmon}")

# switch channel off and off
channel.off()
channel.on()

# set a new value of 'vset'
channel.vset = 300.0 # 300 V
```

