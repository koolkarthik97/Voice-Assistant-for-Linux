# Voice-Assistant-for-Linux
A BING-API based linux voice automation tool in python 

This invloves 3 modules -
---Speaker recognition
---Speech to text conversion
---Text to command interpretation

Speaker recognition:
  This is achieved through Piwho module libraries.
  You can install piWho with the help of other Git repositories.
Speech recognition:
  this is achieved through Microsoft's Bing - Online API services .
 Register online at Bing services to generate a key to utilise this free Module.
 
Command Interpretation:
  Linux commands can be virtually generated with the help of Mouse and Keyboard Falsification tools .
  xdotool and wmctrl can be used to convert the texts into commands in Python and Linux.
  bingtest.py --- Test your BING api odule separately.
  recognise.py -- Check the speaker recognition piWho module that can be trained using train.py.
  "*_cmds.txt" contain certain commands for examples
  
  theRealOne.py is the integration of all the three modules .
  
  Be sure to import all the necessary libraries and install the required packages before proceeding.
  
