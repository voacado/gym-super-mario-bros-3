# Variable Breakdown

- `clock_hundreds` (1-bit, unsigned)
    - first value in game clock (if 297, then 2)
- `clock_tenths` (1-bit, unsigned)
    - second value in game clock (if 297, then 9)
- `clock_ones` (1-bit, unsigned)
    - third value in game clock (if 297, then 7)

- `coins` (1-bit, unsigned)
    - character money
    - 0 to 99 (at 100, resets to 0 and gives a life)

- `cur_world` (1-bit, unsigned)
    - index of current overworld map world 
    - zero-indexed, world 1 == `0`

- `fanfare_music` (1-bit, unsigned)
    - music played upon player "completion" (exiting a level)
    - useful values:
        - `1` = death
        - `4` = fortress boss defeated
        - `32` = normal tile level completed
    - NOTE: Unfortunately, for levels like 8-Airship1, where the level ends with an item acquired, this sound effect is the same as getting a power-up out of a block (value `02` at `$4F2`). For scenarios like this, it's best to rely on the `level_zone` variable.

- `level_zone` (4-bit, unsigned)
    - indicates what "zone" in a stage a player is in
    - `1` == overworld
    - usually in increments of 2 (first part of level == 2, enter pipe == 4, etc)

- `lives` (1-bit, signed)
    - indicates the amount of lives Mario has
    - game over == `-1`

- `map_tile_idx` (1-bit, unsigned)
    - index (for graphic) of tile Mario is standing on in Overworld Map
    - useful values:
        - for level tiles, `idx = level_idx - 2` (for example, level 4 = idx val of 2)
        - fortress = 133, 201
        - airship = 175
        - pipe = 188
        - mushroom = 80 (orange), 224 (red)
        - spade = 232
        - World 2 Exclusives:
            - angry sun = 104
            - pyramid = 105
        - World 5 Exclusives:
            - spiral tower = 95
        - World 8 Exclusives:
            - hand = 230

- `mario_form` (1-bit, unsigned)
    - indicates Mario's current power-up form
        - `00` - Small
        - `01` - Super
        - `02` - Fire
        - `03` - Raccoon
        - `04` - Frog
        - `05` - Tanooki
        - `06` - Hammer
    - NOTE: this value is not updated until in a stage
    - use `0x578` (1-bit, unsigned) to modify value

- `player_hurt` (1-bit, unsigned)
    - flag to indicate whether Mario has taken damage
    - by default, the value is `0`
    - upon taking a hit, the value increases to `~100` and decreases
    - this value represents Mario's I-Frames as well as how long he flickers for

- `player_is_dying` (1-bit, unsigned)
    - flag that determines if Mario is dead
    - 0 = Not dying, 1 = Dying, 2 = Dropped off screen, 3 = Death due to TIME UP

- `score` (3-bit, unsigned)
    - numeric representation of player score divided by (dec)10
    - last value of score on GUI is always 0 (`score` * 10)

- `screen_current` (1-bit, unsigned)
    - current index of the screen Mario is on
    - each stage is divided into screens, advancing in the level increases `screen_current` (TODO: untested)

- `screen_max_in_level` (1-bit, unsigned)
    - indicates the max number of screens in the current level
    - this value is `0` on the Map Screen (overworld)
    - this value is updated immediately upon entering a level

- `x_pos_1st_byte` (1-bit, unsigned)
    - Mario's current position horizontally
    - the left-most part of a level is usually `16`
    - ranges from `0` to `255`
        - after `255`, wraps to `0`

- `x_pos_2nd_byte` (1-bit, unsigned)
    - Mario's current position horizontally
        - going left decreases, whereas going right increases
    - this value defaults to `0`
    - whenever `x_pos_1st_byte` overflows (Mario moves right), increment this value by 1

- `y_pos_1st_byte` (1-bit, unsigned)
    - Mario's current position vertically
        - going up decreases, whereas going down increases
    - ranges from `0` to `255` (wraps around)

