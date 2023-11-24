class NoAmmunitionError(Exception):
    pass

class OutOfRangeError(Exception):
    pass

class Vessel:
    def __init__(self, coordinates: tuple, max_hits: int, weapons):
        self.coordinates = coordinates
        self.max_hits = max_hits
        self.hits = 0
        self.weapons = weapons

    def go_to(self, x: int, y: int, z: int):
        self.coordinates = (x, y, z)

    def get_coordinates(self) -> tuple:
        return self.coordinates

    def fire_at(self, x: int, y: int, z: int):
        if self.hits >= self.max_hits:
            print("The ship is destroyed! Cannot fire.")
            return

        for weapon in self.weapons:
            try:
                weapon.fire_at(x, y, z)
                print("Fire successful!")
                break  # Stop firing after the first successful shot
            except NoAmmunitionError as e:
                print(f"Error: {e}")
            except OutOfRangeError as e:
                print(f"Error: {e}")