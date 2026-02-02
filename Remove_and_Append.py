letters = ['a','b','c','d']
out = []

for ch in letters:
#compare ASCII values of letters with 'c'
    if ch < 'c':
        out.append(ch)
#remove if the condition is met
    letters.remove(ch)

size = len(letters)+len(out)
print(size)

print(out)