# bounce.py
#
# Exercise 1.5

height, ratio = 100, 3/5

for t in range(10):
    height = round(height * ratio, 4)
    print('{0} {1}'.format(t+1, height))
