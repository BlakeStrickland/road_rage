from car import *

class Sim():
    def __init__(self):
        self.num_of_cars = 30
        self.road_length = 1000

    def create_cars(self, position_list):
        self.cars = [Car(pos) for pos in position_list]
        return self.cars

    def create_starting_positions(self):
        x = 0
        pos_list = []
        for _ in range(self.num_of_cars):
            pos_list.append([x])
            x += self.road_length/self.num_of_cars
        return pos_list

    def start_cars(self):
        for car in self.cars:
            car.move_car()

    def look_ahead(self):
        for index, obj in enumerate(self.cars):
            car_index = index
            car1 = self.cars[car_index]
            car2 = self.cars[car_index+1]
            return (car1,car2)

    def avoid_collision(self):
        cars = self.look_ahead()
        car1 = cars[0]
        car2 = cars[1]
        if car1.position[0] + car1.acceleration_rate >= car2.position[0] + car2.acceleration_rate:
            car1.stop()
        elif car1.position[0] - car2.position[0]:
            car1.match_speed(car2.speed)
        else:
            car1.move_car()
