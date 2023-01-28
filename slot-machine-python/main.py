import random

# global constant
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

#  for the machine
ROWS = 3
COLS = 3

# no. of _ in a vertical reel
symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}
symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines

def deposit():
    # will collect the deposit amount from the user.

    # will continuoslly ask the user for the deposit amount until the user enters a valid amount.
    while True:
        amount = input("Enter deposit $ ")
        if amount.isdigit():
            amount = int(amount)

            if amount > 0:          # so that user doesn't enter 0.
                break   
            else:
                print("\n=== Amount must be greater than 0.")
        else:
            print("\n=== Please enter a valid amount.")
    
    print("\n- x - x - x - x - x - x - x - x -\n")
    return amount

def get_number_of_lines():

    while True:
        lines = input(f"Enter the number of lines to bet on? (1-{MAX_LINES}) : ")
        if lines.isdigit():
            lines = int(lines)
            if lines > 0 and lines <= MAX_LINES:
                break
            else:
                print(f"\n=== Number of lines must be between 1 and {MAX_LINES}")
        else:
            print("\n=== Please enter a valid number of lines.")
    
    print("\n- x - x - x - x - x - x - x - x -\n")
    return lines

def get_bet():
    while True:
        amount = input(f"Enter bet amount on each line between({MIN_BET}-{MAX_BET}) : ")
        if amount.isdigit():
            amount = int(amount)

            if amount >= MIN_BET and amount <= MAX_BET:
                break; 
            else:
                print(f"\nPlease enter Bet between ({MIN_BET}-{MAX_BET})")
        else:
            print("\nPlease enter a valid bet Amount")

    print("\n- x - x - x - x - x - x - x - x -\n")
    return amount

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []                        # dict to list
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)      # A will be added to all_symbols 2 times, B will be added 5 times...

    all_columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        
        all_columns.append(column)

    return all_columns

def print_slot_machine(all_columns):
    for row in range(len(all_columns[0])):
        for i, column in enumerate(all_columns):
            if i != len(all_columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="\n")

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You tried to bet ${total_bet} but, Current Balance = ${balance}")
        else:
            break

    # final display for the user
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}.\n")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)

    print_slot_machine(slots)

    winnings, winnings_lines = check_winnings(slots, lines, bet, symbol_value)

    print(f"You won ${winnings}.")
    print(f"You won on lines:", *winnings_lines)

    return winnings - total_bet

# so that we can re-run the program after the user has finished, after asking him if he wants to continue.
def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press Enter to Play (q to quit): ")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You left with ${balance}")

main()
