import tkinter as tk
import math

class Gauge(tk.Canvas):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(width=400, height=300, bg='white')

        # Define gauge parameters
        self.min_value = 0
        self.max_value = 100
        self.value = 0

        # Center coordinates and radius of the gauge
        self.cx = 200
        self.cy = 200
        self.radius = 150

        # Create elements of the gauge
        self.create_arc_gauge()

    def create_arc_gauge(self):
        # Create arcs with different colors
        coord = (self.cx - self.radius, self.cy - self.radius, self.cx + self.radius, self.cy + self.radius)
        self.create_arc(coord, start=90, extent=90, outline="green", style="arc", width=40)  # Green: 0-50
        self.create_arc(coord, start=45, extent=45, outline="yellow", style="arc", width=40)  # Yellow: 50 -75
        self.create_arc(coord, start=0, extent=45, outline="red", style="arc", width=40)     # Red: 75 -100

        # Draw needle
        self.needle_id = self.create_line(self.cx, self.cy, self.cx, self.cy - self.radius, width=10, fill='black')

        # Draw labels
        self.create_text(150, 10, font="Times 20 italic bold", text="Humidity")
        self.create_text(45, 250, font="Times 12 bold", text="0")
        self.create_text(355, 250, font="Times 12 bold", text="100")
        self.value_text_id = self.create_text(200, 240, font="Times 15 bold", text="0 %")

        self.update_gauge()

    def update_gauge(self):
        angle = 135 - (self.value - self.min_value) * 1.8
        angle_rad = math.radians(angle)

        x2 = self.cx + self.radius * math.cos(angle_rad)
        y2 = self.cy - self.radius * math.sin(angle_rad)

        self.coords(self.needle_id, self.cx, self.cy, x2, y2)
        self.itemconfig(self.value_text_id, text=f"{self.value} %")

    def set_value(self, value):
        self.value = min(max(value, self.min_value), self.max_value)  # Clamp value within min and max
        self.update_gauge()

# Create a Tkinter application
root = tk.Tk()
root.title("Gauge")

# Create a Gauge widget
gauge = Gauge(root)
gauge.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

# Example of updating the gauge value
def update_gauge_value(value):
    gauge.set_value(int(value))

# Create a scale widget to simulate changing values
scale = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, command=update_gauge_value)
scale.pack(pady=10)

# Set an initial value for the gauge
gauge.set_value(36)

# Run the Tkinter event loop
root.mainloop()
