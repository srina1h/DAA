def ordered_insert(a,n):
	x=a[n-1]
	i=n-2
	while i>=0:
		if a[i]>x:
			a[i+1]=a[i]
		else:
			break

		i=i-1
	a[i+1]=x
m=int(input("Enter the number of elements: "))
a=[]
for i in range(m):
	a.append(int(input("Enter number: ")))
n=int(input("Enter the value of n: "))
ordered_insert(a,n)
print(a)

"""

OUTPUT:
-------

cs1205@spl8:~/Insertion Sort$ python3 insort4.py
Enter the number of elements: 6
Enter number: 6
Enter number: 2
Enter number: 4
Enter number: 1
Enter number: 5
Enter number: 7
Enter the value of n: 4
[1, 6, 2, 4, 5, 7]


"""
