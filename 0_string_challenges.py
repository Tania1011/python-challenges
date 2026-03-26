# ============================================================
# Python String Methods — 10 Beginner Challenges
# Practice each one before reading the hint!
# Hints are at the bottom of the file.
# ============================================================
def divider(ex_number):
    print("\n",f"Challenge {ex_number}".center(26,"*"), "\n")

# --------------------------------------------------------------
# Challenge 1 — Clean the Input
# The string below simulates messy user input. Clean it up by:
#   1. Stripping all leading and trailing whitespace
#   2. Converting it to title case
#   3. Replacing all double spaces inside with a single space
# Print the final result.
# Methods: strip(), title(), replace()
# --------------------------------------------------------------
divider(1)

raw_input = "   alice   johnson  "
raw_input = raw_input.strip()
print(raw_input)
raw_input = raw_input.title()
print(raw_input)
output = raw_input.replace("  ", " ")
print(output)


# --------------------------------------------------------------
# Challenge 2 — Username Validator
# Write a function called is_valid_username(username) that
# returns True only if ALL of these conditions are met:
#   - Length is between 4 and 16 characters (inclusive)
#   - Contains only alphanumeric characters
#   - Starts with a letter (not a digit)
#   - Is all lowercase
# Test it with at least four different usernames.
# Methods: isalnum(), isalpha(), islower(), len()
# --------------------------------------------------------------
divider(2)

def is_valid_username(username):
    if 4 <= len(username) <= 16:
        if username.isalnum():
            if username[0].isalpha():
                if username.islower():
                    return True
    return False

print(is_valid_username("alice"))       # True
print(is_valid_username("Alice"))       # False — uppercase
print(is_valid_username("4alice"))      # False — starts with digit
print(is_valid_username("ab"))          # False — too short


# --------------------------------------------------------------
# Challenge 3 — Word Frequency Counter
# Split the sentence below into words, then count how many
# times each unique word appears (case-insensitive).
# Print each word and its count, sorted alphabetically.
# Methods: lower(), split(), get()
# --------------------------------------------------------------
divider(3)

sentence = "the cat sat on the mat and the cat sat again"

word_freq = {}
for word in sentence.split():
    # Count word frequencies
    word_freq[word] = word_freq.get(word, 0) + 1

print(word_freq)
sorted_words = sorted(list(word_freq))
print(sorted_words)

# --------------------------------------------------------------
# Challenge 4 — CSV Row Parser
# The string below is a raw CSV row with inconsistent spacing.
# Parse it into a clean list of values by:
#   1. Splitting on the comma
#   2. Stripping whitespace from each value
#   3. Converting numeric strings to integers where possible
# Print the final list.
# Methods: split(), strip(), isdigit()
# --------------------------------------------------------------
divider(4)

csv_row = "Alice , 30 , Toronto ,  developer , 95000"
row_list =  [v.strip() for v in csv_row.split(",")]
print(row_list)
final_row_list = []

for element in row_list:
    column = element.strip()
    if column.isdigit():
        final_row_list.append(int(column))
    else:
        final_row_list.append(column)    

print(final_row_list)

# --------------------------------------------------------------
# Challenge 5 — Title Slug Generator
# Write a function called slugify(title) that converts a
# blog post title into a URL-friendly slug:
#   - Lowercase everything
#   - Strip leading/trailing whitespace
#   - Replace all internal spaces with hyphens
#   - Remove any character that is not alphanumeric or a hyphen
# Example: "  Hello, World! " -> "hello-world"
# Methods: lower(), strip(), replace(), join(), isalnum()
# --------------------------------------------------------------
divider(5)

def slugify(title: str):
    slug = title.lower()
    slug = slug.strip()
    slug = slug.replace(" ", "-")
    slug = "".join(char for char in slug if char.isalnum() or char == "-")
    
    return slug

print(slugify("  Hello, World!  "))         # "hello-world"
print(slugify("Python 3.12 -- What's New")) # "python-312--whats-new"
print(slugify("  Top 10 Tips & Tricks  "))  # "top-10-tips--tricks"


