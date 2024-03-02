

x, y = 2500.0, 2500.0

def move(dx, dy):
    global x, y
    x += dx
    y += dy

    if x < 0.0: 
        x = 0.0
    if y < 0.0:
        y = 0.0



def get_pos():
    global x, y
    return x, y

