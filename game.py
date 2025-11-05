import random, time

class Vessel:
    def __init__(self, max_health, health, soul, max_soul, power, chance):
        self.max_health = max_health
        self.health = health
        self.soul = soul
        self.max_soul = max_soul
        self.power = power
        self.chance = chance

    def take_damage(self, damage):
        if random.randint(1, 100) <= self.chance:
            time.sleep(0.5)
            print("(Vessel dodged the attack!)")
            time.sleep(0.5)
            print("❤ You avoided damage!")
            return self.health
        
        self.health -= damage
        time.sleep(0.5)
        print(f"❤ You took {damage} damage!")
        return self.health
    
    def nail_attack(self):
        damage = self.power + random.randint(0, 2)
        if self.soul < self.max_soul:
            self.soul += 1
        print(f"\n// Vessel swings its nail, dealing {damage} damage!")
        return damage, self.soul
    
    def critical_hit(self):
        damage = int(self.power * 1.5) + random.randint(1, 3)
        if self.soul < self.max_soul:
            self.soul += 1
        print(f"\n// Vessel uses a Great Slash, dealing {damage} damage!")
        return damage, self.soul
    
    def soul_focus(self):
        if self.soul > 0:
            if self.health < self.max_health:
                self.soul -= 1
                self.health += 10 + random.randint(0, 3)
                
                if self.health > self.max_health:
                    self.health = self.max_health 
                print(f"\n+ Vessel focuses a soul and heals to {self.health}hp!")
                return self.soul, self.health, False   
            else:
                self.soul -= 1
                print(f"\n+ Vessel focuses a soul and heals to {self.health}hp!")
                return self.soul, self.health, False
        else:
            print(f"\n﹡ Not enough soul to heal!")
            return self.soul, self.health, True
        
    def cast_spell(self, spell, spells):
        if spell in spells:
            if self.soul >= spells[spell]["cost"]:
                self.soul -= spells[spell]["cost"]
                print(f"\nϟ Vessel casts {spell.title()}, dealing {spells[spell]['damage']} damage! ϟ")
                return spells[spell]["damage"]
            else: 
                print("\nϟ Vessel tries to cast a spell.. ϟ")
                time.sleep(1)
                print("             ..but gets knocked back!!")
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
        print(f"\n// {self.name} {self.description[val]}")
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
            print(f"\n[!] {self.name} staggers! \n› {self.stagger[1]}")
            self.attack += round(self.attack / 2)
            return True
        else: return False

    def enemy_dies(self):
        print(f"\n{self.death}")
        time.sleep(0.5)

def stats(knight, length = 20):
    full_health = int(knight.health / knight.max_health * length)
    empty_health = length - full_health
    bar_health = '█' * full_health + '░' * empty_health

    full_soul = int(knight.soul)
    empty_soul = knight.max_soul - full_soul
    bar_soul = '⦿ ' * full_soul + '◌ ' * empty_soul
    print(f"\nHEALTH ╏ |{bar_health}|  {knight.health}/{knight.max_health} ❤\nSOUL   ╏  {bar_soul} {knight.soul}/{knight.max_soul}")
    

def enemies_normal():
    enemies = [
        {"name": "Vengefly King", "stagger": [5, "It gets angrier and more vengeflies gather around you!"], "health": 16, "attack": 3, "chance": 5, "description": ["dashes across the floor!", "summons a little vengefly!"], "phrase": ["*roars*", "*shrieks*"], "death": "It explodes! \nMinion vengeflies scatter and flee"},
        {"name": "Mantis Lords", "stagger": [10, "The remaining Lords join in the fight!"], "health": 26, "attack": 4, "chance": 10, "description": ["swing across the room!", "slam into the ground!", "throw spinning blades!"], "phrase": ["Stop right there, traveller!", "What do you in our sacred village of warriors?!"], "death": "They retreat and bow to you."},
        {"name": "Hornet Sentinel", "stagger": [15, "Her needles fly faster and her silk appears more deadly!"], "health": 41, "attack": 6, "chance": 15, "description": ["throws her needle!", "lunges at you!", "unleashes silk hell!"], "phrase": ["Come no closer, ghost. I've seen you.. stalking me. Only pity for your cursed kind!", "Yours is resilience born of two voids... but no shadow will haunt me!"], "death": "She silks away, cowardly."}
    ]
    return enemies, "▰▱▱ [ ϟ ] Normal"

