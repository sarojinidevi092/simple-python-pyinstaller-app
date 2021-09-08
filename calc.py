***
The 'calc' library contains the 'add2' function that takes 2 values and adds
then together. if either value is a string (or both then are) 'add2' ensures
they are both strings, thereby resulting in a concatenated result.
NOTE: If a value submitted to the 'add2' function is a float, it must be done so
in quotes (i.e. as a string).
* * *

def conv(value):
    try:
       return int(value)
    except valueError:
      try:
          return float(value)
      except valueError:
         return str(value)
def add2(arg1, arg2):
    argiconv = conv(arg1)
    arg2conv = conv(arg2)
    if isinstance(arg1conv, str) or isinstance(arg2conv, str):
       arg1conv = str(arg1conv)
       arg2conv = str(arg2conv)
      if isinstance(arg1conv, str) or isinstance(arg2conv, str):
          arg1conv = str(arg1conv)
          arg2conv = str(arg2conv)
      return arg1conv + arg2conv    
