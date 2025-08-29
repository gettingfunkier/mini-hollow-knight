# Mini Hollow Knight!
> A terminal-based, **Hollow Knight inspired** boss rush minigame!
> Written in Python as a practice/passion project


## Inspiration

This project takes inspiration from the world of **Hollow Knight** by *Team Cherry*.  
It’s a **text-based combat game** where you, the Vessel, fight a series of bosses in succession.  
It mixes:
- OOP design (player + enemy classes)  
- Turn-based combat flow  
- Console UI with ASCII health/soul bars  


## Setup

1. Clone this repo: *(Or just copy the game.py code into any editor)*
   ```bash
   git clone https://github.com/gettingfunkier/mini-hollow-knight.git
   cd mini-hollow-knight
2. Run with Python:
    ```bash
    python mini_hollow_knight.py
    ```

## How to play

#### Objective
- Defeat three bosses in succession.
- Survive by balancing attacks, spells, and healing.
- Victory comes when all enemies are slain.

#### Actions
- Attack: Deal base damage with your Nail.
    - Every third attack in a row becomes a Critical Hit.
- Heal (Soul Focus): Costs 1 Soul, restores health.
- Cast Spells:
    - Vengeful Spirit → 2 Soul, 15 dmg
    - Howling Wraiths → 3 Soul, 25 dmg

#### Soul System
- Gain 1 Soul with each attack.
- Soul is spent on spells or healing.

## Settings

#### Difficulty
- [ϟ] ▰▱▱ Normal
    - Vengefly King, Mantis Lords, Hornet Sentinel
- [ϟ] ▰▰▰ Hard
    - Lost Kin, Soul Tyrant, Nightmare King Grimm

#### Charms
- **Unbreakable Strength -** *Increases attack power*
- **Shaman Stone -** *Increases spell damage*
- **Lifeblood Heart -** *Boosts maximum health*

## Enemies
Each enemy has:
- Signature moto
- Health & Attack stats
- Chance to dodge attacks
- Unique stagger stage where they get stronger mid-fight
- Death descriptions

#### introduction
```bash
≽ A NEW CHALLENGER HAS APPEARED: Soul Tyrant!! ≼

"The King falls, but I live forever!"
```

#### death
```bash
───[ ACTION ]─────────────────────────────────────┐

ϟ Vessel casts Vengeful Spirit, dealing 15 damage! ϟ

He explodes into fireworks of soul and thunder.

──────────────────────────────────────────────────┘

☓ You killed Soul Tyrant!
```

## UI & Stats
The game uses simple console bars to track progress:

#### Action LOG
```bash
───[ ACTION ]─────────────────────────────────────┐

// Vessel swings its nail, dealing 6 damage!
○ Gained 1 Soul

// Nightmare King Grimm summons his dragons!
(Vessel dodged the attack!)
❤ You avoided damage!

[!] Nightmare King Grimm staggers! 
› He turns into a swarm of dragons, returning more fiery

──────────────────────────────────────────────────┘
```
#### Turn INFO
```bash
 ▰ ▰ ▰ [ NEW TURN ] ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰

HEALTH ╏ |███████████░░░░░░░░░|  29/50 ❤
SOUL   ╏  ⦿ ◌ ◌  1/3

C͟h͟o͟o͟s͟e͟ ͟y͟o͟u͟r͟ ͟a͟c͟t͟i͟o͟n͟:

   [1] Attack Nightmare King Grimm
   [2] Heal yourself
   [3] Cast a spell

▷ 
```

## Credits
- Game concept & assets: [**Hollow Knight, Team Cherry** ↗](https://www.teamcherry.com.au)
- Code: [**gettingfunkier** ↗](https://github.com/gettingfunkier)
- Made with ❤ in Python, during Y1 of Software Egineering, 2025