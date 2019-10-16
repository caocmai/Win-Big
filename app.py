wi_n = [2,3,6,9]
# gu_n = [2,3,7,9]
gu_n = [[2,3,4,5], [2,3,6,8], [2,3,6,9], [5,6,7,8]]

# def win(win_nums, guessed_nums):
#   for i in range(len(guessed_nums)):
#     for numbers in guessed_nums[i]:
#       if numbers not in win_nums:
#         return False
#     return True

def win(win_nums, guessed_nums):
  for num in guessed_nums:
    if num not in win_nums:
      return False
  return True

# print(win(wi_n, gu_n))

def check_all(win_nums, guessed_nums_list):
  for i in range(len(guessed_nums_list)):
    if win(win_nums, guessed_nums_list[i]):
      print("you win")
    else:
      print("you lose")

check_all(wi_n, gu_n)