# --------------------------------------------------------------
# Challenge 6 — Alignment Table
# Print a neatly aligned table for the data below.
# Each row should be:
#   Name left-aligned in 12 chars | score right-aligned in 6 chars
# Add a header row and a separator line of dashes.
# Methods: ljust(), rjust(), or f-string format spec
# --------------------------------------------------------------
divider(6)

results = [
    ("Alice",   95),
    ("Bob",     82),
    ("Charlie", 100),
    ("Diana",   78),
]

print(f"{"Name".ljust(12)}{"Score".rjust(6)}")
print("-" * 18)
for score in results:
    print(f"{score[0].ljust(12)}{str(score[1]).rjust(6)}")

# Here’s a dynamic version of the alignment table that automatically adjusts the column widths based on the longest name and score:
# Sample data
data = [
    ("Alice", 95),
    ("Bob", 87),
    ("Charlie", 78),
    ("Diana", 100),
    ("Elizabeth", 1200),  # longer name and bigger score
]

# Determine max widths dynamically
name_width = max(len(name) for name, _ in data)              #finds the longest name
score_width = max(len(str(score)) for _, score in data)      #finds the largest score length

# Print header
print(f"{'Name'.ljust(name_width)} | {'Score'.rjust(score_width)}") #align dynamically based on column widths
print("-" * (name_width + 3 + score_width))  # The separator line adjusts automatically

# Print each row
for name, score in data:
    print(f"{name.ljust(name_width)} | {str(score).rjust(score_width)}")

#Here’s a concise f-string version with dynamic widths—no .ljust() or .rjust() needed:
# Sample data
data = [
    ("Alice", 95),
    ("Bob", 87),
    ("Charlie", 78),
    ("Diana", 100),
    ("Elizabeth", 1200),
]

# Determine max widths dynamically
name_width = max(len(name) for name, _ in data)
score_width = max(len(str(score)) for _, score in data)

# Print header
print(f"{'Name':<{name_width}} | {'Score':>{score_width}}") #left-align header within dynamic width, right-align header dynamically
print("-" * (name_width + 3 + score_width))

# Print each row
for name, score in data:
    print(f"{name:<{name_width}} | {score:>{score_width}}") #left/right-align each row using the calculated widths



# --------------------------------------------------------------
# Challenge 7 — Email Extractor
# The string below contains a paragraph with an email address.
# Find the starting index of "@", then work outward (left and
# right) to extract the full email address without using regex.
# Print the extracted email.
# Methods: find(), rfind(), rpartition(), partition()
# --------------------------------------------------------------
# Challenge 7:  Find the "@" with find(); then slice left with rfind(" ") and right with find(" ", idx).
divider(7)
text = "Please contact support at help.desk@example.com for assistance."
# Step 1 — find the index of "@"
index_at = text.find("@")

# Step 2 — find the start of the email (space before "@")
start = text.rfind(" ", 0, index_at) + 1  # +1 to skip the space

# Step 3 — find the end of the email (space after "@")
end = text.find(" ", index_at)
if end == -1:  # if no space after, go to end of string
    end = len(text)

# Step 4 — extract the email
email = text[start:end]

# Step 5 — print the result
print(email)


# --------------------------------------------------------------
# Challenge 8 — Palindrome Checker
# Write a function called is_palindrome(text) that returns True
# if the text is a palindrome, ignoring case, spaces, and
# punctuation. Test it with the phrases below.
# Methods: lower(), isalnum(), join(), slicing [::-1]
# --------------------------------------------------------------
divider(8)

def is_palindrome(text):
    pal_str = text.lower().replace(" ", "")
    # Compare the string with its reverse
    return pal_str == pal_str[::-1]

print(is_palindrome("racecar"))                   # True
print(is_palindrome("A man a plan a canal Panama")) # True
print(is_palindrome("hello"))                     # False
print(is_palindrome("Was it a car or a cat I saw")) # True


# --------------------------------------------------------------
# Challenge 9 — Template Report Generator
# Use an f-string with format specifiers to build a short
# report string for the data below. Requirements:
#   - Name: left-aligned, width 15
#   - Score: right-aligned, width 6, 1 decimal place
#   - Percentage: shown as a percentage with 1 decimal place
#   - Total: formatted with a thousands separator
# Print the completed report.
# Concept: f-string format spec, :< :> :. :, :%
# --------------------------------------------------------------
divider(9)

