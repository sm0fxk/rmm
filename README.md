# rmm
Radio Module Manager


This is a graphical user interface to radio transceiver chips, 
so that they can be operated like any ham radio transceiver.
The intention is to write generic code except the driver for the chip in question,
and to take advantage of the large number of drivers from the RadoHead repository.
So far, the Texas instruments CC1101 and the Semcon SX1231 are supported. 

The arcitecture is explained by the picture found under the doc directory.
The radio "front panel" is implemented in Python, 
and talks to the radio module which is implemented in C++, using CAT commands.
The interface is inspired by the Kenwood PC commant set, 
but since the radio module chip significantly differs from an ordinary ham radio transceiver, 
some changes have been made.
It is a wish to make the radio module hamlib compatible, but the this is currently not the primary goal.


How to run the demo
- cd Agent
- cd to the radio chip directory
- Build the agent: make

- go to the Manager directory
- Start the manager: ./rig_control.py
- Click "Connect Agent"
- Select the agent binary file
A pipe is now established between the agent and the manager.
Try to to some config settings
