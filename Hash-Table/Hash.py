grades = {}

grades["A"] = "Outstanding"
grades["B"] = "Brave"

retrieve = grades["A"]

print(retrieve)

if "B" in grades:
    print("B Is In The Hash Table")
else:
    print("B Is Not In The Hash Table")