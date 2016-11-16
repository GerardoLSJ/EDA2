#include <stdio.h>
#include <stdlib.h>
#include <time.h>



int main() {
  long sum_p = 0, suma_n = 0;
  long sum = 1;
  int n = 4;
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

//Sacar diagonales

  for ( i = 0; i < n; i++) {
    for ( j = 0; j < n; j++) {
      printf("[%d,%d]",j,(j+i)%n );
      sum*=m[j][(j+i)%n];


    }
    sum_p += sum;
    printf("Suma:%li \n",sum );

    sum = 1;
  }
printf("Suma posi: %li\n",sum_p );
  return 0;
}
