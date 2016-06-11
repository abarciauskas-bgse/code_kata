def moveDisk(fromPole, toPole):
    print "Moving disk from " + fromPole + " to " + toPole

# 1. Move a tower of height-1 to an intermediate pole, using the final pole.
# 2. Move the remaining disk to the final pole.
# 3. Move the tower of height-1 from the intermediate pole to the final pole using the original pole.
# credit: http://interactivepython.org/runestone/static/pythonds/Recursion/TowerofHanoi.html
def towerOfHanoi(height, fromPole, withPole, toPole):
    if height >= 1:
        towerOfHanoi(height-1, fromPole, withPole, toPole)
        moveDisk(fromPole, toPole)
        towerOfHanoi(height-1, withPole, toPole, fromPole)
