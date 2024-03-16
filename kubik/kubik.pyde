s=100
d=1
ras=1
def setup():
    size(600,600)
def draw():
    global s,ras,d
    background(250)
    rotate(radians(d))
    rect(250,250,s,s)
    s=s+ras
    if s > 200:
        ras=-1
    
    if s < 100:
        ras=+1
    
