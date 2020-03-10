def PNF(a,low,high):
	piv=a[low]
	x=low+1
	while a[x]<piv:
		x=x+1
	i=x
	print(a[low:i])
	print(a[i:n])
	

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

cs1205@ssn15:~/Polish National Flag$ python3 PNF2.py
Enter the number of elements: 6
Enter element: -2
Enter element: -1
Enter element: -3
Enter element: 5
Enter element: 2
Enter element: 6
Enter the low index: 2
Enter the high index: 5
[-3]
[5, 2, 6]

"""
