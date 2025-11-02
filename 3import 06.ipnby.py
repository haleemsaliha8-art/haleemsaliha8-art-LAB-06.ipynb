import random

past_temps = []
current_temp = random.randint(18, 26)

def thermostat_agent(current_temp, past_temps):
    if len(past_temps) >= 3:
        trend = current_temp - past_temps[-3]  # Compare 3 readings ago
    else:
        trend = 0
    
    if current_temp < 20:
        action = "Turn ON Heater"
    elif current_temp > 24:
        action = "Turn ON Cooler"
    elif trend > 2:
        action = "Trend rising fast → Preemptively Cool"
    elif trend < -2:
        action = "Trend dropping fast → Preemptively Heat"
    else:
        action = "Maintain Current State"
    
    return action
for step in range(10):
    past_temps.append(current_temp)
    current_temp += random.choice([-2, -1, 0, 1, 2])
    action = thermostat_agent(current_temp, past_temps)
    print(f"Step {step + 1}: Temp={current_temp}°C | Action: {action}")
