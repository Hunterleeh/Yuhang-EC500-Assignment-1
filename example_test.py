from example import *
import pytest

def test_c2f():
  #assert some right cases
  assert c2f(0) == 32.00
  assert c2f(100) == 212.00
  assert c2f(999) == 1830.20
  #assert some error here
  assert c2f("String") == "ERROR -----> It is not a number"
  assert c2f("-123") == "ERROR -----> It is not a number"
  assert c2f("ec500") == "ERROR -----> It is not a number"
  
def test_f2c():
  #assert some right cases
  assert f2c(32) == 0.00
  assert f2c(212) == 100.00
  assert f2c(932) == 500.00
  #assert some error here
  assert f2c("String") == "ERROR -----> It is not a number"
  assert f2c("-123") == "ERROR -----> It is not a number"
  assert f2c("ec500") == "ERROR -----> It is not a number"

def test_meter2foot():
  #assert some right cases
  assert meter2foot(0) == 0.00
  assert meter2foot(50) == 15.24
  assert meter2foot(100.5) == 30.63
  #assert some error here
  assert meter2foot("String") == "ERROR -----> It is not a positive number"
  assert meter2foot(-123) == "ERROR -----> It is not a positive number"
  assert meter2foot("ec500") == "ERROR -----> It is not a positive number"
  
  
def test_foot2meter():
  #assert some right cases
  assert foot2meter(0) == 0.00
  assert foot2meter(50) == 164.00
  assert foot2meter(100.5) == 329.64
  #assert some error here
  assert foot2meter("String") == "ERROR -----> It is not a positive number"
  assert foot2meter(-123) == "ERROR -----> It is not a positive number"
  assert foot2meter("ec500") == "ERROR -----> It is not a positive number"
  
def test_inch2meter():
  #assert some right cases
  assert inch2meter(0) == 0.00
  assert inch2meter(50) == 1.27
  assert inch2meter(100.5) == 2.55
  #assert some error here
  assert inch2meter("String") == "ERROR -----> It is not a positive number"
  assert inch2meter(-123) == "ERROR -----> It is not a positive number"
  assert inch2meter("ec500") == "ERROR -----> It is not a positive number"

def test_meter2inch():
  #assert some right cases
  assert meter2inch(0) == 0.00
  assert meter2inch(50) == 1968.50 
  assert meter2inch(100.5) == 3956.68
  #assert some error here
  assert meter2inch("String") == "ERROR -----> It is not a positive number"
  assert meter2inch(-123) == "ERROR -----> It is not a positive number"
  assert meter2inch("ec500") == "ERROR -----> It is not a positive number"
  
def test_KgtoPound():
  #assert some right cases
  assert KgtoPound(0) == 0.000
  assert KgtoPound(50) == 22.700
  assert KgtoPound(100.5) == 45.627
  #assert some error here
  assert KgtoPound("String") == "ERROR -----> It is not a positive number"
  assert KgtoPound(-123) == "ERROR -----> It is not a positive number"
  assert KgtoPound("ec500") == "ERROR -----> It is not a positive number"
  
def test_PoundtoKg():
  #assert some right cases
  assert PoundtoKg(0) == 0.00
  assert PoundtoKg(50) == 110.00
  assert PoundtoKg(100.5) == 221.10
  #assert some error here
  assert PoundtoKg("String") == "ERROR -----> It is not a positive number"
  assert PoundtoKg(-123) == "ERROR -----> It is not a positive number"
  assert PoundtoKg("ec500") == "ERROR -----> It is not a positive number"

def test_breaker():
  #assert some right cases
  assert breaker("what is 100 inches in meters") == [100.0, 'inches', 'meters']
  assert breaker("what is 100 meters in feet") == [100.0, 'meters', 'feet']
  assert breaker("what is 100 Celsius in Fahrenheit") == [100.0, 'Celsius', 'Fahrenheit']
  assert breaker("what is 100 kilograms in kilograms") == [100.0, 'kilograms', 'kilograms']
  #assert some error cases
  assert breaker("So what is 100 inches in meters") == "ERROR -----> You have inputed an invalid texture!"
  assert breaker("what is 100 meters") == "ERROR -----> You have inputed an invalid texture!"
  assert breaker("what is 100 Celsius in F") == "ERROR -----> You have inputed an invalid texture!"

def test_convertor():
  #assert some right cases
  assert convertor("what is 50 inches in meters") == 1.27
  assert convertor("what is 50 meters in inches") == 1968.50
  assert convertor("what is 50 meters in feet") == 15.24
  assert convertor("what is 50 feet in meters") == 164.00
  assert convertor("what is 50 kilograms in pounds") == 22.700
  assert convertor("what is 50 pounds in kilograms") == 110.00
  assert convertor("what is 100 Celsius in Fahrenheit") == 212.00
  assert convertor("what is 212 Fahrenheit in Celsius") == 100.00
  #assert some error cases
  assert convertor("what is 212 Fahrenheit in Fahrenheit") == "ERROR -----> You have inputed an invalid unit pair!"
  assert convertor("what is 212 kg in pounds") == "ERROR -----> You have inputed an invalid texture!"
