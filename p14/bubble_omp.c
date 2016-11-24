#include <stdio.h>
#include <time.h>

int main() {

  int i,j;
  int dim = 20; //numero de elementos
  int bandera[dim-2]; //dim -2
  int temp;
  srand(time(NULL));
  int arr[dim];
  for (i = 0; i < dim; i++) {
    arr[i] = (rand()%1000)+1;
  }
  //Imprimir

for (i = 0; i < dim; i++) {
  printf("%d, ",arr[i] );
}

  printf("\n");
  //Imprimir

//Bubble Sort
#pragma omp parallel num_threads(dim-2) shared(bandera) //Compartimos la variable "i" y tenemos 5 threads
{
  int temp;
  int id = omp_get_thread_num();

  int valor = 1;
  while (valor) {

  if (arr[id] > arr[id+1]) {
    #pragma omp critical (one)
    {
      //printf("Thread: %d,   [%d] y [%d]\n",id,arr[id],arr[id+1]);
      temp    = arr[id];
      arr[id]  = arr[id+1];
      arr[id+1]  = temp;
      bandera[id] = 1;
    }
  }
  else{
    bandera[id] = 0;
  } //Critical


  if (arr[id+1] > arr[id+2]) {
    #pragma omp critical (two)
    {
        temp    = arr[id+1];
        arr[id+1]  = arr[id+2];
        arr[id+2]  = temp;
        bandera[id] = 1;
      } //Critical

}
else{
  bandera[id] = 0;
}

  #pragma omp barrier

  #pragma critical
  {
    if (id == 0) {
      for (i = 0; i < dim-2; i++) {
        if(bandera[i] > 0){
          valor = 1;
          break;
        }else{
          valor = 0;
        }
      }
    }
 }

} //while

}//End pragma
//Bubble Sort

//Imprimir
printf("Arr:\n");
  for (i = 0; i < dim; i++) {
    printf("%d  ", arr[i] );
  }
  //Imprimir
  return 0;
}
