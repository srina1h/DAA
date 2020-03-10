def ordered_insert(a):
	n=len(a)
	for i in range(1,n):
		if(a[i-1]>a[i]):
			t=a[i-1]
			a[i-1]=a[i]
			a[i]=t
n=int(input("Enter the number of elements: "))
a=[]
for i in range(n):
	a.append(int(input("Enter number: ")))
ordered_insert(a)
print(a)


"""
OUTPUT:
-------

cs1205@spl8:~/Insertion Sort$ python3 insort6.py
Enter the number of elements: 5
Enter number: 3
Enter number: 2
Enter number: 1
Enter number: 5
Enter number: 8 
[2, 1, 3, 5, 8]

"""
