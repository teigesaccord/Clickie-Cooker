import time

cheating = True


click = 1
auto_click = 0
multiplier = 1
score = 0 
passive = 0

def info():
	global click
	global score
	global multiplier
	global auto_click
	global passive
	print("\nWelcome to Clickie Cooker! To click just write C or click into the terminal."+
	 "To go to the store just write s or store."+" If you have more questions, you can type info or i to read this again.\n")

	print(f"Current Score {score}")
	print(f"Current Auto Clickers: {auto_click} Current Multiplier: {multiplier}")
	print(f"Passive bonus from extra equipment and grannys{passive}")



def bank(price):
	global score
	if score >= price or cheating == True:
		return True
	else:
		print("Sorry Bro. You are too broke. I'm not running a charity.")
		return False


def store():
	global click
	global score
	global multiplier
	global auto_click
	global passive

	print(f"Current Auto Clickers: {auto_click} Current Multiplier: {multiplier}")
	stock = {"#1 Auto Clicker": 50, "#2 Click Multiplier": 100, "#3 Craigslist Microwave": 250, "#4 Solid Microwave": 1000, "#5 Sexy Microwave":5000,
	"#6 Small Oven":15000, "#7 Craigslist Grandma's Help":50000, "#8 Solid Grandma's Help":150000, "#9 Sexy Grandma's Help":500000, 
	"#10 Craigslist Angelic essence ":1000000, "#11 Solid Angelic essence ":25000000, "#12 Sexy Angelic essence ":100000000}

	print(f"Welcome to the circus of values! {stock}")
	purchase = input("What are ya buyin?")
	if purchase == "1":
		if bank(50):
			score = score - 50
			auto_click = auto_click + .3
			return auto_click
	if purchase =="2":
		if bank(100):
			score = score - 100
			multiplier = multiplier + .5
			return multiplier

	if purchase =="3":
		if bank(250):
			score = score - 250
			passive = passive + 5

	if purchase =="4":
		if bank(1000):
			score = score - 1000
			passive = passive + 25

	if purchase =="5":
		if bank(5000):
			score = score - 5000
			passive = passive + 150

	if purchase =="6":
		if bank(15000):
			score = score - 15000
			passive = passive + 500

	if purchase =="7":
		if bank(50000):
			score = score - 50000
			passive = passive + 10000

	if purchase =="8":
		if bank(150000):
			score = score - 150000
			passive = passive + 35000


	if purchase =="9":
		if bank(500000):
			score = score - 500000
			passive = passive + 90000


	if purchase =="10":
		if bank(1000000):
			score = score - 1000000
			passive = passive + 300000


	if purchase =="11":
		if bank(25000000):
			score = score - 25000000
			passive = passive + 1000000

	if purchase =="12":
		if bank(100000000):
			score = score - 100000000
			passive = passive + 99999999999


def clicker():
	global click
	global score
	global multiplier
	global auto_click
	global passive
	info()
	while True:
		start = time.time()
		print(f"Score = {score}")
		move = input("Show me your Move!")
		if move == "click" or move == "c":
			score = score + (click * multiplier)

		if move == "store" or move == "s":
			store()

		if move == "info" or move == "i":
			info()

		if move == "exit" or move == "e":
			break

		end = time.time()
		seconds = end - start
		score = score + (seconds * (auto_click * multiplier)) + (seconds * passive)


clicker()