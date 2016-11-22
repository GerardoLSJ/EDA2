// gcc -fopenmp hola.c -o hola
#include <stdio.h>
#include <stdlib.h>
#include <time.h>


int main() {
  int r = 100;
  int g=0;        //conteo de gotas
  int c=0;        //gotas dentro del circulo
  int x,y;      //Coordenadas
  int n = 20000000;  //veces que se reptie
  double pi;
  double elapsed;
  clock_t t1, t2;
  srand(time(NULL));

  int i;

  time_t start_t, end_t;
   double diff_t;

   printf("Starting of the program...\n");
   time(&start_t);



  #pragma omp parallel 
  {
    #pragma omp for
    for ( i=0; i < n; i++) {
      x = (rand() % (2*r) )- r; //-r para abarcar negativos
      y = (rand() % (2*r) )- r;
      #pragma omp critical (gplus)
      {
            g++; //contador de gotas totales
      }

      if ( ((x*x) + (y*y)) <= (r*r) ) { //Esta dentro del circulo
        #pragma omp critical (cplus)
        {
          c++;  //La  gota cayo adentro
        }

      }
    }

}//pragma

  pi = (c*4)/(double)g;
  
  printf("Gotas total: %d\n",g );
  printf("Gotas dentro: %d\n",c );
  printf("Pi:  %f\n",pi );

  time(&end_t);
  diff_t = difftime(end_t, start_t);

   printf("Execution time = %f\n", diff_t);
   printf("Exiting of the program...\n");
  return 0;
}


//TODO Speed up
