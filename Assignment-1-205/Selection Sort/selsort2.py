def read_array(a):
	i=0
	ch ='Y'
	while(ch != 'N'):
		a[i] = int(input())
		print("Continue Y/N?")
		ch = str(input())
		i=i+1
	return(i)
	
a = [-1 for i in range(100)]

x = read_array(a)
print("Number of elements read:"+str(x))

''' 
	OUTPUT:
   --------

cs1205@spl3:~$ python selsort2.py
1
Continue Y/N?
Y
2
Continue Y/N?
Y
3
Continue Y/N?
Y
4
Continue Y/N?
Y
5
Continue Y/N?
Y
6
Continue Y/N?
N
Number of elements read:6

'''
