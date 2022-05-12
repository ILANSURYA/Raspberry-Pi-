from sense_hat import SenseHat 
import time 
s = SenseHat() 
s.low_light = True 
blue = (0, 0, 255) 
white = (255,255,255) 
nothing=(0,0,0) 
def first(): 
 B = blue 
 S = white 
 O=nothing 
 logo = [ 
 B, B, S, S, S, S, B, B, 
 B, B, S, B, B, B, B, B, 
 B, B, S, B, B, B, B, B, 
 B, B, S, S, S, S, B, B, 
 B, B, B, B, B, S, B, B, 
 B, B, B, B, B, S, B, B, 
 B, B, S, S, S, S, B, B, 
 O, O, O, O, O, O, O, O, 
 ] 
 return logo 
def second(): 
 B = blue 
 S = white 
 O=nothing 
 logo = [ 
 B, B, S, S, S, S, B, B, 
 B, B, S, O, O, S, B, B, 
 B, B, S, O, O, S, B, B, 
 B, B, S, S, S, S, B, B, 
 B, B, S, S, B, B, B, B, 
 B, B, S, B, S, B, B, B, 
 B, B, S, B, B, S, B, B, 
 O, O, O, O, O, O, O, O, 
 ] 
 return logo 
def third(): 
 B = blue 
 W = white 
 logo = [ 
 B, B, B, B, B, B, B, B, 
 B, B, B, B, B, B, B, B, 
 B, W, B, B, B, W, B, B, 
 B, W, W, B, W, W, B, B, 
 B, W, B, W, B, W, B, B, 
 B, W, B, B, B, W, B, B, 
 B, W, B, B, B, W, B, B, 
 B, B, B, B, B, B, B, B, 
 ] 
 return logo 
images = [first,third,second] 
count = 0 
while True: 
 s.set_pixels(images[count % len(images)]()) 
 time.sleep(2) 
 count += 1 
 count += 1
