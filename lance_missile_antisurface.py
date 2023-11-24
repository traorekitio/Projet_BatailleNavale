class Lance_missile_antisurface(Weapon):
    def _init_(self, ammunitions: int):
        super()._init_(ammunitions, 100)


    def is_valid_target(self, x: int, y: int, z: int):
        return z == 0