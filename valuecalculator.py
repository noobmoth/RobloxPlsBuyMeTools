#very basic script made by suepunk on discord (username Bosacius on Roblox)
while True:
    print("ROBLOX PLS BUY ME card value calculator")
    print("My discord: suepunk")
    print("1 for calculating taxes, 2 for calculating best value to sell certain item for")
    operation = input()
    if operation == "1":
        price = input("Price: ")
        print("If you sell for that price, you get: " + str(round((60 * int(price)/100)))) #round(30 * valuebought/100)
    elif operation == "2":
        print("(input 0 if its your own card)")
        valuebought = int(input("Value you bought the item for: "))
        if valuebought == 0:
            editionsleft = int(input("Editions left: "))
            valueofcard = int(input("Fame: "))
            totalprice = 0
            if valueofcard < 500:
                totalprice += 7
            if editionsleft <= 5 and valueofcard >= 500:
                totalprice += 30
            elif editionsleft <= 10:
                totalprice += 15
            elif editionsleft <= 20:
                totalprice += 5
            if valueofcard >= 10000:
                totalprice += round((1 * valueofcard)/100)
            elif valueofcard >= 7000:
                totalprice += 90
            elif valueofcard >= 3000:
                totalprice += 40
            elif valueofcard >= 1000:
                totalprice += 20
            elif valueofcard >= 500:
                totalprice += 10
            if totalprice <= 12:
                print("Ideal price is between "+ str(totalprice) +" and " + str(totalprice + 5))    
            else:
                print("Ideal price is between "+ str(totalprice - 5) +" and " + str(totalprice + 5))    
        else:
            totalprice = 0
            fameofcard = int(input("Fame of the card: "))
            if fameofcard <= 200:
                while True:
                    print("")
                    result55 = input("is it at least a famous user, namesnipe, old account or a card that is going up? (yes/no): ")
                    if result55 == "yes" or result55 == "Yes":
                        print("")
                        print("Oh okay, then wait for it to be more valuable, good one tho")
                        break
                    elif result55 == "no" or result55 == "No":
                        print("")
                        print("sorry for being toxic, but except you bought that card intentionally this isnt a good game for you, go back to brookhaven.")
                        break
                    else:
                        print("")
                        print("Repeat that again, remember to answer yes or no but in lowercase...")
            elif fameofcard <= 1000:
                totalprice += 15
            elif fameofcard <= 2000:
                totalprice += 30
            elif fameofcard <= 5000:
                totalprice += 55
            elif fameofcard <= 10000:
                totalprice += 70
            elif fameofcard <= 15000:
                totalprice += 90
            elif fameofcard <= 30000:
                totalprice += 110
            elif fameofcard <= 60000:
                totalprice += 200
            elif fameofcard <= 150000:
                totalprice += 300
            else:
                totalprice += 750
            extrabenefit = round(30 * valuebought/100)
            totalprice += (valuebought + extrabenefit)
            print("")
            print("You shouldn't sell that card for less than " + str(totalprice))
            print("If you sell for "+str(totalprice)+", you get: " + str(round((60 * int(totalprice)/100))))
            print("")
            print("In case it's a known user, add more price depending on how famous he is.")
    print("")
    closing = input("Press any key to continue")
