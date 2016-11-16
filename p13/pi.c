// gcc -fopenmp hola.c -o hola
#include <stdio.h>
#include <stdlib.h>
#include <time.h>


int main() {
  int r = 100;
  int g=0;        //conteo de gotas
  int c=0;        //gotas dentro del circulo
  int x,y;      //Coordenadas
  int n = 50000;  //veces que se reptie
  double pi;
  double elapsed;
  clock_t t1, t2;
  srand(time(NULL));

  int i;
  t1 = clock();
  #pragma omp parallel
  {
    #pragma omp for
    for ( i=0; i < n; i++) {
      x = (rand() % (2*r) )- r; //-r para abarcar negativos
      y = (rand() % (2*r) )- r;
      #pragma omp critical
      {
            g++; //contador de gotas totales
      }

      if ( ((x*x) + (y*y)) <= (r*r) ) { //Esta dentro del circulo
        #pragma omp critical
        {
          c++;  //La  gota cayo adentro
        }

      }
    }

}//pragma

  pi = (c*4)/(double)g;
  t2 = clock();
  elapsed = (t2-t1);
  printf("Gotas tota + %d\n",g );
  printf("Gotas dentro + %d\n",c );
  printf("Pi:  %f\n",pi );
  printf("t1  %li\n",t1 );
  printf("t2  %li\n",t2 );
  printf("elapsed  %f\n",elapsed );
  return 0;
}


//TODO Speed up
