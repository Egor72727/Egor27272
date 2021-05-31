#1.1

import numpy as np

A = np.array([[10,4,0,0],[7,11,3,0],[0,6,12,2],[0,0,5,13]])
b = np.array([20,23,26,29])


def solve_lu3(A,b):

	d = np.array([A[i,i] for i in range(len(A))],float)
	e = np.array([A[i,i+1] for i in range(len(A)-1)],float)
	c = np.array([A[i+1,i] for i in range(len(A)-1)],float)

	aa = np.zeros(len(A),float)
	aa[1] = -e[0]/d[0]

	for i in range(2,len(A)):
		aa[i] = -e[i-1]/(d[i-1]+c[i-1]*aa[i-1])

	bb = np.zeros(len(A),float)
	bb[1] = b[0]/d[0]

	for i in range(2,len(A)):
		bb[i] = (-c[i-1]*bb[i-1] + b[i-1]) / (d[i-1] + c[i-1]*aa[i-1])

	x = np.zeros(len(A),float)
	x[-1] = (-c[-1]*bb[-1] + b[-1])/(d[-1] + c[-1]*aa[-1])

	for i in range(len(A)-2,-1,-1):
		x[i] = aa[i+1]*x[i+1] + bb[i+1]
	return x
    
x = solve_lu3(A,b)
print(np.dot(A,x))