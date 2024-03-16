a=0
naprav=5
def setup():
    size(600,600)
def draw():
    global a,naprav
    background(0)
    ellipse(300,a,100,100)
    a=a+naprav
    if a > 595:
        naprav=-5
        
    if a < 5:
        naprav=+5
    
