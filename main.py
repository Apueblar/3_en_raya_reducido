import os
def borra_pantalla():
  if os.name == "posix": os.system ("clear") 
  else: os.system ("cls")
def ganaste(q):
  dibujar_tablero()
  print("+-------------------+\n| Ganaste jugador %1s |\n+-------------------+" % (q))
  return 1
def empate():
  dibujar_tablero()
  print("+--------+\n| Empate |\n+--------+")
def dibujar_tablero():
  print("   | A | B | C |")
  for i in range(3):
    print(("---+---+---+---+\n %1s | %1s | %1s | %1s |") % (i+1, tablero[i][0], tablero[i][1], tablero[i][2]))
  print("---+---+---+---+\n")
def preguntar_posicion(n):
  if n % 2 == 1: q = "X"
  else: q = "O"
  g,p = 1,0
  while g != 0:
    F,C = 4,4
    while F != 1 and F != 2 and F != 3:
      try: 
        F = int(input("Dime la fila de la ficha (%s) que quieres poner: (1,2,3): " % (q)))
        if F != 1 and F != 2 and F != 3: print("Mete un número correcto")
      except ValueError: print("Mete un número correcto")
    while C != 0 and C != 1 and C != 2:
        C = input("Dime la columna de la ficha (%s) que quieres poner: (A,B,C): " % (q))
        if C.upper() == "A": C = 0
        elif C.upper() == "B": C = 1
        elif C.upper() == "C": C = 2
        else: print("Mete una letra correcta")
    if tablero[F-1][C] == "":
      tablero[F-1][C] = q
      g = 0
      borra_pantalla()
      for x in range(3):
        if tablero[x][0] == q and tablero[x][1] == q and tablero[x][2] == q:
          p = ganaste(q)
          return p
      for x in range(3):
        if tablero[0][x] == q and tablero[1][x] == q and tablero[2][x] == q:
          p = ganaste(q)
          return p
      if (tablero[0][0] == q and tablero[1][1] == q and tablero[2][2] == q) or (tablero[0][2] == q and tablero[1][1] == q and tablero[2][0] == q) :
        p = ganaste(q)
        return p
      if n == 8 and p == 0: empate()
    else: print("\nMete una casilla no ocupada\n")
n,L,tablero = 0,0,[["","",""],["","",""],["","",""]]
print("Bienvenido al juego del tres en raya\n")
while L != 1 and n != 9:
  dibujar_tablero()
  L = preguntar_posicion(n)
  n += 1
