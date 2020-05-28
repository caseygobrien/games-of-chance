import random
money = 1000
# Write your game of chance functions here


def coin_flip(bet, call):
	payout = 0
	flip = random.randint(1, 2)
	if flip == 1:
		flip = "heads"
		print("The coin landed on heads.")
	else:
		flip = "tails"
		print("The coin landed on tails")
	if flip == call:
		print("You won ${}".format(bet))
		payout = bet *2
	else:
		print("You lost ${}".format(bet))
	return payout

def cho_han(bet, call):
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
		payout = bet * 2
	else:
		print("You have lost ${}".format(bet))
	return payout

def highest_card(bet):
	payout = 0
	player1_card = ''
	player2_card = ''
	deck_of_cards = {"Spades": [], "Hearts": [], "Clubs": [], "Diamonds": []}
	for cards in deck_of_cards.values():
		for card in range(2, 15):
			cards.append(card)
	suits = list(deck_of_cards)
	numbers_to_cards = {11: "Jack", 12: "Queen", 13: "King", 14: "Ace"}
	player1_suit = random.choice(suits)
	player1_num = deck_of_cards[player1_suit].pop(random.randint(0, len(player1_suit) - 1))
	if player1_num in numbers_to_cards:
		for number in numbers_to_cards:
			if player1_num == number:
				player1_card = "{} of {}".format(numbers_to_cards[number], player1_suit)
	else:
		player1_card = "{} of {}".format(player1_num, player1_suit)
	player2_suit = random.choice(suits)
	player2_num = deck_of_cards[player2_suit].pop(random.randint(0, len(player2_suit) - 1))
	if player2_num in numbers_to_cards:
		for number in numbers_to_cards:
			if player2_num == number:
				player2_card = "{} of {}".format(numbers_to_cards[number], player2_suit)
	else:
		player2_card = "{} of {}".format(player2_num, player2_suit)
	print("You drew the {}, and your opponent drew the {}".format(player1_card, player2_card))
	if player1_num == player2_num:
		print("It's a tie")
		payout = bet
	elif player1_num > player2_num:
		payout = bet * 2
		print("You have won ${}".format(bet))
	else:
		print("You have lost ${}".format(bet))
	return payout

	
def roulette(betting):
	# possible bets in roulette are individual numbers, red, black, odd, and even
	# arguments will be {what you're betting on : bet amount}
	payout = 0
	wheel = []
	black_numbers = []
	for number in range(-1, 37):
		wheel.append(number)
	red_numbers = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
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
	print("Your Bets")
	for key, value in betting.items():
		print("{}: ${}".format(key, value))
	print("-" * 30)
	for key, value in betting.items():
		if key == '00':
			betting[-1] = betting.pop("00")
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
				winnings = value * 35
				print("Your bet on number {} has made ${}".format(key, winnings))
				money_made += winnings
				payout += (winnings + value)
			else:
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
	while betting:
		try:
			bet = int(input("Your bet?\n"))
		except ValueError:
			print("Bet must be an integer")
			print()
			continue
		if bet > money:
			print("You don't have enough money to make that bet")
			print()
			continue
		money -= bet
		betting = False
	return bet
	


# Call your game of chance functions here
print()
print("Welcome to our exciting text-based casino!")
playing = True
while playing:
	if money == 0:
		print("You are out of money")
		print("Better luck next time!")
		break
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
			coin = input("Heads or tails?\n").lower()
			if coin != "heads" and coin != "tails":
				print("Please choose 'heads' or 'tails'")
				print()
				continue
			bet = get_bet()
			print('-' * 30)
			money += coin_flip(bet, coin)
			print('-' * 30)
			print("You have ${} remaining".format(money))
			if money ==0:
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
			elif type_of_bet =='s':
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
