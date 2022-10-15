print("5")
print("Anna has {} apples and peaches.".format(2))
print()
print("6")
print("Anna has {0} apples and {1} peaches.".format("three","one thousand"))
print()
print("7")
print("Anna has {b1} apples and {b2} peaches.".format(b1="three",b2="one thousand"))
print()
print("8")
print("Anna has {0:5} apples and {1:3} peaches.".format("three","one thousand"))
print()
print("9")
var1="three"
var2="one thousand"
print(f"Anna has {var1} apples and {var2} peaches.")
print()
print("10")
var1="three"
var2="one thousand"
print('Anna has %s apples and %s peaches.' % (var1,var2))
print()
print("11")
var1="three"
var2="one thousand"
data_dict={"one": var1, "two": var2}
print('Anna has %(one)s apples and %(two)s peaches.' % data_dict)
