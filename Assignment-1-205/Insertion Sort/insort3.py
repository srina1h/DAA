def ordered_insert(a,n):
	if n<=1:
		return
	ordered_insert(a,n-1)
	x=a[n-1]
	j=n-2
	for i in range(n-1):
		if x<a[i]:
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

cs1205@spl8:~/Insertion Sort$ python3 insort3.py
Enter the number of elements: 5
Enter number: 7
Enter number: 1
Enter number: 2
Enter number: 4
Enter number: 3
Enter the value of n: 3
[1, 2, 7, 4, 3]


"""
