from converter import *
import pytest

def test_c2f():
  assert some right cases
  assert c2f(0) == 32.00
  assert c2f(100) == 212.00
  assert c2f(999) == 1830.20
  assert some error here
  assert c2f("String") == "ERROR -----> It is not a int"
  assert c2f("-123") == "ERROR -----> It is not a int"
  assert c2f("ec500") == "ERROR -----> It is not a int"
  
def test_f2c():
  pass