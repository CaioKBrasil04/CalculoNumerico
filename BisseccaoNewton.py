import numpy as np

e = 2.718281
pi = 3.141593

#e**(-(x**2)) - np.cos(x)
#(e**(-(x**2))- np.cos(x)) / (-2*x*(e**(-(x**2)) + np.sin(x)))

def F(x):
  return np.sin(x) - np.cos(x)

def Fd(x):
  return np.cos(x) + np.sin(x)

def IntervalIsValid(a, b):
  return F(a)*F(b) < 0

def IntervalIsUnique(a, b):
  return not SignalChange(Fd(a), Fd(b))

def SignalChange(v, x):
  return (v > 0 and x < 0) or (v < 0 and x > 0)

def Bissection():
  a = pi/6
  b = pi/2

  if not IntervalIsValid(a, b):
    return 0
  if not IntervalIsUnique(a, b):
    return 0

  print("Bissecção")
  print("Intervalo definido - [" + str(a) + ", " + str(b) + "]")
  definedPrecision = 0.0001
  x = (a + b) / 2

  fa = F(a)
  fx = F(x)
  fb = F(b)

  currentPrecision = (b - a) / 2
  i = 0
  while currentPrecision > definedPrecision and i < 3:
    print("a: " + str(a) + "\nx: " + str(x) + "\nb: " + str(b) +
          "\nfa: " + str(fa) + "\nfx: " + str(fx) + "\nfb: " + str(fb) + "\nprec: " + str(currentPrecision) + "\n")

    if SignalChange(fa, fx):
      b = x
      fb = fx
    else:
      a = x
      fa = fx

    x = (a + b) / 2
    fx = F(x)
    currentPrecision = (b - a) / 2
    i += 1

  return x

def Error(xn, xn1):
  return abs(xn - xn1)

def Newton():
  print("Newton")
  xn = 0.654498541
  print("x0 = " + str(xn))
  definedError = 0.0001
  while True:
    print(xn)
    x = xn - (F(xn)/Fd(xn))
    if (Error(x, xn) < definedError):
      return x
    xn = x

b = Bissection()
print(b)
print("-----------------------------------")

n = Newton()
print(n)

print("Erro absoluto: |" + str(n) + "-" + str(b) + "| = " + str(Error(n, b)))