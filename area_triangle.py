#!/usr/bin/env python3

# Created by Jenoe Balote
# Created on May 2021
# This program calculates the area of a triangle

def calculate_area(num_base, num_height):
    # process & output

    area = (num_base * num_height) / 2
    print("\nThe area is {}cm².".format(area))


def main():
    # this function calls other functions
    # input

    print("Let's calculate the area of a triangle!")
    print("")
    string_base = str(input("Enter base (cm): "))
    string_height = str(input("Enter height (cm): "))

    # call function and output
    try:
        num_base = int(string_base)
        num_height = int(string_height)
        calculate_area(num_base, num_height)
    except Exception:
        print("\nInvalid.")
    finally:
        print("\nThanks for participating!")


if __name__ == "__main__":
    main()
