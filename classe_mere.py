
class NoAmmunitionError(Exception):
    pass

class OutOfRangeError(Exception):
    pass


class Weapon:
    def _init_(self, ammunitions: int, weapon_range: int):
        self.ammunitions = ammunitions
        self.range = weapon_range

    def fire_at(self, x: int, y: int, z: int):
        if self.ammunitions <= 0:
            raise NoAmmunitionError("Out of ammunition!")
        self.ammunitions -= 1
        if not self.is_valid_target(x, y, z):
            raise OutOfRangeError("Target out of range!")

    def is_valid_target(self, x: int, y: int, z: int):
        # Méthode à redéfinir dans les classes filles selon les règles spécifiques
        pass

