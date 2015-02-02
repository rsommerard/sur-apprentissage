# -*- coding: utf8 -*-

import numpy
from matplotlib import pyplot
import random

def load_data():
  global t, p
  t = numpy.loadtxt('data/x_C3.txt')
  p = numpy.loadtxt('data/y_C3.txt')
  
def enrichissement(ligne, ordre):
  matrix = numpy.vstack((numpy.ones((1, len(ligne))), ligne))
  
  for i in range(2, ordre):
    matrix = numpy.vstack((matrix, numpy.power(ligne, i)))
    
  return matrix

def main():
  load_data()
  print enrichissement(t, 3)

if __name__ == '__main__':
  main()
  
