#!/usr/bin/env python3

from brain_games.engine import game_core
from brain_games.games import gcd


def main():
    game_core(gcd)

if __name__ == '__main__':
    main()
