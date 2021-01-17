#!/usr/bin/env python

from PIL import Image
from math import e, sin, pi

width = 500
height = 500

image = Image.new( mode="RGB",
        size=( width, height ),
        color=( 0, 0, 0 ))

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
d1 = 0.00085
d2 = 0
d3 = 0.0065
d4 = 0

#phases
p1 = 0
p2 = 7 * pi / 16
p3 = 0
p4 = 0

t = 0
dt = pi / ( height + width )

pixels = [ [ 0 for i in range( width ) ] for j in range( height )]

count = 0
iterations = 100 * ( width + height )

for iters in range( iterations ) :

    x = 150 * sin( f1 * t + p1 ) * e ** ( -t * d1 ) + 100 * sin( f2 * t + p2 ) * e ** ( -t * d2 )
    y = 150 * sin( f3 * t + p3 ) * e ** ( -t * d3 ) + 100 * sin( f4 * t + p4 ) * e ** ( -t * d4 )

    x = int( x ) + ( width // 2 )
    y = int( y ) + ( height // 2 )

    print( f"\r x : {x}, y : {y}", end="\r" )
    if ( x == y ) :
        count += 1

    if ( count > 100 ) :
        break

    try :

        pixels[y+1][x-1] = 1+iters*254/iterations;
        pixels[y+0][x-1] = 1+iters*254/iterations;
        pixels[y-1][x-1] = 1+iters*254/iterations;
        pixels[y+1][x+0] = 1+iters*254/iterations;
        pixels[y+0][x+0] = 1+iters*254/iterations;
        pixels[y-1][x+0] = 1+iters*254/iterations;
        pixels[y+1][x+1] = 1+iters*254/iterations;
        pixels[y+0][x+1] = 1+iters*254/iterations;
        pixels[y-1][x+1] = 1+iters*254/iterations;

    except IndexError:
        print( f" Out of range x : {x}, y : {y}" )
        continue

    t += dt

index = 0
for y in range( height ) :
    for x in range( width ) :

        if ( pixels[ y ][ x ] > 0 ) :
            r = int( 128-pixels[y][x]//2) ;index += 1 
            g = int( 255-pixels[y][x]//2) ;index += 1
            b = int( 128+pixels[y][x]//2) ;index += 1

            image.putpixel( ( x, y ), (r, g, b) )
        else :
            r = 0 ;index += 1 
            g = 0 ;index += 1
            b = 0 ;index += 1

            image.putpixel( ( x, y ), ( r, g, b ) )

filename = input( " Filename to save : " )
image.save( filename )