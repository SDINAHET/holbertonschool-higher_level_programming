#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            # Essayer d'accéder aux deux éléments et de faire la division
            num1 = my_list_1[i]
            num2 = my_list_2[i]
            result = num1 / num2
        except IndexError:
            # Si une des listes est trop courte
            print("out of range")
            result = 0
        except TypeError:
            # Si un élément n'est pas un nombre (int ou float)
            print("wrong type")
            result = 0
        except ZeroDivisionError:
            # Division par zéro
            print("division by 0")
            result = 0
        finally:
            # Ajouter le résultat (même s'il est 0) à la nouvelle liste
            new_list.append(result)
    return new_list
