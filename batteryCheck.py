#!/usr/bin/env python3
import gi
gi.require_version('Notify', '0.7')
import subprocess
import time
from gi.repository import Notify
Notify.init('Battery Warning')

cmd = ['upower', '-i', '/org/freedesktop/UPower/devices/battery_BAT0']
control = 0

def BatteryCheck():
    global percentage
    proc = subprocess.Popen(cmd, stdout = subprocess.PIPE)
    output = proc.stdout.read()
    converted = output.decode()
    pos = int(converted.find('%'))
    percentage = int(converted[pos-2 : pos])


while True:
    BatteryCheck()
    showlevel = str(percentage),'%'
    if percentage <= 25 and control == 0:
        notification = Notify.Notification.new('WARNING LOW BATTERY', showlevel)
        notification.set_urgency(2)
        notification.show()
        control = 1
    if percentage > 25 and control == 1:
        control = 0
    time.sleep(60)


"""
while True:

    proc = subprocess.Popen(cmd, stdout = subprocess.PIPE)
    output = proc.stdout.read()
    converted = output.decode()
    trigger = converted.find('25%')
    if(trigger != -1):
        notification.show()
    time.sleep(30)

"""
