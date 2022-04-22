import unittest
from blackjack2 import Game, Human, Dealer

class Test_Blackjack(unittest.TestCase):

    #testing score for player
    def test_human_score(self):
        self.assertAlmostEqual(Human.score([1,3]), 4)
        self.assertAlmostEqual(Human.score([10,10]), 20)
        self.assertAlmostEqual(Human.score([1,11]), 12)
    #testing winner
    def test_winner(self):
        self.assertEqual(Game.winner(21,20), "Dealer wins!")
        self.assertEqual(Game.winner(20,21), "You win!")
    #testing while loop for player    
    def test_human_turn(self):
        self.assertTrue(Human.human_turn(True,  [10,9]), True)
    #make sure that dealer has a score of 17 or more 
    def test_dealer_score(self):
        self.assertGreater(Dealer.dealer_turn([5,7], 12),16)
    #make sure that dealer's first card is being hidden
    def test_hide_deck(self):
        self.assertEqual(Dealer.hide_deck()[0], 'X')




