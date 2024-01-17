"""This file tests the BMI calculator program using PyTest.

Run "pytest" in this folder to automatically run these tests.

Expected output:
    36 passed in 0.xx seconds

References:
    * https://realpython.com/python-testing/
    * http://docs.pytest.org/en/latest/getting-started.html
    * https://stackoverflow.com/questions/66652450/catch-systemexit-message-with-pytest
    * Cory Lassila: my friend and fellow programmer


"""
import pytest
import bmi_calculator


def test_get_feet_returns_valid_input():
    input_values = ['5.5']

    def input(prompt=None):
        return input_values.pop(0)

    bmi_calculator.input = input
    assert bmi_calculator.get_feet() == 5.5


def test_get_inches_returns_valid_input():
    input_values = ['5.5']

    def input(prompt=None):
        return input_values.pop(0)

    bmi_calculator.input = input
    assert bmi_calculator.get_inches() == 5.5


def test_get_pounds_returns_valid_input():
    input_values = ['155.5']

    def input(prompt=None):
        return input_values.pop(0)

    bmi_calculator.input = input
    assert bmi_calculator.get_pounds() == 155.5


def test_get_feet_ignores_invalid_input():
    input_values = ['-1', "n", 5]

    def input(prompt=None):
        return input_values.pop(0)

    bmi_calculator.input = input
    assert bmi_calculator.get_feet() == 5


def test_get_feet_ignores_string_input():
    input_values = ['five', "n", 5]

    def input(prompt=None):
        return input_values.pop(0)

    bmi_calculator.input = input
    assert bmi_calculator.get_feet() == 5


def test_get_inches_ignores_string_input():
    input_values = ['five', "n", 5]

    def input(prompt=None):
        return input_values.pop(0)

    bmi_calculator.input = input
    assert bmi_calculator.get_inches() == 5


def test_get_pounds_ignores_string_input():
    input_values = ['one hundred', "n", 100]

    def input(prompt=None):
        return input_values.pop(0)

    bmi_calculator.input = input
    assert bmi_calculator.get_pounds() == 100


def test_get_inches_ignores_invalid_input():
    input_values = ['-1', "n", 5]

    def input(prompt=None):
        return input_values.pop(0)

    bmi_calculator.input = input
    assert bmi_calculator.get_inches() == 5


def test_get_pounds_ignores_invalid_input():
    input_values = ['-1', "n", 5]

    def input(prompt=None):
        return input_values.pop(0)

    bmi_calculator.input = input
    assert bmi_calculator.get_pounds() == 5


def test_calculate_height_raises_value_error_on_non_numeric_value():
    with pytest.raises(ValueError):
        bmi_calculator.calculate_height(float("X"), 1)


def test_calculate_height_raises_value_error_below_zero():
    with pytest.raises(ValueError):
        bmi_calculator.calculate_height(-1.0, -1.0)


def test_calculate_height_returns_accurate():
    assert bmi_calculator.calculate_height(5, 9) == 69
    assert bmi_calculator.calculate_height(4, 9.5) == 57.5
    assert bmi_calculator.calculate_height(6, 4.7) == 76.7
    assert round(bmi_calculator.calculate_height(6.0, 6.6), 1) == 78.6


def test_calculate_squared_height_raises_value_error_on_non_numeric_value():
    with pytest.raises(ValueError):
        bmi_calculator.calculate_squared_height(float("X"), 1)


def test_calculate_squared_height_raises_value_error_below_zero():
    with pytest.raises(ValueError):
        bmi_calculator.calculate_squared_height(-1.0)


def test_calculate_squared_height_returns_accurate():
    assert bmi_calculator.calculate_squared_height(69) == 4761
    assert bmi_calculator.calculate_squared_height(57.5) == 3306.25
    assert bmi_calculator.calculate_squared_height(76.7) == 5882.89
    assert round(bmi_calculator.calculate_squared_height(78.6), 1) == 6178.0


def test_calculate_bmi_raises_value_error_on_non_numeric_value():
    with pytest.raises(ValueError):
        bmi_calculator.calculate_bmi(float("X"), 1)


