# -*- coding: utf8 -*-

import numpy
from matplotlib import pyplot
import random


def load_data():
  global x, y, N
  x = numpy.loadtxt('data/x_C3.txt')
  N = len(x)
  y = numpy.loadtxt('data/y_C3.txt')


def calc_theta(a):
  return numpy.dot(numpy.linalg.inv(numpy.dot(a, a.T)), numpy.dot(a, y))


def f_theta(matrix, theta):
  return numpy.dot(theta.T, matrix)


def j_theta(a, b, theta):
  tmp = (b - numpy.dot(a.T, theta))
  return ((1.0/N) * numpy.dot(tmp.T, tmp))


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
  
  K = 10
  i = 1
  
  print "Ordre: ", i
  error = 0
  for part in range(0, K):
    matrix_x = numpy.split(x, K)
    matrix_y = numpy.split(y, K)
  
    matrix_x.pop(part)
    matrix_y.pop(part)
  
    numpy.concatenate(matrix_x)
    numpy.concatenate(matrix_y)
    
    matrix_x = numpy.array(matrix_x)
    matrix_y = numpy.array(matrix_y)
    
    print matrix_x
    print matrix_y
      
    theta = calc_theta(matrix_x)
    error = error + j_theta(matrix_x, matrix_y, theta)
    
  error = (error / K)
  print "Erreur: ", error
  diff = error
  
  while(diff > 0):
    i = i + 1
    print "Ordre: ", i
    error = 0
    for part in range(0, K):
      matrix_x = numpy.split(x, K)
      matrix_y = numpy.split(y, K)
  
      matrix_x.pop(part)
      matrix_y.pop(part)
  
      numpy.concatenate(matrix_x)
      numpy.concatenate(matrix_y)
      
      matrix_x = numpy.array(matrix_x)
      matrix_y = numpy.array(matrix_y)
      
      theta = calc_theta(matrix_x)
      error = error + j_theta(matrix_x, matrix_y, theta)
    
    error = (error / K)
    print "Erreur: ", error
    diff = diff - error
    print "Diff: ", diff

  #print "Matrice: \n", enrichissement(x, 10)
  #print "Theta: ", theta(enrichissement(x, 10))
  #print_graphs()


if __name__ == '__main__':
  main()
  
