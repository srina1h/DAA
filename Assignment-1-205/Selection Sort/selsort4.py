def minimum(a,low,high):
	n = len(a)
	mini = a[low]
	index = low
	for i in range(low,high):
		if(a[i] < mini):
			index = i
	return(index)


print("Enter if you wish to test function: (Y/N) ")
ch = str(input())
while(ch != 'N'):
	print("enter number of elements:")
	n = int(input())
	a = [999 for i in range(n)]
	for i in range(n):
		a[i] = int(input())
	print("Enter range for subarray:")
	low = int(input())
	high = int(input())
	x = minimum(a,low,high)
	print("minimum is at "+str(x))
	print("Do you wish to continue ?")
	ch = str(input())
	

"""

OUTPUT:
-------

def minimum(a):
	n = len(a)
	mini = a[0]
	index =0
	for i in range(n):
		if(a[i] < mini):
			index = i
	return(index)


print("Enter if you wish to test function: (Y/N) ")
ch = str(input())
while(ch != 'N'):
	print("enter number of elements:")
	n = int(input())
	a = [999 for i in range(n)]
	for i in range(n):
		a[i] = int(input())
	x = minimum(a)
	print("minimum is at "+str(x))
	print("Do you wish to continue ?")
	ch = str(input())
	
"""
