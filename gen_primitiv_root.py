import sage.all as sa
import sys


print()

argv = sys.argv
argc = len(argv)

if argc != 3:
    print("\nUsage: python3 gen_primitiv_root.py n a\n")
    exit(1)

n = int(argv[1])
a = int(argv[2])

v = []
p = []
y = sa.factor(n - 1)

isPrim = True

for yi in y:
    v.append(yi[0])

for i in range(n - 1):
    for val in v:
        if i % val == 0:
            isPrim = False
            break
    
    if isPrim:
        p.append(i)
    
    isPrim = True

for p_i in p:
    print("%3d" % (sa.power(a, p_i) % n), end=" ")

print("\n")