import random, time

class Vessel:
    def __init__(self, max_health, health, soul, power, chance):
        self.max_health = max_health
        self.health = health
        self.soul = soul
        self.power = power
        self.chance = chance

    def take_damage(self, damage):
        if random.randint(1, 100) <= self.chance:
            time.sleep(0.5)
            print("(Vessel dodged the attack!)")
            return self.health
        
        self.health -= damage
        return self.health
    
    def nail_attack(self):
        damage = self.power + random.randint(0, 2)
        if self.soul < 3:
            self.soul += 1
        print(f"\n- Vessel swings its nail and deals {damage} damage! Has {self.soul} soul")
        return damage, self.soul
    
    def soul_focus(self):
        if self.soul > 0:
            if self.health < self.max_health:
                self.soul -= 1
                self.health += 10 + random.randint(0, 3)
                
                if self.health > self.max_health:
                    self.health = self.max_health 
                print(f"\n- Vessel focuses 1 soul and heals to {self.health}hp! {self.soul} soul left")
                return self.soul, self.health, False   
            else:
                self.soul -= 1
                print(f"\n- Vessel focuses 1 soul and heals to {self.health}hp! {self.soul} soul left")
                return self.soul, self.health, False
        else:
            print(f"\nNot enough soul to heal!")
            return self.soul, self.health, True
        
    def cast_spell(self, spell, spells):
        if spell in spells:
            if self.soul >= spells[spell]["cost"]:
                self.soul -= spells[spell]["cost"]
                print(f"\n- Vessel casts {spell.title()}, dealing {spells[spell]['damage']} damage!")
                return spells[spell]["damage"]
            else:
                print("Not enough soul!")
                return 0
        else:
            print("Unknown spell!")
            return 0
    

class Enemy:
    def __init__(self, name, stagger, health, attack, chance, description, phrase, death):
        self.name = name
        self.stagger = stagger
        self.health = health
        self.attack = attack
        self.chance = chance
        self.description = description
        self.phrase = phrase
        self.death = death

    def take_damage(self, damage):
        if random.randint(1, 100) <= self.chance:
            time.sleep(0.5)
            print(f"({self.name} dodged the attack!)")
            return self.health

        self.health -= damage

    def attack_player(self):
        damage = self.attack + random.randint(0, 2)
        val = random.randint(1, len(self.description)) - 1
        print(f"\n- {self.name} {self.description[val]}")
        return damage
    
    def character_moto(self):
        value = random.randint(0, len(self.phrase) - 1)
        if self.name == "Lost Kin":
            print(f'\n{self.phrase[value]}')
        else:
            print(f'\n"{self.phrase[value]}"')

    def stagger_stage(self):
        if self.health <= self.stagger[0]:
            time.sleep(1)
            print(f"\n〉{self.name} staggers! {self.stagger[1]} 〈")
            self.attack += round(self.attack / 2)
            return True
        else: return False

    def enemy_dies(self):
        print(f"\n{self.death}")
        time.sleep(2)

def stats(knight):
    print(f"\nVessel: {knight.health}hp | {knight.soul} soul")

enemies = [
    {"name": "Lost Kin", "stagger": [10, "It shivers and the infection glows brighter"], "health": 20, "attack": 4, "chance": 15, "description": ["swings its nail around!", "spits a ball of radiance!", "dashes across the room!"], "phrase": ["*screams*", "*yells*"], "death": "The infection scatters. An empty, broken vessel falls to the ground."},
    {"name": "Soul Tyrant", "stagger": [12, "He gasps, leaking soul everywhere"], "health": 32, "attack": 5, "chance": 20, "description": ["desolate dives onto the ground!", "casts a soul orb!"], "phrase": ["The King falls, but I live forever!", "My dreams are eternal and so am I!"], "death": "He explodes into fireworks of soul and thunder."},
    {"name": "Nightmare King Grimm", "stagger": [20, "He turns into a swarm of dragons, returning more fiery"], "health": 52, "attack": 8, "chance": 35, "description": ["summons his dragons!", "dashes into the air!", "spawns fire from below!"], "phrase": ["This searing fire... It carries well the Ritual's promise.", "Dance with me, my friend. The crowd awaits. Show them you are worthy of a starring role!"], "death": "His nightmarish form vanishes to the dream realm."}
]

