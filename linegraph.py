#!/usr/bin/env python

from PIL import Image, ImageDraw
from math import e, sin, pi

width = 500
height = 500

image1 = Image.new( mode="RGB",
                   size=( width, height ),
                   color="black")#( 0, 0, 0 ))

image2 = Image.new( mode="RGB",
                   size=( width, height ),
                   color="black")#( 0, 0, 0 ))

#Image 1: f1=3.001 f2=2 f3=3 f4=2 d1=0.004 d2=0.0065 d3=0.008 d4=0.019 p1=0 p2=0 p3=pi/2 p4=3pi/2
#Image 2: f1=10 f2=3 f3=1 f4=2 d1=0.039 d2=0.006 d3=0 d4=0.0045 p1=0 p2=0 p3=pi/2 p4=0
#Image 3: f1=2.01 f2=3 f3=3 f4=2 d1=0.0085 d2=0 d3=0.065 d4=0 p1=0 p2=7 pi/16 p3=0 p4=0
#Image 4: f1=2 f2=6 f3=1.002 f4=3 d1=0.02 d2=0.0315 d3=0.02 d4=0.02 p1=pi/16 p2=3pi/2 p3=13 pi/16 p4=pi

#frequencies
f1 = 2.01
f2 = 3
f3 = 3
f4 = 2

#damp forces
d1 = 0.0085
d2 = 0
d3 = 0.065
d4 = 0

#phases
p1 = 0
p2 = 7 * pi / 16
p3 = 0
p4 = 0

t = 0
dt = 0.05

count = 0

xi = width // 2
yi = height // 2

draw1 = ImageDraw.Draw( image1 )
draw2 = ImageDraw.Draw( image2 )

amp = 100

for _ in range( 10000 ) :

    x = amp * sin( f1 * t + p1 ) * e ** ( -t * d1 ) + amp * sin( f2 * t + p2 ) * e ** ( -t * d2 )
    y = amp * sin( f3 * t + p3 ) * e ** ( -t * d3 ) + amp * sin( f4 * t + p4 ) * e ** ( -t * d4 )

    x = int( x ) + ( width // 2 )
    y = int( y ) + ( height // 2 )

    print( f"\r x : {x}, y : {y}", end="\r" )
    if ( x == y ) :
        count += 1

    if ( count == 50 ) :
        break

    try :

        draw1.line( ( xi, yi ) + ( x, y ), fill="orange", width = 1 )
        draw2.line( ( xi, yi ) + ( x, y ), fill="white", width = 1 )
        xi = x
        yi = y
        
    except IndexError:
        continue

    t += dt

name = input(" Filename : ")
image1.save( f"{name}_orange_image.png" )
image2.save( f"{name}_white_image.png" )