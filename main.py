from sim import *

def main():
    counter = 60
    simon = Sim()
    all_positions = []
    cars = simon.create_cars(simon.create_starting_positions())
    while counter > 0:
        for car in cars:
            all_positions.append(car.position)
        simon.avoid_collision()
        counter -= 1

    print(all_positions)



if __name__ == "__main__":
    main()
