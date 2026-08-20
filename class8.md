# Lists
- Lists are built in data types
- Lists are used to store multiple items in a single variable.
- It can store elemtns pof different types (integer, float, string etc.)
- Lists are mutable (changeable)
- Lists are created using square brackets
- List items are:
  - Ordered: Items have a defined order, and that order will not change. If you add new items to a list, the new items will be placed at the end of the list.
  - Changeable: We can change, add, and remove items in a list after it has been created.
  - Allow duplicate values: Since lists are indexed. lists can have items with the same value.
- List items are indexed, the first item has **index of 0**.
- To determine how many items a list has, use thhe len() function.

List is a collection of items that is written with square brackets. It is mutable, ordered, and allows duplicate members.

Example:
```python
marks=[67.1, 55.6, 33.2, 78.1]
print(marks)
print(type(marks)) #Output: <class 'list'>
```
Example:
```python
list = [1, 2, 3, 'A', 'B', 7, 8, [10, 11]] #multiple type list
thislist = ["apple", "banana", "cherry"]
mix_list1 = ["abc", 34, True, 40, "male"]
thislist = list(("apple", "banana", "cherry")) #Note: Double round brackets are for lists, single round bracket for tuple
```
To see list type:
```python
print(type(thislist))
```
List: according to index assign values

```python
marks=[23.6, 45.1, 70.9, 99.4, 23.4, 44.6]
print(marks)
print(marks[0]) #23.6
print(marks[1]) #45.1
print(len(marks)) #6
```
List slicing

list_name[starting_idx : ending_idx] #ending idx is not included
marks = [10,20,30,40,50]
marks[1:4] is [20,30,40] #print(marks[1:4])
marks[:4] is same as marks [0:4]
marks[1:] 

List Methods

```python
list = [5, 2, 7]
list.append(8)
print(list) #After adding one element at the end list = [5, 2, 7, 8]
```
```python
list.sort() #sorts in ascending order 



