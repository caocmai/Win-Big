import random
random.seed(40)
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    """Return homepage."""
    return 'Hello, world!'

if __name__ == '__main__':
    app.run(debug=True)


winning_nums = [2,3,6]
# all_guessed_nums = [2,3,7,9]
all_guessed_nums = [[2,3,4,5], [2,3,6], [2,3,5], [5,6,7,8]]

# random_guessed_nums = []

# def generate_random_num(times):
#   for _ in range(times):
#     random_num = random.randrange(1,11)
#     random_guessed_nums.append(random_num)

# generate_random_num(3)
# print(random_guessed_nums)


def win(win_nums, guessed_nums):
  for i in range(len(win_nums)):
      if win_nums[i] != guessed_nums[i]:
          return False
  return True

# print(win(winning_nums, all_guessed_nums))

def check_all(win_nums, guessed_nums_list):
  win_count = 0
  for i in range(len(guessed_nums_list)):
    if win(win_nums, guessed_nums_list[i]):
      win_count += 1
    # else:
      # print("you lose")
  return win_count

print(f"You won {check_all(winning_nums, all_guessed_nums)} out of {len(all_guessed_nums)} plays.")
print("For " + str(check_all(winning_nums, all_guessed_nums)/len(all_guessed_nums)) + " percent.")
# print((check_all(winning_nums, all_guessed_nums)/len(all_guessed_nums)))