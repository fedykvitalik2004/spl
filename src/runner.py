"""
Module: runner

A module for initializing and running various lab menu objects.

Classes:
- Runner: A class for managing and running different lab menus.
"""
from src.config import logger
from src.ui.menu.lab2.calculator_menu import CalculatorMenu
from src.ui.menu.lab3.ascii_art_generator_menu import AsciiArtGeneratorMenu
from src.ui.menu.lab4.own_ascii_art_generator import OwnAsciiArtGeneratorMenu
from src.ui.menu.lab5.figures import FigureMenu
from src.ui.menu.lab7.user_menu import UserMenu
from src.ui.menu.lab8.diagrams_menu import DiagramMenu


class Runner:
    """
    Class for initializing and running various lab menu objects.

    Attributes:
    - __calculator: Instance of CalculatorMenu.
    - __ascii_art_generator: Instance of AsciiArtGeneratorMenu.
    - __own_ascii_art_generator: Instance of OwnAsciiArtGeneratorMenu.
    - __figure: Instance of FigureMenu.
    - __user_menu: Instance of UserMenu.
    - __diagram_menu: Instance of DiagramMenu.
    """

    def __init__(self):
        """Initialize the Runner with different lab menu objects."""
        self.__calculator = CalculatorMenu()
        self.__ascii_art_generator = AsciiArtGeneratorMenu()
        self.__own_ascii_art_generator = OwnAsciiArtGeneratorMenu()
        self.__figure = FigureMenu()
        self.__user_menu = UserMenu()
        self.__diagram_menu = DiagramMenu()

    def run(self):
        """Run the main menu."""
        print("Welcome to the main menu!")
        while True:
            try:
                print("Please, choose the lab you would like to run")
                print("1. Lab 2")
                print("2. Lab 3")
                print("3. Lab 4")
                print("4. Lab 5")
                print("5. Lab 7")
                print("6. Lab 8")
                print("7. Exit")
                choice = int(input("Your choice is "))
                if choice == 1:
                    self.__calculator.run()
                elif choice == 2:
                    self.__ascii_art_generator.run()
                elif choice == 3:
                    self.__own_ascii_art_generator.run()
                elif choice == 4:
                    self.__figure.run()
                elif choice == 5:
                    self.__user_menu.run()
                elif choice == 6:
                    self.__diagram_menu.run()
                elif choice == 7:
                    break
                else:
                    logger.error("The number is not defined in the list")
                    print("Wrong input! Please, try again")
            except ValueError:
                logger.error("The input is not a number")
                print("Wrong input! Please, try again")


if __name__ == '__main__':
    runner = Runner()
    runner.run()
