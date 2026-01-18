# L-System Fractal Architect 

## Overview
The **L-System Fractal Architect** is a Python-based graphical application that visualizes  
**Lindenmayer Systems (L-systems)** using **Turtle Graphics embedded inside a Tkinter GUI**.

L-systems are formal grammars and parallel rewriting systems originally introduced by  
**Aristid Lindenmayer (1968)** to model natural growth patterns such as trees, plants, and fractals.

This application allows users to define their own L-system rules and generate complex fractal
structures interactively.

---

## Features
- Hybrid **Tkinter + Turtle** GUI
- Parallel L-system string expansion
- Supports standard L-system commands:
  - `F` → Move forward and draw
  - `+` → Turn right
  - `-` → Turn left
  - `[` → Save turtle state (push)
  - `]` → Restore turtle state (pop)
- Stack-based branching for tree-like structures
- Color gradient for visual depth
- Optimized rendering using `tracer(0, 0)` to prevent lag
## 🛠️ Technologies Used
- **Python 3**
- `tkinter`
- `turtle`
