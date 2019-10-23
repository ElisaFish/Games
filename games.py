import random
import string

class Games:

    money = 100

    def __init__(self):
        pass

    # Checks if the bet is valid
    def check_bet(self, bet):
        if bet < 0:
            print("Please bet a positive amount.")
            return False
        elif bet >= self.money:
            print(f"You can bet up to {self.money}.")
            return False
        else:
            return True

    # Formats the call for spaces, punctuations, and capitalizes
    def format_call(self, call):
        call = call.strip()
        for element in string.punctuation:
            call = call.strip(element)
        call = call.capitalize()
        return call
        
#Write your game of chance functions here
    # Flip a coin!
    def coin_flip(self, bet, call):
        if not self.check_bet(bet):
            return 0
        call = self.format_call(call)

        flip = random.randint(0,1)
        flip_side = ''
        
        if flip == 0:
            flip_side = 'Heads'
        elif flip == 1:
            flip_side = 'Tails'

        win_lose = ''
        amount = 0
        if flip_side == call:
            win_lose = 'win'
            amount = bet
        else:
            win_lose = 'lose'
            amount = -bet
        self.money += bet
        print(f"You flipped a {flip_side}. You called {call}, and {win_lose} ${bet}. You now have ${self.money}.")

        return amount

# Cho-Han allows you to place a bet and call Even or Odd. It rolls two dice, and the
# sum is even or odd.
    def cho_han(self, bet, call):
        if not self.check_bet(bet):
            return 0

        call = self.format_call(call)

        roll = random.randint(0,6) + random.randint(0,6)
        result = ''
        if roll % 2:
            result = 'Odd'
        elif roll % 2 == 0:
            result = 'Even'
        
        win_lose = ''
        amount = 0
        if result == call:
            win_lose = 'win'
            amount = bet
        elif result != call:
            win_lose = 'lose'
            amount = -bet

        self.money += amount
        print(f"You rolled {roll}, which is {result}. You called {call} and {win_lose} ${bet}. You now have ${self.money}.")

        return amount
    
    # Two opponents draw cards from the deck. High card wins
    def high_card(self, bet):
        if not self.check_bet(bet):
            return 0
        suits = ['Spades', 'Hearts', 'Clubs', 'Diamonds']
        card_values = ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King']
        deck = []
        number_value = {'Ace': 1, 'Jack':11, 'Queen': 12, 'King': 13}
        for card in card_values:
            for suit in suits:
                deck.append((card, suit))

        # Draws a card from the deck and removes it from the deck
        def draw_card():
            index = random.randint(0,len(deck)-1)
            card = deck[index]
            deck.pop(index)
            return card

        player_one = draw_card()
        player_two = draw_card()
        player_one_number = number_value.get(player_one[0], player_one[0])
        player_two_number = number_value.get(player_two[0], player_two[0])

        outcome = ''
        amount = 0
        if player_one_number > player_two_number:
            outcome = 'win'
            amount = bet
        elif player_one_number < player_two_number:
            outcome = 'lose'
            amount = -bet
        elif player_one_number == player_two_number:
            outcome = 'tie'
            amount = 0
        
        self.money += amount

        print(f"You drew {player_one[0]} of {player_one[1]}, and your opponent drew {player_two[0]} of {player_two[1]}. You {outcome} ${abs(amount)}. You now have ${self.money}.")

        return amount

# Roulette function rolls a roulette square
# Takes a bet and a call in str format, even if the call is a number, because of 00
    def roulette(self, bet, call):
        if not self.check_bet(bet):
            return 0

        call = self.format_call(call)

        win_lose = ''
        amount = 0
        squares = '0-28-9-26-30-11-7-20-32-17-5-22-34-15-3-24-36-13-1-00-27-10-25-29-12-8-19-31-18-6-21-33-16-4-23-35-14-2'
        pockets = squares.split('-')
        
        call_includes = {
            'Odd': [n for n in range(1, 36, 2)],
            'Even': [n for n in range(2, 37, 2)],
            'Red': [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36],
            'Black': [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35],
            '1 to 18': [n for n in range(1, 19)],
            '19 to 36': [n for n in range(19, 37)]
            }

        win = pockets[random.randint(0, len(pockets)-1)]
        try:
            if type(int(call)) == int:
                odds = bet * 35
                if call == win:
                    win_lose = 'win'
                    amount = odds
                else:
                    win_lose = 'lose'
                    amount = -bet
        except Exception:
            if type(call) == str:
                odds = bet
                if int(win) in call_includes[call]:
                    win_lose = 'win'
                    amount = odds
                else:
                    win_lose = 'lose'
                    amount = -bet

        self.money += amount
        print(f"The ball landed on {win}. You called {call} and {win_lose} ${abs(amount)}. You now have ${self.money}.")

        return amount

        



#Call your game of chance functions here
game = Games()
game.coin_flip(208, 'Heads!')
game.coin_flip(5, 'Heads!')
game.cho_han(10, 'Even')
game.high_card(5)
game.roulette(20, 'Even')