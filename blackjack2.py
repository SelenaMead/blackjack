import math
import random 
class Card:
    pass
    def cards():
        #OPTION OF CARDS
        deck_of_cards = [1,2,3,4,5,6,7,8,9,10,10,10,10,11]
        
        
        #randomizing deck and returning a card
        return random.choice(deck_of_cards)


# Deck should consist of Card objects
class Deck:
    pass
    def deck():
        #two cards being returned
        card = Card.cards()
        card2 = Card.cards()
        return [card, card2]


class Dealer:
    #dealers deck
    def dealers_deck():
        dealer_deck = Deck.deck()
        return dealer_deck
    #hiding first card of dealers
    def hide_deck():
        hiddencard = "X"
        deck = Dealer.dealers_deck()
        deck[0] = hiddencard
        return deck
    #dealers hit
    def hit_again():
        new_card = Card.cards()
        return new_card
    #dealers score
    def score(cards):
        total = 0
        for card in cards:
            total = card + total
        return total
    #displaying dealer's first card        
    def display_cards(deck):
        deck[0] = Card.cards()
        return deck       
    def dealer_turn(dealer_deck, dealer_score):
        while dealer_score < 17:
            dealer_deck.append(Dealer.hit_again())
            print("dealer has hit, their deck is now")
            print(dealer_deck)
            dealer_score = Dealer.score(dealer_deck)
        return dealer_score


class Human:
    pass
    #human's deck
    def deck():
        human_deck = Deck.deck()
        return human_deck
     #humans hit   
    def hit():
        return Card.cards()
        #human's score
    def score(cards):
        total = 0
        for card in cards:
            total = card + total
        return total 
    def human_turn(hit_or_stay, human_deck):
        #humans hit sequence
        while hit_or_stay == 'hit':
            hit_or_stay = input("Would you like to hit or stay?")
            if hit_or_stay == 'hit':
                print("Your new deck looks like: ")
                human_deck.append(Human.hit())
                print(human_deck)

   


# Run your program throught he run() method
class Game:
    #deciding on winner
    def winner(dealer, human):
        if human > dealer:
            return "You win!"
        elif human == dealer:
            return "You are tied!"
        elif human > 21:
            return "You bust! Dealer wins!"
        elif dealer > 21:
            return "Dealer bust! You win!"
        elif dealer and human > 21:
            return "Tie, you both bust"
        else:
            return "Dealer wins!"
    def __init__(self):
        print()
    def run():
        #variables
        human_deck = Human.deck()
        hit_or_stay = 'hit'
        dealer_deck = Dealer.hide_deck()

        print("Your cards are:  ")
        print(human_deck)
        print("Dealer's cards are " )
        print(dealer_deck)
        
       
        Human.human_turn(hit_or_stay, human_deck)
        
        print("Dealers cards are now shown: ")
        Dealer.display_cards(dealer_deck)
        print(dealer_deck)
        #checking score
        dealer_score = Dealer.score(dealer_deck)
        #dealers hit sequence
        dealer_score = Dealer.dealer_turn(dealer_deck, dealer_score)


        print("Your score is " )
        score = Human.score(human_deck)
        if score == 21:
            print("You have blackjack!")
        print(score)
        print("Dealer score is ")
        print(dealer_score)
        #bust scoring
        print(Game.winner(dealer_score, score))
        

        
    
Game.run()