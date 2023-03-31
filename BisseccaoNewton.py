import numpy as np

# e = 2.718281
pi = 3.141593

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

    xFinal = x
    x = (a + b) / 2
    fx = F(x)
    currentPrecision = (b - a) / 2
    i += 1

  return xFinal

def Error(xn, xn1):
  return abs(xn - xn1)

def Newton(xn):
  print("Newton")
  print("x0 = " + str(xn))
  definedError = 0.0001
  while True:
    print(xn)
    x = xn - (F(xn)/Fd(xn))
    if (Error(x, xn) < definedError):
      return x
    xn = x

def PrintResults(): 
  b = Bissection()
  print("Resultado bissecção: " + str(b))
  print("-----------------------------------")

  n = Newton(b)
  print("Resultado Newton: " + str(n))

  #Considerando o valor n como absoluto e b como aproximação
  print("Valor absoluto: " + str(n))
  erroAbsoluto = Error(n, b);
  print("Erro absoluto Bissecção: |" + str(n) + " - " + str(b) + "| = " + str(erroAbsoluto))
  erroRelativo = erroAbsoluto / b
  print("Erro relativo Bissecção: |" + str(erroAbsoluto) + " / " + str(b) + "| = " + str(erroRelativo))

  erroAbsoluto = Error(n, n);
  print("Erro absoluto Newton: |" + str(n) + "-" + str(n) + "| = " + str(erroAbsoluto))
  erroRelativo = erroAbsoluto / n
  print("Erro relativo Newton: |" + str(erroAbsoluto) + " / " + str(n) + "| = " + str(erroRelativo))

PrintResults()
