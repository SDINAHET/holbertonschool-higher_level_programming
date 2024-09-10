#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    if 0 <= idx < len(my_list):
        # Utilisation de l'instruction del pour supprimer l'élément
        del my_list[idx]
    return my_list
