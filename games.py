import random
money = 1000
# Write your game of chance functions here


def coin_flip(coin_bet, call):
	payout = 0
	coin = ('heads', 'tails')
	flip = random.choice(coin)
	print("The coin landed on {}".format(flip))
	if flip == call:
		print("You won ${}".format(bet))
		payout = coin_bet * 2
	else:
		print("You lost ${}".format(bet))
	return payout


def cho_han(dice_bet, call):
	payout = 0
	roll = 0
	for i in range(2):
		die = random.randint(1, 6)
		roll += die
	print("The dice roll is {}".format(roll))
	if roll % 2 == 0:
		roll = "even"
	else:
		roll = "odd"
	if call == roll:
		print("You have won ${}".format(bet))
		payout = dice_bet * 2
	else:
		print("You have lost ${}".format(bet))
	return payout


def highest_card(card_bet):
	payout = 0
	player1_card = ''
	player2_card = ''
	# create a full deck of cards
	deck_of_cards = {"Spades": [], "Hearts": [], "Clubs": [], "Diamonds": []}
	for cards in deck_of_cards.values():
		for card in range(2, 15):
			cards.append(card)
	suits = list(deck_of_cards)
	numbers_to_cards = {11: "Jack", 12: "Queen", 13: "King", 14: "Ace"}
	suit_values = {"Spades": 3, "Hearts": 2, "Clubs": 1, "Diamonds": 0}
	# player 1 draws a random card
	player1_suit = random.choice(suits)
	player1_num = deck_of_cards[player1_suit].pop(random.randint(0, len(player1_suit) - 1))
	if player1_num in numbers_to_cards:
		for number in numbers_to_cards:
			if player1_num == number:
				player1_card = "{} of {}".format(numbers_to_cards[number], player1_suit)
	else:
		player1_card = "{} of {}".format(player1_num, player1_suit)
	# player 2 draws a random card
	player2_suit = random.choice(suits)
	player2_num = deck_of_cards[player2_suit].pop(random.randint(0, len(player2_suit) - 1))
	if player2_num in numbers_to_cards:
		for number in numbers_to_cards:
			if player2_num == number:
				player2_card = "{} of {}".format(numbers_to_cards[number], player2_suit)
	else:
		player2_card = "{} of {}".format(player2_num, player2_suit)
	# compare cards
	print("You drew the {}, and your opponent drew the {}".format(player1_card, player2_card))
	# in the event of a tie, add the suit value to the number
	if player1_num == player2_num:
		player1_num += suit_values[player1_suit]
		player2_num += suit_values[player2_suit]
	if player1_num > player2_num:
		payout = card_bet * 2
		print("You have won ${}".format(bet))
	else:
		print("You have lost ${}".format(bet))
	return payout

	
def roulette(betting):
	# possible bets in roulette are individual numbers, red, black, odd, and even
	# arguments will be {what you're betting on : bet amount}
	# build a roulette wheel with numbers from -1 to 36 with -1 representing 00
	payout = 0
	wheel = []
	black_numbers = []
	for number in range(-1, 37):
		wheel.append(number)
	# set the red numbers
	red_numbers = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
	# anything not in red will be black except 0 and 00
	for number in wheel:
		if number not in red_numbers:
			black_numbers.append(number)
	black_numbers.remove(-1)
	black_numbers.remove(0)
	# spin the wheel
	spin = random.choice(wheel)
	if spin in red_numbers:
		spin_plus_color = "Red {}".format(spin)
	elif spin in black_numbers:
		spin_plus_color = "Black {}".format(spin)
	elif spin == 0:
		spin_plus_color = "Green 0"
	else:
		spin_plus_color = "Green 00"
	print("The ball has landed on {}".format(spin_plus_color))
	# determine bets and payouts
	money_made = 0
	# first show the player his or her bets
	print("Your Bets")
	for key, value in betting.items():
		temp_key = key
		if temp_key == -1:
			temp_key = '00'
		print("{}: ${}".format(temp_key, value))
	print("-" * 30)
	# determine which bets are winners
	for key, value in betting.items():
		if key == 'red':
			if spin in red_numbers:
				print("Your red bet has made ${}".format(value))
				money_made += value
				payout += 2 * value
			else:
				print("Your red bet has lost ${}".format(value))
				money_made -= value
		elif key == 'black':
			if spin in black_numbers:
				print("Your black bet has made ${}".format(value))
				money_made += value
				payout += 2 * value
			else:
				print("Your red bet has lost ${}".format(value))
				money_made -= value
		elif key == "odd":
			if spin == -1 or spin == 0 or spin % 2 == 0:
				print("Your odd bet has lost ${}".format(value))
				money_made -= value
			else:
				print("Your odd bet has made ${}".format(value))
				money_made += value
				payout += 2 * value
		elif key == "even":
			if spin == -1 or spin == 0 or spin % 2 == 1:
				print("Your even bet has lost ${}".format(value))
				money_made -= value
			else:
				print("Your even bet has made ${}".format(value))
				money_made += value
				payout += 2 * value
		else:
			if key == spin:
				if key == -1:
					key = '00'
				winnings = value * 35
				print("Your bet on number {} has made ${}".format(key, winnings))
				money_made += winnings
				payout += (winnings + value)
			else:
				if key == -1:
					key = '00'
				print("Your bet on number {} has lost ${}".format(key, value))
				money_made -= value
	if money_made > 0:
		print("You have made ${}".format(money_made))
	elif money_made < 0:
		positive_money = money_made * -1
		print("You have lost ${}".format(positive_money))
	else:
		print("You broke even")
	return payout


