list1 = ['a', 'b', 'b', 'a']
copy_list1 = list1.copy()
copy_list1.reverse()
if (copy_list1 == list1):
    print("List is palindrome.")
else:
    print("Not a palindrome.")