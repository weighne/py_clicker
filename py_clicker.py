import mouse
import sys
from time import sleep

sleep(1)
x=1
while x <= int(sys.argv[1]):
    mouse.click("left")
    x+=1

print("DONE!")
