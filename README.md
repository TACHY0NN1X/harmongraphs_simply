# harmongraphs_simply
Generating some cool harmongraph images with simple math and physics using simple code

All the code is inspired and based on this [awesome article](https://walkingrandomly.com/?p=151)\
It talks about how dampened oscillations can generate some pretty cool images\
with a simple equation 

<img src="https://render.githubusercontent.com/render/math?math=x_{(t)} = A \cdot \sin( \omega\cdot t %2B \phi ) \cdot e ^{ -d \cdot t}">

The scripts and C code are not interdependent

Python scripts require Pillow \
```pip install pillow```

C code requires for image operations [stb image library](https://github.com/nothings/stb)\
It is a single header based library without any dependencies\
It is awesome, and I can't thank the creators enough for it.
You need to make a folder/directory named **stb** and in it place : \
[+]https://github.com/nothings/stb/blob/master/stb_image.h \
[+]https://github.com/nothings/stb/blob/master/stb_image_write.h 

# C code :
Worked out together with Mike Field aka "hamster_nz" \
He's the most helpful \
Easter egg : I've been mentioned somewhere with another alias \
Go checkout his project : \
https://github.com/hamsternz/ProgrammingPosters

[user_based.c](https://github.com/TACHY0NN1X/harmongraphs_simply/blob/main/user_based.c)

**To compile**
```
gcc -o user_based user_based.c -lm
```

# Python Scripts :
[harmonograph.py](https://github.com/TACHY0NN1X/harmongraphs_simply/blob/main/harmonograph.py)\
[linegraph.py](https://github.com/TACHY0NN1X/harmongraphs_simply/blob/main/linegraph.py)

All the math is pretty simple and basic\
Some images I generated :

# The classics :

<img src="https://raw.githubusercontent.com/TACHY0NN1X/harmongraphs_simply/main/001.png">
<img src="https://raw.githubusercontent.com/TACHY0NN1X/harmongraphs_simply/main/002.png">
<img src="https://raw.githubusercontent.com/TACHY0NN1X/harmongraphs_simply/main/037.png">
<img src="https://raw.githubusercontent.com/TACHY0NN1X/harmongraphs_simply/main/038.png">
<img src="https://raw.githubusercontent.com/TACHY0NN1X/harmongraphs_simply/main/036.png">
<img src="https://raw.githubusercontent.com/TACHY0NN1X/harmongraphs_simply/main/003.png">

# Some Random :

<img src="https://raw.githubusercontent.com/TACHY0NN1X/harmongraphs_simply/main/016.png">
<img src="https://raw.githubusercontent.com/TACHY0NN1X/harmongraphs_simply/main/017.png">
<img src="https://raw.githubusercontent.com/TACHY0NN1X/harmongraphs_simply/main/018.png">
<img src="https://raw.githubusercontent.com/TACHY0NN1X/harmongraphs_simply/main/019.png">
<img src="https://raw.githubusercontent.com/TACHY0NN1X/harmongraphs_simply/main/032.png">
<img src="https://raw.githubusercontent.com/TACHY0NN1X/harmongraphs_simply/main/033.png">
<img src="https://raw.githubusercontent.com/TACHY0NN1X/harmongraphs_simply/main/030.png">
<img src="https://raw.githubusercontent.com/TACHY0NN1X/harmongraphs_simply/main/010.png">
<img src="https://raw.githubusercontent.com/TACHY0NN1X/harmongraphs_simply/main/012.png">
<img src="https://raw.githubusercontent.com/TACHY0NN1X/harmongraphs_simply/main/022.png">
<img src="https://raw.githubusercontent.com/TACHY0NN1X/harmongraphs_simply/main/023.png">
<img src="https://raw.githubusercontent.com/TACHY0NN1X/harmongraphs_simply/main/014.png">
<img src="https://raw.githubusercontent.com/TACHY0NN1X/harmongraphs_simply/main/029.png">
