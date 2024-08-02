def rem(l, word):
    n = []
    for item in l:
        if not (item == word):
            n.append(item.strip(word))

    return n


l = ["Harry", "Raj", "Ritiksha", "Gaurav", "Rohan", "Sohan", "an"]
print(rem(l, "an"))
