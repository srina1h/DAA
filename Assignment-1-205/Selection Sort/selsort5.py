def minimum(a,low,high):
	n = len(a)
	mini = 100000
	index = low
	for i in range(low,high):
		if(a[i] < mini):
			mini = a[i]
			index = i
	return(index)
	
def selsort(a):
	n = len(a)
	for i in range(n):
		x = minimum(a,i,n)
		temp = a[i]
		a[i] = a[x]
		a[x] = temp
	print("FINAL SORTED ARRAY")
	print(a)
	

print("enter number of elements:")
n = int(input())
a = [999 for i in range(n)]
for i in range(n):
	a[i] = int(input())
selsort(a)

"""		
OUTPUT:
--------

cs1205@spl8:~/Untitled Folder$ python3 selsort5.py
enter number of elements:
5
8
5
9
1
4
FINAL SORTED ARRAY
[1, 4, 5, 8, 9]
"""
