// gcc -fopenmp hola.c -o hola
#include <stdio.h>
#include <stdlib.h>
#include <omp.h>

int main() {
  int i;
  #pragma omp parallel num_threads(5) shared(i) //Compartimos la variable "i" y tenemos 5 threads
  {
    #pragma omp critical //Bloque atomico
    {
      int id = omp_get_thread_num();
      i = id;
      printf("La var fue mod por %d, nuevo i: %d\n",id,i );

    }


  }
  printf("\n");
  printf("Fin de EJECUACION\n");
  printf("varlor final de i: %d\n",i );
  printf("\n");
return 0;
}
