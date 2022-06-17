list_of_numbers = [4,	80,	85,	59,	37, 25, 5, 64, 66, 81, 20, 64, 41, 22, 76, 76, 55, 96, 2, 68]


#Your code here:
def merge_two_list(list_of_integers):
  odds = []
  evens = []
  merdeg_list = []
  for number in list_of_numbers:
    if number % 2 != 0:
      odds.append(number)
    else:
      evens.append(number)
  merdeg_list.append(odds)
  merdeg_list.append(evens)
  return merdeg_list

print(merge_two_list(list_of_numbers))

