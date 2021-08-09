# rgb-potentiometers

Code used in Prof. Gallaugher's demo board for RGB and Potentiometers

Color can be assigned by combining values for Red, Green, and Blue (RGB). The sliders allow each color to be set. The top light strip shows the color from the combined RGB setting, while the bottom strip shows the individual Red, Green, and Blue values.

Sliders are potentiometers. They are resistors that report a value from 0 to 65520. This value is scaled from 0 to 255 so that can be used as an R, G, or B value.

The circular knob is also a potentiometer. Here the 0 to 65520 value is scaled to 1 through 12 and will color the ring lights when turned.

The 0.91" display reports values as the potentiometers are moved. The board is an Adafruit Feather RP2040. 
