"""This program asks users for their weight in pounds and their height
in feet and inches and then calculates and displays their BMI

Input:
    User's height in feet
    User's remaining height in inches
    User's weight in pounds

Output:
    User's Body Mass Index (BMI)

References:
    * https://en.wikipedia.org/wiki/Body_mass_index
    * https://blog.excelstrategiesllc.com/2019/01/30/coding-a-bmi-calculator-in-python/
    * https://www.cdc.gov/healthyweight/assessing/bmi/adult_bmi/index.html
    * https://www.geeksforgeeks.org/python-exit-commands-quit-exit-sys-exit-and-os-_exit/
    * https://www.w3schools.com/python/python_ref_exceptions.asp
    * https://www.geeksforgeeks.org/print-lists-in-python-4-different-ways/
Created by Frank Boxenbaum

"""


def get_feet():
    """This function gets the user's inputted height in feet as height_feet

    Args: None

    Returns:
        float: User's height in feet

    Exits:
        ValueError: If user's height in feet is not a valid float.
        ValueError: If user's height in feet is less than 0.
        SystemExit: If the user chooses to exit by typing 'y'.

    """
    while True:
        print("Please enter your height in feet without inches")
        height_feet = input()
        try:
            height_feet = float(height_feet)
            if height_feet < 0:
                print("Invalid height, height in feet must be greater than 0")
                print("Would you like to exit? y/n")
                user_exit = input()
                user_exit = str(user_exit)
                if user_exit == 'y':
                    exit()
            else:
                return height_feet

        except ValueError:
            print(f"ValueError:{height_feet} is invalid.")
            print("Your height in feet must be a valid number")
            height_feet = str(height_feet)
            print("Would you like to exit? y/n")
            user_exit = input()
            user_exit = str(user_exit)
            if user_exit == 'y':
                exit()
            else:
                print("Your height in feet must be a valid number")


def get_inches():
    """This function gets the user's remaining inputted height in inches
    as height_inches

    Args: None

    Returns:
        float: User's remaining height in inches

    Exits:
        ValueError: If user's remaining height in inches is not a valid float.
        ValueError: If user's remaining height in inches is less than 0.
        SystemExit: If the user chooses to exit by typing 'y'.

    """
    while True:
        print("Please enter your remaining height in inches")
        height_inches = input()
        try:
            height_inches = float(height_inches)
            if height_inches < 0:
                print("Invalid input, height in inches must be greater than 0")
                print("Would you like to exit? y/n")
                user_exit_in = input()
                user_exit_in = str(user_exit_in)
                if user_exit_in == 'y':
                    exit()
            else:
                return height_inches

        except ValueError:
            print(f"ValueError:{height_inches} is invalid.")
            print("Your remaining height in inches must be a valid number")
            height_inches = str(height_inches)
            print("Would you like to exit? y/n")
            user_exit_in = input()
            user_exit_in = str(user_exit_in)
            if user_exit_in == 'y':
                exit()
            else:
                print("Your remaining height in inches must be a valid number")


def get_pounds():
    """This function gets the user's inputted weight in pounds
    as weight_pounds

    Args: None

    Returns:
        float: User's weight in pounds

    Exits:
        ValueError: If user's weight in pounds is not a valid float.
        ValueError: If user's weight in pounds is less than 0.
        SystemExit: If the user chooses to exit by typing 'y'.

    """
    while True:
        print("Please enter your weight in pounds")
        weight_pounds = input()
        try:
            weight_pounds = float(weight_pounds)
            if weight_pounds < 0:
                print("Invalid input, weight in pounds must be greater than 0")
                print("Would you like to exit? y/n")
                user_exit_lb = input()
                user_exit_lb = str(user_exit_lb)
                if user_exit_lb == 'y':
                    exit()
            else:
                return weight_pounds

        except ValueError:
            print(f"ValueError:{weight_pounds} is invalid.")
            print("Your weight in pounds must be a valid number")
            weight_pounds = str(weight_pounds)
            print("Would you like to exit? y/n")
            user_exit_lb = input()
            user_exit_lb = str(user_exit_lb)
            if user_exit_lb == 'y':
                exit()
            else:
                print("Your weight in pounds must be a valid number")


def calculate_height(height_feet, height_inches):
    """This function converts the user's total height to inches
    as total_height using height_feet and height_inches

    Args:
        height_feet (float): User's height in feet
        height_inches (float): User's remaining height in inches

    Returns:
        float: User's total height in inches

    Exits:
        ValueError: If user's total height in inches is not a valid float.
        ValueError: If user's total height in inches is less than 0.
        ValueError: If user's total height in feet is not a valid float.
        ValueError: If user's total height in feet is less than 0.

    """
    try:
        height_feet = float(height_feet)
    except ValueError:
        raise ValueError(f"Input must be float. Received '{height_feet}'")

    if height_feet < 0:
        raise ValueError(f"Input must be >=  0. Received '{height_feet}'")

    try:
        height_inches = float(height_inches)
    except ValueError:
        raise ValueError(f"Input must be float. Received '{height_inches}'")

    if height_inches < 0:
        raise ValueError(f"Input must be >=  0. Received '{height_inches}'")

    total_height = height_feet * 12 + height_inches
    total_height = float(total_height)

    return total_height


