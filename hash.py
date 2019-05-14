#!/usr/bin/env python
# coding: utf8
from fractions import Fraction
def hash(xb,xu,yb,yu,ab,au,bb,bu,m1,m2):

a1 = [];
a2 = [];
for x in range (xb, xu):
    for y in range (yb, yu):
        for a in range (ab, au):
            for b in range (bb, bu):
                hx = (((a*x+b)%m1)%m2)
                hy = (((a*y+b)%m1)%m2)
                a1.append(hx);
                a2.append(hy);
low = 0;
up = (au-ab)*(bu-bb);
cl = [];
clf = [];
wr = [];
for g in range(0, (xu-xb)*(yu-yb)*(au-ab)*(bu-bb)):
    cl.append(0);
for w in range (0, (xu-xb)*(yu-yb)):
    for v in range (low, up):
        if a1[v]==a2[v]:
            cl[v]=1;
    low = up;
    up += (au-ab)*(bu-bb);
l=0;
u=(au-ab)*(bu-bb);
z=0;
for ff in range (0, (xu-xb)*(yu-yb)):
    for fy in range (l, u):
        z = z+cl[fy];
    clf.append(z);
    z=0;
    l=u;
    u +=(au-ab)*(bu-bb);
i=0
while i < (xu-xb)*(yu-yb):
    clf[i]=0
    i += (yu+1)

#  for f in range (0, len(clf)):
#     print (clf[f]);
    #print ("Wahrsch.");

#print (len(clf))
f=0
for x in range (xb, xu):
    print (" ")
    for y in range (yb, yu):
        if(x!=y):
            print ("Kollisionswahrsch. für |h(%d) = h(%d) ist: %f|"  % (x, y, (float(float(clf[f])/float((au-ab)*(bu-bb))))) )
            f += 1;
        else:
            f += 1;
print ("_____________________Erste_______________________")
hash(0,5,0,5,1,5,0,5,5,4)
print ("_____________________Erste_______________________")
print ("_____________________Zweite______________________")

hash(0,6,0,6,1,5,0,5,6,4)
print ("_____________________Zweite______________________")