def get_bet():
	global money
	betting = True
	cash_bet = ''
	while betting:
		try:
			cash_bet = int(input("Your bet?\n"))
		except ValueError:
			print("Bet must be an integer")
			print()
			continue
		if cash_bet > money:
			print("You don't have enough money to make that bet")
			print()
			continue
		money -= cash_bet
		betting = False
	return cash_bet
	

# Call your game of chance functions here
print()
print("Welcome to our exciting text-based casino!")
playing = True
while playing:
	if money == 0:
		print("You are out of money")
		print("Better luck next time!")
		playing = False
		continue
	print("You have ${}".format(money))
	print()
	game = input("""Choose a game:
[F]lip coin
[C]ho Han
[H]igh card
[R]oulette
[Q]uit
""").lower()
	if game == 'f':
		flipping = True
		while flipping:
			coin_call = input("Heads or tails?\n").lower()
			if coin_call == 'h':
				coin_call = 'heads'
			elif coin_call == 't':
				coin_call = 'tails'
			if coin_call != "heads" and coin_call != "tails":
				print("Please choose 'heads' or 'tails'")
				print()
				continue
			bet = get_bet()
			print('-' * 30)
			money += coin_flip(bet, coin_call)
			print('-' * 30)
			print("You have ${} remaining".format(money))
			if money == 0:
				flipping = False
				continue
			again = input("Play again? (y/n)\n").lower()
			print()
			if again == 'y':
				continue
			else:
				flipping = False
	elif game == "c":
		rolling = True
		while rolling:
			dice = input("Odd or even?\n").lower()
			if dice != "odd" and dice != "even":
				print("Please choose 'odd' or 'even'")
				print()
				continue
			bet = get_bet()
			print('-' * 30)
			money += cho_han(bet, dice)
			print('-' * 30)
			print("You have ${} remaining".format(money))
			if money == 0:
				rolling = False
				continue
			again = input("Roll again? (y/n)\n").lower()
			print()
			if again == 'y':
				continue
			else:
				rolling = False
	elif game == 'h':
		drawing = True
		while drawing:
			bet = get_bet()
			print('-' * 30)
			money += highest_card(bet)
			print('-' * 30)
			print("You have ${} remaining".format(money))
			if money == 0:
				drawing = False
				continue
			again = input("Draw again? (y/n)\n").lower()
			print()
			if again == 'y':
				continue
			else:
				drawing = False
	elif game == 'r':
		spinning = True
		roulette_bets = {}
		while spinning:
			print()
			type_of_bet = input("""Place your bets on the table:
[N]umber
[O]dd
[E]ven
[R]ed
[B]lack
[S]pin
""").lower()
			if type_of_bet == 'n':
				number_to_bet = input("What number whould you like to bet?\n")
				if number_to_bet == '00':
					number_to_bet = '-1'
				try:
					number_to_bet = int(number_to_bet)
				except ValueError:
					print("Value must be a number between 00 and 36")
					print()
					continue
				if number_to_bet < -1 or number_to_bet > 36:
					print("Value must be a number between 00 and 36")
					print()
				roulette_bets[number_to_bet] = get_bet()
			elif type_of_bet == 'o':
				roulette_bets['odd'] = get_bet()
			elif type_of_bet == 'e':
				roulette_bets['even'] = get_bet()
			elif type_of_bet == 'r':
				roulette_bets['red'] = get_bet()
			elif type_of_bet == 'b':
				roulette_bets['black'] = get_bet()
			elif type_of_bet == 's':
				print('-' * 30)
				money += roulette(roulette_bets)
				print('-' * 30)
				print("You have ${} remaining".format(money))
				if money == 0:
					spinning = False	
					continue			
				again = input("Spin again? (y/n)\n")
				if again == 'y':
					roulette_bets = {}
					continue
				else:
					spinning = False	
	elif game == 'q':
		print("You walked away with ${}".format(money))
		if money > 1000:
			print("Great job!")
		else:
			print("Better luck next time.")
		playing = False
