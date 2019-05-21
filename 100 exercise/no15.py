#Keyboard Row


def keyboardRow(words):
    keyboard = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
    out = []
    for i in words:
        for line in keyboard:
            lword = i.lower()
            if set(lword).issubset(set(line)):
                out.append(i)
    return out
#   print(set('abc'))

input = ["Hello", "Alaska", "Dad", "Peace"]
print(keyboardRow(input))

