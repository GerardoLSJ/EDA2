#include <stdio.h>
#include <stdlib.h>
#include <omp.h>

int main() {
  int i;
  #pragma omp parallel{
    for ( i = 0; i < 10; i++) {
      printf("Hola mundo\n");
    }
    return 0;
  }

}
