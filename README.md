Lüftersteuerung
Lüfter und LED abhängig von CPU Temperatur steuern
Gesteuert können z.B. folgende LED

1x grün leuchtet bis 50 Grad CPU Temperatur

1x gelb leuchtet ab 50 Grad CPU Temperatur

1x rot leuchtet ab 60 Grad CPU Temperatur, Lüfter schalet sich ein bis die CPU-Temperatur unter 60 Grad beträgt

Programm starten:

/home/pi/lueftersteuerung/lueftersteuerung.py

LED und Lüfter schalten sich je nach CPU Temperatur an und wieder aus, damit das Programm automatisch startet empfiehlt sich folgender Cronjob:

crontab -e

@reboot python3 /home/pi/lueftersteuerung/temperatur.py

Nach dem Crontab eintrag rebooten:

sudo reboot
