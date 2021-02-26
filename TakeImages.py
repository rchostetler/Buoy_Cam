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

#drive = "/media/pi/usb/1/"

def main():
    os.chdir("/home/pi/Documents/Captures/")
    d_time = time.time()
    print("Time is %s" % d_time)
    print("Starting Camera 1")
    i2c = "i2cset -y 1 0x70 0x00 0x04"
    os.system(i2c)
    gp.output(7,False)
    gp.output(11,False)
    gp.output(12,True)
    capture(d_time,1)
    transmit(d_time,1)
    print("Starting Camera 2")
    i2c = "i2cset -y 1 0x70 0x00 0x05"
    os.system(i2c)
    gp.output(7,True)
    gp.output(11,False)
    gp.output(12,True)
    capture(d_time,2)
    transmit(d_time,2)
    print("Starting Camera 3")
    i2c = "i2cset -y 1 0x70 0x00 0x06"
    os.system(i2c)
    gp.output(7,False)
    gp.output(11,True)
    gp.output(12,False)
    capture(d_time,3)
    transmit(d_time,3)
    print("Starting Camera 4")
    i2c = "i2cset -y 1 0x70 0x00 0x07"
    os.system(i2c)
    gp.output(7,True)
    gp.output(11,True)
    gp.output(12,False)
    capture(d_time,4)
    transmit(d_time,4)
  
def capture(timed,cam):
    cmd = "raspistill -o /home/pi/Documents/Captures/%s_Cam%d.jpg" % (timed,cam)
    os.system(cmd)
    optim = "jpegoptim --size=100k %s_Cam%d.jpg" % (timed,cam)
    os.system(optim)
#    cp = "sudo cp %s_Cam%d.jpg /media/pi/usb/1/" % (timed,cam)
#	os.system(cp)	##Back up data to USB drive
    
def transmit(timed,cam)
    os.chdir("/home/pi/Documents/Captures")
    tran = "sshpass -p '*******' scp %s_Cam%d.jpg robert@###.###.###.###:~/Documents/Telemetered_Images/" % (timed,cam)
    os.system(tran)
  
if __name__ == "__main__":
    main()
  
    gp.output(7,False)
    gp.output(11,False)
    gp.output(12,True)
