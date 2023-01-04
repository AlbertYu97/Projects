############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
import random
# from replit import clear
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
# Cards deck
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Define a funcion to count the score of a card list  
# If an ace is drawn, count it as 11. But if the total goes over 21, count the ace as 1 instead.
def count_score(card_list):
  score = sum(card_list)
  if score == 21 and len(card_list) == 2:
    score = 0  
  if score > 21:
    for index in range(len(card_list)):
      # For every of the A, count it as 1
      if card_list[index] == 11:
        card_list[index] = 1
    score = sum(card_list)
  return score

# Define a function to deal random cards from the list
def deal_card():
  card = random.choice(cards)
  return card

  
def blackjack():
  print(logo)
  # Deal 2 cards for Player and Dealer and store them in a list
  player_cards = []
  dealer_cards = []
  for step in range(2):
    player_cards.append(deal_card())
    dealer_cards.append(deal_card())  

  # Calculate scores for dealer and player
  dealer_score = count_score(dealer_cards)
  player_score = count_score(player_cards)
  print(f"Your cards: {player_cards}, current score: {player_score}")
  print(f"Dealer first card: {dealer_cards[0]}")  
  continue_play = True
  # Detect the blackjack situation. If dealer has blackjack, dealer wins
  # Use a while loop to keep running the game until player type 'n'
  if dealer_score== 21 and len(dealer_cards) == 2:
      print("Dealer wins, Blackjack!")
      continue_play = False
  elif player_score == 21 and len(player_cards) == 2:
      print("Player wins, Blackjack")
      continue_play = False
  
         
  #Ask the user if they want to get another card.
  
  while continue_play:
    player_continue = input("Type 'y' to get another card, type 'n' to pass: ").lower()
    if player_continue == 'y':
      player_cards.append(deal_card())
      player_score = count_score(player_cards)
      # Check if the score gets over 21
      if player_score > 21:
        print(f"You went over. You lose.")
        continue_play = False
      print(f"Your cards: {player_cards}, final score: {player_score}")
      print(f"Dealer's first card: {dealer_cards[0]}")
    elif player_continue == 'n':
      continue_play = False
  
  # Dealer play
  # The dealer should keep drawing cards unless their score goes over 17.
  if player_score < 21:
    while count_score(dealer_cards) < 17:
      dealer_cards.append(deal_card())
    # If two orginal cards sum over 17 and has an Ace
    dealer_score = count_score(dealer_cards)
      # Print Player and Dealer's final hand
    print(f"Your final hand: {player_cards}, final score: {player_score}")
    print(f"Dealer's final hand: {dealer_cards}, final score: {dealer_score}")
    # check if dealer's score is over 21  
    if dealer_score > 21:    
        print("Dealer went over. You win.")
    elif dealer_score > player_score:
      print("You lose")
    elif dealer_score == player_score:
      print("Tie game")
    else:
      print("You win")
  while input("Do you want to play a game of Blackjack? Type 'y' or 'n': "). lower() == 'y':
    # clear()
    blackjack()

blackjack()