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

def meter2foot(m):
  if not isinstance(m, float):
    return "ERROR -----> It is not a number"
  if m < 0:
    return "ERROR -----> It is a negative number"
  f = 0.3048 * m
  return round(f, 2) # Keep 2 decimals

def foot2meter(f):
  if not isinstance(f, float):
    return "ERROR -----> It is not a number"
  if f < 0:
    return "ERROR -----> It is a negative number"
  m = 3.28 * f
  return round(m, 2) # Keep 2 decimals

def inch2meter(i):
  if not isinstance(i, float):
    return "ERROR -----> It is not a number"
  if i < 0:
    return "ERROR -----> It is a negative number"
  m = 39.37 * i
  return round(m, 2) # Keep 2 decimals

def meter2inch(m):
  if not isinstance(m, float):
    return "ERROR -----> It is not a number"
  if m < 0:
    return "ERROR -----> It is a negative number"
  i = 0.0254 * m
  return round(i, 4) # Keep 2 decimals

def KgtoPound(kg):
  if not isinstance(kg, float):
    return "ERROR -----> It is not a number"
  if kg < 0:
    return "ERROR -----> It is a negative number"
  p = 0.454 * kg
  return round(p, 3) # Keep 2 decimals

def PoundtoKg(p):
  if not isinstance(p, float):
    return "ERROR -----> It is not a number"
  if p < 0:
    return "ERROR -----> It is a negative number"
  kg = 2.2 * p
  return round(kg, 2) # Keep 2 decimals
