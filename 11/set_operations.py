# Program to perform set operations
# Taking input from user
set1 = set(map(int, input("Enter elements of Set 1 separated by space: ").split()))
set2 = set(map(int, input("Enter elements of Set 2 separated by space: ").split()))
# Union
union_set = set1.union(set2)
# Intersection
intersection_set = set1.intersection(set2)
# Difference
difference_set1 = set1.difference(set2)
difference_set2 = set2.difference(set1)
# Symmetric Difference
symmetric_difference_set = set1.symmetric_difference(set2)
# Displaying results
print("\nUnion: ", union_set)
print("Intersection: ", intersection_set)
print("Difference (Set1 - Set2): ", difference_set1)
print("Difference (Set2 - Set1): ", difference_set2)
print("Symmetric Difference: ", symmetric_difference_set)