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


def training_matrix(k):
  tmpx = x
  tmpy = y

  rnd = numpy.arange(N)
  numpy.random.shuffle(rnd)
  print N/k
  for i in range(0, (N/k)):
    print rnd[i]
    tmpx = numpy.delete(tmpx, rnd[i])
    tmpy = numpy.delete(tmpy, rnd[i])

  print len(tmpx)
  print len(tmpy)
  return tmpx, tmpy


def main():
  load_data()
  
  K = 10

  matrix = enrichissement(x, 1)
  test = numpy.split(x, K)

  print numpy.concatenate(test)
  print len(numpy.concatenate(test))

  """matrix = enrichissement(x, 1)
  theta = calc_theta(matrix)
  error = j_theta(matrix, y, theta)
  print "Ordre: 1"
  print "Theta: ", theta
  print "Erreur: ", error

  matrix = enrichissement(x, 10)
  theta = calc_theta(matrix)
  error = j_theta(matrix, y, theta)
  print "Ordre: 10"
  print "Theta: ", theta
  print "Erreur: ", error

  matrix = enrichissement(x, 20)
  theta = calc_theta(matrix)
  error = j_theta(matrix, y, theta)
  print "Ordre: 20"
  print "Theta: ", theta
  print "Erreur: ", error

  matrix = enrichissement(x, 23)
  theta = calc_theta(matrix)
  error = j_theta(matrix, y, theta)
  print "Ordre: 23"
  print "Theta: ", theta
  print "Erreur: ", error

  matrix = enrichissement(x, 25)
  theta = calc_theta(matrix)
  error = j_theta(matrix, y, theta)
  print "Ordre: 25"
  print "Theta: ", theta
  print "Erreur: ", error"""

  """K = 10
  ordre = 1
  diff = 1
  while(diff > 0):
    matrix = enrichissement(x, ordre)
    for i in range(0, 10):
      tx, ty = training_matrix(K)
      theta = theta(training)
      error = j_theta(training, y, theta)
      diff = error - diff"""

  #matrix = enrichissement(x, 1)
  #theta = theta(matrix)

  #print "Matrice: \n", enrichissement(x, 10)
  #print "Theta: ", theta(enrichissement(x, 10))
  #print_graphs()


if __name__ == '__main__':
  main()
  
