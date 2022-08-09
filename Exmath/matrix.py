#working
from numpy import matrix

#working
def checkRows(matrix):
  hist = None
  for x in matrix:
    if(hist != None and hist != len(x)):
      return False
    hist = len(x)
  return True

#working
def formatMatrix(matrix):
  new_matrix = []
  for x in matrix:
    if(type(x) != list):
      new_matrix.append([x])
    else:
      new_matrix.append(x)
  return new_matrix


def additionSMx(scaler, matrix):
  format_matrix = formatMatrix(matrix)
  new_matrix = []
  for n in format_matrix:
    row = []
    for m in n:
      row.append(m + scaler)
    new_matrix.append(row)
  return new_matrix

#working
def multiplicationSMx(scaler, matrix):
  format_matrix = formatMatrix(matrix)
  new_matrix = []
  for n in format_matrix:
    row = []
    for m in n:
      row.append(m * scaler)
    new_matrix.append(row)
  return new_matrix

#working
def additionMMx(matrixA, matrixB):
  format_matrixA = formatMatrix(matrixA)
  format_matrixB = formatMatrix(matrixB)
  nA = len(format_matrixA)
  nB = len(format_matrixB)
  mA = len(format_matrixA[0])
  mB = len(format_matrixB[0])
  if(checkRows(format_matrixA) and checkRows(format_matrixB) and nA == nB and mA == mB):
    new_matrix = []
    for i in range(0,len(format_matrixA)):
      row = []
      for x in range(0, mA):
        row.append(format_matrixA[i][x] + format_matrixB[i][x])
      new_matrix.append(row)
    return new_matrix

#working
def cols(matrix):
  colsmatrix = []
  format_matrix = formatMatrix(matrix)
  
  for x in format_matrix:
    if(colsmatrix == []):
      for i in x:
        colsmatrix.append([i])
    else:
      for i in range(len(x)):
        colsmatrix[i].append(x[i])

  return colsmatrix

def dotproductVVx(vectorA, vectorB):
  vectorAB = 0
  for x in range(len(vectorA)):
    vectorAB += vectorA[x]*vectorB[x]
  return vectorAB

#not working
def dotproductMMx(matrixA, matrixB):
  format_matrixA = formatMatrix(matrixA)
  format_matrixB = formatMatrix(matrixB)

  if (checkRows(format_matrixA) and checkRows(format_matrixB) and len(format_matrixA[0]) == len(format_matrixB)):
    new_matrix = []
    cols_matrixB = cols(format_matrixB)
    for x in format_matrixA:
      for i in cols_matrixB:
        new_matrix.append(dotproductVVx(x, i))
    return new_matrix
