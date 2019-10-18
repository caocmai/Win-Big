import random
random.seed(40)

all_guessed_nums = [[2,3,4,5], [2,3,6], [2,3,5], [5,6,7,8]]


def check_all(win_nums, guessed_nums_list):
  win_count = 0
  for i in range(len(guessed_nums_list)):
    if win(win_nums, guessed_nums_list[i]):
      win_count += 1
    # else:
      # print("you lose")
  return win_count

winning_nums = [] # 8,10,9
guessed_nums = []

for _ in range(3):
  random_num = random.randrange(1,11)
  winning_nums.append(random_num)

def win(win_nums, guessed_nums):
    for i in range(len(win_nums)):
        if win_nums[i] != guessed_nums[i]:
            return False
    return True

count_lose = 0
count_win = 0
# running = True
while count_win <= 0:
  # random.seed(30) # 9,5,10
  guessed_nums.sort()
  winning_nums.sort()

  for _ in range(3):
    random_num = random.randrange(1,11)
    guessed_nums.append(random_num)
  # print(guessed_nums)
  
  if win(winning_nums,guessed_nums):
    count_win += 1
    print(f"Guessed number: {guessed_nums}")
    print(f"Winning Number: {winning_nums}")

    print("win")
    # break
  else:
    count_lose += 1
    # print("lose")

  guessed_nums = []
  
  
print(f"win count: {count_win}")
print(f"lose count: {count_lose}")

print("probablity of wiining " + str(round((count_win/count_lose * 100), 2 )))
print(f"Winning numbers are: {winning_nums}")

