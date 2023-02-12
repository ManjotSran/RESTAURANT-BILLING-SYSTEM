import pytest
import io
import sys
from unittest.mock import patch
from project import display_menu
from project import take_order
from project import calculate_bill


def main():
    test_display_menu()
    test_take_order()
    test_calculate_bill()


def test_display_menu():
    menu = {
        'Coffee': 2.5,
        'Tea': 2.0,
        'Vegan Sandwich': 4.5,
        'Cake': 3.5,
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00,
        "Butter Chicken": 12.50,
        "Salmon Curry": 9.77
    }

    expected_result = "Menu:\n"
    for item, price in menu.items():
        expected_result += f"{item}: ${price}\n"

    result = display_menu()
    assert result == expected_result


def test_take_order():
    menu = {
        'Coffee': 2.5,
        'Tea': 2.0,
        'Vegan Sandwich': 4.5,
        'Cake': 3.5,
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00,
        "Butter Chicken": 12.50,
        "Salmon Curry": 9.77
    }
    
    order = []
    
    with patch('builtins.input', side_effect=['Coffee', '2', 'Tea', '3', 'e']):
        take_order(menu, order)
        
    assert order == [('Coffee', 2), ('Tea', 3)]


def test_calculate_bill():
    menu = {
        'Coffee': 2.5,
        'Tea': 2.0,
        'Vegan Sandwich': 4.5,
        'Cake': 3.5,
    }
    order = [('Coffee', 2), ('Tea', 3)]

    result = calculate_bill(menu, order)
    assert result == (2.5 * 2) + (2.0 * 3)


if __name__ == '__main__':
    main()