def calculate_squared_height(total_height):
    """This function squares the total height for the BMI calculation
    as squared_height using total_height

    Args:
        total_height (float): User's total height in inches

    Returns:
        float: User's height in inches squared for calculating BMI

    Raises:
        ValueError: If user's total height in inches is not a float.
        ValueError: If user's total height in inches is less than 0.

    """
    try:
        total_height = float(total_height)
    except ValueError:
        raise ValueError(f"Input must be float. Received '{total_height}'")

    if total_height < 0:
        raise ValueError(f"Input must be >= 0. Received '{total_height}'")

    squared_height = float(total_height * total_height)

    return squared_height


def calculate_bmi(squared_height, weight_pounds):
    """This function calculates the users BMI from their inputted information
    as user_bmi using squared_height and weight_pounds

    Args:
        squared_height (float): User's height in inches squared
        weight_pounds (float): User's weight in pounds

    Returns:
        float: User's BMI based on their height and weight

    Raises:
        ValueError: If user's weight in pounds is not a float.
        ValueError: If user's weight in pounds is less than 0.
        ValueError: If user's height in inches squared is less than 0.
        ValueError: If user's height in inches squared is not a valid float.

    """
    try:
        weight_pounds = float(weight_pounds)
    except ValueError:
        raise ValueError(f"Weight must be a float. Received '{weight_pounds}'")

    if weight_pounds < 0:
        raise ValueError(f"Weight must be >= 0. Received '{weight_pounds}'")

    try:
        squared_height = float(squared_height)
    except ValueError:
        raise ValueError(f"Input must be a float. Received '{squared_height}'")

    if squared_height < 0:
        raise ValueError(f"Input must be >= 0. Received '{squared_height}'")

    user_bmi = round((weight_pounds / squared_height) * 703, 1)

    return user_bmi


def create_table():
    """This function displays a sample BMI table using height_table as
    sample heights and weight_table as sample weights

    Args: None
`
    Returns: None

    Exits:
        Exception: Invalid data passed.

    """
    try:
        height_table = []
        for heights in range(58, 78, 2):
            height_table.append(heights)
        pass
        weight_table = []
        for weights in range(100, 260, 10):
            weight_table.append(weights)
        pass
        print("\n" + "Sample BMI Chart" + "\n")
        print("", end="\t")
        for heights in height_table:
            print(str(heights) + " in", end="\t")
        pass
        print("\n")
        for weights in weight_table:
            print(str(weights) + " lb", end="\t")
            for heights in height_table:
                sample_square_height = calculate_squared_height(heights)
                sample_bmi = calculate_bmi(sample_square_height, weights)
                print(sample_bmi, end="\t")
            pass
            print("")
    except:  # pragma: no cover
        print("Unexpected error.")
        exit()


def display_results(user_bmi):
    """This function displays the calculated BMI using user_bmi
    and a BMI reference scale

    Args:
        user_bmi (float): User's BMI based on their height and weight

    Returns: None

    Raises:
        AssertionError: If User's BMI is not a valid float

    """
    assert isinstance(user_bmi, float) or isinstance(user_bmi, int), \
        "User BMI must be a float. Received {type(user_bmi)}"
    print("\n" + "Your BMI is " + str(user_bmi) + "." + "\n")
    print("A BMI below 18.5 is underweight.")
    print("A BMI of 18.5 - 24.9 is within a normal weight range.")
    print("A BMI of 25 - 29.9 is overweight.")
    print("A BMI of 30 or higher is obese.")


def main():  # pragma: no cover
    """This function executes all functions in the program.

    Args: None

    Returns: None

    Exits:
        SystemExit: If user chooses to exit from input selection.
        Exception: Invalid data passed.

    """
    while True:
        try:
            height_feet = get_feet()
            height_inches = get_inches()
            weight_pounds = get_pounds()
            total_height = calculate_height(height_feet, height_inches)
            squared_height = calculate_squared_height(total_height)
            user_bmi = calculate_bmi(squared_height, weight_pounds)
            display_results(user_bmi)
            create_table()
            print("\n" + "Would you like to continue or exit? c/e")
            user_continue = input()
            user_continue = str(user_continue)
            if user_continue == 'e':
                break
            else:
                pass

        except SystemExit:
            exit()
        except:
            print("Unexpected error.")
            exit()


if __name__ == "__main__":  # pragma: no cover
    main()
