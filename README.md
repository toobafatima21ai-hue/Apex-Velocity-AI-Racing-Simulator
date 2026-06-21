
# 🏁  Apex-Velocity-AI-Racing-Simulator
### 🎮 AI-Powered F1 Broadcast Racing Simulator (Streamlit + Multi-Agent AI + Physics Engine)
---

## 🚀 Overview

Apex Protocol: Neon Overdrive is a real-time AI-driven F1-style racing simulator built using Streamlit, multi-agent AI drivers, and a custom physics engine.

It simulates:
- Real-time racing physics
- AI opponents with different driving personalities
- Player-controlled racing actions
- Live leaderboard + track visualization
- Broadcast-style commentary system

This project is designed as a **portfolio-grade AI simulation game** showcasing:
- Game loop architecture
- Multi-agent systems
- Real-time Streamlit UI
- Physics-based simulation

---

## 🎮 Features

### 🏎 Racing System
- Real-time car movement simulation
- Speed, tire degradation, and position tracking
- Dynamic race progression system

### 🤖 AI Drivers
- VOLT → Aggressive AI driver
- NEON → Balanced strategist
- SHADOW → Defensive racer
- CYBER → Risk-based AI driver

Each AI reacts to race conditions dynamically.

---

### 🎮 Player Controls
- ⚡ Accelerate
- 🚀 Nitro Boost
- 🛡 Defensive mode
- ⛽ Pit Stop strategy
- 🔄 Reset race

---

### 🎥 Broadcast UI System
- Live leaderboard
- Track minimap visualization
- Camera modes:
  - BROADCAST
  - LEADER
  - PLAYER VIEW

---

### 📡 Commentary System
- Real-time race commentary generation
- Event-based reactions
- Broadcast-style narration

---

## 🧠 AI Architecture

This project uses:

### 🔹 Multi-Agent Simulation
Each driver is an independent agent:
- Evaluates race state
- Chooses actions (attack / defend / boost)
- Updates performance dynamically

### 🔹 Physics Engine
- Tire degradation model
- Speed influence system
- Position-based progression

---

## 🤖 Ollama Integration (Optional Upgrade)

This project supports integration with **Ollama local LLMs** for:

- Dynamic race commentary
- AI driver personality reasoning
- Strategic decision explanations

Example:
```python
from ollama import chat

response = chat(
  model="llama3",
  messages=[{"role": "user", "content": "Generate F1 race commentary"}]
)
```

## 🎮 How It Works

### 1. Initialization
Cars are created with:
- Position
- Speed
- Tire health

---

### 2. Game Loop
Every frame:
- Cars move based on speed
- Tire degradation reduces performance
- AI agents make decisions
- Player actions affect player car

---

### 3. Player Interaction
Player can:
- Boost speed
- Defend position
- Use pit stop
- Reset race

---

### 4. AI Behavior
AI drivers:
- Analyze race conditions
- Compete for position
- Adapt strategy dynamically

---

### 5. Visualization Layer
Streamlit renders:
- Live leaderboard
- Track minimap
- Camera feed
- Commentary feed

---

## 🎥 UI Components

| Component | Purpose |
|----------|--------|
| 🏁 Leaderboard | Race ranking |
| 🗺 Minimap | Track visualization |
| 🎥 Camera Mode | Race perspective |
| 📡 Commentary | Live narration |
| 🎮 Controls | Player input |

---

 

## 👨‍💻 Author

 TOOBA FATIMA
## 🏁 Final Result

A fully interactive F1-style AI racing simulator featuring:
- Real-time racing engine
- AI drivers
- Player control system
- Broadcast UI
- Commentary system

---
 
---

🔥 “Neon speed meets artificial intelligence on the digital track.”
