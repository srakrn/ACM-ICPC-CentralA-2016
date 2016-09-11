import math
amount = int(input())
k = [0]*amount
for i in range(0,amount):
	a,b,c = input().split()
	k[i] = math.sqrt(abs(int(b)/int(a)))
for i in range(0,amount):
	print(k[i])
