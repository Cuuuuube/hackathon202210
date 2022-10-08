import sys
""" 
#### factorial function example ### 
 fact n 
 n integer number
 commande_type fact
 args : n , positive integer 
 in  case of of negative return 0
"""

def factorielle(a):
    fact = 1
    while a > 0 :
        fact *= a
        a -= 1
    return fact

def cmd_fact(n):
    return str(factorielle(n))
