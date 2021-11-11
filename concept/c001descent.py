# Just try the idea of gradient descent and cost function.
# Below, there are 2 sample cost functions: f_kuadrat(x) and f_contoh(x)

import random

def cari_minimum(costf, steps = 20, rate = 0.1, xrange = [-10, 10]):
  '''Return x and minimum costf(x) given number of steps and learning rate.'''
  x = random.randint(xrange[0], xrange[1])
  cx = costf(x)
  print(f'Started with x = {x} and cost = {cx}')

  # Every step contains (x, cost(x), d_x, d_cost)
  lacak = [(x, cx, 0, 0)]

  def gradiencx(x, r = rate, kiri = True):
    '''A simple gradient calculator'''
    tengah = costf(x)
    if kiri:
      return (tengah - costf(x - r)) / r
    else:
      return (costf(x + r) - tengah) / r

  # Put every step inside lacak (tracker)
  for i in range(steps):
    x = lacak[i][0] - rate * gradiencx(lacak[i][0])
    cx = costf(x)
    dx = x - lacak[i][0]
    dc = cx - lacak[i][1]
    lacak.append((x, cx, dx, dc))

  return x, cx, lacak

def f_kuadrat(x):
  '''Return power of 2 of x, minimum at x = 0'''
  return x*x

def f_contoh(x):
  '''Local minima at x = [3, -2, 0]'''
  if x < -1: return (x + 2) ** 2
  if -1 <= x < 2: return abs(x) + 1
  if 2 <= x < 3: return (x - 4) ** 2 - 2
  if 3 <= x: return x - 4

x, cost, track = cari_minimum(f_contoh, 100)
print('Ended with x = {0:.2f} and cost = {1:.2f}'.format(x, cost))
