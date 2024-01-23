fh = open('sorting.txt','w')
a = [2,3,45,12,87,98,44,60,35] 
b = input("Enter your choice to sort the numbers (ascending/descending): ") 
if b == 'ascending': 
    a.sort() 
    fh.write(str(a)) 
else: 
    a.sort( reverse = True) 
    fh.write(str(a))
fh.close()