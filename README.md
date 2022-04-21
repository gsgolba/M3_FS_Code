# M3-FS_movement

## The Plan
- submodules will remain intact, I'll just copy the necessary files I need from them.
- Double check if any copyright licenses need to be added


## Instructions
1. Associate M3-USB interface to a virtual COM port
   __To change the USB to UART’s vendor/product id to that of a VCP you must do the following…__
   ## How to create virtual COM port
    1. Install the NST Pathway software onto a Windows PC as well as the SiLabs VCP driver for Windows.

    2. Run the NST USB Bridge Setup program to change it to appear as a Virtual COM Port (this utility is available from the Start menu once the Pathway s/w has been installed).
    3.  Connect to the M3-FS, through the M3 USB Interface, using the Pathway s/w.

        * From the Pathway Setup Connection dialog, you must manually change the baud rate selection from 115200 (the default for a COM port) to 250000 (the preset baud rate in the M3 USB Interface).

        * Once connected (i.e. you close the Setup Connection dialog and click Connect on the main window), change the M3 USB Interface’s baud rate to 115200 by entering the following command into the Manual Command Entry text box (excluding quotes): “TR<54 1 03>” and click Send.  You must do this because Linux may not accept a baud rate of 250000.   After sending that command, wait at least 5 seconds before removing the M3 USB Interface from the PC.   To test it, plug it back in and, this time, when selecting the COM port from the Setup Connection dialog, select the baud rate of 115200 and confirm that it communicates.

   4. The following link takes you to the available VCP drivers: https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers.  For Windows, use the “CP210x Windows Drivers”.  They have multiple choices for Linux and I don’t know which you should use. __Raspberry pi debian OS often already comes with this driver installed. After restarting, the raspberry pi it should recognize the M3-FS (for me it was on /dev/ttyUSB0)__
2. use either the python or C++ code to send messages through the M3-FS either manually or automatically based on PX4 data
