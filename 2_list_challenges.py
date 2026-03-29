# ============================================================
# Python List Methods — 10 Beginner Challenges
# Practice each one before reading the hint!
# Hints are at the bottom of the file.
# ============================================================


# --------------------------------------------------------------
# Challenge 1 — Build Your Grocery List
# Start with an empty list. Add "eggs", "milk", and "bread"
# one at a time, then print the final list.
# Method: append()
# Challenge 1:  Call append() three times, once per item.
# --------------------------------------------------------------

grocery = []
# your code here

for item in ["eggs", "milk", "bread"]:
    grocery.append(item)

print(grocery)


# --------------------------------------------------------------
# Challenge 2 — Merge the Shelves
# Combine shelf_b into shelf_a WITHOUT creating a new list,
# then print the result.
# Method: extend()
# Challenge 2:  extend() adds all items from another iterable in place.
# --------------------------------------------------------------

shelf_a = ["pasta", "rice"]
shelf_b = ["beans", "lentils", "oats"]
# your code here

shelf_a.extend(shelf_b)
print(shelf_a)


# --------------------------------------------------------------
# Challenge 3 — VIP Guest
# Insert "Diana" at position 1 so she appears second.
# Method: insert()
# Challenge 3:  insert(index, value) shifts existing items to the right.
# --------------------------------------------------------------

guests = ["Alice", "Bob", "Charlie"]
# your code here
guests.insert(1, "Diana")
print(guests)

# --------------------------------------------------------------
# Challenge 4 — Remove the Duplicate
# Remove the FIRST occurrence of 7 and print the updated list.
# Method: remove()
# Challenge 4:  remove() only deletes the first match — the second 7 stays.
# --------------------------------------------------------------

numbers = [4, 7, 2, 7, 9]
# your code here
# Remove the first occurrence of 7
numbers.remove(7)
print(numbers)


# --------------------------------------------------------------
# Challenge 5 — Stack Simulation
# Push 10, 20, 30 onto a stack (list), then pop the top two
# items and print each popped value.
# Methods: append(), pop()
# Challenge 5:  Stack is last-in first-out; pop() with no argument removes the last item.
# --------------------------------------------------------------

stack = []
# your code here
# Push items onto the stack
stack.append(10)
stack.append(20)
stack.append(30)

# Pop the top two items
top1 = stack.pop()
print(top1)  # 30
top2 = stack.pop()
print(top2)  # 20


# --------------------------------------------------------------
# Challenge 6 — Sort the Scores
# Sort scores from HIGHEST to LOWEST and print the result.
# Method: sort(reverse=True)
# Challenge 6:  Pass reverse=True to sort() for descending order.
# --------------------------------------------------------------

scores = [88, 45, 92, 67, 73]
# your code here
# Sort from highest to lowest
scores.sort (reverse=True)
print (scores)


# --------------------------------------------------------------
# Challenge 7 — Alphabetical, but Fair
# Sort the list below case-insensitively.
# Method: sort(key=str.lower)
# Challenge 7:  Without key=str.lower, uppercase letters sort before lowercase due to ASCII values.
# --------------------------------------------------------------

words = ["banana", "Apple", "cherry", "Mango"]
# your code here
# Sort case-insensitively
words.sort(key=str.lower)
print (words)


# --------------------------------------------------------------
# Challenge 8 — Find & Count
# 1. How many times does "yes" appear?
# 2. What is the index of the first "no"?
# Methods: count(), index()
# Challenge 8:  count() gives total occurrences; index() returns the position of the first match.
# --------------------------------------------------------------

votes = ["yes", "no", "yes", "yes", "no", "yes"]
# your code here
# Count how many times "yes" appears
count = votes.count("yes")

# Find index of the first "no"
idx = votes.index("no")

print("Number of 'yes':", count)
print("Index of first 'no':", idx)


# --------------------------------------------------------------
# Challenge 9 — Reverse Without Sorting
# Reverse the list IN PLACE and print it.
# Method: reverse()
# Challenge 9:  reverse() returns None — don't assign its result to a variable.
# --------------------------------------------------------------

letters = ["a", "b", "c", "d", "e"]
# your code here
# Reverse the list in place
letters.reverse()
print(letters)


# --------------------------------------------------------------
# Challenge 10 — Sort Without Touching the Original
# Create a new sorted list (ascending) while keeping temps
# unchanged, then print both to verify.
# Method: sorted()
# Challenge 10: Unlike sort(), sorted() never modifies the original list.
# --------------------------------------------------------------

temps = [36.6, 37.2, 35.9, 38.1, 36.0]
# your code here
# Create a new sorted list without modifying the original
temps_sorted = sorted(temps)      # sorted() is a built-in function, not a method

print("Original temps:", temps)
print("Sorted temps:", temps_sorted)



# ============================================================
# BONUS TIPS
# - sort() and reverse() modify in place and return None.
#   Never write: my_list = my_list.sort()  <- this loses data!
# - sorted() always returns a new list; original is untouched.
# - When unsure, print the list before and after each method.
# ============================================================




