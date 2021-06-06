# Raspberry Pi 4 Fan control and Temperature display  

Python script to control fan and display current CPU temperature  

Guide for Raspberry Pi 4:
1. Use NPN transistor, e.g. S8050  
Connect emitter to the fan  
Connect collector to GND  
Connect GPIO 18 to base  
2. Connect second fan lead to 5V
3. git clone https://github.com/AlexanderApanovich/rpi4-fan-control.git
4. cd rpi4-fan-control
5. sudo ./install
6. sudo crontab -e  
Add following string: @reboot python /usr/local/bin/rpi4_fan_control.py &

Uninstallation guide:
1. sudo crontab e  
Remove following string: @reboot python /usr/local/bin/rpi4_fan_control.py &
2. cd rpi4-fan-control
3. sudo ./uninstall
