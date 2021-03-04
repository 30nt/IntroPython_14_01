class Unit:
    def __init__(self):
        self._intelligence = 1
        self._strength = 1

    def __repr__(self):
        return f"strength: {self._strength}, intelligence: {self._intelligence}"

    def increase_base_skill(self):
        raise NotImplementedError


class Mage(Unit):
    def increase_base_skill(self):
        self._intelligence += 1


class Knight(Unit):
    def increase_base_skill(self):
        self._strength += 1


gendalf = Mage()
gendalf.increase_base_skill()


print(gendalf)