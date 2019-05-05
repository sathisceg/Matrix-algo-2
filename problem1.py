

import numpy as np

def QR_Algorithm(input_data):

	# print input_data

	inputArray = np.matrix(input_data)

	inputArray=np.matrix(inputArray).getT()

	# print inputArray

	# print

	# print inputArray[:,0:2]

	print

	# print inputArray[0:2,:]

	n,m = inputArray.shape

	# print n,m

	R = np.zeros(shape=(n,m))

	# print R

	k=0
	while (k<m):
		# print k
		# print
		i=0
		while (i<=k-1):
			# print "k",k
			# print "i",i
			# print inputArray[:,i:i+1]
			# print
			# print inputArray[:,k:k+1]
			# print 

			vi = inputArray[:,i:i+1]
			vk = inputArray[:,k:k+1]
			 
			R[i][k]=vi.getT()*vk 
			i=i+1
	
		i=0
		vk = inputArray[:,k:k+1]
		while (i<=k-1):
			vi= inputArray[:,i:i+1]
			vk = vk-R[i][k]*vi
			i=i+1
			# print vk

		rkk =np.linalg.norm(vk)
		R[k][k]=rkk
		# print rkk

		# rkk=0
		if (rkk==0):
			print "vectors are linearly dependent"
			return
		# print vk/rkk
		vk = vk/rkk
		inputArray[:,k:k+1]=vk
		k=k+1
			
	# print R
	# print
	# print inputArray
	# print "QR_Algorithm"
	return inputArray,R







if __name__=='__main__':

	input_data=[[1,0,0],[2,0,3],[4,5,6]]

	Q,R=QR_Algorithm(input_data)



	print "Q matrix"
	print Q
	print
	print "R matrix"
	print R