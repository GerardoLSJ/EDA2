#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

typedef struct nodo nodo;
struct nodo{
    nodo *next;
    int key;
};

nodo *head = NULL, *tail = NULL;

nodo* crear(int e){
  nodo *nuevo =  malloc(sizeof(nodo));
  nuevo->key = e;
  return nuevo;
}

void enq(int e){
  nodo *nodo = crear(e);
  if(head == NULL){
      head = nodo;  //La cola esta vacia
      tail = nodo;
  }else{
    tail->next = nodo;
    tail = tail->next;
  }

}

int deq(){
  if(head != NULL){
      nodo *tmp = head;
      head = head->next;
      if(head == NULL){
        tail = NULL;
      }
      return tmp->key;
}else{
  return -1;
}

}

void imprimir_cola(){
  nodo *aux = head;
  printf("Contenido de la cola { ");
  while (aux != NULL) {
    printf("%i , ",aux->key );
    aux = aux->next;
  }
  printf("}");
}


int main() {
  #pragma omp parallel num_threads(10)
  {
      int id = omp_get_thread_num();
      enq(id);
      #pragma omp critical
      {
        imprimir_cola();
        printf("Eliminando: %d thread: %d\n",deq(),id );

      }


  }

  return 0;
}
