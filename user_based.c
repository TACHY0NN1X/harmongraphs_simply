#include <stdio.h>
#include <math.h>

#define STB_IMAGE_IMPLEMENTATION
#include "stb/stb_image.h"

#define STB_IMAGE_WRITE_IMPLEMENTATION
#include "stb/stb_image_write.h"

#define WIDTH  1000
#define HEIGHT 1000
#define CHANNELS 3

//#Image 1: f1=3.001 f2=2 f3=3 f4=2 d1=0.004 d2=0.0065 d3=0.008 d4=0.019 p1=0 p2=0 p3=pi/2 p4=3pi/2
//#Image 2: f1=10 f2=3 f3=1 f4=2 d1=0.039 d2=0.006 d3=0 d4=0.0045 p1=0 p2=0 p3=pi/2 p4=0
//#Image 3: f1=2.01 f2=3 f3=3 f4=2 d1=0.0085 d2=0 d3=0.065 d4=0 p1=0 p2=7 pi/16 p3=0 p4=0
//#Image 4: f1=2 f2=6 f3=1.002 f4=3 d1=0.02 d2=0.0315 d3=0.02 d4=0.02 p1=pi/16 p2=3pi/2 p3=13 pi/16 p4=pi

// Frequencies
float f1 = 3.001;
float f2 = 3.0;
float f3 = 3.0;
float f4 = 2.0;
//// Damp Force
float d1 = 0.004;
float d2 = 0.0065;
float d3 = 0.008;
float d4 = 0.018;
//// Phases
float p1 = 0.0;
float p2 = 0.0;
float p3 = 3 * M_PI_2;
float p4 = 3 * M_PI_2;

const float amp = HEIGHT/5.0;

unsigned char pixels[HEIGHT][WIDTH];
uint8_t image[ HEIGHT *  WIDTH * CHANNELS];

int main(int argc, char *argv[]){
   //if(argc != 2) {
   //   fprintf(stderr,"Please supply image name\n");
   //   return 0;
   //}

   char filename[ 32 ];
   printf( " Filename : " );
   scanf( "%s", &filename );

   float floats[ 12 ];
   int n = 0;
   int u = 1;
   for (; n < 4; n++ ){
      printf( " f%i : ", u++);
      scanf( "%f", &floats[n] );
   }

   u = 1;
   for (; n < 8; n++ ){
      printf( " d%i : ", u++ );
      scanf( "%f", &floats[n] );
   }

   u = 1;
   for (; n < 12; n++ ){
      printf( " p%i : pi * ", u++);
      scanf( "%f", &floats[n] );
   }
   // Frequencies
   f1 = floats[ 0 ];       
   f2 = floats[ 1 ];        
   f3 = floats[ 2 ];       
   f4 = floats[ 3 ];        
   // Damp Force
   d1 = floats[ 4 ];       
   d2 = floats[ 5 ];      
   d3 = floats[ 6 ];       
   d4 = floats[ 7 ];        
   // Phases
   p1 = M_PI * floats[ 8 ];        
   p2 = M_PI * floats[ 9 ];      
   p3 = M_PI * floats[ 10 ];      
   p4 = M_PI * floats[ 11 ];      

   int x, y;
   float t = 0;
   float dt = M_PI/(WIDTH+HEIGHT);
   int iterations = 100*(WIDTH+HEIGHT);

   for ( int i = 0; i < iterations; i++ ){
      x = amp * sin(f1*t+p1) * pow(M_E,(-t*d1)) +
          amp * sin(f2*t+p2) * pow(M_E,(-t*d2));
      y = amp * sin(f3*t+p3) * pow(M_E,(-t*d3)) +
          amp * sin(f4*t+p4) * pow(M_E,(-t*d4));

      x = ( int ) x + ( WIDTH / 2 );
      y = ( int ) y + ( HEIGHT / 2 );

      printf( "\r Calculating x : %d, y : %d ", x, y );

      if(x > 1 && y > 1 && y < HEIGHT-1 && x < WIDTH-1) {
         pixels[y+1][x-1] = 1+i*254/iterations;
         pixels[y+0][x-1] = 1+i*254/iterations;
         pixels[y-1][x-1] = 1+i*254/iterations;
         pixels[y+1][x+0] = 1+i*254/iterations;
         pixels[y+0][x+0] = 1+i*254/iterations;
         pixels[y-1][x+0] = 1+i*254/iterations;
         pixels[y+1][x+1] = 1+i*254/iterations;
         pixels[y+0][x+1] = 1+i*254/iterations;
         pixels[y-1][x+1] = 1+i*254/iterations;
      }
      t += dt;
   }

   int index = 0;
   for(y = 0; y < HEIGHT; y++) {
      for(x = 0; x < WIDTH; x++) {

         printf( "\r Co ordinate x : %d, y : %d ", x, y );
         if(pixels[y][x]>0) {
            image[ index++ ] = 128-pixels[y][x]/2 ;
            image[ index++ ] = 255-pixels[y][x]/2 ;
            image[ index++ ] = 128+pixels[y][x]/2 ;
         } else {
            image[ index++ ] = 0;
            image[ index++ ] = 0;
            image[ index++ ] = 0;
         }
      }
   }

   stbi_write_png( filename , WIDTH, HEIGHT, CHANNELS, image, WIDTH * CHANNELS );

   printf( " Done.\n" );
   return 0;
}