def test_calculate_bmi_raises_value_error_below_zero():
    with pytest.raises(ValueError):
        bmi_calculator.calculate_bmi(-1.0, -1.0)


def test_calculate_bmi_returns_accurate():
    assert bmi_calculator.calculate_bmi(4900, 174) == 25
    assert bmi_calculator.calculate_bmi(5776, 287) == 34.9
    assert bmi_calculator.calculate_bmi(3364, 96) == 20.1
    assert round(bmi_calculator.calculate_bmi(3422.25, 96.7), 1) == 19.9


def test_display_results_raises_assertion_error():
    with pytest.raises(AssertionError):
        bmi_calculator.display_results("X")


def test_display_results_displays_results(capsys):
    bmi_calculator.display_results(20)
    captured = capsys.readouterr()
    assert "\n" + "Your BMI is 20." + "\n" in captured.out


def test_get_inches_exits_from_negative_input():
    input_values = ['-1', "y"]

    def input(prompt=None):
        return input_values.pop(0)

    with pytest.raises(SystemExit):
        bmi_calculator.input = input
        bmi_calculator.get_inches()


def test_get_feet_exits_from_negative_input():
    input_values = ['-1', "y"]

    def input(prompt=None):
        return input_values.pop(0)

    with pytest.raises(SystemExit):
        bmi_calculator.input = input
        bmi_calculator.get_feet()


def test_get_pounds_exits_from_negative_input():
    input_values = ['-1', "y"]

    def input(prompt=None):
        return input_values.pop(0)

    with pytest.raises(SystemExit):
        bmi_calculator.input = input
        bmi_calculator.get_pounds()


def test_create_table_output(capsys):
    bmi_calculator.create_table()
    captured = capsys.readouterr()
    assert "Sample BMI Chart" in captured.out
    assert "58 in\t60 in\t62 in\t64 in\t66 in\t68 in" in captured.out
    assert "250 lb\t52.2\t48.8\t45.7\t42.9\t40.3\t38.0\t35.9" in captured.out


def test_get_feet_exits_from_string_input():
    input_values = ['five', "y"]

    def input(prompt=None):
        return input_values.pop(0)

    with pytest.raises(SystemExit):
        bmi_calculator.input = input
        bmi_calculator.get_feet()


def test_get_inches_exits_from_invalid_input():
    input_values = ['five', "y"]

    def input(prompt=None):
        return input_values.pop(0)

    with pytest.raises(SystemExit):
        bmi_calculator.input = input
        bmi_calculator.get_inches()


def test_get_pounds_exits_from_invalid_input():
    input_values = ['one hundred', "y"]

    def input(prompt=None):
        return input_values.pop(0)

    with pytest.raises(SystemExit):
        bmi_calculator.input = input
        bmi_calculator.get_pounds()


def test_calculate_height_feet_value_error_float():
    with pytest.raises(ValueError):
        bmi_calculator.calculate_height("X", 1)


def test_calculate_height_inches_value_error_float():
    with pytest.raises(ValueError):
        bmi_calculator.calculate_height(1, "X")


def test_calculate_height_feet_value_error_negative():
    with pytest.raises(ValueError):
        bmi_calculator.calculate_height(-1, 5)


def test_calculate_height_inches_value_error_negative():
    with pytest.raises(ValueError):
        bmi_calculator.calculate_height(5, -1)


def test_calculate_squared_height_total_height_value_error_string():
    with pytest.raises(ValueError):
        bmi_calculator.calculate_squared_height("X")


def test_calculate_squared_height_total_height_value_error_negative():
    with pytest.raises(ValueError):
        bmi_calculator.calculate_squared_height(-1)


def test_calculate_bmi_weight_pounds_value_error_string():
    with pytest.raises(ValueError):
        bmi_calculator.calculate_bmi(50, "X")


def test_calculate_bmi_squared_height_value_error_string():
    with pytest.raises(ValueError):
        bmi_calculator.calculate_bmi("X", 50)


def test_calculate_bmi_squared_height_value_error_negative():
    with pytest.raises(ValueError):
        bmi_calculator.calculate_bmi(-50, 50)
