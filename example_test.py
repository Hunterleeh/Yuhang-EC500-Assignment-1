from example import *
import pytest

def test_c2f():
  #assert some right cases
  assert c2f(0) == 32.00
  assert c2f(100) == 212.00
  assert c2f(999) == 1830.20
  #assert some error here
  assert c2f("String") == "ERROR -----> It is not a int"
  assert c2f("-123") == "ERROR -----> It is not a int"
  assert c2f("ec500") == "ERROR -----> It is not a int"
  
def test_f2c():
  #assert some right cases
  assert f2c(32) == 0.00
  assert f2c(212) == 100.00
  assert f2c(932) == 500.00
  #assert some error here
  assert f2c("String") == "ERROR -----> It is not a int"
  assert f2c("-123") == "ERROR -----> It is not a int"
  assert f2c("ec500") == "ERROR -----> It is not a int"
