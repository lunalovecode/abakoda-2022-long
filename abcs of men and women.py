name = input()
# I just reused and slightly modified my code from a past round lol 
def match(word, patt):
    ans_arr = [False for i in range(len(patt))]
    # check if the non-period letters match in the same position
    if len(word) != len(patt):
        return False
    for i in range(len(patt)):
        if word[i] == patt[i] or patt[i] == ".":
            ans_arr[i] = True
    
    if all(ans_arr):
        return True
    else:
        return False

if name == ".....":
    print("CAN'T TELL")
elif match("Alice", name):
    print("Alice")
elif match("Bob", name):
    print("Bob")
elif match("Cindy", name):
    print("Cindy")
else:
    print("SOMETHING'S WRONG")