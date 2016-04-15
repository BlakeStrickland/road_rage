from sim import *

def main():
    counter = 60
    while counter > 0:
        simon = Sim()
        cars = simon.create_cars(simon.create_starting_positions())
        # for car in cars:
        #     print(car.position)

        simon.avoid_collision()
        counter -= 1





if __name__ == "__main__":
    main()
