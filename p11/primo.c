// gcc -fopenmp hola.c -o hola
#include <stdio.h>
#include <stdlib.h>
#include <omp.h>

int isPrime(int i){
  int counter = 0;
  int j = 1;
  for ( j = 1; j <= i ; j++) {
    if( i % j == 0  &&   i != j  ){
      if ( j != 1 ) {
        return 0;
      }
    }
  }
  return 1;

}

int main() {
  int contador = 1;
  #pragma omp parallel num_threads(5) shared(contador) //Compartimos la variable "i" y tenemos 5 threads
  {
    int id = omp_get_thread_num();
    int temp ,res;
    #pragma omp critical //Bloque atomico
    {
      temp = contador;
      contador++;
    }
    //printf("Thread: %d\n",id );
    res = isPrime(temp);
    if(res == 1){
      printf("Numero primo: %d , thread: %d\n",temp,id );
    }


  }
  printf("\n");
  printf("Fin de EJECUACION\n");
  printf("varlor final de i: %d\n",contador );
  printf("\n");
return 0;
}
