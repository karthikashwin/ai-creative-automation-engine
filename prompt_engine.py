import random

HOOKS = [
    "Only 1% can solve this level!",
    "Can you beat this puzzle?",
    "Unlock rare rewards now!",
    "This game is addictive!"
]

EMOTIONS = [
    "excited character",
    "shocked reaction",
    "intense focus",
    "celebration moment"
]

STYLE = "vibrant mobile game advertisement, cinematic lighting, high detail"

def generate_prompt(base_theme):
    hook = random.choice(HOOKS)
    emotion = random.choice(EMOTIONS)

    return f"{base_theme}, {hook}, {emotion}, {STYLE}"