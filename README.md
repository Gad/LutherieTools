# LuTOOL

The ambition of LuTOOL is/was to provide a set of tools for guitar makers. I'm publishing the first one that works, i.e. the fretboard generator. 
The generator can output fretboard vector files for any scale length in millimeters or inches.  
This vector file (in SVG format) can then be used for cutting the fretboard (laser cut, CNC, etc.).
Bear in mind we use the color code of our own laser cutting service [Link](http://www.damengo.com) : red for cutting, green for engraving. 
The fretboards shape and features are largely inspired by those published by [Link](https://www.lutherie-amateur.com/Forum/index.php). Big thanks to them !



## Installation 

Use [pip](https://pip.pypa.io/en/stable/) to install LuTOOL dependencies

```bash
pip install requirements.txt
```

and run :

```bash
python LuTOOL.py
```

or download one of the (future) releases

## License 

[GNU GPLv3](https://choosealicense.com/licenses/gpl-3.0/)

## Warning 

You can/should check the generated template is Ok (for example you can open it with Inkscape and measure the distance between the frets). no warranty or guarantee is made as to its accuracy.

Code is hugly but I have no time for improving it :)