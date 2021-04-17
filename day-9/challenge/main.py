from art import logo

print(logo)


all_bid_list = {}
bid_end = False


def highest_bid(all_bid_list):
    highest_bid = 0
    winner = ""
    for bid_name in all_bid_list:
        price = all_bid_list[bid_name]
        if price > highest_bid:
            highest_bid = price
            winner = bid_name
    print(f"The winner is {winner} with a bid of ${highest_bid}")


while not bid_end:
    name = input("What is your name?\n")
    price = int(input("What is your bid amount? \n"))
    all_bid_list[name] = price

    restart = input(
        "Is there any other BID 'yes' or 'no'.\n")
    if restart == "no":
        bid_end = True
        highest_bid(all_bid_list)
