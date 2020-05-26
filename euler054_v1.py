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
        # hc = 1
        # pair = 2
        # 2 pair = 3
        # 3oak = 4
        # straight = 5
        # flush = 6
        # full house = 7
        # 4oak = 8
        # straight flush = 9
        
        d_by_val = {}
        d_by_suit = {}
        for card in self.cards:
            if card.val not in d_by_val:
                d_by_val[card.val] = []
            d_by_val[card.val].append(card.suit)
            if vard.suit not in d_by_suit:
                d_by_suit[card.suit] = []
            d_by_suit[card.suit].append(card.val)
        
        ret_val = 0
        ret_kickers = []

        # flushes (straight and not)
        if len(d_by_suit.keys()) == 1:
            ret_val = 6
            l = list(d_by_suit.values())[0]
            if max(l) - min(l) == 4:
                ret_val = 9
            return ret_val, [max(l)]

        # 4oak and full house
        if len(d_by_val.keys()) == 2:
            longest_len = 0
            longest_len_kicker = 0
            for i in range(2):
                longest_len = d_
            




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
