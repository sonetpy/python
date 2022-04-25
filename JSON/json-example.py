import json
with open('superheroes.json') as f:
    superHeroSquad = json.load(f)
print(superHeroSquad)
print(superHeroSquad.keys())
print(superHeroSquad.values())
