class Car:
    def __init__(self,road_length, time):
        self.max_speed = 33.33333333333333333333333
        self.acceleration_rate = 2
        self.slow_down = 2
        self.position = (road_length, time)
        self.size = 5

    def move_car(self):
        self.position[0] = self.position[0] + self.acceleration_rate
        self.position += 1
        return self.position

    def avoid_collision(self):
        self.position[0] = self.position[0] - self.slow_down
        self.position[1] += 1
        return self.position
        
