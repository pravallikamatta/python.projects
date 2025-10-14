import os
def find_winner(bidder_details):
        highest_bid=0
        winner="" 
        for bidder in bidder_details:
           bidding_price=bidder_details[bidder]
           if bidding_price>highest_bid:
                  highest_bid=bidding_price
                  winner=bidder
        print(f"here is the list of all the bidders:{bidder_details}")  
        print(f"the winner is {winner} with a bid price of {highest_bid}")        
bidder_data={}
endofbid=False
while not endofbid:
        name= input("whats your name:- ")
        price= int(input("what much is your bid?-"))
        morebidders=input("is there any more bidders:-").lower()
        bidder_data[name]=price
        if morebidders=="no":
                endofbid=True
                find_winner(bidder_data)
        elif morebidders=="yes":
                os.system('cls')
     