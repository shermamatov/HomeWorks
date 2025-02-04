# 1
myfamily = ("mother", "father", "sister", "brother", "sister")
print("Type of myfamily:", type(myfamily))
print("First 'sister':", myfamily[2]) 
print("Second 'sister':", myfamily[4]) 
try:
    myfamily.append("me")
except AttributeError as e:
    print("Error:", e, "- we can't change tuple")

try:
    myfamily.pop()
except AttributeError as e:
    print("Error:", e, "- we can't remove some element from tuple")
