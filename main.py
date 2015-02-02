# -*- coding: utf8 -*-

import numpy
from matplotlib import pyplot
import random


def load_data():
  global x, y, N
  x = numpy.loadtxt('data/x_C3.txt')
  N = len(x)
  y = numpy.loadtxt('data/y_C3.txt')


def theta(a):
  return numpy.dot(numpy.linalg.inv(numpy.dot(a, a.T)), numpy.dot(a, y))


def f_theta(matrix, theta):
  return numpy.dot(theta.T, matrix)


def enrichissement(matrix, ordre):
  tmp = numpy.vstack((numpy.ones(N), matrix))
  
  if ordre == 0:
    return numpy.ones(N)
    
  if ordre == 1:
    return tmp
  
  for i in range(2, ordre+1):
    tmp = numpy.vstack((tmp, numpy.power(matrix, i)))
    
  return tmp


def print_graphs():
  pyplot.figure(1)
  pyplot.plot(x, y, '.')
  pyplot.plot(x, f_theta(enrichissement(x, 10), theta(enrichissement(x, 10))), '.')
  pyplot.legend()
  pyplot.grid(True)
  pyplot.ylabel('y')
  pyplot.xlabel('x')

  pyplot.show()


def main():
  load_data()
  print "Matrice: \n", enrichissement(x, 10)
  print "Theta: ", theta(enrichissement(x, 10))
  print_graphs()
  
  a = numpy.array([0, 1, 2, 3, 4, 5])
  numpy.delete(a, 3)


if __name__ == '__main__':
  main()
  
