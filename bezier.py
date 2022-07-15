from kandinsky import *

def draw(x, y):
    fill_rect(x-3,y-3,6,6,'red')

def L(t, TUP):
  if len(TUP)==2:
    return (1-t)*TUP[0]+t*TUP[1]
  a = L(t, TUP[:len(TUP)-1])
  b = L(t, TUP[1:])
  return L(t, (a,b))

def drawBit(x,y):
  set_pixel(round(x),round(y),"black")

def get_n_points():
    print("Frappez <EXE> quand vous aurez fini de renter vos points.")
    L = []
    while 1:
        try:
            x = int(input("Point (x) : "))
            y = int(input("Point (y) : "))
            L.append(x)
            L.append(y)
        except:
          if len(L)>3:
            return L

def get_draw():
    reponse = input("Dessiner les points ? (o/n) ")
    if reponse == 'o' or reponse == '0': return True
    else: return False

def run():
  points = get_n_points()
  if get_draw():
    for i in range(0,len(points),2):
      draw(points[i], points[i+1])
  t=0
  while t<1:
    drawBit(L(t, TUP=[points[x] for x in range(len(points)) if x%2==0]), L(t, TUP=[points[y] for y in range(len(points)) if y%2==1]))
    t+=1/500

run()