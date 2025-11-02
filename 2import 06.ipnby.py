def smart_light_agent(time, motion, ambient_light):
    """
    Rule-based light control:
    time: 'day' or 'night'
    motion: True or False
    ambient_light: value from 0 (dark) to 100 (bright)
    """
    if time == "night" and motion and ambient_light < 40:
        action = "Turn ON light"
    elif time == "day" and ambient_light < 30:
        action = "Dim light"
    else:
        action = "Turn OFF light"
    return action
scenarios = [
    ("night", True, 20),
    ("day", False, 80),
    ("night", False, 10),
    ("day", True, 25)
]

for s in scenarios:
    print(f"Time: {s[0]}, Motion: {s[1]}, Light: {s[2]} → Action: {smart_light_agent(*s)}")
