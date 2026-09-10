# Dice_Game

A small text-based RPG project inspired by dungeon-crawling games (D&D, Slay the Spire and Final Fantasy), turn-based combat.

Still a work in progress, main idea: player wakes up in a mysterious dungeon, chooses a class, explores the area, finds artifacts, fights enemies, and tries to survive long enough to escape.

## Project Overview
Player starts in a dungeon with the goal of surviving 20 explorations.

At the moment, the project is focused on building the core systems for:
- player creation and character stats
- combat and dice-based mechanics
- enemy definitions
- artifacts and item effects
- exploration flow and game progression

## Current File Structure
- `main.py` — the game loop and overall flow
- `character_classes.py` — `Character`, `Warrior`, and `Sage` classes
- `dice.py` — dice rolling (D4, D6 ... to D20)
- `enemies.py` — enemy data and descriptions
- `artifacts.py` — artifact definitions and effects
- `welcome_msg.py` — intro scene
- `create_player` — placeholder/unfinished player creation logic

## Character Classes
The project currently includes a base `Character` class with shared stats and behavior, plus:
- `Warrior` — stronger physical stats and a special attack
- `Sage` — stronger magical stats and a different special attack

Each class uses a shared stat system based on strength, intelligence, endurance, and health.

## Dice and Combat Mechanics
Dice rolling is handled through `roll_dice()`, which supports various dice types for future combat and ability effects.

The combat system is still being developed, but main points:
- stat-based attacks (INT vs STR)
- damage driven from dice rolls
- class abilities with cooldowns
- buffs/ progression after battles

## Artifacts
list includes:
- common artifacts
- rare artifacts
- mythic artifacts

They will have different probabilities of showing up.

## Enemies
Enemies are currently stored in `enemies.py`
- standard enemies
- sage-themed enemies
- warrior-themed enemies

## Notes
This is a personal project with a very loose structure at the moment, so some files are still placeholders and some mechanics are unfinished.
