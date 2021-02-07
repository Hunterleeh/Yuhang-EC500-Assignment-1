import numpy as np

# Fahrenheit = (Celsius * 9/5) + 32
def c2f(c):
  if not isinstance(c, int):
    return "ERROR -----> It is not a int"
  
  f = (c * 9 / 5) + 32
  return round(f, 2) # Keep 2 decimals

# Celsius = (Fahrenheit – 32) * 5/9
def f2c(f):
  if not isinstance(f, int):
    return "ERROR -----> It is not a int"
  
  c = (f - 32) * 5 / 9
  return round(c, 2) # Keep 2 decimals
