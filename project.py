import pygame
pygame.init()
pygame.mixer.init()
from gtts import gTTS
import os

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

def main():
    print("Welcome to Singh's restaurant 👋")
    mytext = "Welcome to Singh's restaurant, Have a look at the menu and order what you want"
    tts = gTTS(text=mytext, lang="en", slow=False)
    file_name = "voice1.mp3"
    tts.save(file_name)
    pygame.mixer.init()
    pygame.mixer.music.load(file_name)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pass
    print("Have a look at the menu and order what you want 😊")
    print(menu)
    display_menu()
    take_order(menu, order)
    bill = calculate_bill(menu, order)
    print("Total Bill: ${:.2f}".format(bill))
    speak_number(bill)


def display_menu():
    menu_str = "Menu:\n"
    
    for item, price in menu.items():
        menu_str += f"{item}: ${price}\n"
    return menu_str


def take_order(menu, order):
    while True:
        item = input('Enter item name (press e to finish ordering): ').title()
        if item in menu:
            quantity = int(input('Enter quantity: '))
            order.append((item, quantity))
        if item == 'E':
            break
        if item not in menu:
            print(f'{item} not in menu 😥. Please Try again.')
            continue


def calculate_bill(menu, order):
    total = 0
    for item, quantity in order:
        total += menu[item] * quantity
    print("Thank you very much for ordering food from our restaurant. Visit again 🙏")
    return total


def speak_number(bill):
    text = "Your total bill is dollars: " + str(bill) + ". Thank you very much for ordering food from our restaurant. Visit again."
    tts = gTTS(text, lang='en')
    tts.save("number.mp3")
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("number.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    pygame.quit()


if __name__ == '__main__':
    main()