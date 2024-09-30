# CaenHVPSGUI Documentation

## Overview
The `CaenHVPSGUI` is a graphical user interface (GUI) designed to control and monitor CAEN High Voltage Power Supply (HVPS) modules. The interface is built using Python's `tkinter` library, with threading to handle background tasks and maintain responsive interaction. The GUI supports various functionalities such as setting voltages, turning channels on or off, monitoring channel states, and handling alarms.

The communication with the CAEN HVPS is done by the [hvps](https://github.com/lobis/hvps.git) python library.

## Features
- **Real-time Monitoring**: Voltage (`vmon`), current (`imon`), and state indicators are updated in real-time.
- **Multi-Channel Support**: The GUI can handle modules with multiple channels, providing individual control and monitoring for each channel.
- **Alarm and Interlock Management**: Visual indicators and tooltips provide status information on the module alarms and interlock.
- **Threaded Background Processing**: Ensures the GUI remains responsive during long-running operations.
- **Tooltips**: Interactive tooltips provide additional information when hovering over various GUI elements.

## How to Use
### Requirements
Make sure to have tkinter installed in your system (check [this](https://stackoverflow.com/a/74607246) if you don't) and the hvps python library (check [hvps installation guide](https://github.com/lobis/hvps?tab=readme-ov-file#installation-%EF%B8%8F)).

Download the [gui.py](gui.py) script or clone the repository.
### Usage
At the directory where this [gui.py](gui.py) is found, run
``` bash
python3 gui.py --port /dev/ttyUSB0
```
Note that you may need to change the port. To show available ports run
``` bash
python -m hvps --ports
```
#### Test mode
If you want to test the GUI without having the hardware available, copy the [caen_simulator.py](caen_simulator.py) module to the same directory where the [gui.py](gui.py) script is found and just run
``` bash
python3 gui.py --test
```

## Code Structure

### Main Classes
- **ToolTip**: A class for creating and managing tooltips for GUI widgets.
- **CaenHVPSGUI**: The main class for creating and managing the GUI.

### Key Methods
- GUI initializer and frames constructors:
    - `create_gui()`: Initializes the GUI, setting up frames for alarms, channels, and other controls.
    - `create_main_frame()`, `create_alarm_frame()`, `create_channels_frame()`: Methods for creating specific sections of the GUI.
    - `open_channel_property_window()`: Opens a window with advanced settings for a specific channel.
- Action and user interaction handlers:
    - `start_background_threads()`: Starts background threads for reading values and processing commands.
    - `issue_command()`: Manages the queueing and execution of commands to the module. This is key to ensure the CAEN module does not receive multiple commands at the same time. Please, use this for any method that interacts with the CAEN module.
    - `read_values()`: Continuously reads and updates the displayed values for each channel.

### GUI Components
- **Alarm Frame**: Displays alarm and interlock indicators with buttons to clear signals.
- **Channels Frame**: Lists all available channels with options to set voltages, monitor values, and toggle states.
- **Multichannel Frame**: Provides batch operations on multiple channels.