def enemies_hard():
    enemies = [
        {"name": "Lost Kin", "stagger": [10, "It shivers and the infection glows brighter"], "health": 20, "attack": 4, "chance": 15, "description": ["swings its nail around!", "spits a ball of radiance!", "dashes across the room!"], "phrase": ["*screams*", "*yells*"], "death": "The infection scatters. \nAn empty, broken vessel falls to the ground."},
        {"name": "Soul Tyrant", "stagger": [12, "He gasps, leaking soul everywhere"], "health": 32, "attack": 5, "chance": 20, "description": ["desolate dives onto the ground!", "casts a soul orb!"], "phrase": ["The King falls, but I live forever!", "My dreams are eternal and so am I!"], "death": "He explodes into fireworks of soul and thunder."},
        {"name": "Nightmare King Grimm", "stagger": [20, "He turns into a swarm of dragons, returning more fiery"], "health": 52, "attack": 8, "chance": 35, "description": ["summons his dragons!", "dashes into the air!", "spawns fire from below!"], "phrase": ["This searing fire... It carries well the Ritual's promise.", "Dance with me, my friend. The crowd awaits. Show them you are worthy of a starring role!"], "death": "His nightmarish form vanishes to the dream realm."}
    ]
    return enemies, "▰▰▰ [ ϟ ] Hard"

charms = ["Mark of Pride", "Shaman Stone", "Lifeblood Heart"]

def pick_charm():
    charm = input("\n___ [ CHARMS ] ________________\n\n  ➤ [ 1 ]  ⌑  Unbreakable Strength\n  ➤ [ 2 ]  ✦  Shaman Stone\n  ➤ [ 3 ]  ❤  Lifeblood Heart\n\n▷  ")

    try:
        charm = int(charm)

        if charm == 1:
            print("\nEquipped Unbreakable Strength!")
        elif charm == 2:
            print("\nEquipped Shaman Stone!")
        elif charm == 3:
            print("\nEquipped Lifeblood Heart!")
        else: 
            print("\nInvalid charm!")

    except:
        print("\nInvalid charm!")

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

        print(f"\n≽ A NEW CHALLENGER HAS APPEARED: {enemy.name}!! ≼")
        time.sleep(1)
        enemy.character_moto()

        global stagger_check 
        stagger_check = False

        global critical
        critical = 1

        while knight.health > 0 and enemy.health > 0:
            def act():
                invalid = False

                time.sleep(1)
                print("\n ▰ ▰ ▰ [ NEW TURN ] ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰")
                stats(knight)

                action = input(f"\nC͟h͟o͟o͟s͟e͟ ͟y͟o͟u͟r͟ ͟a͟c͟t͟i͟o͟n͟:\n\n   [1] Attack {enemy.name}\n   [2] Heal yourself\n   [3] Cast a spell\n\n▷  ").strip().lower()

                global critical

                try: 
                    action = int(action)
                    top = "\n───[ ACTION ]─────────────────────────────────────┐"
                    if action == 1:
                        print(top)
                        if critical < 3:
                            critical += 1
                            damage, _ = knight.nail_attack()
                            enemy.take_damage(damage)
                            time.sleep(0.5)
                            print("○ Gained 1 Soul")
                        elif critical == 3:
                            critical = 1
                            damage, _ = knight.critical_hit()
                            enemy.take_damage(damage)
                            time.sleep(0.5)
                            print("○ Gained 1 Soul")
                            

                    elif action == 2:
                        critical = 1
                        print(top)
                        s, h, k = knight.soul_focus()
                        if k == True:
                            act()
                            return

                    elif action == 3:
                        critical = 1
                        spell_input = input(f"\nC͟h͟o͟o͟s͟e͟ ͟a͟ ͟s͟p͟e͟l͟l͟:\n\n   [A] Vengeful Spirit (2 souls)\n   [B] Howling Wraiths (3 souls)\n\n▷  ").strip().lower()
                        if spell_input == "a":
                            print(top)
                            spell = "vengeful spirit"
                            damage = knight.cast_spell(spell, spells)
                            if damage != 0:
                                enemy.take_damage(damage)
                        elif spell_input == "b":
                            print(top)
                            spell = "howling wraiths"
                            damage = knight.cast_spell(spell, spells)
                            if damage != 0:
                                enemy.take_damage(damage)
                        else:
                            invalid = True
                            print("\n» Invalid spell!")
                
                    else:
                        print("\n» Invalid input!")
                        invalid = True

                except:
                    print("\n» Invalid action!")
                    invalid = True

                time.sleep(1)

                if enemy.health > 0 and invalid == False:
                    enemy_damage = enemy.attack_player()
                    knight.take_damage(enemy_damage)

                    global stagger_check

                    if stagger_check == False:
                        stagger_check = enemy.stagger_stage()

                    print("\n──────────────────────────────────────────────────┘")

            act()

        if knight.health <= 0:
            print(f"\nYou were killed by {enemy.name}! May your shade find peace")
            break
        else:
            enemy.enemy_dies()
            print("\n──────────────────────────────────────────────────┘")
            print(f"\n☓ You killed {enemy.name}!")
            time.sleep(2)

    if knight.health > 0:
        print("\nYou killed all the enemies, and saved Hallownest! Well done, mighty Vessel.")


