import tkinter as tk
import turtle

# L-System Expansion (Parallel)

def expand_lsystem(axiom, rules, iterations):
    """
    Expands the L-system string using parallel rewriting.
    """
    current = axiom
    for _ in range(iterations):
        next_string = ""
        for char in current:
            next_string += rules.get(char, char)
        current = next_string
    return current

# Draw the L-System using Turtle

def draw_lsystem(t, instructions, angle):
    """
    Interprets the expanded L-system string and draws it.
    """
    stack = []
    step_length = 5
    total_steps = len(instructions)

    turtle.tracer(0, 0)  # Disable animation for performance

    for i, cmd in enumerate(instructions):
        # Gradient color effect
        t.pencolor(0, i / total_steps, 0)

        if cmd == "F":
            t.forward(step_length)
        elif cmd == "+":
            t.right(angle)
        elif cmd == "-":
            t.left(angle)
        elif cmd == "[":
            stack.append((t.position(), t.heading()))
        elif cmd == "]":
            pos, heading = stack.pop()
            t.penup()
            t.setposition(pos)
            t.setheading(heading)
            t.pendown()

    turtle.update()  # Refresh screen once


# ---------------------------------
# Generate Button Callback
# ---------------------------------
def generate():
    """
    Reads user input, expands L-system, and draws it.
    """
    t.clear()
    t.penup()
    t.goto(0, -250)
    t.setheading(90)
    t.pendown()

    axiom = axiom_entry.get()
    angle = float(angle_entry.get())
    iterations = int(iter_entry.get())

    rules_input = rules_entry.get()
    rules = {}

    for rule in rules_input.split(","):
        key, value = rule.split(":")
        rules[key.strip()] = value.strip()

    final_string = expand_lsystem(axiom, rules, iterations)
    draw_lsystem(t, final_string, angle)


# ---------------------------------
# Tkinter GUI Setup
# ---------------------------------
root = tk.Tk()
root.title("L-System Fractal Architect")
root.geometry("1000x700")

# Control Panel
control_frame = tk.Frame(root, padx=10, pady=10)
control_frame.pack(side=tk.LEFT, fill=tk.Y)

tk.Label(control_frame, text="Axiom").pack()
axiom_entry = tk.Entry(control_frame)
axiom_entry.insert(0, "F")
axiom_entry.pack()

tk.Label(control_frame, text="Rules (F:F+F--F+F)").pack()
rules_entry = tk.Entry(control_frame, width=30)
rules_entry.insert(0, "F:F+F--F+F")
rules_entry.pack()

tk.Label(control_frame, text="Angle").pack()
angle_entry = tk.Entry(control_frame)
angle_entry.insert(0, "60")
angle_entry.pack()

tk.Label(control_frame, text="Iterations").pack()
iter_entry = tk.Entry(control_frame)
iter_entry.insert(0, "4")
iter_entry.pack()

tk.Button(control_frame, text="Generate", command=generate).pack(pady=10)

# Canvas for Turtle
canvas_frame = tk.Frame(root)
canvas_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

canvas = tk.Canvas(canvas_frame, bg="white")
canvas.pack(fill=tk.BOTH, expand=True)

screen = turtle.TurtleScreen(canvas)
t = turtle.RawTurtle(screen)
t.speed(0)
t.hideturtle()

root.mainloop()
