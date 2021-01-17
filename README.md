# harmongraphs_simply
Generating some cool harmongraph images with simple math and physics using simple code

There are simple python scripts and a C code,\
For image operations [stb image library](https://github.com/nothings/stb)\
is used. It is a single header based library without any dependencies\
It is awesome, and I can't thank the creators enough for it.
You need to make a folder/directory named **stb** and in it place : \
(#) https://github.com/nothings/stb/blob/master/stb_image.h \
(#) https://github.com/nothings/stb/blob/master/stb_image_write.h 

All the code is inspired and based on this [awesome article](https://walkingrandomly.com/?p=151)\
It talks about how dampened oscillations can generate some pretty cool images\
with a simple equation \
<img src="https://render.githubusercontent.com/render/math?math=x_{(t)} = A \cdot \sin( \omega %2B \phi ) \cdot e ^{ -d \cdot t}">

# C code :
[user_based.c](https://github.com/TACHY0NN1X/harmongraphs_simply/user_based.c)

**To compile**
```
gcc -o user_based user_based.c -lm
```

# Python Scripts :
[harmonograph.py](https://github.com/TACHY0NN1X/harmongraphs_simply/harmonograph.py)\
[linegraph.py](https://github.com/TACHY0NN1X/harmongraphs_simply/linegraph.py)

All the math is pretty simple and basic\
Some images I generated :

# The classics :

<img src="https://raw.githubusercontent.com/TACHY0NN1X/harmongraphs_simply/main/001.png">
<img src="https://raw.githubusercontent.com/TACHY0NN1X/harmongraphs_simply/main/002.png">
<img src="https://raw.githubusercontent.com/TACHY0NN1X/harmongraphs_simply/main/003.png">

# Some Random :

<img src="https://raw.githubusercontent.com/TACHY0NN1X/harmongraphs_simply/main/016.png">
<img src="https://raw.githubusercontent.com/TACHY0NN1X/harmongraphs_simply/main/017.png">
<img src="https://raw.githubusercontent.com/TACHY0NN1X/harmongraphs_simply/main/018.png">
<img src="https://raw.githubusercontent.com/TACHY0NN1X/harmongraphs_simply/main/019.png">
<img src="https://raw.githubusercontent.com/TACHY0NN1X/harmongraphs_simply/main/032.png">
<img src="https://raw.githubusercontent.com/TACHY0NN1X/harmongraphs_simply/main/033.png">





