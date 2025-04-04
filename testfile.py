from skiplist_functions import *

skiplist = initialize_skiplist()

insert(skiplist, 3, 5, "Lahore")
insert(skiplist, 7, 2, "Islamabad")
insert(skiplist, 3, 5, "Karachi")
insert(skiplist, 7, 2, "Lahore2")


display(skiplist)

print("Search (3, 5) in x skiplist:", search(skiplist, 3, 5))
print("Search (7, 2) in y skiplist:", search(skiplist, 7, 2))
print("Search (7, 2) in x skiplist:", search(skiplist, 7, 2))
print("Search unknown point in x skiplist", search(skiplist, 10, 10))
print("Search unknown point in y skiplist", search(skiplist, 4, 10))