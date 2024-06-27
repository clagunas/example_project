import functions
from classes import Animal
import argparse
import random


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Example of a project - Advanced Python bootcamp"
    )
    parser.add_argument(
        "--species", type=str, default="Dog", help="Species for the class Animal"
    )
    parser.add_argument("--age", type=float, default=3.0, help="Age of the Animal")
    parser.add_argument(
        "--n_list", type=int, default=4, help="Number of values in a random list"
    )
    args = parser.parse_args()

    print("Running the main code...")

    print(f"Creating your {args.species} object...")
    animal = Animal(args.species, args.age)
    animal.description()

    print("Creating a random list of values...")
    randomlist = random.sample(range(0, 30), args.n_list)
    print(
        f"The median of a random list of {len(randomlist)} elements is {functions.calculate_median(randomlist)}"
    )
