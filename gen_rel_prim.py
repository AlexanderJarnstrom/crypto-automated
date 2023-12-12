import sys
import sage.all as sa

def gpr(n: int):

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
            print("%3d" % (i), end=" ")
            p.append(i)
        
        isPrim = True

    print("\n")
    
    return p


if (__name__ == "__main__"):
    print()

    argv = sys.argv
    argc = len(argv)

    if argc != 2:
        print("\nUsage: python3 gen_rel_prim.py n\n")
        exit(1)

    n = int(argv[1])
    
    gpr(n=n)