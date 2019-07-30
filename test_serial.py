import serial
#import serial.tools.list_ports
#import serial.tools.list_ports
from serial.tools import list_ports

print ('Search ports...')
ports = list(serial.tools.list_ports.comports())

for p in ports:
    print ('-- Find ports --')
    print (p.device, p.description)