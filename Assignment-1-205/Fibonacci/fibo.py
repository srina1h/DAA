def fibo(n):
	if(n==0):
		return 0
	elif(n==1):
		return 1
	else:
		return(fibo(n-2)+fibo(n-1))

print("Enter a value ")
n = int(input())
print("Fibonacci value is: "+str(fibo(n)))

''' 
	OUTPUT:
   --------
   
cs1205@spl3:~$ python fibo.py
Enter a value 
3
Fibonacci value is: 2
cs1205@spl3:~$

'''
