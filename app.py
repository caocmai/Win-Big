import random
from flask import Flask, render_template, url_for, request, redirect
from pymongo import MongoClient
from bson.objectid import ObjectId
import os
# random.seed(40)

# For Heroku
host = os.environ.get("MONGODB_URI", "mongodb://admin:abc123@ds335678.mlab.com:35678/heroku_c4rczcz7")
client = MongoClient(host=f'{host}?retryWrites=false')
db = client.get_default_database()
tickets = db.tickets

# For Local
# client = MongoClient()
# db = client.first_intensive
# tickets = db.tickets

app = Flask(__name__)
winning_nums = [2,3,6]

''' This is the index route '''
@app.route("/")
def index(): 
  return render_template("home.html", title={}, ticket={})

''' This route get the information from the form and adds it to the tickets db '''
@app.route("/get_form_data", methods=["POST"])
def get_form_data():
  # num1 = request.form.get("number1")
  ticket = {
    "number1" : request.form.get("number1"),
    "number2" : request.form.get("number2"),
    "number3" : request.form.get("number3")
  }
  tickets.insert_one(ticket)
  # guessed_nums.append(int(num1))
  return redirect(url_for("view_ticket"))

# Deletes entire ticket list
@app.route("/delete_all")
def delete_all():
    tickets.remove()
    return redirect(url_for("index"))

# This page displays all the tickets in the tickets db
@app.route("/view_ticket")
def view_ticket():
  return render_template("ticket_page.html", tickets=tickets.find(), title="View Ticket")

''' This route takes the ticket id and finds it in the database and gets passed to edit ticket page '''
@app.route("/tickets/<ticket_id>/edit")
def edit_ticket(ticket_id):
  ticket = tickets.find_one({"_id": ObjectId(ticket_id)})
  return render_template("edit_ticket.html", ticket=ticket, title="Edit Ticket")

''' This route updates the ticket with new information from the ticket form with the original information '''
@app.route("/tickets/<ticket_id>", methods=["POST"])
def update_ticket(ticket_id):
  updated_ticket = {
    "number1" : request.form.get("number1"),
    "number2" : request.form.get("number2"),
    "number3" : request.form.get("number3")
  }
  tickets.update_one(
    {"_id": ObjectId(ticket_id)},
    {"$set": updated_ticket}
    )
  return render_template("ticket_page.html", tickets=tickets.find(), title="Check Ticket")

# This route deletes the ticket with a specific id and reroutes to the view ticket page
@app.route("/tickets/delete/<ticket_id>", methods=["POST"])
def delete_single(ticket_id):
  tickets.delete_one({"_id": ObjectId(ticket_id)})
  return redirect(url_for("view_ticket"))

# Helper function to determine if numbers are matched to winning numbers
def win(win_nums, guessed_nums):
  for i in range(len(win_nums)):
      if win_nums[i] != guessed_nums[i]:
          return False
  return True

# This is a function to check all instances in the list wether matches or not and adds to the win count
def check_all(win_nums, guessed_nums_list):
  win_count = 0
  for i in range(len(guessed_nums_list)):
    if win(win_nums, guessed_nums_list[i]):
      win_count += 1
    # else:
      # print("you lose")
  return win_count

''' This route has all the logic and calculations to determine if ticket(s) matched to winning nums '''
@app.route("/check_ticket")
def check_ticket():
  all_guessed_nums = []
  num_tickets = 0
  cost = 0
  for ticket in tickets.find({}):
    guessed_nums_temp = []
    guessed_nums_temp.append(int(ticket["number1"]))
    guessed_nums_temp.append(int(ticket["number2"]))
    guessed_nums_temp.append(int(ticket["number3"]))
    # guessed_nums_temp.sort()
    num_tickets += 1
    all_guessed_nums.append(guessed_nums_temp)
    guessed_nums_temp = []
  
  win_times = check_all(winning_nums, all_guessed_nums)

  if num_tickets > 0:
    for _ in range(num_tickets):
      cost -= 2
  if win_times > 0:
    cost = (500 * win_times) + cost

  return render_template("checking_page.html", win=win_times, 
                          winning_nums=winning_nums, tickets=tickets.find(), 
                          count=num_tickets, cost=cost, title="Results")

# This route goes to the play to win form when play till win is clicked
@app.route("/play_to_win")
def play_to_win():
  return render_template("play_to_win_form.html", title="Play Till Win", ticket={})

''' This route has all the logic and calculations to determin the number of time
    to win at least once when the play select their ticket numbers '''
@app.route("/check_play_to_win", methods=["POST"])
def check_play_to_win():
  to_win_nums = []
  generated_num = []

  to_win_nums.append(int(request.form.get("number1")))
  to_win_nums.append(int(request.form.get("number2")))
  to_win_nums.append(int(request.form.get("number3")))

  count_lose = 1
  count_win = 0
  while count_win <= 0:
    # to_win_nums.sort()
    # generated_num.sort()
    # random.seed(40)

    for _ in range(3):
      new_num = random.randrange(1,10)
      generated_num.append(new_num)
  
    print(generated_num)
    if win(to_win_nums,generated_num):
      count_win += 1
    else:
      count_lose += 1
    
    generated_num = []

    cost = (count_lose * 2) - (count_win * 500)

  return render_template("till_win_check.html", to_win_nums=to_win_nums, 
                          count_lose=count_lose, count_win=count_win, cost=cost)

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))