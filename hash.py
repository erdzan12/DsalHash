def hash():
	i=0;
	a1 = [];
	a2 = [];
	for a in range (1, 5):
		for b in range (0, 5):
			for x in range (0, 5):
				for y in range (0, 5):
					hx = (((a*x+b)%5)%4)
					hy = (((a*y+b)%5)%4)
					a1.append(hx);
					a2.append(hy);
					i += 1;
	low = 0;
	up = 25;
	cl = [];
	clf = [];
	wr = [];
	for g in range(0, 500):
		cl.append(0);
	for w in range (0, 20):
		for v in range (low, up):
			if a1[v]==a2[v]:
				cl[v]=1;
		low = up;
		up += 25;
	l=0;
	u=5;
	z=0;
	for ff in range (0, 100):
		for fy in range (l, u):
			z += cl[fy];
		clf.append(z);
		z=0;
	for f in range (0, len(clf)):
		print clf[f];
		print "Wahrsch.";
		print(float(float(clf[f])/float(5)))

	print len(clf)
def hash2():
        i=0;
        a1 = [];
        a2 = [];
        for a in range (1, 5):
                for b in range (0, 5):
                        for x in range (0, 6):
                                for y in range (0, 6):
                                        hx = (((a*x+b)%6)%4)
                                        hy = (((a*y+b)%6)%4)
                                        a1.append(hx);
                                        a2.append(hy);
                                        i += 1;
        low = 0;
        up = 36;
        cl = [];
        clf = [];
        wr = [];
        for g in range(0, 720):
                cl.append(0);
        for w in range (0, 20):
                for v in range (low, up):
                        if a1[v]==a2[v]:
                                cl[v]=1;
                low = up;
                up += 36;
        l=0;
        u=6;
        z=0;
        for ff in range (0, 120):
                for fy in range (l, u):
                        z += cl[fy];
                clf.append(z);
                z=0;
        for f in range (0, len(clf)):
                print (clf[f]);
                print ("Wahrsch.");
                print(float(float(clf[f])/float(5)))

        print (len(clf))

hash()
