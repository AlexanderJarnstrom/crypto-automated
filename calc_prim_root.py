import sys
import sage.all as sa

# Same as ord_table but trash

argv = sys.argv
argc = len(argv)

if argc != 4:
    print("\nUsage: python3 calc_prim_root.py a n k\n")
    exit(1)

a = int(argv[1])
n = int(argv[2])
k = int(argv[3])

v = []

x = 1

while (x <= k):
    val = sa.power(a, x) % n
    print("%3d: %3d" % (x, val))
    v.append(val)
    x += 1
    
print()
print(v, end="\n\n")