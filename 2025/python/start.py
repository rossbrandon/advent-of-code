"""
Takes an Advent of Code day number input and creates a new directory with starter files.
"""

import argparse
import os
import shutil


def parse_args():
    parser = argparse.ArgumentParser(description="Start an Advent of Code day.")
    parser.add_argument("day", type=int, help="The day number to create (01-25).")
    return parser.parse_args()


def validate_day(day: int) -> bool:
    if 1 < day <= 25:
        return True
    return False


def create_day_dir(day: int):
    print(f"Creating day-{day} directory...")
    os.makedirs(f"day-{day}", exist_ok=True)


def create_day_files(day: int):
    print(f"Creating day-{day} files...")
    shutil.copy("starter/starter_main.py", f"day-{day}/main.py")
    with open(f"day-{day}/test.txt", "w") as file:
        file.write("")
    with open(f"day-{day}/data.txt", "w") as file:
        file.write("")
    with open(f"day-{day}/README.md", "w") as file:
        file.write(f"# Day {day}\n")


def main():
    args = parse_args()
    if not validate_day(args.day):
        print("Invalid day number. Must be between 01 and 25.")
        return

    day = f"{args.day:02d}"
    print("Welcome back! It's good to learn with you again.")
    if os.path.exists(f"day-{day}"):
        print(f"Day {day} already exists! Do you want to reset it? (y/n)")
        response = input()
        if response == "y":
            shutil.rmtree(f"day-{day}")
        else:
            print("Exiting...")
            return
    print(f"Starting {day}...")
    create_day_dir(day)
    create_day_files(day)
    print("You're all set! Happy coding!")


if __name__ == "__main__":
    main()
