bids = {}
continue_bidding = True

def highest_bidder(bidding_dictionary):
    key = max(bidding_dictionary,key=bidding_dictionary.get)
    amount = bidding_dictionary[key]
    highest_bid = 0
    winner = ''
    print(f'The winner is {key} with a bid of ₹{amount}')
    # for bidder in bidding_dictionary:
    #     bid_amount = bidding_dictionary[bidder]
    #     if bid_amount > highest_bid:
    #         highest_bid = bid_amount
    #         winner = bidder
    #
    # print(f"The winner is {winner} with a bid of ₹{highest_bid}")


while continue_bidding:

    name = input("what is your name: ").upper()
    price = int(input("What is your bid? : ₹"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'Yes' or 'No'").lower()
    if should_continue == "no":
        continue_bidding = False
        highest_bidder(bids)
    else:
        print("\n" * 100)