# '1' = Dirty, '0' = Clean
rooms = {
    "A": int(input("Status of Room A (1=Dirty, 0=Clean): ")),
    "B": int(input("Status of Room B (1=Dirty, 0=Clean): ")),
}
loc = input("Initial location (A or B): ").upper()

if rooms[loc] == 1:
  print(f"Room {loc} is Dirty. Cleaning now.")
  rooms[loc] = 0
else:
  print(f"Room {loc} is already Clean.")

loc = "B" if loc == "A" else "A"
print(f"Moving to Room {loc}...")

if rooms[loc] == 1:
  print(f"Room {loc} is Dirty. Cleaning now.")
  rooms[loc] = 0
else:
  print(f"Room {loc} is already Clean.")

print("Final State:", rooms)
print("Goal reached: Both rooms are clean!")