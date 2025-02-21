import sys


class CustomError(Exception):
    def __init__(self, message):
        super().__init__(message)


class CoinTowerTopple:
    """
    Implements the logic for the Coin Tower Topple game, including:
    - menu navigation and user input validation
    - main game-play logic

    Use the start() method to launch the app
    """

    DIFFICULTY_DESCRIPTION_MAP = {1: "Easy", 2: "Medium", 3: "Hard"}

    def __init__(self):
        """
        Initializes the CoinTowerTopple game with default settings.

        Defines:
        - default game settings: difficulty, topple height, possible actions
        - Main Menu options: option IDs, descriptions and callback methods
        """
        # Game settings
        self.difficulty_level = 1  # Key for DIFFICULTY_DESCRIPTION_MAP
        self.topple_height = 21  # Number of coins that causes tower to topple
        self.possible_actions = [1, 2, 3]  # Number of coins that can be added

        # Main Menu options:
        # Key: option ID (user input)
        # Value: [description, callback methods]
        self.main_options = {
            1: ["Play Game", self._play],
            2: ["Change Game Settings", self._change_settings],
            3: ["Show Game Rules", self._show_rules],
            4: ["Quit", self._quit],
        }

    def start(self):
        """
        Launches the app.

        Displays the game title and default game settings before starting the
        Main Menu loop.
        """
        print("\n\n#### COIN TOWER TOPPLE ####\n")
        print(self._get_settings_str())
        self._run_main_menu()

    def _get_settings_str(self):
        """
        Returns a formatted string of the current game settings.
        """
        settings_str = (
            "GAME SETTINGS\n"
            f"{'- Difficulty: ':<20} "
            f"{self.DIFFICULTY_DESCRIPTION_MAP[self.difficulty_level]}\n"
            f"{'- Topple Height: ':<20} {self.topple_height}\n"
            f"{'- Possible Actions: ':<20} "
            f"{', '.join(map(str, self.possible_actions))}"
        )
        return settings_str

    def _run_main_menu(self):
        print(self._get_main_menu_str())
        prompt = (
            f"Choose option (1 to {len(self.main_options)}): "
        )

        while True:
            try:
                # Display options and get user response
                response = int(input(prompt))

                # Call relevant function
                self.main_options[response][1]()

            except (KeyError, ValueError):
                print(
                    "- INVALID ENTRY: "
                    "must be a number between 1 and "
                    f"{len(self.main_options)}\n"
                )

    def _get_main_menu_str(self):
        main_options_str = "\nMAIN MENU\n"
        for key, (description, _) in self.main_options.items():
            main_options_str += f"{key}. {description}\n"
        return main_options_str

    def _get_rules_str(self):
        """
        Returns the game rules as a formatted multiline string.
        """
        rules_str = """
RULES OF THE GAME

Players take turns to add to a tower of coins until the tower 'topples'.
This happens when the number of coins in the tower is greater than or equal
to the 'topple height'.

  1. The game starts with 1 coin in the tower.
     The player to take the first move is chosen at random.

  2. On their turn, each player chooses how many coins to add to the tower.
     They must choose from a predefined set of numbers (e.g. 1, 3 or 4).

  3. A player wins the game if they force their opponent to topple the tower.

"""
        return rules_str

    def _play(self):
        print("PLAY THE GAME")

    def _get_valid_int(self, prompt, min, max):
        """
        Repeatedly prompts the user for an integer input until a valid
        response is provided.

        Ensures that the input is a number within the specified range
        [min, max]. Displays an error message for invalid entries.
        """
        while True:
            try:
                response = int(input(prompt))
                if min <= response <= max:
                    return response
                raise ValueError
            except ValueError:
                print(
                    "- INVALID ENTRY: "
                    f"number must be between {min} and {max}\n")

    def _get_valid_int_list(self, prompt, min, max):
        """
        Repeatedly prompts the user for a comma-separated list of integers
        until a valid list is provided.

        Ensures that the input:
        - Contains at least two numbers.
        - Consists only of unique integers.
        - Falls within the specified range [min, max].

        Returns a sorted list (low to high)
        """
        while True:
            try:
                response = input(prompt)
                nums = response.split(",")

                # Check enough items in list
                if len(nums) < 2:
                    raise CustomError(
                        "- INVALID ENTRY: "
                        "list must contain at least 2 numbers\n"
                    )

                # Convert to integers (or raise error)
                nums = [int(item) for item in nums]

                # Check numbers are unique
                if len(nums) != len(set(nums)):
                    raise CustomError(
                        "- INVALID ENTRY: "
                        "list must not contain duplicates\n"
                    )

                # Sort nums and check within range
                nums.sort()
                if nums[0] < min or nums[-1] > max:
                    raise CustomError(
                        "- INVALID ENTRY: "
                        f"all numbers must be between {min} and {max}\n"
                    )

            except CustomError as e:
                print(f"{e}")
            except ValueError:
                print(
                    "- INVALID ENTRY: "
                    "at least one list item was not an integer\n"
                )
            else:
                return nums

    def _change_settings(self):
        """
        Allows the user to modify the game settings by prompting for the 
        difficulty level, topple height, and possible actions.

        If all inputs are valid, the updated configuration is displayed 
        before returning to the main menu.
        """

        # Show introductory message
        print(
            "-----------------------------------------------------------\n"
            "------------------ CHANGE GAME SETTINGS -------------------\n"
            "-----------------------------------------------------------\n"
            "Difficulty Options\n"
            "1. Easy\n"
            "2. Medium\n"
            "3. Hard\n"
        )

        # Choose difficulty
        prompt = "Choose difficulty option (1, 2 or 3): "
        self.difficulty_level = self._get_valid_int(prompt, 1, 3)
        print("- OK\n")
        print("-----------------------------------------------------------\n")

        # Choose topple height
        prompt = "Specify the Topple Height (between 10 and 100): "
        self.topple_height = self._get_valid_int(prompt, 10, 100)
        print("- OK\n")
        print("-----------------------------------------------------------\n")

        # Write possible actions (list of numbers)
        print(
            "State the possible actions\n"
            "i.e. how many coins may be added to the tower on each turn\n")
        prompt = "Write a comma separated list of numbers (e.g. '1,3,4'): "
        self.possible_actions = self._get_valid_int_list(
            prompt, 1, self.topple_height
        )
        print("- OK\n")
        print("-----------------------------------------------------------\n")

        # Write new settings
        print(f"{self._get_settings_str()}\n")
        input("Press Enter to return to main menu\n")
        print(self._get_main_menu_str())

    def _show_rules(self):
        """
        Retrieves and displays the game rules, then waits for user confirmation
        before returning to the main menu.
        """
        print(self._get_rules_str())
        input("Press Enter to return to main menu\n")
        print(self._get_main_menu_str())

    def _quit(self):
        """
        Exits the game by displaying a farewell message and terminating
        the program.
        """
        print("\nThanks for playing!\nSee you next time.\n")
        sys.exit(0)
