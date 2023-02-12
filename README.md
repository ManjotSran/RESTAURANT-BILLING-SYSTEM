# RESTAURANT BILLING PROJECT
    #### Video Demo:  <https://youtu.be/_-KDnUxSCg0RE>
    #### Description:
    
    # Project Introduction: 

    This is a restaurant billing program written in Python, designed to make ordering food and calculating the bill quick and easy. It is a command line application that allows customers to order food items from a menu and calculate the final bill. In project.py, the menu is stored as a dictionary in the program, and customers can add items to their order by entering the name of the item and the quantity they want. The take_order function will prompt the users to enter items and their quantity until the users hit "e" from their keyboard. After, "e" is pressed, the program then calculates the total bill amount based on the items and quantities in the order. Additionally, the program uses the gTTS library to produce audio output, welcoming customers as well as for generating an audio message announcing the total bill. The final bill is calculated automatically, ensuring accurate and efficient billing for restaurants.


    # project.py file

    project.py implements a simple restaurant billing system. The menu is defined as a dictionary called "menu" with items as the keys and their prices as the values. An empty list called "order" is also defined to store the items and quantities ordered by the customer.

    The main function starts by printing a welcome message (That says Welcome to singh's restaurant) and using the gTTS library to convert the text to speech, playing the audio file using the mixer module of the pygame library. The menu is then displayed using the display_menu() function and the customer is prompted to make an order using the take_order() function. The bill is calculated using the calculate_bill() function and the total amount is displayed.

    The display_menu() function returns a string representation of the menu items and their prices. The take_order() function repeatedly prompts the user to enter an item name and quantity. If the item name entered is not in the menu, the user is informed and prompted to try again. If the user enters 'E', the ordering process is ended and the user is thanked.

    The calculate_bill() function calculates the total bill by adding up the cost of each item ordered and returns the total amount. The total bill is then displayed to the customer.

    The code uses if name == 'main': to ensure that the main function is only executed when the script is run as a standalone program and not when it is imported as a module.


    # test_project.py file

    The test_project.py defines a series of tests for functions of project.py file. "test_project.py" imports several required modules including pytest, io, sys, and unittest.mock. It also import the three functions from the project.py file, namely the display_menu, take_order, and calculate_bill. The main function calls three test functions: test_display_menu, test_take_order, and test_calculate_bill. The test_display_menu function tests the display_menu function of the project.py file. It first creates a dictionary menu with items and their prices. The function then creates a string expected_result by concatenating each item in the menu, along with its price. Finally, the function calls the display_menu function, and the result is compared to the expected_result. If both match, the test case is considered to be passed.

    The test_take_order function tests the take_order function of the project.py file. The function uses unittest.mock.patch to mock the input function, providing predefined inputs to the take_order function. The take_order function is called with the menu dictionary and an empty list order, and the resulting list order is compared to an expected value.

    The test_calculate_bill function tests the calculate_bill function of the project.py file. The function creates a dictionary menu and a list order with sample values, and then calls the calculate_bill function, passing the menu and order as arguments. The resulting value is then compared to an expected value. The code runs the main function if it is being run as the main program, causing the tests to be executed. Test the text_project.py using the python -m pytest command.


    # voice1.mp3 file

    The project folder also contains an mp3 file named as voice1.mp3 that contains an audio welcoming the customers to the singh's restaurant.
    

    # number.mp3 file

    The project folder also contains an mp3 file named as number.mp3 that contains an audio announcing the total bill as well as an gratitude message.


    # requirements.txt file

    There is also an requirements.txt (text) file that contains the list of pip-installable libraries that my project requires to work efficiently. 