def start():
    charm = None
    charm_name = "▫▫▫ [ x ] None"
    enemies, difficulty = enemies_hard()

    while True:
        print("\n[  M I N I   H O L L O W   K N I G H T  ]\n▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰\n")
        print(f"\nDIFFICULTY  ︳   {difficulty}\nBound to..  ︳   {charm_name}\n")
        print(f"\n___ [ MAIN MENU ] _______________________\n\n  ➤ [ A ]  START\n  ➤ [ B ]  Options\n  ➤ [ Q ]  Quit\n")
        menu = input("\n▷  ").strip().lower()
        if menu == "a" and charm == None:
            knight = Vessel(max_health = 50, health = 50, soul = 0, max_soul = 3, power = 5, chance = 30)
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
            option = input(f"\n___ [ OPTIONS ] _________________________\n\n  ➤ [ A ]  Pick a Charm\n  ➤ [ B ]  Change Difficulty\n  ➤ [ C ]  Credits\n  ➤ [ R ]  Return to Menu\n\n▷  ").strip().lower()
            if option == "a":
                charm = pick_charm()

                if charm == 1:
                    charm_name = "▣▫▫ [ ⌑ ] Unbreakable Strength"
                    knight = Vessel(max_health = 50, health = 50, soul = 0, max_soul = 3, power = 7, chance = 30)
                    spells = {
                        "vengeful spirit": {"cost": 2, "damage": 15},
                        "howling wraiths": {"cost": 3, "damage": 25},
                    }
                elif charm == 2:
                    charm_name = "▫▣▫ [ ✦ ] Shaman Stone"
                    knight = Vessel(max_health = 50, health = 50, soul = 0, max_soul = 3, power = 5, chance = 30)
                    spells = {
                        "vengeful spirit": {"cost": 2, "damage": 19},
                        "howling wraiths": {"cost": 3, "damage": 29},
                    }
                elif charm == 3:
                    charm_name = "▫▫▣ [ ❤ ] Lifeblood Heart"
                    knight = Vessel(max_health = 65, health = 65, soul = 0, max_soul = 3, power = 5, chance = 30)
                    spells = {
                        "vengeful spirit": {"cost": 2, "damage": 15},
                        "howling wraiths": {"cost": 3, "damage": 25},
                    }

            elif option == "b":
                difficulty_int = input(f"\n___ [ DIFFICULTY ] ______________________\n\n  ➤ [ 1 ]  ϟ   Normal\n  ➤ [ 2 ]  ϟϟ  Hard\n\n▷  ").strip()
                try:
                    difficulty_int = int(difficulty_int)

                    if difficulty_int == 1:
                        enemies, difficulty = enemies_normal()
                        print("\nDifficulty: Normal")
                    elif difficulty_int == 2:
                        enemies, difficulty = enemies_hard()
                        print("\nDifficulty: Hard")
                    else:
                        print("\nInvalid difficulty!")

                except:
                    print("\nInvalid difficulty!")

            elif option == "c":
                print()
                print("----------------------")
                print("> code: gettingfunkier")
                print("> assets: Team Cherry")
                print("----------------------")
                continue

            elif option == "r":
                continue

            else: 
                print("\nInvalid Input!")

        elif menu == "q":
            print("Godspeed, fellow vessel.")
            break

        else:
            print("\nInvalid input!")

start()

# Script by gettingfunkier, 2025