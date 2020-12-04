#!/usr/bin/env/python

import RPi.GPIO as gp
import os
import time

gp.setwarnings(FALSE)
gp.setmode(gp.BOARD)

gp.setup(7,gp.OUT)
gp.setup(11,gp.OUT)
gp.setup(12,gp.OUT)

gp.setup(15,gp.OUT)
gp.setup(16,gp.OUT)
gp.setup(21,gp.OUT)
gp.setup(22,gp.OUT)

gp.output(11, True)
gp.output(12, True)
gp.output(15, True)
gp.output(16, True)
gp.output(21, True)
gp.output(22, True)

drive = "/media/pi/usb/1/"

def main():
    d_time = time.time()
    print"Starting Camera 1"
    i2c = "i2cset -y 1 0x70 0x00 0x04"
    os.system(i2c)
    gp.output(7,False)
    gp.output(11,False)
    gp.output(12,True)
    capture(d_time,1)
    transmit(d_time,1)
    print"Starting Camera 2"
    i2c = "i2cset -y 1 0x70 0x00 0x05"
    os.system(i2c)
    gp.output(7,True)
    gp.output(11,False)
    gp.output(12,True)
    capture(d_time,2)
    transmit(d_time,2)
    print"Starting Camera 3"
    i2c = "i2cset -y 1 0x70 0x00 0x06"
    os.system(i2c)
    gp.output(7,False)
    gp.output(11,True)
    gp.output(12,False)
    capture(d_time,3)
    transmit(d_time,3)
    print"Starting Camera 4"
    i2c = "i2cset -y 1 0x70 0x00 0x07"
    os.system(i2c)
    gp.output(7,True)
    gp.output(11,True)
    gp.output(12,False)
    capture(d_time,4)
    transmit(d_time,4)
  
def capture(timed,cam):
    cmd = "raspi still -o %s_Cam%d.jpg" % (timed,cam)
    os.system(cmd)
    optim = "jpegoptim %s_Cam%d.jpg" % (timed,cam)
    os.system(optim)
    
def transmit(timed,cam)
    sshpass -p '*******' scp /home/pi/Documents/%s.txt.bz2 whale-srv@******:~/Whale_Srv/Incoming/1/" % timed
  
if __name__ == "__main__":
    main()
  
    gp.output(7,False)
    gp.output(11,False)
    gp.output(12,True)
