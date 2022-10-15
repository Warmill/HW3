import functools
lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]

print("20")
print("old list ",lst_to_sort)
print("sorted min to max ",sorted(lst_to_sort))

print()
print("21")
print("old list ",lst_to_sort)
print("sorted max to min ",sorted(lst_to_sort, reverse=True))

print()
print("22")
print("old list ",lst_to_sort)
new_lst=list(map(lambda x:x*2,lst_to_sort))
print("multiplied elements by 2 ", new_lst)

print()
print("23")
list_A=[2,3,4]
print("list A",list_A)
new_lst1=[x+3 for x in list_A]
new_lst2=list(map(lambda x:x+3,list_A))
print("raised List var1",new_lst1)
print("raised list var2",new_lst2)

print()
print("24")
print("old list ",lst_to_sort)
new_lst=list(filter(lambda x:(x%2==1),lst_to_sort))
print("list filtered by x%2==1 ", new_lst)

print()
print("25")
b= list(range (-10,10))
print(b)
new_lst=list(filter(lambda x:(x<0),b))
print(new_lst)

print()
print("26")
list_1=[1,2,3,5,7,9]
list_2=[2,3,5,6,7,8]
new_lst=list(filter(lambda x:(x in list_2),list_1))
print(new_lst)
