from data.data_skills import skills

pokemon = {
    "bulbasaur": {
        "type": {
            "Grass",
            "Poison",
        },
        "base_stats": {
            "hp": 45,
            "attack": 49,
            "defense": 49,
            "sp-atk": 65,
            "sp-def": 65,
            "speed": 45,
        },
        "skills": {
            "growl": skills["growl"],
            "tackle": skills["tackle"],
            "vine_whip": skills["vine_whip"],
        },
    },
    "charmander": {
        "type": {
            "Fire",
        },
        "base_stats": {
            "hp": 39,
            "attack": 52,
            "defense": 43,
            "sp-atk": 60,
            "sp-def": 50,
            "speed": 65,
        },
        "skills": {},
    },
    "squirtle": {
        "type": {
            "Water",
        },
        "base_stats": {
            "hp": 44,
            "attack": 48,
            "defense": 65,
            "sp-atk": 65,
            "sp-def": 65,
            "speed": 64,
        },
        "skills": {},
    },
}
