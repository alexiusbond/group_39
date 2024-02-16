from random import randint, choice
from enum import Enum


class SuperAbility(Enum):
    HEAL = 1
    BLOCK_DAMAGE_AND_REVERT = 2
    BOOST = 3
    CRITICAL_DAMAGE = 4


class GameEntity:
    def __init__(self, name, health, damage):
        self.__name = name
        self.__health = health
        self.__damage = damage

    @property
    def name(self):
        return self.__name

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        if value < 0:
            self.__health = 0
        else:
            self.__health = value

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, value):
        self.__damage = value

    def __str__(self):
        return (f'{self.__name} HEALTH: {self.__health} '
                f'DAMAGE: {self.__damage}')


class Boss(GameEntity):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage)
        self.__defence = None

    @property
    def defence(self):
        return self.__defence

    def choose_defence(self, heroes: list):
        random_hero: Hero = choice(heroes)
        self.__defence = random_hero.ability

    def attack(self, heroes: list):
        for hero in heroes:
            if hero.health > 0:
                # if hero.ability == SuperAbility.BLOCK_DAMAGE_AND_REVERT:
                if (type(hero) == Berserk and
                        self.__defence != SuperAbility.BLOCK_DAMAGE_AND_REVERT):
                    berserk: Berserk = hero
                    # berserk.blocked_damage = int(self.damage / 5)
                    berserk.blocked_damage = int(self.damage / (randint(1, 2) * 5))  # 5, 10
                    berserk.health -= (self.damage - berserk.blocked_damage)
                else:
                    hero.health -= self.damage

    def __str__(self):
        return ('BOSS ' + super().__str__()
                + f' DEFENCE: {self.__defence}')


class Hero(GameEntity):
    def __init__(self, name, health, damage, ability):
        super().__init__(name, health, damage)
        self.__ability = ability

    @property
    def ability(self):
        return self.__ability

    def attack(self, boss: Boss):
        boss.health -= self.damage  # boss.health = boss.health - self.damage

    def apply_super_power(self, boss: Boss, heroes: list):
        pass


class Warrior(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbility.CRITICAL_DAMAGE)

    def apply_super_power(self, boss: Boss, heroes: list):
        crit = randint(2, 5) * self.damage
        boss.health -= crit
        print(f'Warrior {self.name} hits critically {crit}')


class Magic(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbility.BOOST)

    def apply_super_power(self, boss: Boss, heroes: list):
        pass


class Berserk(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage,
                         SuperAbility.BLOCK_DAMAGE_AND_REVERT)
        self.blocked_damage = 0

    @property
    def blocked_damage(self):
        return self.__blocked_damage

    @blocked_damage.setter
    def blocked_damage(self, value):
        self.__blocked_damage = value

    def apply_super_power(self, boss: Boss, heroes: list):
        boss.health -= self.__blocked_damage
        print(f'Berserk {self.name} reverted {self.__blocked_damage}')


class Medic(Hero):
    def __init__(self, name, health, damage, heal_points):
        super().__init__(name, health, damage, SuperAbility.HEAL)
        self.__heal_points = heal_points

    def apply_super_power(self, boss: Boss, heroes: list):
        for hero in heroes:
            if hero.health > 0 and self != hero:
                hero.health += self.__heal_points


round_number = 0


def start_game():
    boss = Boss('Putch', 1000, 50)

    warrior_1 = Warrior('Tilek', 270, 10)
    warrior_2 = Warrior('Aidyn', 280, 15)
    magic = Magic('Heldolf', 290, 20)
    berserk = Berserk('Viking', 260, 10)
    doc = Medic('Aibolit', 250, 5, 15)
    assistant = Medic('Junior', 300, 5, 5)

    heroes_list = [warrior_1, warrior_2, magic, berserk, doc, assistant]
    show_statistics(boss, heroes_list)

    while not is_game_over(boss, heroes_list):
        play_round(boss, heroes_list)


def is_game_over(boss: Boss, heroes: list):
    if boss.health <= 0:
        print('Heroes won!')
        return True
    all_heroes_dead = True
    for hero in heroes:
        if hero.health > 0:
            all_heroes_dead = False
            break
    if all_heroes_dead:
        print('Boss won!')
    return all_heroes_dead


def show_statistics(boss: Boss, heroes: list):
    print(f'ROUND {round_number} -----------')
    print(boss)
    for hero in heroes:
        print(hero)


def play_round(boss: Boss, heroes: list):
    global round_number
    round_number += 1
    boss.choose_defence(heroes)
    boss.attack(heroes)
    for hero in heroes:
        if (hero.health > 0 and boss.health > 0
                and boss.defence != hero.ability):
            hero.attack(boss)
            hero.apply_super_power(boss, heroes)
    show_statistics(boss, heroes)


start_game()
