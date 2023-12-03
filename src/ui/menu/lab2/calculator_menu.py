"""Module for implementing a simple calculator menu."""
from src.service.lab2.calculator_service import CalculatorService


class CalculatorMenu:
    """A simple calculator menu class."""

    def run(self):
        """Run the calculator program."""
        calculator_service = CalculatorService()

        while True:
            try:
                self.display_menu()
                choice = input("Enter your choice: ")

                if choice == '1':
                    calculator_service.input_values()
                    print(f"The result is {calculator_service.calculate()}")
                elif choice == '2':
                    break
                else:
                    print("Invalid choice. Please try again.")

            except ValueError as ve:
                print(f"Invalid input: {ve}")

    def display_menu(self):
        """Display the calculator menu."""
        print("1. Perform calculation")
        print("2. Exit")
