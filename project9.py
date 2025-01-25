# secret auction program

def find_highest_bidder(bid_dictionary):
    highest_bid = 0
    winner = ""
    for bidder in bid_dictionary:
        amount = bid_dictionary[bidder]
        if amount > highest_bid:
            highest_bid = amount
            winner = bidder
    
    print(f"the winner is {winner} with a bid of ${highest_bid}")

bidders = {}
more_bidders = False
while not more_bidders:
    name = input("what is your name?: ")
    bid_amount = int(input("what is your bid?: $"))
    bidders[name] = bid_amount

    other_bidders = input("are there any other bidders? type 'yes' or 'no': ").lower()

    if other_bidders == "no":
        more_bidders = True
        find_highest_bidder(bidders)
    elif other_bidders == "yes":
        print("\n" * 50)