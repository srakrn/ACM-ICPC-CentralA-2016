x = int(input())
b = ["NO"]*x

for i in range(0,x):
	# Don't forget that x may be up to 10^100000. Since, NO datatypes are enough to store this.
	m = input()
	x = 0;
	for k in range(0,len(m)):
		x+=int(m[k]);
	if(x%9==0):
		b[i] = "YES"

for j in b:
	print(j)
