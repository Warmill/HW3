int_a = 55
str_b = 'cursor'
set_c = {1, 2, 3}
lst_d = [1, 2, 3]
dict_e = {'a': 1, 'b': 2, 'c': 3}

print("1")
print("int_a id is ",id(int_a)," , ","str_b id is ",id(str_b)," , ",
      "set_c id is ",id(set_c)," , ","lst_d id is ",id(lst_d)," , ",
      "dict_e id is ",id(dict_e))
print()

print("2")
lst_d.append(4)
lst_d.append(5)
print("lst_d after append is ",lst_d)
print("lst_d id after append is ",id(lst_d))
print()

print("3")
print("int_a is ",type(int_a),", ","str_b is ",type(str_b),", ",
      "set_c is ",type(set_c),", ","lst_d is ",type(lst_d),", ",
      "dict_e is ",type(dict_e))
print()

print("4")
def func(varia):
    if isinstance(varia,int)==True :
        return(" is int")
    else:
        if isinstance(varia,str)==True :
            return(" is str")
        else:
            if isinstance(varia, set) == True:
                return(" is set")
            else:
                if isinstance(varia, list) == True:
                    return(" is list")
                else:
                    if isinstance(varia, dict) == True:
                        return(" is dict")
                    else:
                        return(" is undifined variable type")


print ("int_a",func(int_a))
print ("str_b",func(str_b))
print ("set_c",func(set_c))
print ("lst_d",func(lst_d))
print("dict_e",func(dict_e))