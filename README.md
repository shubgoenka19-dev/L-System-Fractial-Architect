L-System Fractal Architect
 Project Overview

The L-System Fractal Architect is a Python-based graphical application that visualizes Lindenmayer Systems (L-systems) using turtle graphics embedded inside a Tkinter GUI.

L-systems are a type of formal grammar and parallel rewriting system, originally introduced by Aristid Lindenmayer (1968) to model plant growth and natural fractal structures such as trees, snowflakes, and ferns.

This project allows users to define:

An axiom (initial string)

Production rules

Turning angle

Number of iterations

The system expands the L-system string iteratively and interprets it as drawing commands using turtle graphics.
 Features

Hybrid Tkinter + Turtle GUI

Parallel L-system string expansion

Support for standard L-system commands:

F → Move forward and draw

+ → Turn right

- → Turn left

[ → Save turtle state (push)

] → Restore turtle state (pop)

Stack-based branching for tree-like structures

Color gradient for visual depth

Optimized rendering using tracer(0, 0) to avoid lag

🛠️ Technologies Used

Python 3

tkinter

turtle
