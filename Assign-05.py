#!/usr/bin/env python3
# Created by: Tomi o
# Created on: Nov 1, 2022
# This program calculates the user energy
def calc_time(power, work):
    time = power / work
    return time


def calc_power(time, work):
    power = work / time
    return power


def calc_work(time, power):
    work = time * power
    return work


def main():
    # displays opening message to user.
    print("Welcome to the Energy calculator.")
    # uses loop to ask user if they want to continue or
    # end at the beginning and end of the question
    while True:
        # Asks user if they want to continue at
        # the beginning and the end.
        print("")
        print("Do you wish to continue?")
        # asks user to input Y for yes and N for no
        # caps only
        ask_user_continue = input("Enter (Y) for yes or (N) for no: ")
        try:
            # checks to make sure that user input is a string
            ask_cont = str(ask_user_continue)
            # checks to see if user input is a capital Y
            # if it is capital Y then it
            # continues to the rest of the code
            if ask_cont == "Y":
                print("This calculator solves for either", end="")
                print("work, power or time.")
                print("Enter w to calculate for work,", end="")
                print(" p to calculate for power and,", end="")
                print(" t to calculate time.")
            # checks to see if user input is a capital N
            # if it is capital N then it prints
            # the message and ends the program
            elif ask_cont == "N":
                print("Thanks for using the energy calculator")
                break
            # if it neither then it displays the
            # message ans loops back to get user input
            else:
                print("Invalid input, you can only enter (Y) or (N),", end="")
                print(" Capital only")
                print("")
                continue
        # if it not a string then it tells user it is an invalid input
        # and loops back to get user input
        except Exception:
            print("{0} is an invalid input".format(ask_user_continue))
            continue
        while True:
            Ask_user = input("Enter what you would like to calculate: ")
            # checks to see if user input is w or not.
            if Ask_user == "w":
                # tells user what the chose
                print("You chose work.")
                print("")
                # asks user for time and power
                power_input = input("Enter the power: ")
                time_input = input("Enter the time: ")
                try:
                    # converts power_input from string to float
                    power_user = float(power_input)
                    try:
                        # converts time_input string to float
                        time_user = float(time_input)
                        # makes sure user number is bigger than zero
                        if power_user < 0 / time_user < 0:
                            print("Your input is lower than 0")
                            continue
                        else:
                            # calls the functions and displays it to user
                            work_user = calc_work(power_user, time_user)
                            print("")
                            print(
                                "The total work is equal to {:.2f} Joules".format(
                                    work_user
                                )
                            )
                            break
                    except Exception:
                        print("{0} is not a valid number.".format(time_input))
                        break
                except Exception:
                    print("{0} is not a valid number.".format(power_input))
                    break
            # if user input is p then continue with this part of the code
            elif Ask_user == "p":
                print("You chose power.")
                print("")
                # Ask user to enter time and work
                time_input = input("Enter the time: ")
                work_input = input("Enter the work: ")
                try:
                    # change time_input to a float
                    time_user = float(time_input)
                    try:
                        # change work_user to a float
                        work_user = float(work_input)
                        # makes sure user input isn't lower than 0
                        if work_user < 0 or time_user < 0:
                            print("Your input is lower than 0")
                            continue
                        # calls the the power function
                        power_user = calc_power(time_user, work_user)
                        print("")
                        print("The power is equal to {:.2f} Watts".format(power_user))
                        break
                    except Exception:
                        print("{0} is not a valid number.".format(work_input))
                        break
                except Exception:
                    print("{0} is not a valid number.".format(time_input))
                    break
            # if user input is t then continue with this part of the code
            elif Ask_user == "t":
                # display what user chose to user
                print("You chose time.")
                print("")
                # Ask user to input power and work
                power_input = input("Enter the power: ")
                work_input = input("Enter the work: ")
                try:
                    # changes power_input to a float
                    power_user = float(power_input)
                    try:
                        # changes work_input to a float
                        work_user = float(work_input)
                        # makes sure user input isn't lower than 0
                        if power_user < 0 / work_user < 0:
                            print("Your input is lower than 0")
                            continue
                        # calls time and displays the calculation
                        time_user = calc_time(power_user, work_user)
                        print("")
                        print(
                            "The total time is equivalent to {:.2f} seconds".format(
                                time_user
                            )
                        )
                        break
                    except Exception:
                        print("{0} is not a valid number.".format(work_input))
                        break
                except Exception:
                    print("{0} is not a valid number.".format(power_input))
                    break
            # if user input isn't p, w or t
            # then display to user
            else:
                print("You can't solve for {0}".format(Ask_user))
                continue


if __name__ == "__main__":
    main()
