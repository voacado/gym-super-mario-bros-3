<p>
  <a href="https://en.wikipedia.org/wiki/Super_Mario_Bros._3">
    <img src="https://upload.wikimedia.org/wikipedia/en/a/a5/Super_Mario_Bros._3_coverart.png" alt="Mario is seen flying using the &quot;Raccoon Mario&quot; power-up over a yellow/gold background. The Game's logo appears on the top and the game's tagline appears on the bottom." height="377" width="264" align="right">
  </a>
</p>

# Gym Environment for Super Mario Bros. 3 (NES) 🎮
> A reinforcement learning environment for the Nintendo video game Super Mario Bros. 3 on the Nintendo Entertainment System

### What is Super Mario Bros. 3 (NES)?
Super Mario Bros. 3 is a platform game developed and published by Nintendo for the Nintendo Entertainment System in 1988. In this video game, players control Mario or Luigi and save Princess Toadstool from Bowser. Players have the ability to move left and right, walk, run, use their power-up ability, and jump to traverse 90 levels across 8 worlds.

### What is a Gym Environment?
In 2016, OpenAI announced Gym, an open-source Python library for developing reinforcement learning algorithms by providing a standard API to communicate between these learning algorithms and their environments. 

In a way, you can imagine a Gym Environment as a way for a program to get information about the state of an environment as well as interact with it. Usually, metrics like a game's score or life points can be extracted, and using reinforcement learning, policies can be developed to algorithmically play through an environment. For a game like Super Mario Bros. 3, we can imagine the distance from the end of a map to be an example of a feature we could use.

## Features and Heuristics to Evalulate Game State

| Feature | Description |
| ------- | ----------- |

TODO: WIP

## Roadmap

This project will use the [Gymnasium](https://github.com/Farama-Foundation/Gymnasium) and [stable-retro](https://github.com/Farama-Foundation/stable-retro) packages from [Farama-Foundation](https://github.com/Farama-Foundation) to create an environment for Super Mario Bros 3.

#### Status

This project has just begun. First, I will look into the following resources to try to create a rough draft of something:
- [YouTube Playlist - OpenAI retro game integration tool tutorial](https://www.youtube.com/playlist?list=PLmwlWbdWpZVvWqzOxu0jVBy-CaRpYha0t)
