'''
Author: Juan Felipe Lopez Sanabria
Date: 14/10/2022
Language: Python 3.0
'''

#Importaciones

from SinlgleLinkedList import SingleLinkedList
from DoubleLinkedList import DoubleLinkedList
from re import I
from colorama import *
init()

inst_SLL = SingleLinkedList()
inst_DLL = DoubleLinkedList()

#Creacion de la clase Menu

class Menu:

    #Constructor de la clase

    def __init__(self):
        self.option = 0

    #Metodos de la clase

        #Metodo para mostrar el menu

        def menu(self):
            print(Fore.CYAN + '1. Single Linked List')
            print('2. Double Linked List')
            print('3. Exit')
            print(Fore.RESET)
            
            self.option = int(input('Seleccione una opcion: '))
            if(self.option == 1):
                self.menu_SLL()
            elif(self.option == 2):
                self.menu_DLL()
            elif(self.option == 3):
                exit()

        #Metodo para mostrar el menu de la Single Linked List

        def menu_SLL(self):

            #Menu de la single linked list

            print(Fore.GREEN + '. Añadir nodo')
            print('2. Eliminar nodo')
            print('3. Consultar valor contenido en un nodo')
            print('4. Modificar valor de un nodo')
            print('5. Invertir toda la lista')
            print('6. Revertir la lista, pero los valores de los nodos se convierten en la raiz cuadrada de su valor original')
            print(Fore.RESET)

            #Opciones del menu

            self.option = int(input('Seleccione una opcion: '))
            if(self.option == 1):
                print(Fore.RED + '1. Añadir nodo al principio')
                print('2. Añadir nodo al final')
                print('3. Añadir nodo en una posicion especifica')
                self.option = int(input('Seleccione una opcion: '))

                #Opciones para añadir nodo
                
                if(self.option == 1):
                    inst_SLL.append_node(int(input('Ingrese el valor del nodo: ')))
                    inst_SLL.validate()
                elif(self.option == 2):
                    inst_SLL.append_node(int(input('Ingrese el valor del nodo: ')))
                    inst_SLL.validate()
                elif(self.option == 3):
                    inst_SLL.insert_node(int(input('Ingrese la posicion donde desea insertar el nodo: ')), int(input('Ingrese el valor del nodo: ')))
                    inst_SLL.validate()
                    print(Fore.RESET)

                #Opciones para eliminar nodo

            elif(self.option == 2):
                print(Fore.RED + '1. Eliminar nodo al principio')
                print('2. Eliminar nodo al final')
                print('3. Eliminar nodo en una posicion especifica')
                self.option = int(input('Seleccione una opcion: '))
                if(self.option == 1):
                    inst_SLL.shift_node()
                elif(self.option == 2):
                    inst_SLL.pop_node()
                elif(self.option == 3):
                    inst_SLL.remove_node(int(input('Ingrese la posicion del nodo que desea eliminar: ')))
                print(Fore.RESET)

                #Opcion para consultar el nodo

            elif(self.option == 3):
                print(Fore.RED)
                inst_SLL.get_node(int(input('Ingrese la posicion del nodo que desea consultar: ')))
                print(Fore.RESET)

                #Opcion para modificar el nodo

            elif(self.option == 4):
                print(Fore.RED)
                inst_SLL.update(int(input('Ingrese la posicion del nodo que desea modificar: ')), int(input('Ingrese el nuevo valor del nodo: ')))
                print(Fore.RESET)

                #opcion para invertir la lista

            elif(self.option == 5):
                print(Fore.RED)
                inst_SLL.reverse()
                print(inst_SLL)
                print(Fore.RESET)

                #Opciones especiales

            elif(self.option == 6):
                print(Fore.RED)
                print('En proceso')
                print(Fore.RESET)

        #Metodo para mostrar el menu de la Double Linked List

        def Menu_DLL(self):

            #Menu de la double linked list

            print(Fore.GREEN + '1. Añadir nodo')
            print('2. Eliminar nodo')
            print('3. Consultar valor contenido en un nodo')
            print('4. Modificar valor de un nodo')
            print('5. Invertir toda la lista')
            print('6. Validaciones especiales')
            print(Fore.RESET)

            #Opciones del menu

            self.option = int(input('Seleccione una opcion: '))
            if(self.option == 1):
                print(Fore.RED + '1. Añadir nodo al principio')
                print('2. Añadir nodo al final')
                print('3. Añadir nodo en una posicion especifica')
                print('4. Volver a menu principal')

                #Opciones para añadir nodo

                self.option = int(input('Seleccione una opcion: '))
                if(self.option == 1):
                    inst_DLL.push_head_node(int(input('Ingrese el valor del nodo: ')))
                    inst_DLL.validate()
                elif(self.option == 2):
                    inst_DLL.push_tail_node(int(input('Ingrese el valor del nodo: ')))
                    inst_DLL.validate()
                elif(self.option == 3):
                    inst_DLL.insert_node(int(input('Ingrese la posicion donde desea insertar el nodo: ')), int(input('Ingrese el valor del nodo: ')))
                    inst_DLL.validate()
                elif(self.option == 4):
                    self.Menu()
                print(Fore.RESET)

                #Opciones para eliminar nodo

            elif(self.option == 2):
                print(Fore.RED + '1. Eliminar nodo al principio')
                print('2. Eliminar nodo al final')
                print('3. Eliminar nodo en una posicion especifica')
                print('4. Volver a menu principal')
                self.option = int(input('Seleccione una opcion: '))
                if(self.option == 1):
                    inst_DLL.shift_head_node()
                elif(self.option == 2):
                    inst_DLL.pop_node()
                elif(self.option == 3):
                    inst_DLL.shift_search_node(int(input('Ingrese la posicion del nodo que desea eliminar: ')))
                elif(self.option == 4):
                    self.Menu()
                print(Fore.RESET)
            
                #Opcion para consultar el nodo

            elif(self.option == 3):
                print(Fore.RED)
                inst_DLL.get_node(int(input('Ingrese la posicion del nodo que desea consultar: ')))
                print(Fore.RESET)

                #Opcion para modificar el nodo

            elif(self.option == 4):
                print(Fore.RED)
                inst_DLL.update(int(input('Ingrese la posicion del nodo que desea modificar: ')), int(input('Ingrese el nuevo valor del nodo: ')))
                print(Fore.RESET)

                #Opcion para invertir la lista

            elif(self.option == 5):
                print(Fore.RED)
                inst_DLL.reverse_nodes()
                print(inst_DLL)
                print(Fore.RESET)

                #Opciones especiales

            elif(self.option == 6):
                print('1. Actualizar un nodo de la lista, pero el valor del nodo debe ser el cuadrado del valor del nodo anterior')
                print('2. Revertir la lista, pero los valores de los nodos se convierten en la raiz cuadrada de su valor original')
                print('3. Volver a menu principal')
                self.option = int(input('Seleccione una opcion: '))

                if(self.option == 1):
                    inst_DLL.update_node()
                elif(self.option == 2):
                    inst_DLL.reverse_nodes_sqrt()
                elif(self.option == 3):
                    self.Menu()