def fibo(n):
	if(n==0):
		return 0
	elif(n==1):
		return 1
	else:
		return(fibo(n-2)+fibo(n-1))
		
gbarray = [-1 for i in range(100)]
i=0
ch = 'Y'
while(ch != 'N'):
	print("Enter a value ")
	n = int(input())
	if(gbarray[n] != -1):
		print("Fibonacci value is: "+str(gbarray[n]))
	else:
		gbarray[n] = fibo(n)
		print("Fibonacci value is: "+str(gbarray[n]))
	print("Enter more ? Y/N")
	ch = str(input())
	
	
'''

	OUTPUT:
   --------

cs1205@spl3:~$ python fibo3.py
Enter a value 
5
Fibonacci value is: 5
Enter more ? Y/N
Y
Enter a value 
2
Fibonacci value is: 1
Enter more ? Y/N
Y
Enter a value 
3
Fibonacci value is: 2
Enter more ? Y/N
Y
Enter a value 
2
Fibonacci value is: 1
Enter more ? Y/N
N

'''
