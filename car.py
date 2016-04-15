class Car:
    def __init__(self,road_length):
        self.max_speed = 33.33333333333333333333333
        self.acceleration_rate = 2
        self.slow_down = 2
        self.position = road_length
        self.size = 5
        self.speed = 0

    def move_car(self):
        self.position[0] = self.position[0] + self.acceleration_rate
        return self.position

    def slow_car(self):
        self.acceleration_rate -= self.slow_down
        self.position[0] += self.acceleration_rate
        self.speed = self.slow_down
        return self.position

    def stop_car(self):
        self.speed = 0
        return self.position

    def match_speed(self, speed):
        self.speed = speed
        return self.speed
