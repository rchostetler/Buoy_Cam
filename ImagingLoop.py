import RPi.GPIO as GPIO
import os

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.OUT)
GPIO.output(16, 0)

source = "/home/pi/Documents/Data/"
drive = "/media/pi/usb/1/"

## Mount USB Drive
os.system("sudo mount /dev/sda1 /media/pi/usb -o uid=pi,gid=pi")

def imtake():
	print("Beginning next image set")
	os.system("sudo /home/pi/Documents/ImageTaker") ## Take & Transmit images
  time.sleep(300)

while True:
	imtake()
