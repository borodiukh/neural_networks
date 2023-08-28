yTab1 = [[],
     [],
     [],
     [],
     []]

yTab2 = [[],
     [],
     [],
     [],
     []]

theta = 2.5

def f(x):
    if x < 0:
        return 0
    else:
        return 1


def y(i,j,x):
    sum = 0
    for iP in range(3):
        for jP in range(3):
            sum += x[i+iP][j+jP]
    return f( 1/9* (sum - theta))


x1 = [[0,0,0,0,0,0,0],
      [0,0,1,0,0,0,0],
      [0,0,0,1,0,0,0],
      [0,0,1,0,0,0,0],
      [0,0,0,1,0,0,0],
      [0,0,1,0,0,0,0],
      [0,0,0,0,0,0,0]]

x2 = [[0,0,0,0,0,0,0],
      [0,0,0,0,1,0,0],
      [0,0,0,0,0,1,0],
      [0,0,0,0,1,0,0],
      [0,0,0,0,0,1,0],
      [0,0,0,0,1,0,0],
      [0,0,0,0,0,0,0]]

for i in range(5):
    for j in range(5):
        yTab1[i].append( y(i,j,x1) )
    print(yTab1[i])
print("")

for i in range(5):
    for j in range(5):
        yTab2[i].append( y(i,j,x2) )
    print(yTab2[i])
print("")