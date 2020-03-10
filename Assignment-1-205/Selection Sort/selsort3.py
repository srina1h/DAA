def minimum(a):
	n = len(a)
	mini = a[0]
	index =0
	for i in range(n):
		if(a[i] < mini):
			index = i
	return(index)


print("Enter if you wish to test function: (Y/N) ")
ch = str(input())
while(ch != 'N'):
	print("enter number of elements:")
	n = int(input())
	a = [999 for i in range(n)]
	for i in range(n):
		a[i] = int(input())
	x = minimum(a)
	print("minimum is at "+str(x))
	print("Do you wish to continue ?")
	ch = str(input())
	
"""
	
OUTPUT:
------

cs1205@spl21:~$ python3 selsort3.py
Enter if you wish to test function: (Y/N) 
Y
enter number of elements:
5
2
1
3
4
5
minimum is at 1
Do you wish to continue ?
Y
enter number of elements:
4
3
2
5
6
minimum is at 1
Do you wish to continue ?
Y
enter number of elements:
7
9
6
5
3
2
4
5
minimum is at 6
Do you wish to continue ?
N
cs1205@spl21:~$

"""
	
		
