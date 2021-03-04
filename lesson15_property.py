class Unit:
    def __init__(self):
        self._intelligence = 1
        self._strength = 1
        self._base_skill = 1

    @property
    def intelligence(self):
        return self._intelligence

    @property
    def strength(self):
        return self._strength

    def __repr__(self):
        return f"strength: {self._strength}, intelligence: {self._intelligence}"

    def increase_base_skill(self):
        self._base_skill += 1


class Mage(Unit):
    @property
    def intelligence(self):
        self._intelligence = self._base_skill
        return self._intelligence

    def __repr__(self):
        self._intelligence = self._base_skill
        return super().__repr__()


class Knight(Unit):
    @property
    def strength(self):
        self._strength = self._base_skill
        return self._strength


gendalf = Mage()
gendalf.increase_base_skill()
gendalf.increase_base_skill()
gendalf.increase_base_skill()
print(gendalf)