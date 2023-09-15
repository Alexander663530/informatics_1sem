A = list(map(int, input().split()))
a = 1
for i in range(len(A)):
	a = a*A[i]
a = a**(1/len(A))
print(a)




	
