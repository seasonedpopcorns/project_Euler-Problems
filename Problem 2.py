t=1

s=1

z=1

x=0

limit = 4000000
while z < limit:
    z=s+t
    t=s
    s=z
    if z%2==0:
        x=x+z 
    

print(z)
print(x)
