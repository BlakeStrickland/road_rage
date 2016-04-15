class Sim():
    def __init__(self):
        self.num_of_cars = 30


    def create_cars(self, position_list):
        cars = [Car(pos) for pos in position_list]
        return cars

    def create_starting_positions(self, num_of_cars):
        y = 0
        x = 0
        pos_list = []
        for _ in range(num_of_cars):
            pos_list.append([x,y])
            x += 1000/num_of_cars
        return pos_list

    def move_cars(self):
        for car in self.num_of_cars:
            car.move_car()

    def sim_start(self):
        pass
