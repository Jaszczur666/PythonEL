# PythonEL #
PythonEL is replacement for previous code written in C#. The way it works is as follows.
First we initialize all needed devices, which can include opening serial port, and sending some configuration changes that will 
help us communicate efficiently. For example SRS Boxcar has a feature that was useful in early years of computers - it 
waits for x microseconds after each character it sends through serial interface. This value defaults to 255 microseconds
which makes response with value of signal on a channel take around a second. If we set x=0 it will take only a fraction 
of that.

Once we have our devices waiting and ready, the loop begins. We take first task from list and we execute it. Once its done 
we report task done, which will take another task from list, which will then be executed, and so on.  In C# version 
command in the list had two elements, deviceID, and a string with actual command. Strings are parsed inside equipment 
classes, so the main loop has only to send command to appropriate class. 
There are also some commands that have no equipment associated (wait some time, save data to text file, some other time 
related commands come to mind too)