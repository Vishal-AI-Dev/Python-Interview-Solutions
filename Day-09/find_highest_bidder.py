import os

# Function to clear console (Works on Windows/Mac/Linux)
def clear_screen():
    # 'nt' is for Windows, else is for Unix (Mac/Linux)
    os.system('cls' if os.name == 'nt' else 'clear')

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    
    # Looping through a dictionary gives you the Keys (Names)
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
            
    print(f"The winner is {winner} with a bid of ${highest_bid}")

# ---------------- Main Execution ---------------- #

bids = {} # Empty Dictionary
bidding_finished = False

print("Welcome to the Secret Auction Program.")

while not bidding_finished:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    
    # Store data in dictionary: Key=Name, Value=Price
    bids[name] = price
    
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    
    if should_continue == "no":
        bidding_finished = True
        clear_screen()
        find_highest_bidder(bids)
    elif should_continue == "yes":
        clear_screen()
    else:
        print("Invalid input. Ending auction.")
        bidding_finished = True
