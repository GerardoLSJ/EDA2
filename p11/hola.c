// gcc -fopenmp hola.c -o hola
#include <stdio.h>
#include <stdlib.h>
#include <omp.h>

int main() {
  int i;
  #pragma omp parallel num_threads(5)
  {
    int id = omp_get_thread_num();
    printf("Hola mundo\n");
    for ( i = 0; i < 10; i++) {
      printf("Al Thread %d, numero: %d\n",id,i );
    }

  }
return 0;
}
