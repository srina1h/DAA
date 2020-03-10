def ordered_insert(a,n):
	x=a[n-1]
	for i in range(n-1):
		if x<a[i]:
			t=x
			x=a[i]
			a[i]=t
	a[n-1]=x
def sort_array(a,n): 
	if(n!=1):
		sort_array(a,n-1) 
		ordered_insert(a,n)
	else:	
		return

m=int(input("Enter the number of elements: "))
a=[]
for i in range(m):
	a.append(int(input("Enter number: ")))

sort_array(a,m)
print(a)

"""
OUTPUT:
-------

cs1205@spl8:~/Insertion Sort$ python3 insort5.py
Enter the number of elements: 5
Enter number: 3
Enter number: 7
Enter number: 23
Enter number: 98
Enter number: 1
[1, 3, 7, 23, 98]


"""
