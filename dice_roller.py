import random
def dice_type(sides):
    roll = random.randint(1, sides)
    return roll
print(dice_type(20))

class life_tracker:
    def __init__(self, baseline_life=20):
        self.baseline_life = baseline_life
        self.current_total = baseline_life
        
    def life_total_add(self, life_gain):
        self.current_total += life_gain
        
    def life_total_sub(self, life_lost):
        self.current_total -= life_lost
        if self.current_total <= 0:
            print(' You Died ')
        
    def life_visual(self):
        print(self.current_total)

display_life = life_tracker()

while display_life.current_total > 0:
    display_life.life_total_sub(int(input()))
    display_life.life_visual()
    if display_life.current_total < 0:
        break
