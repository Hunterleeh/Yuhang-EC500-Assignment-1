import string

units=['meter', 'meters',
       'foot', 'feet',
       'inch', 'inches',
       'kilogram', 'kilograms',
       'pound', 'pounds',
       'Celsius', 'Fahrenheit']

# Fahrenheit = (Celsius * 9/5) + 32
def c2f(c):
  if not isinstance(c, int) and not isinstance(c, float):
    return "ERROR -----> It is not a number"  
  f = (c * 9 / 5) + 32
  return round(f, 2) # Keep 2 decimals

# Celsius = (Fahrenheit – 32) * 5/9
def f2c(f):
  if not isinstance(f, int) and not isinstance(f, float):
    return "ERROR -----> It is not a number"
  c = (f - 32) * 5 / 9
  return round(c, 2) # Keep 2 decimals

def meter2foot(m):
  if not isinstance(m, float) and not isinstance(m, int):
    return "ERROR -----> It is not a positive number"
  if m < 0:
    return "ERROR -----> It is not a positive number"
  f = 0.3048 * m
  return round(f, 2) # Keep 2 decimals

def foot2meter(f):
  if not isinstance(f, float) and not isinstance(f, int):
    return "ERROR -----> It is not a positive number"
  if f < 0:
    return "ERROR -----> It is not a positive number"
  m = 3.28 * f
  return round(m, 2) # Keep 2 decimals

def meter2inch(i):
  if not isinstance(i, float) and not isinstance(i, int):
    return "ERROR -----> It is not a positive number"
  if i < 0:
    return "ERROR -----> It is not a positive number"
  m = 39.37 * i
  return round(m, 2) # Keep 2 decimals

def inch2meter(m):
  if not isinstance(m, float) and not isinstance(m, int):
    return "ERROR -----> It is not a positive number"
  if m < 0:
    return "ERROR -----> It is not a positive number"
  i = 0.0254 * m
  return round(i, 2) # Keep 2 decimals

def KgtoPound(kg):
  if not isinstance(kg, float) and not isinstance(kg, int):
    return "ERROR -----> It is not a positive number"
  if kg < 0:
    return "ERROR -----> It is not a positive number"
  p = 0.454 * kg
  return round(p, 3) # Keep 3 decimals

def PoundtoKg(p):
  if not isinstance(p, float) and not isinstance(p, int):
    return "ERROR -----> It is not a positive number"
  if p < 0:
    return "ERROR -----> It is not a positive number"
  kg = 2.2 * p
  return round(kg, 2) # Keep 2 decimals

#The program has a fixed stucture: What is xxx xxx in xxx
def breaker(texture):
  if len(texture.split()) != 6:
    return "ERROR -----> You have inputed an invalid texture!"
  information = [0, '', '']
  information[0] = float(texture.split()[2])
  information[1] = texture.split()[3]
  information[2] = texture.split()[5]
  if not information[1] in units or not information[2] in units:
    return "ERROR -----> You have inputed an invalid texture!"
  return information

def convertor(texture):
  num, source_unit, goal_unit = breaker(texture)
  if (source_unit == units[0] or source_unit == units[1]) and (goal_unit == units[2] or goal_unit == units[3]):
    return meter2foot(num)
  elif (source_unit == units[2] or source_unit == units[3]) and (goal_unit == units[0] or goal_unit == units[1]):
    return foot2meter(num)
  elif (source_unit == units[0] or source_unit == units[1]) and (goal_unit == units[4] or goal_unit == units[5]):
    return meter2inch(num) 
  elif (source_unit == units[4] or source_unit == units[5]) and (goal_unit == units[0] or goal_unit == units[1]):
    return inch2meter(num)
  elif (source_unit == units[6] or source_unit == units[7]) and (goal_unit == units[8] or goal_unit == units[9]):
    return KgtoPound(num)
  elif (source_unit == units[8] or source_unit == units[9]) and (goal_unit == units[6] or goal_unit == units[7]):
    return PoundtoKg(num)
  elif source_unit == units[10] and goal_unit == units[11]:
    return c2f(num)
  elif source_unit == units[11] and goal_unit == units[10]:
    return f2c(num)
  else:
    return "ERROR -----> You have inputed an invalid unit pair!"
  
#This is a demo!!!!!!!!
#info = breaker("what is 100 inches in meters")
#result = convertor(info[0], info[1], info[2])

