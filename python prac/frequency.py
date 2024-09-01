string = (input("enter a string :"))
list1 = list(string)
freq = [list1.count(ele) for ele in list1]
d = dict(zip(list1,freq))
print(d)