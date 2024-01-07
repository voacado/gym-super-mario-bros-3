"""
Super Mario Bros. 3 for Gymnasium Gym
"""

# General Imports
import argparse
import sys

# Emulator Imports
import gymnasium as gym
from nes_py.wrappers import JoypadSpace
from nes_py.app.play_human import play_human
from nes_py.app.play_random import play_random

# Game Actions Imports
from ..game_actions import RIGHT_MOVEMENT, BASIC_MOVEMENT, ADVANCED_MOVEMENT, FULL_MOVEMENT

# Map defined action spaces to shorter reference variables
ACTION_SPACES = {
    'right': RIGHT_MOVEMENT,
    'basic': BASIC_MOVEMENT,
    'advanced': ADVANCED_MOVEMENT,
    'full': FULL_MOVEMENT
}


def get_cli_arguments() -> argparse.Namespace:
    """
    Parse command line arguments from the user.
    """
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--path', '-p',
                        type=str,
                        default='',
                        help='The path to Super Mario Bros. 3 ROM'
                        )
    parser.add_argument('--mode', '-m',
                        type=str,
                        default='human',
                        choices=['human', 'random'],
                        help='Control how the game is played (user or random)'
                        )
    parser.add_argument('--actionspace', '-a',
                        type=str,
                        default='nes',
                        choices=['nes', 'right', 'basic', 'advanced', 'full'],
                        help='The available action space for agent'
                        )
    parser.add_argument('--steps', '-s',
                        type=int,
                        default=1000,
                        help='The number of random steps to take.',
                        )
    # parser.add_argument('--level', '-l',
    #                     type=str,
    #                     default='1-1',
    #                     help='The level to begin starting on. Format: {world}-{level}, like 2-4',
    #                     )

    return parser.parse_args()


def main() -> None:
    args = get_cli_arguments()

    # TODO: convert ROM path here to something gymnasium supports
    # TODO: This will not work right now!
    # TODO: if path not valid, should run `sys.exit(1)`, check SHA

    env = gym.make('super_mario_bros_3')

    # If action space is not 'nes', we unwrap keys available and create a JoypadSpace with it
    if args.actionspace != 'nes':
        print(args.actionspace)
        # Unwrap actions list by key
        actions = ACTION_SPACES[args.actionspace]
        # Wrap env with new action space
        env = JoypadSpace(env, actions)

    # Play env with given mode
    if args.mode == 'human':
        play_human(env)
    else:
        play_random(env, args.steps)

    # Allow any import of this package to have global scope over it (for import *).
    __all__ = [main.__name__]
