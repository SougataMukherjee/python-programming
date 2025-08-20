import random

subjects=[
    "Sougata Mukherjee",
    "Rupai",
    "Sam Muk",
    "a group of girls",
    "company CEO",
    "Bus driver in bangalore"
]

actions=[
    "cancels",
    "swimming with",
    "sleep",
    "celebrate"
]
places=[
    "at home",
    "at office",
    "at roof",
    "at airport",
    "at bus stop"
]

while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place=random.choice(places)

    heading=f"Breaking News:{subject} {action} {place}"
    print("\n" + heading)

    user_input=input("\n Do you want to another headline? (Yes/NO)".strip())
    if user_input =="no":
        break

print("\n thanks for using fake heading")