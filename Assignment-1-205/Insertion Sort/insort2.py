def ordered_insert(a,n):
	x=a[n-1]
	for i in range(n-1):
		if(x<a[i]):
			t=x
			x=a[i]
			a[i]=t
	a[n-1]=x
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

cs1205@spl8:~/Insertion Sort$ python3 insort2.py
Enter the number of elements: 7
Enter number: 4
Enter number: 2
Enter number: 7
Enter number: 1
Enter number: 5
Enter number: 9
Enter number: 8
Enter the value of n: 4
[1, 2, 4, 7, 5, 9, 8]

"""