charms = ["Mark of Pride", "Shaman Stone", "Lifeblood Heart"]

def pick_charm():
    charm = int(input("\n1 - Mark of Pride\n2 - Shaman Stone\n3 - Lifeblood Heart\n\nPick a charm: "))

    if charm == 1:
        print("\nYou've chosen Mark of Pride!")
    elif charm == 2:
        print("\nYou've chosen Shaman Stone!")
    elif charm == 3:
        print("\nYou've chosen Lifeblood Heart!")
    else: 
        print("Invalid input!")

    return charm


def game_round(knight, spells):
    for item in enemies:
        enemy = Enemy(
            name = item["name"], 
            stagger = item["stagger"],
            health = item["health"], 
            attack = item["attack"], 
            chance = item["chance"], 
            description = item["description"], 
            phrase = item["phrase"],
            death = item["death"]
            )

        print(f"\n〉A NEW CHALLENGER HAS APPEARED: {enemy.name}!! 〈")
        time.sleep(1)
        enemy.character_moto()

        global stagger_check 
        stagger_check = False

        while knight.health > 0 and enemy.health > 0:
            def act():
                invalid = False

                global stagger_check

                if stagger_check == False:
                    stagger_check = enemy.stagger_stage()

                time.sleep(1)
                print("\n - - - NEW TURN - - -")
                stats(knight)

                action = input("Choose action [ attack / heal / spell ] : ").strip().lower()

                if action == "attack":
                    damage, _ = knight.nail_attack()
                    enemy.take_damage(damage)

                elif action == "heal":
                    s, h, k = knight.soul_focus()
                    if k == True:
                        act()
                        return

                elif action == "spell":
                    spell = input("Choose a spell [ Vengeful Spirit / Howling Wraiths ] : ")
                    damage = knight.cast_spell(spell, spells)
                    enemy.take_damage(damage)
                
                else:
                    print("Invalid input!")
                    invalid = True

                time.sleep(1)

                if enemy.health > 0 and invalid == False:
                    enemy_damage = enemy.attack_player()
                    knight.take_damage(enemy_damage)

            act()

        if knight.health <= 0:
            print(f"\nYou were killed by {enemy.name}! May your shade find peace")
            break
        else:
            enemy.enemy_dies()

    if knight.health > 0:
        print("\nYou killed all the enemies, and saved Hallownest! Well done, mighty Vessel.")


def start():
    print("\nWelcome to mini Hollow Knight!")
    charm = None

    while True:
        menu = input("\nA - START\nB - Pick a charm\n\nChoose: ").strip().lower()
        if menu == "a" and charm == None:
            knight = Vessel(max_health = 50, health = 50, soul = 0, power = 5, chance = 30)
            spells = {
                "vengeful spirit": {"cost": 2, "damage": 15},
                "howling wraiths": {"cost": 3, "damage": 25},
            }
            game_round(knight, spells)
            break

        elif menu == "a" and charm != None:
            game_round(knight, spells)
            break

        elif menu == "b":
            charm = pick_charm()

            if charm == 1:
                knight = Vessel(max_health = 50, health = 50, soul = 0, power = 7, chance = 30)
                spells = {
                    "vengeful spirit": {"cost": 2, "damage": 15},
                    "howling wraiths": {"cost": 3, "damage": 25},
                }
            elif charm == 2:
                knight = Vessel(max_health = 50, health = 50, soul = 0, power = 5, chance = 30)
                spells = {
                    "vengeful spirit": {"cost": 2, "damage": 19},
                    "howling wraiths": {"cost": 3, "damage": 29},
                }
            elif charm == 3:
                knight = Vessel(max_health = 65, health = 65, soul = 0, power = 5, chance = 30)
                spells = {
                    "vengeful spirit": {"cost": 2, "damage": 15},
                    "howling wraiths": {"cost": 3, "damage": 25},
                }
        else:
            print("Invalid input!")

start()