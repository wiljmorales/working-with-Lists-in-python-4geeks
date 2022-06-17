theBools = [0,1,0,0,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1]

#Your code go here:
def wiki_woko(number):
  if number:
    return "wiki"
  else:
    return "woko"

print(list(map(wiki_woko, theBools)))
