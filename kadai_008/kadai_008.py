# -*- coding: utf-8 -*-
"""kadai_008

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WZ0sawcoG5zbv3f9yfGLM48JX32QWfe2
"""

var = 15

if var % 3  == 0 and var % 5 == 0:
  print("FizzBuzz")

elif var % 3 == 0:
  print("Fizz")

elif var % 5 == 0:
  print("Buzz")

else:
  print(var)