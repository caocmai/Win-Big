import random
from flask import Flask, render_template, url_for, request, redirect
# random.seed(40)

app = Flask(__name__)
winning_nums = [2,3,6]
guessed_nums = []

@app.route("/get_form_data", methods=["POST"])
def get_form_data():
  num1 = request.form.get("number1")
  guessed_nums.append(int(num1))
  return redirect(url_for("view_ticket"))

@app.route("/")
def index():
  return render_template("home.html", title={})

@app.route("/view_ticket")
def view_ticket():
  guessed_nums.sort()
  return render_template("ticket_page.html", all_guessed_nums=guessed_nums)

@app.route("/get_random_num")
def get_random_num():
  random_num = random.randrange(1,11)
  guessed_nums.append(random_num)
  return redirect(url_for("view_ticket"))

@app.route("/check_ticket")
def check_ticket():
  if win(winning_nums, guessed_nums):
    return render_template("check_ticket.html", win=True, winning_nums=winning_nums, guessed_nums=guessed_nums)
  else:
    return render_template("check_ticket.html", win={}, winning_nums=winning_nums, guessed_nums=guessed_nums)

@app.route("/reset_num")
def reset_num():
  guessed_nums.clear()
  return redirect(url_for("view_ticket"))

if __name__ == "__main__":
    app.run(debug=True)



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

# print(f"You won {check_all(winning_nums, all_guessed_nums)} out of {len(all_guessed_nums)} plays.")
# print("For " + str(check_all(winning_nums, all_guessed_nums)/len(all_guessed_nums)) + " percent.")
# print((check_all(winning_nums, all_guessed_nums)/len(all_guessed_nums)))