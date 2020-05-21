import random
money = 100

#Write your game of chance functions here
def coin_flip(bet=5, call="heads"):
	global money
	if call.lower() != "heads" and call.lower() != "tails":
		return
	flip = random.randint(1, 2)
	if flip == 1:
		flip = "heads"
		print("The coin has landed on heads.")
	else:
		flip = "tails"
		print("The coin has landed on tails")
	if flip == call:
		print("You have won ${}".format(bet))
		money += bet
	else:
		print("You have lost ${}".format(bet))
		money -= bet
	print("You now have ${} remaining.".format(money))


def cho_han(bet=5, call="even"):
	global money
	if call.lower() != "odd" and call.lower() != "even":
		return
	roll = random.randint(2, 12)
	print("The dice roll is {}".format(roll))
	if roll % 2 == 0:
		roll = "even"
	else:
		roll = "odd"
	if call == roll:
		print("You have won ${}".format(bet))
		money += bet
	else:
		print("You have lost ${}".format(bet))
		money -= bet
	print("You now have ${} remaining.".format(money))


def highest_card():
	deck_of_cards = []
	for suit in range(4):
		for card in range(2, 15):
			deck_of_cards.append(card)
	player1_card_index = random.randint(0, 52)
	player1_card = deck_of_cards.pop(player1_card_index)
	player2_card_index = random.randint(0, 51)
	player2_card = deck_of_cards.pop(player2_card_index)
	print(player1_card)
	print(player2_card)
	print(deck_of_cards)	

#Call your game of chance functions here
# coin_flip(10, "tails")
# cho_han(20, "even")

highest_card()