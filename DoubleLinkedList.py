'''
Author: Juan Felipe Lopez Sanabria
Date: 14/10/2022
Language: Python 3.0
'''

import math


class DoubleLinkedList: 

    #* Clase Nodo
    class Node: 
        #*Inicializamos los valores del Nodo
        def __init__(self, value):
            self.value = value
            self.next = None
            self.previous = None

    #*Constructor de la clase
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    #*Metodo insertar al principio de la lista
    def push_head_node(self, value):
        #*Crear nuevo Nodo
        new_node = self.Node(value)

        #*Condicional para saber si la lista esta vacia
        if self.length == 0:
            self.head = new_node
            self.tail = new_node 
        else:
            #*Si la lista no está vacia se agrega el nodo al principio
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node

        self.length+=1
        
    #*Metodo insertar al final de la lista
    def push_tail_node(self, value):
        #*Crear nuevo Nodo
        new_node = self.Node(value)

        #*Condicional para saber si la lista esta vacia para agregar el nodo nuevo
        if self.length == 0:
            self.head = new_node
            self.tail = new_node 
        else:
            #*Si la lista no está vacia se agrega el nodo al final
            new_node.previous = self.tail
            self.tail.next = new_node
            self.tail = new_node

        self.length+=1
        
    #*Metodo para insertar un nodo en una posicion especifica
    def insert_node(self, index, value):
        #*Crear nuevo Nodo
        new_node = self.Node(value)
        
        #*Condicional para comparar el indice con la longitud de la lista
        if index == 0:
            #*Se agrega a la cabeza de la lista usando la funcion push_head_node
            self.push_head_node(value)
        elif index == self.length:
            #*Se agrega al final de la lista usando la funcion push_tail_node
            self.push_tail_node(value)
        elif index > 0 and index < self.length:
            #*Si no, se agrega en una posicion especifica
            current_node = self.head
            for i in range(index-1):
                current_node = current_node.next
            new_node.next = current_node.next
            new_node.previous = current_node
            current_node.next.previous = new_node
            current_node.next = new_node
            self.length+=1
        else:
            #*Si el indice es mayor o  menor a la longitud de la lista, se imprime un mensaje de error
            print('index out of range')
            
    

    #*Metodo para mostrar la lista
    def show_list(self):
        print_dll = []
        current_node = self.head

        #*Recorremos la lista
        while current_node != None: 
            #*Agregamos los valores de los nodos a la lista
            print_dll.append(current_node.value)
            current_node = current_node.next

        #*Imprimimos la lista
        print(f'lista actual: {print_dll} \n cantidad de nodos {self.length}' )
        
    #*Metodo para eliminar el primer nodo
    def shift_head_node(self):
        
        #*Condicional para saber si la lista esta vacia
        if self.length == 0:
            self.head = None
            self.tail = None 
        
        #*Si la lista no está vacia se elimina el primer nodo
        else: 
            remove_node = self.head
            self.head = remove_node.next 
            remove_node.next = None 
            self.head.previous = None
        self.length-=1

    #*Metodo para eliminar el ultimo nodo
    def pop_node(self):
        if self.length == 0:  
            self.head = None
            self.tail = None 
        else: 
            remove_node = self.tail 
            self.tail = remove_node.previous  
            remove_node.previous = None
            self.tail.next = None
        self.length-=1

    #*Metodo para eliminar un nodo en una posicion especifica por valor del nodo
    def shift_search_node(self, value):
        #*Condicional para saber si la lista esta vacia
        if self.length == 0:
            print('Lista vacía')
        #*Si la lista no esta vacia se busca el nodo por valor
        else:
            current_node = self.head
            #*Recorremos la lista
            while (current_node != None):
                if current_node.value == value:
                    if current_node == self.head:
                        self.shift_head_node()
                    elif current_node == self.tail:
                        self.pop_node()
                    else:
                        current_node.previous.next = current_node.next
                        current_node.next.previous = current_node.previous
                        current_node.next = None
                        current_node.previous = None
                        self.length-=1
                current_node = current_node.next

    #*Metodo para invertir los valores de la lista
    def reverse_nodes(self):
        #*Condicional para saber si la lista esta vacia
        if self.length == 0: 
            print('Lista vacía')
        
        #*Si la lista no esta vacia se invierten los valores de los nodos
        else:
            current_node1 = self.head
            current_node2 = current_node1.next
            current_node1.next = None
            current_node1.previous = current_node2
            self.tail = current_node1

            while current_node2 is not None:
                current_node2.previous = current_node2.next
                current_node2.next = current_node1
                current_node1 = current_node2
                current_node2 = current_node2.previous

            self.head = current_node1

        #Consultar el valor de un nodo en una posicion especifica
    def get_node(self, index):
        #Condicional para saber si la lista esta vacia
        if self.length == 0:
            print('Lista vacía')
        #Si la lista no esta vacia se busca el nodo por valor
        else:
            current_node = self.head
            #*Recorremos la lista
            for i in range(index):
                current_node = current_node.next
            return current_node.value

        #Metodo para modificar el valor de un nodo en una posicion especifica
    def update(self, index, value):
        #Condicional para saber si la lista esta vacia
        if self.length == 0:
            print('Lista vacía')
        #Si la lista no esta vacia se busca el nodo por valor
        else:
            current_node = self.head
            #*Recorremos la lista
            for i in range(index):
                current_node = current_node.next
            current_node.value = value

        #Valida que no hayan numeros repetidos en los nodos

    def validate(self):
        # Valida que no haya numeros repetidos en la linkedlist
        current_node = self.head
        while current_node != None:
            if current_node.value == current_node.linked_next_node.value:
                return False
            current_node = current_node.linked_next_node
        return True

        #Actualizar un nodo por posicion y valor siendo el valor el cuadrado del valor del nodo anterior

    def update_node(self, index, value):
        if self.length == 0:
            print('Lista vacía')
        else:
            current_node = self.head
            for i in range(index):
                current_node = current_node.next
            current_node.value = current_node.previous.value**2

        #Revertir la lista, pero los valores deben ser la raiz cuadrada de los valores originales

    def reverse_sqrt(self):
        current_node = self.head
        while current_node != None:
            current_node.value = math.sqrt(current_node.value)
            current_node = current_node.linked_next_node
        return self.head