- `y_pos_2nd_byte` (1-bit, unsigned)
    - Mario's current position vertically
    - this value is usually `1` to start
    - whenever `y_pos_1st_byte` underflows (Mario moves up), decrease this value by 1

#### Variable References and Documentation

- Position memory addresses:
    - https://tasvideos.org/GameResources/NES/SuperMarioBros3#ImportantRamAddresses
    - https://tasvideos.org/UserFiles/Info/637936906462581196

- SMB3 RAM/ROM Mapping
    - https://smb3p.kafuka.org/thread.php?id=17
    - https://datacrystal.romhacking.net/wiki/Super_Mario_Bros._3:RAM_map
    - https://www.smwcentral.net/?p=memorymap&game=smas&u=0&address=&sizeOperation=%3D&sizeValue=&region%5B%5D=ram&type=*&context=Super+Mario+Bros.+3/Global&description=
        - Contains through descriptions and byte sizes

- Gym Retro Integration Tutorial
    - https://stable-retro.farama.org/integration/
        - Information on types

#### Game Genie Cheat Codes
Reference: https://themushroomkingdom.net/smb3_ggcodes.shtml

| **Description** | **Game Genie Cheat Code** |
|:---:|:---:|
| Start on World 2 | PEUZUGAA |
| Start on World 3 | ZEUZUGAA |
| Start on World 4 | LEUZUGAA |
| Start on World 5 | GEUZUGAA |
| Start on World 6 | IEUZUGAA |
| Start on World 7 | TEUZUGAA |
| Start on World 8 | YEUZUGAA |
| Debug Mode | KKKZSPIU |
| Remove status bar at bottom | GSZUIZ |
| Change background to black | EINEUYEY |
| Enter levels faster | ASXEEAAL |
| Move on any map tile | OXKIPZOS |
| Invicible (cannot interact with pipes) | VXKXGLIE |

##### More info on Debug Mode
https://themushroomkingdom.net/smb3_lost.shtml#debug

```
Start at any level - Press Up and Down to select from Worlds 1 through 8, then press Start and you're there! Or, on controller 2, press B + A + Down to rescue Princess Toadstool or B + A + Right to go straight to the credits.

Start with 99 lives - Each time you press A before starting the game, five lives are added to Mario's extra-lives total. The maximum is 99 lives.

Start with every item - On the map screen, your inventory has one of each item, with P-Wings filling in the final two boards.

Anytime-power-ups - In a level, pressing Select upgrades Mario's power. (When Mario has the Hammer Brother Suit, pressing Select takes him back down to "small" Mario.) The best part: Hold A or B and press Select to enable/disable Kuribo's Shoe! The shoe might look a bit weird in levels it was never supposed to appear in, however (as seen in the third screen shot below).

Unlimited time - Nothing happens when the timer runs out, and Mario can continue on.
```

# Level Progression

#### World 1
1 -> 2 -> 3 -> 4 -> Fortress -> 5 -> 6 -> Airship

#### World 2
1 -> 2 -> Fortress -> 3 -> Angry Sun -> 4 -> 5 -> Pyramid -> Airship

#### World 3
1 -> 2 -> 3 -> Fortress1 -> 4 -> 5 -> 6 -> 7 -> Fortress2 -> 8 -> 9 -> Airship

#### World 4
1 -> 2 -> 3 -> Fortress1 -> 4 -> 5 -> 6 -> Fortress2 -> Airship

#### World 5
1 -> 2 -> 3 -> Fortress1 -> Spiral Tower -> 4 -> 5 -> 6 -> 7 -> Fortress2 -> 8 -> 9 -> Airship

#### World 6
1 -> 2 -> 3 -> Fortress1 -> 4 ->5 -> 6 -> 7 -> Fortress2 -> 8 -> 9 -> 10 -> Fortress3 -> Airship

#### World 7
1 -> 2 -> 3 -> 4 -> 5 -> Fortress1 -> 6 -> 7 -> 8 -> 9 -> Fortress2 -> Airship

#### World 8
Tank1 -> Airship1 -> Hand1 -> Hand2 -> Hand3 -> Airship2 -> 1 -> 2 -> Fortress -> Tank2 -> Castle