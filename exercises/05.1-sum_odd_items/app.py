arr = [4,5,734,43,45,100,4,56,23,67,23,58,45]

#Your code go here:

def sumOdds(list):
  result = 0
  for number in list:
    if number % 2 != 0:
      result += number
  print(result)
  return result

sumOdds(arr)