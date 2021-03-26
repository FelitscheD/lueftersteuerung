Lueftersteuerung
Lüfter und LED abhängig von CPU Temperatur steuern
Gesteuert können folgende LED

1x grün
1x gelb
1x rot

LED und Lüfter schalten sich je nach CPU Temperatur an und wieder aus, damit das Programm automatisch startet empfiehlt sich folgender Cronjob:

@reboot python3 /home/pi/lueftersteuerung/temperatur.py
