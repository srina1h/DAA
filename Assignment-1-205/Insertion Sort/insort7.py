def ordered_insert(a,n):
	for i in range(1,n):
		if a[pow(2,i-1)]>a[pow(2,i)]:
			t=a[pow(2,i-1)]
			a[pow(2,i-1)]=a[pow(2,i)]
			a[pow(2,i)]=t
			
n=int(input("Enter the number of elements: "))
a=[0 for i in range (pow(2,n))]
for i in range(n):
	a[pow(2,i)]=int(input("Enter number: "))
ordered_insert(a,n)
for i in range(n):
	print(a[pow(2,i)])

"""
OUTPUT:
-------

cs1205@spl8:~/Insertion Sort$ python3 insort7.py
Enter the number of elements: 5
Enter number: 7
Enter number: 2
Enter number: 4
Enter number: 8
Enter number: 9
2
4
7
8
9

"""
