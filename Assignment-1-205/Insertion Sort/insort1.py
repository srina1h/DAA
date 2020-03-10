def ordered_insert(a):
	n=len(a)
	x=a[n-1]
	for i in range(n-1):
		if x<a[i]:
			t=x
			x=a[i]
			a[i]=t
	a[n-1]=x
n=int(input("Enter the number of elements: "))
a=[]
for i in range(n):
	a.append(int(input("Enter number: ")))
ordered_insert(a)
print(a)

"""
OUTPUT:
--------

cs1205@spl8:~/Insertion Sort$ python3 insort1.py
Enter the number of elements: 5
Enter number: 8
Enter number: 2
Enter number: 4
Enter number: 7
Enter number: 1
[1, 2, 4, 7, 8]


"""
