#!/usr/bin/python3

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-l", "--log", help="logging level; one of DEBUG, INFO, WARNING", type=str)
args = parser.parse_args()

import logging
if args.log:
    loglevel = getattr(logging, args.log.upper())
else:
    loglevel = logging.WARN
logging.basicConfig(level=loglevel)
        
import time
tStart = time.time()

def parse_hands(line):
    tokens = line.split(sep=' ')
    return tokens[:5], tokens[5:]

def max_diff(l):
    return max(l) - min(l)

class Card:
    def __init__(self, strin):
        try:
            self.val = int(strin[0])
        except ValueError:
            if strin[0] == 'A':
                self.val = 14
            elif strin[0] == 'K':
                self.val = 13
            elif strin[0] == 'Q':
                self.val = 12
            elif strin[0] == 'J':
                self.val = 11
            elif strin[0] == 'T':
                self.val = 10
        self.suit = strin[1]

class Hand:
    def __init__(self, str_list):
        self.cards = set((
            Card(str_list[0]),
            Card(str_list[1]),
            Card(str_list[2]),
            Card(str_list[3]),
            Card(str_list[4])
            ))

    def value(self):
        """Return int, kickers list"""
        
        d_by_val = {}
        d_by_suit = {}
        for card in self.cards:
            if card.val not in d_by_val:
                d_by_val[card.val] = []
            d_by_val[card.val].append(card.suit)
            if card.suit not in d_by_suit:
                d_by_suit[card.suit] = []
            d_by_suit[card.suit].append(card.val)
        
        d_by_val_keys = list(d_by_val.keys())
        d_by_val_keys_sorted = sorted(d_by_val_keys, key=lambda x : (len(d_by_val[x]), x), reverse=True)
        d_by_val_values_sorted = []
        for key in d_by_val_keys_sorted:
            d_by_val_values_sorted.append(d_by_val[key])

        d_by_suit_keys = list(d_by_suit.keys())
        d_by_suit_values = list(d_by_suit.values())

        ret_val = 0
        ret_kickers = []
        
        # straight flush
        if len(d_by_suit_keys) == 1 and max_diff(d_by_suit_values[0]) == 4:
            return 9, sorted(d_by_suit_values[0], reverse=True)

        # 4oak
        elif len(d_by_val_values_sorted[0]) == 4:
            return 8, d_by_val_keys_sorted

        # full house
        elif len(d_by_val_keys) == 2 and (len(d_by_val_values_sorted[0]) == 3) and (len(d_by_val_values_sorted[1]) == 2):
            return 7, d_by_val_keys_sorted
        
        # flush
        elif len(d_by_suit_keys) == 1:
            return 6, sorted(d_by_suit_values[0], reverse=True)

        # straight
        elif len(d_by_val_keys) == 5 and max_diff(d_by_val_keys) == 4:
            return 5, sorted(d_by_val_keys, reverse=True)

        # 3oak
        elif len(d_by_val_keys) == 3 and (len(d_by_val_values_sorted[0]) == 3):
            return 4, d_by_val_keys_sorted

        # 2 pair
        elif len(d_by_val_keys) == 3 and (len(d_by_val_values_sorted[0]) == 2) and (len(d_by_val_values_sorted[1]) == 2):
            return 3, d_by_val_keys_sorted
        
        # 1 pair
        elif len(d_by_val_keys) == 4 and (len(d_by_val_values_sorted[0]) == 2):
            return 2, d_by_val_keys_sorted

        else:
            return 1, d_by_val_keys_sorted


    def __lt__(self, other):
        self_val, self_kickers = self.value()
        other_val, other_kickers = other.value()
        if self_val < other_val:
            return True
        elif self_val > other_val:
            return False
        else:
            for pair in zip(self_kickers, other_kickers):
                if pair[0] < pair[1]:
                    return True
                elif pair[0] > pair[1]:
                    return False

p1_win_count = 0
for line in open('./p054_poker.txt', 'r').readlines():
    list1, list2 = parse_hands(line.strip())
    hand1 = Hand(list1)
    hand2 = Hand(list2)
    if hand2 < hand1:
        p1_win_count += 1

print("{}: answer: {!s}".format(__file__, p1_win_count))
print("Run time: " + '{:.20f}'.format(time.time() - tStart) + " sec")
