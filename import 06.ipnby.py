import random
rooms = {"A": "Dirty", "B": "Dirty", "C": "Dirty"}
clean_counter = 0
agent_position = "A"

def is_all_clean(rooms):
    return all(status == "Clean" for status in rooms.values())
for step in range(10): 
    print(f"\nStep {step + 1}: Agent in Room {agent_position}")
    print("Room states:", rooms)
    
    if rooms[agent_position] == "Dirty":
        print(f"Cleaning Room {agent_position}...")
        rooms[agent_position] = "Clean"
        clean_counter += 1
    else:
        if is_all_clean(rooms):
            agent_position = random.choice(list(rooms.keys()))
            print(f"All rooms clean! Moving randomly to Room {agent_position}.")
        else:
            dirty_rooms = [r for r, s in rooms.items() if s == "Dirty"]
            agent_position = random.choice(dirty_rooms)
            print(f"Moving to Room {agent_position} (Dirty).")

print("\n✅ All rooms are clean!")
print("🧹 Total times cleaned:", clean_counter)
