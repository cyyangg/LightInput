from gpiozero import LED
from time import sleep


green = LED(4)

green.off()
sleep(3)

green.on()
sleep(5)

green.off()


