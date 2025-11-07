import time,rotatescreen as pp

check = pp.get_primary_display()
list = [90,180,270,0]
while True:
    for j in list:
        check.rotate_to(j)
        time.sleep(.5)