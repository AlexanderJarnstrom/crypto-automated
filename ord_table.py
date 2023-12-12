import sage.all as sa
import sys;

arg = sys.argv
if (len(arg) >= 2):
    n = int(arg[1]);

print("\nVal: %d" % (n), end="\n\n")

y = 2
x = 1

while x < n:
    print("%4d" % (x), end="")
    if x == 1:
        print(end="|")
    x += 1

x = 1
print()

while x < n:
    print("----", end="")
    if x == 1:
        print(end="|")
    x += 1

x = 1
print()

if (len(arg) == 2):
    while (y < n):
        while (x < n):
            val = sa.power(y,x) % n
            print("%4d" % (val), end="")
            
            if x == 1:
                print(end="|")
            
            x += 1
            if (val == 1):
                break;
        
        y += 1 
        x = 1       
        print("\n    |")
elif (len(arg) == 3):
    
    y = int(arg[2])
    
    while (x < n):
        val = sa.power(y,x) % n
        print("%4d" % (val), end="")
        
        if x == 1:
            print(end="|")
        
        x += 1
        if (val == 1):
            break;
        

print("\n")
