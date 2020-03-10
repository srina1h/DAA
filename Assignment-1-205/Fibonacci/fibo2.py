def fibo(n):
		l = 0
		m = 1
		i = 1
		fib = 0
		while(i < n):
			fib = l+m
			l=m
			m=fib
			i=i+1
		return fib

print("Enter a value ")
n = int(input())
print("Fibonacci value is: "+str(fibo(n)))

'''
	OUTPUT:
	-------

cs1205@spl3:~$ python fibo2.py
Enter a value 
3
Fibonacci value is: 2

'''
