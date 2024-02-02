# PERSON CLASS

import random
class person:
    def __init__(self):
        self.names = ["María", "Juan", "Gabriela", "Alejandro", "Laura", "Carlos", "Sofía", "Luis", "Valentina", "Martín"]
        self.name = random.choice(self.names)
        self.age = random.randint(18,50)
        self.skill_level = random.randint(1,10)
        self.winning_count = 0

    def add_skill(self,n):
        self.skill_level = n

    def add_winning(self):
        self.winning_count += 1

    def set_name(self,name):
        self.name = name

    def set_age(self,age):
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_skill_level(self):
        return self.skill_level

    def get_winning_count(self):
        return self.winning_count

    def play_against(self, opponent):
        skill_difference = abs(self.skill_level - opponent.skill_level)

        if skill_difference <= 2:
            probability = 0.5
        elif skill_difference <= 4:
            probability = 0.75
        else:
            probability = 1.0

        self.define_result(probability,opponent)

    def define_result(self,probability,opponent):

        result = random.choices([True, False], weights=[probability, 1 - probability])[0]

        print("game result : "f"{result}")

        if probability == 0.5 or opponent.get_skill_level() < self.get_skill_level():
            if result:
                self.add_winning()
            else:
                opponent.add_winning()
        else:

            if result:
                opponent.add_winning()
            else:
                self.add_winning()


# CREATE PEOPLE LIST AND PLAY
people_list = [person() for p in range(10)]

for p in range(20):
    players = random.sample(people_list,2)
    player_one = players[0]
    print("Beginning:")
    print("player One : "f"{player_one.get_name()} - Skill: {player_one.get_skill_level()}, Winning Count: {player_one.get_winning_count()}")
    player_Two = players[1]
    print("player Two : "f"{player_Two.get_name()} - Skill: {player_Two.get_skill_level()}, Winning Count: {player_Two.get_winning_count()}")
    player_one.play_against(player_Two)
    print("results:")
    print("player One : "f"{player_one.get_name()} - Skill: {player_one.get_skill_level()}, Winning Count: {player_one.get_winning_count()}")
    print("player Two : "f"{player_Two.get_name()} - Skill: {player_Two.get_skill_level()}, Winning Count: {player_Two.get_winning_count()}")
    print("----------------------------------------------------------------------------------------------")

#for person in people_list:
#    print ("General results: ")
#    print(f"{person.get_name()} - Skill: {person.get_skill_level()}, Winning Count: {person.get_winning_count()}")







