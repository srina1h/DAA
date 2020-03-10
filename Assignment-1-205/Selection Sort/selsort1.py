def printarray(a, low, high):
	for i in range(low,high):
		print(str(a[i])+" ")

print("Enter limit of array:")
n = int(input())
print("Enter "+str(n)+" values")
a = [-1 for i in range(n)]
for i in range(n):
	a[i] = int(input())
print("enter low and high limits to print between")
low = int(input())
high = int(input())
print("array:")
printarray(a,low,high)
		
'''
	OUTPUT:
   --------

Enter limit of array:
5
Enter 5 values
1
2
3
4
5
enter low and high limits to print between
2
4
array:
3 
4 

'''
