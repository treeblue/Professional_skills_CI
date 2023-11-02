import scipy as sc
import numpy as np

def function(f,a,b):
	return sc.integrate.quad(f,a,b)/(b-a)

if __name__=='__main__':
	def const(x):
		return 5.
	def gaus(x):
		return np.exp(-(x**2))
	a = 0
	b = 1
	while b < 1e7:
		function(const,a,b)
		function(gaus,a,b)
		b *=10		
	

	
