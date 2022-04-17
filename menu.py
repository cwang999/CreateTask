main_menu = [
    ["Option 1", n],
    ["Option 2", s],
    # ["Loopy", loopy.main],
]

# Submenu list of [Prompt, Action]
# Works similarly to main_menu
math_sub_menu = [
    ["Dictionaries", infodb.tester],
    ["Factorials", Factorial.tester],
    ["Fibonacci", fibonacci.fib_tester],
]

patterns_sub_menu = [
    ["Christmas", christmas],
    ["Titanic", ship],
    ["Keypad", keypad.driver],
    ["Swap", swap.driver],
]

# week2_sub_menu = [["Factorials using __call__", Factorial_with_call.driver],
#                   ["Cube Root using Imperative and OOP", CubeRoot.driver]]

# Menu banner is typically defined by menu owner
border = "=" * 25
banner = f"\n{border}\nPlease Select An Option\n{border}"


# def menu
# using main_menu list:
# 1. main menu and submenu reference are created [Prompts, Actions]
# 2. menu_list is sent as parameter to menuy.menu function that has logic for menu control
def menu():
    title = "Function Menu" + banner
    menu_list = main_menu.copy()
    menu_list.append(["Patterns", patterns_submenu])
    menu_list.append(["Math and Databases", databases_submenu])
#     menu_list.append(["Week 2", week2_submenu])
    buildMenu(title, menu_list)


# def submenu
# using sub menu list above:
# sub_menu works similarly to menu()
def patterns_submenu():
    title = "Patterns" + banner
    buildMenu(title, patterns_sub_menu)


def databases_submenu():
    title = "Math and Databases" + banner
    buildMenu(title, math_sub_menu)


# def week2_submenu():
#     title = "Week 2 Deliverables" + banner
#     buildMenu(title, week2_sub_menu)


def buildMenu(banner, options):
    # header for menu
    print(banner)
    # build a dictionary from options
    prompts = {0: ["Exit", None]}
    for op in options:
        index = len(prompts)
        prompts[index] = op

    # print menu or dictionary
    for key, value in prompts.items():
        print(key, '->', value[0])

    # get user choice
    choice = input("Type your choice ==[ ")

    # validate choice and run
    # execute selection
    # convert to number
    try:
        choice = int(choice)
        if choice == 0:
            # stop
            return
        try:
            # try as function
            action = prompts.get(choice)[1]
            action()
        except TypeError:
            try:  # try as playground style
                exec(open(action).read())
            except FileNotFoundError:
                print(f"File not found!: {action}")
            # end function try
        # end prompts try
    except ValueError:
        # not a number error
        print(f"Not a number: {choice}")
    except UnboundLocalError:
        # traps all other errors
        print(f"Invalid choice: {choice}")
    # end validation try

    buildMenu(banner, options)  # recursion, start menu over again


if __name__ == "__main__":
    menu()