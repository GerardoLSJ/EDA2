#include <stdio.h>
#include <stdlib.h>
#include <time.h>



int main() {
  long sum_p = 0, suma_n = 0;
  //long sum = 1;
  int n = 2;
  int m[n][n];
  int i,j;
  srand(time(NULL));

//Llenar matriz
  for (i = 0; i < n; i++) {
    for ( j = 0; j < n; j++) {
      m[i][j] = (rand() % n) +1;
    printf(" %d",m[i][j]);
    }
    printf("\n");
  }

//Sacar diagonales positivas
#pragma omp parallel num_threads(n)
{
    long sum = 1;
    //for ( i = 0; i < n; i++) { }
    i = omp_get_thread_num();
      for ( j = 0; j < n; j++) {
        #pragma omp critical
        {
          printf("[%d,%d]",j,(j+i)%n );
          sum*=m[j][(j+i)%n];
        }



      }
      #pragma omp critical
      {
        sum_p += sum;
      }
      printf("Thread() %d Suma:%li \n",i,sum );

      sum = 1;

}


//Sacar diagonales negativas
/*
#pragma omp parallel num_threads(n)
{
}

*/

printf("Suma posi: %li\n",sum_p );
  return 0;
}
