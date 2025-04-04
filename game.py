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
                print(f"\nNot enough soul!")
                return 0
        else:
            print(f"\nUnknown spell!")
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
        if self.name == "Lost Kin" or self.name == "Vengefly King":
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

def enemies_easy():
    enemies = [
        {"name": "Vengefly King", "stagger": [5, "It gets angrier and more vengeflies gather around you!"], "health": 16, "attack": 3, "chance": 5, "description": ["dashes across the floor!", "summons a little vengefly!"], "phrase": ["*roars*", "*shrieks*"], "death": "It explodes! Minion vengeflies scatter and flee"},
        {"name": "Mantis Lords", "stagger": [10, "The remaining Lords join in the fight!"], "health": 26, "attack": 4, "chance": 10, "description": ["swing across the room!", "slam into the ground!", "throw spinning blades!"], "phrase": ["Stop right there, traveller!", "What do you in our sacred village of warriors?!"], "death": "They retreat and bow to you."},
        {"name": "Hornet Sentinel", "stagger": [15, "Her needles fly faster and her silk appears more deadly!"], "health": 41, "attack": 6, "chance": 15, "description": ["throws her needle!", "lunges at you!", "unleashes silk hell!"], "phrase": ["Come no closer, ghost. I've seen you.. stalking me. Only pity for your cursed kind!", "Yours is resilience born of two voids... but no shadow will haunt me!"], "death": "She silks away, cowardly."}
    ]
    return enemies

def enemies_hard():
    enemies = [
        {"name": "Lost Kin", "stagger": [10, "It shivers and the infection glows brighter"], "health": 20, "attack": 4, "chance": 15, "description": ["swings its nail around!", "spits a ball of radiance!", "dashes across the room!"], "phrase": ["*screams*", "*yells*"], "death": "The infection scatters. An empty, broken vessel falls to the ground."},
        {"name": "Soul Tyrant", "stagger": [12, "He gasps, leaking soul everywhere"], "health": 32, "attack": 5, "chance": 20, "description": ["desolate dives onto the ground!", "casts a soul orb!"], "phrase": ["The King falls, but I live forever!", "My dreams are eternal and so am I!"], "death": "He explodes into fireworks of soul and thunder."},
        {"name": "Nightmare King Grimm", "stagger": [20, "He turns into a swarm of dragons, returning more fiery"], "health": 52, "attack": 8, "chance": 35, "description": ["summons his dragons!", "dashes into the air!", "spawns fire from below!"], "phrase": ["This searing fire... It carries well the Ritual's promise.", "Dance with me, my friend. The crowd awaits. Show them you are worthy of a starring role!"], "death": "His nightmarish form vanishes to the dream realm."}
    ]
    return enemies

charms = ["Mark of Pride", "Shaman Stone", "Lifeblood Heart"]

def pick_charm():
    charm = int(input("\nPick a Charm:\n  [1] Mark of Pride\n  [2] Shaman Stone\n  [3] Lifeblood Heart\n\nChoose: "))

    if charm == 1:
        print("\nEquipped Mark of Pride!")
    elif charm == 2:
        print("\nEquipped Shaman Stone!")
    elif charm == 3:
        print("\nEquipped Lifeblood Heart!")
    else: 
        print("Invalid input!")

    return charm


def game_round(knight, spells, enemies):
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
                    spell_input = input(f"\n  [A] Vengeful Spirit - 2 souls\n  [B] Howling Wraiths - 3 souls\n\nChoose: ").strip().lower()
                    if spell_input == "a":
                        spell = "vengeful spirit"
                        damage = knight.cast_spell(spell, spells)
                        enemy.take_damage(damage)
                    elif spell_input == "b":
                        spell = "howling wraiths"
                        damage = knight.cast_spell(spell, spells)
                        enemy.take_damage(damage)
                    else:
                        invalid = True
                        print("Invalid spell!")
                
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
    print("\nWelcome to Mini Hollow Knight!")
    charm = None
    enemies = enemies_hard()

    while True:
        menu = input("- - - - - - - - - - - - - - - -\n  [A] START\n  [B] Options\n  [Q] Quit\n\nChoose: ").strip().lower()
        if menu == "a" and charm == None:
            knight = Vessel(max_health = 50, health = 50, soul = 0, power = 5, chance = 30)
            spells = {
                "vengeful spirit": {"cost": 2, "damage": 15},
                "howling wraiths": {"cost": 3, "damage": 25},
            }
            game_round(knight, spells, enemies)
            break

        elif menu == "a" and charm != None:
            game_round(knight, spells, enemies)
            break

        elif menu == "b":
            option = input(f"\nOPTIONS\n- - - - - - - - - - - - - - - -\n  [A] Pick a Charm\n  [B] Set difficulty\n  [R] Return to menu\n\nChoose: ").strip().lower()
            if option == "a":
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

            elif option == "b":
                difficulty = int(input(f"\nChange difficulty:\n  [1] Easy\n  [2] Hard\n\nChoose: ").strip())
                if difficulty == 1:
                    enemies = enemies_easy()
                    print("\nDifficulty: Easy")
                elif difficulty == 2:
                    enemies = enemies_hard()
                    print("\nDifficulty: Hard")

            elif option == "r":
                print("\nWelcome to Mini Hollow Knight!")
                continue

        elif menu == "q":
            print("Godspeed, fellow vessel.")
            break

        else:
            print("Invalid input!")

start()