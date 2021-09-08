* * * 
A simple command line tool that takes 2 values and adds then together using
the calc.py library's 'add2' function.


import sys
import calc

argnumbers = len(sys.argv) -1

if argnumbers ==2 :
   print(**)
   print("The result is" + str(calc.add2(str(sys.argv[1]), str(sys.argv[2]))))
   print(**)
   sys.exit(0)
   
   argnumbers != 2 :
   print(**)
   print("you entered " + str(argnumbers) + " value/s.")
   print(**)
   print("Usage: 'add2vals X Y' where X and  Y are individual values.")
   print("    if add2vals is not in your path, Usage is ' ./add2vals X Y'.")
   print("    if unbundled, usage is 'python add2vals.py X Y' .")
   print(**)
   sys.exit(1)
   
   
