bid = list(map(int,input("Enter All Bid : ").split()))
if len(bid) > 1:
    bid.sort(reverse=True)
    # print(bid)
    if bid[0] == bid[1]:
        print("error : have more than one highest bid")
    else:
        print(f"winner bid is {bid[0]} need to pay {bid[1]}")
else:
    print("not enough bidder")