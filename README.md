# qtileconfig
A set of configuration files for Qtile and Rofi.

It includes a configuration for the window manager Qtile along with a configuration and theme for the app menu Rofi.

Here are some screenshots:

![Screenshot from 2021-05-01 01-38-51](https://user-images.githubusercontent.com/60475104/116760590-fbc99e00-aa1d-11eb-8188-b5883880c4c2.png)
![Screenshot from 2021-04-30 22-07-32](https://user-images.githubusercontent.com/60475104/116760608-07b56000-aa1e-11eb-957e-72c2021204ea.png)

To get the config, place the files as follows:
 - config.py in ~/.config/qtile/
 - config.rasi and DarkIce.rasi in ~/.config/rofi/

Make sure to have installed the following:
 - qtile
 - rofi

Also make an autostart.sh script with any startup commands you may want. My script is made to take advantage of one. If you don't need one, remove the startup hook from the end of the config.py file.
