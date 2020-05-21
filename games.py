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


def highest_card(bet=5):
	global money
	deck_of_cards = {"Spades": [], "Hearts": [], "Clubs": [], "Diamonds": []}
	for cards in deck_of_cards.values():
		for card in range(2, 15):
			cards.append(card)
	suits = list(deck_of_cards)
	numbers_to_cards = {11: "Jack", 12: "Queen", 13: "King", 14: "Ace"}
	player1_suit = random.choice(suits)
	player1_num = deck_of_cards[player1_suit].pop(random.randint(0,12))
	if player1_num in numbers_to_cards:
		for number in numbers_to_cards:
			if player1_num == number:
				player1_card = "{} of {}".format(numbers_to_cards[number], player1_suit)
	else:
		player1_card = "{} of {}".format(player1_num, player1_suit)
	player2_suit = random.choice(suits)
	if player2_suit == player1_suit:
		player2_num = deck_of_cards[player2_suit].pop(random.randint(0,11))
	else:
		player2_num = deck_of_cards[player2_suit].pop(random.randint(0,12))
	if player2_num in numbers_to_cards:
		for number in numbers_to_cards:
			if player2_num == number:
				player2_card = "{} of {}".format(numbers_to_cards[number], player2_suit)
	else:
		player2_card = "{} of {}".format(player2_num, player2_suit)
	print("You drew the {}, and your opponent drew the {}".format(player1_card, player2_card))
	if player1_num == player2_num:
		print("It's a tie")
		print("You now have ${}".format(money))
	elif player1_num > player2_num:
		money += bet
		print("You have won ${}".format(bet))
		print("You now have ${}".format(money))
	else:
		money -= bet
		print("You have lost ${}".format(bet))
		print("You now have ${}".format(money))

	
	
#Call your game of chance functions here
coin_flip(10, "tails")
cho_han(20, "even")
highest_card(50)