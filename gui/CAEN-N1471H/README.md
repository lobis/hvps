# CaenHVPSGUI Documentation

## Overview
The `CaenHVPSGUI` is a graphical user interface (GUI) designed to control and monitor CAEN High Voltage Power Supply (HVPS) modules. The interface is built using Python's `tkinter` library, with threading to handle background tasks and maintain responsive interaction. The GUI supports various functionalities such as setting voltages, turning channels on or off, monitoring channel states, and handling alarms.

## Features
- **Real-time Monitoring**: Voltage (`vmon`), current (`imon`), and state indicators are updated in real-time.
- **Multi-Channel Support**: The GUI can handle modules with multiple channels, providing individual control and monitoring for each channel.
- **Alarm and Interlock Management**: Visual indicators and tooltips provide status information on the module alarms and interlock.
- **Threaded Background Processing**: Ensures the GUI remains responsive during long-running operations.
- **Tooltips**: Interactive tooltips provide additional information when hovering over various GUI elements.

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

## How to Use

### Real Usage
1. Ensure you have the `hvps` library installed and the CAEN HVPS connected to your system.
2. Instantiate the `CaenHVPSGUI` class with a valid `module` object from the `hvps` library.

   Example:
   ```python
   import hvps
   caen = hvps.Caen(port='/dev/ttyUSB0')
   m = caen.module(0)
   CaenHVPSGUI(module=m)
   ```
