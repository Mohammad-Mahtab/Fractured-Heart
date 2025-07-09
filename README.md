#  Fractured‑Heart

*A 2D Zelda‑Inspired Adventure Game*
**Date**: February 2025

---

## Table of Contents

- [Introduction](#1-introduction)
- [Hardware/Software Requirements](#2-hardwaresoftware-requirements)
- [Design Strategies](#3-design-strategies)
- [AI and Dialogue System](#4-ai-and-dialogue-system)
- [Project Architecture](#5-project-architecture)
- [Screenshots](#8-screenshots)

---

## 1.  Introduction

**Fractured‑Heart** is a 2D action-adventure game inspired by classic *Zelda* titles. Players explore detailed maps, battle enemies, and engage in narrative-driven interactions with dynamic, branching dialogues.

###  Project Objectives

- **Engaging Gameplay**: Craft a rewarding, exploration-based experience.
- **Performance**: Optimize for smooth play on large maps using chunk loading and view culling.
- **AI Integration**: Implement intelligent enemy/NPC behavior and dialogue trees.
- **Team Collaboration**: Use GitHub tools for agile, modular development.

---

## 2.  Hardware/Software Requirements

###  Hardware

- **CPU**: Intel Core i3 or equivalent  
- **RAM**: 4 GB minimum (8 GB recommended)  
- **GPU**: Integrated or dedicated  
- **Storage**: 500 MB+  
- **Display**: 1280×720 resolution or higher

###  Software

- **OS**: Windows, macOS, or Linux
- **Python**: v3.7+
- **Pygame**: v2.0+
- **Libraries**: `os`, `sys`, `random`, `threading`  
- **IDE**: PyCharm, VSCode, or any Python IDE

---

## 3.  Design Strategies

###  Performance Optimizations

- **Chunk Loading & View Culling**: Render only visible map sections.
- **Enemy Respawn & Object Pooling**: Efficiently manage enemies off-screen.

---

## 4.  AI and Dialogue System

###  Enemy Behavior

- State-based AI (idle, move, attack)
- Distance checks and cooldown timers
- Reactive behavior based on player proximity

###  NPC Dialogue System

- Branching conversations
- Decision trees loaded from external files
- Player choices affect dialogue flow and outcomes

---

## 5.  Project Architecture

Module Structure
The project is organized into several key directories and modules:

assets/
Contains all images, sounds, and other media files.

code/
Houses the main game logic:

main.py: Entry point of the game.
level.py / level_story.py: Manage map creation, sprite grouping, chunk loading, and enemy respawning.
player.py & enemy.py: Define entity behavior (movement, combat, animation).
particles_story.py: Handles particle effects (magic spells, enemy death animations).
enemy_spawner.py: Implements the enemy respawn system.
start_screen.py: Provides the main menu interface.
npc.py: Manages NPC behaviors and dialogues.
docs/
Contains documentation files.

tests/
Houses unit tests and integration tests.

Key Components and Their Roles
Main Game Loop (main.py):
Initializes Pygame, loads assets, displays loading and transition screens, and launches the main menu. It then conditionally starts the regular game or story mode based on user input.

Level Management (level.py / level_story.py):
Constructs the game map from CSV files, assigns sprites to chunks, and manages enemy spawn points.

Entity Classes (player.py & enemy.py):
Define the behaviors, collision logic, and animations for the player and enemy characters.

Optimization Techniques (ChunkedCameraGroup):
Implements chunk loading and view culling to ensure that only visible sprites are rendered.

AI Integration (enemy_ai, Dialogue System in npc.py):
Enemies and NPCs use AI logic to interact with the player. Dialogue systems provide branching conversations that influence gameplay.
---

## 6. Screenshots 

![Main Menu](assets/screenshots/menu.png)

