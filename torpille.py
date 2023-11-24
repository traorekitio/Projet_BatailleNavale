from classe_mere import Weapon
 
class LanceTorpilles(Weapon):
    def __init__(self, ammunitions : int):
        super().__init__(ammunitions, 40)
    def is_valid_target(self, x:int, y:int, z:int):
        return(z<=0)   

    