student   = "Charlie"
score     = 432.7
max_score = 500
total_students = 1_284
# your code here
# Calculate percentage
percentage = score / max_score
# Build report string
report = f"Name: {student:<15} | Score: {score:>6.1f} | Percentage: {percentage:.1%} | Total Students: {total_students:,}"
print(report)

# Build a neatly aligned table for multiple students using the same formatting rules.
# Sample data: (Name, Score, Max Score)
students = [
    ("Alice", 478.5, 500),
    ("Bob", 392.3, 500),
    ("Charlie", 432.7, 500),
    ("Diana", 499.2, 500)
]

# Total students
total_students = len(students)

# Print header
print(f"{'Name':<15} | {'Score':>6} | {'%':>9} | {'Total Students':>14}")
print("-" * 52)

# Print each student's report row
for name, score, max_score in students:
    percentage = score / max_score
    print(f"{name:<15} | {score:>6.1f} | {percentage:.1%} | {total_students:>14,}")


# --------------------------------------------------------------
# Challenge 10 — String Compressor
# Write a function called compress(s) that performs basic
# run-length encoding on a string:
#   "aabbccddaa" -> "a2b2c2d2a2"
#   "abcd"       -> "a1b1c1d1"
#   "aaabba"     -> "a3b2a1"
# If the compressed string is NOT shorter than the original,
# return the original unchanged.
# Methods: string building with join(), len()
# --------------------------------------------------------------
divider(10)

def compress(s):
    if not s:   #If the input is empty (""), there’s nothing to compress.
        return s
    
    compressed = []  # to store parts of the compressed string
    count = 1        # start counting first character then keeps track of how many times the current character repeats consecutively
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1 # the character is repeating
        else:
            compressed.append(s[i-1] + str(count)) # append the previous character and its count to compressed
            count = 1 # reset count =1 for the new character (occurs at least once)
    
     # append the last character group
    compressed.append(s[-1] + str(count))

    # join list into string
    compressed_str = "".join(compressed)

    # return the shorter of original or compressed
    return compressed_str if len(compressed_str) < len(s) else s

print(compress("aabbccddaa"))    # "a2b2c2d2a2"
print(compress("aaabba"))        # "a3b2a1"
print(compress("abcd"))          # "abcd" — compressed is not shorter


# ============================================================
# BONUS TIPS
# - Strings are immutable — every method returns a NEW string.
#   Doing s.upper() does nothing unless you assign the result.
# - prefer f-strings over .format() or % for new code —
#   they are faster, more readable, and support full expressions.
# - join() is much faster than building a string with += in a
#   loop because strings are immutable and += copies each time.
# - casefold() is safer than lower() for Unicode comparisons.
# - removeprefix() and removesuffix() require Python 3.9+.
# ============================================================


# ============================================================
# HINTS — try to solve each challenge before reading these!
# ============================================================

# Challenge 1:  Chain the methods: raw_input.strip().title().replace("  ", " ").

# Challenge 2:  Check each condition with an early return False; return True only if all pass.

# Challenge 3:  Loop over sentence.lower().split(); use word_freq.get(word, 0) + 1 to count.

# Challenge 4:  Use a list comprehension: [v.strip() for v in csv_row.split(",")], then check isdigit().

# Challenge 5:  After lowering and replacing spaces with hyphens, filter chars with a join+isalnum check.

# Challenge 6:  Use f"{name:<12}{score:>6}" inside a loop, or .ljust()/.rjust() equivalents.

# Challenge 7:  Find the "@" with find(); then slice left with rfind(" ") and right with find(" ", idx).

# Challenge 8:  Build a cleaned string with "".join(c for c in text.lower() if c.isalnum()), then compare to its reverse.

# Challenge 9:  f"{student:<15}{score:>6.1f}  {score/max_score:>6.1%}  {total_students:,}"

# Challenge 10: Walk the string tracking current char and count; append f"{char}{count}" on each change.
