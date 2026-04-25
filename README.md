# CLI Calculator

Simple command-line calculator written in Python.

## Features

- Basic operations:
  - addition
  - subtraction
  - multiplication
  - division
- Input validation
- Division by zero handling
- Calculation history

## How it works

The user selects an operation from the menu and enters two numbers.
The program performs the calculation and displays the result.

All calculations are stored and can be displayed using the history option.

## Example
````
=== CLI Calculator ===
1. Add
2. Subtract
3. Multiply
4. Divide
5. Show history
6. Exit
Choose an option: 3
Enter first number: 4
Enter second number: 5
Result: 20.0
````

## Technologies

- Python 3
- Standard library

## Project structure
```
cli-calculator/
├── main.py
├── calculator.py
├── README.md
├── .gitignore
```
## How to run
````
python main.py
````

## Notes

This project demonstrates:
- clean code structure
- separation of logic and interface
- basic error handling
- working with program state
