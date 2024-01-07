"""
Registration of Gymnasium environment(s).
"""

import gymnasium as gym


def register_gym_env(id: str, is_random: bool = False, include_seven: bool = True, **kwargs) -> None:
    """
    Register a Super Mario Bros. 3 environment with Farama Foundation's Gymnasium package.

    Args:
        :param id: id to register environment under
        :param is_random: randomize level order
        :param include_seven: include World 7 (vertical levels)
        :param kwargs: keyword arguments for init
    """

    # Set entry_point ID based on params
    if is_random:
        if include_seven:
            # Code for is_random and include_seven
            entry_point = 'gym_super_mario_bros_3:SuperMarioBros3RandomStagesEnv'
        else:
            # Code for is_random and not include_seven
            entry_point = 'gym_super_mario_bros_3:SuperMarioBros3RandomStagesNoWorld7Env'
    else:
        if include_seven:
            # Code for not is_random and include_seven
            entry_point = 'gym_super_mario_bros_3:SuperMarioBros3Env'
        else:
            # Code for not is_random and not include_seven
            entry_point = 'gym_super_mario_bros_3:SuperMarioBros3NoWorld7Env'

    # Register environment
    gym.envs.registration.register(
        id=id,
        entry_point=entry_point,
        max_episode_steps=9999999,
        reward_threshold=9999999,
        kwargs=kwargs,
        nondeterministic=True,
    )


def register_gym_stage_env(id: str, **kwargs) -> None:
    """
    Register Super Mario Bros. 3 environments using Gymnasium that begin at specific levels.

    Args:
        :param id: id to register environment under
        :param kwargs: keyword arguments for init
    """

    # Register environment
    gym.envs.registration.register(
        id=id,
        entry_point='gym_super_mario_bros:SuperMarioBrosEnv',
        max_episode_steps=9999999,
        reward_threshold=9999999,
        kwargs=kwargs,
        nondeterministic=True,
    )


# Register environments for Super Mario Bros. 3 (begins at 1-1)
register_gym_env('SuperMarioBros3', is_random=False, include_seven=True)
register_gym_env('SuperMarioBros3-NoWorld7', is_random=False, include_seven=False)
register_gym_env('SuperMarioBros3-RandomStages', is_random=True, include_seven=True)
register_gym_env('SuperMarioBros3-RandomStages-NoWorld7', is_random=True, include_seven=False)


# Register level environments for Super Mario Bros.3 (user chooses level)
# Naming convention for levels
ID_TEMPLATE: str = 'SuperMarioBros3{}-{}-{}-v{}'

# Level order in Super Mario Bros. 3
smb3_level_order = {
    1: ['1', '2', '3', '4', 'Fortress', '5', '6', 'Airship'],  # World 1
    2: ['1', '2', 'Fortress', '3', 'AngrySun', '4', '5', 'Pyramid', 'Airship'],  # World 2
    3: ['1', '2', '3', 'Fortress1', '4', '5', '6', '7', 'Fortress2', '8', '9', 'Airship'],  # World 3
    4: ['1', '2', '3', 'Fortress1', '4', '5', '6', 'Fortress2', 'Airship'],  # World 4
    5: ['1', '2', '3', 'Fortress1', 'SpiralTower', '4', '5', '6', '7', 'Fortress2', '8', '9', 'Airship'],  # World 5
    6: ['1', '2', '3', 'Fortress1', '4', '5', '6', '7', 'Fortress2', '8', '9', '10', 'Fortress3', 'Airship'],  # World 6
    7: ['1', '2', '3', '4', '5', 'Fortress1', '6', '7', '8', '9', 'Fortress2', 'Airship'],  # World 7
    8: ['Tank1', 'Airship1', 'Hand1', 'Hand2', 'Hand3', 'Airship2', '1', '2', 'Fortress', 'Tank2', 'Castle']  # World 8
}

# iterate over all worlds (1-8), and stages
for world in smb3_level_order:
    for level in smb3_level_order[world]:
        target = (world, level)
        env_id = ID_TEMPLATE.format('', world, level)
        register_gym_stage_env(env_id, target=target)


# create an alias to gym.make for ease of access
make = gym.make

# define the outward facing API of this module (none, gym provides the API)
__all__ = [make.__name__]
