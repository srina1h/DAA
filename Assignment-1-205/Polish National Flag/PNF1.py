def PNF(a,low,high):
	x=low
	while x<high:
		if a[x]>=0:
			i=x
			break
		x=x+1
	print(a[low:i])
	print(a[i:high])
	
n=int(input("Enter the number of elements: "))
a=[0 for i in range(n)]
for i in range(n):
	a[i]=int(input("Enter element: "))
low=int(input("Enter the low index: "))
high=int(input("Enter the high index: "))
PNF(a,low,high)

"""
OUTPUT:
-------

cs1205@ssn15:~/Polish National Flag$ python3 PNF1.py
Enter the number of elements: 8
Enter element: -2
Enter element: -1
Enter element: -5
Enter element: -3
Enter element: 5
Enter element: 3
Enter element: 7
Enter element: 2
Enter the low index: 2
Enter the high index: 7
[-5, -3]
[5, 3, 7]
 
"""
