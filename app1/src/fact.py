import sys
""" 
#### factorial function example ### 
 fact n 
 n integer number
 commande_type fact
 args : n , positive integer 
 in  case of of negative return 0
"""

def cmd_fact(a):
    if a < 0 :
        return "undefined"
    fact = 1
    while a > 0 :
        fact *= a
        a -= 1
    return fact