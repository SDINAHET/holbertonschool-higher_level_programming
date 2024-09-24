#!/usr/bin/env python3
from task_02_verboselist import VerboseList

vl = VerboseList([1, 2, 3])
vl.append(4)      # Attendu : "Added [4] to the list."
vl.extend([5, 6]) # Attendu : "Extended the list with [2] items."
vl.remove(2)      # Attendu : "Removed [2] from the list."
vl.pop()          # Attendu : "Popped [6] from the list."
vl.pop(0)         # Attendu : "Popped [1] from the list."
