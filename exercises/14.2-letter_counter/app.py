par = "Lorem ipsum dolor sit amet consectetur adipiscing elit Curabitur eget bibendum turpis Curabitur scelerisque eros ultricies venenatis mi at tempor nisl Integer tincidunt accumsan cursus"

counts = {}
#your code go here:
for letter in par.lower().replace(" ", ""):
  if counts.get(letter) == None:
    counts[letter] = 1
  else:
    counts[letter] += 1

print(counts)

