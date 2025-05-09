import sys
import random


class CustomError(Exception):
    """
    Custom exception class for handling specific input validation errors.
    """
    def __init__(self, message):
        super().__init__(message)


class CoinTowerTopple:
    """
    Implements the logic for the Coin Tower Topple game, including:
    - menu navigation and user input validation
    - main game-play logic

    Use the start() method to launch the app
    """

    # Mapping of difficulty levels to their properties:
    # Key: difficulty_level
    # Value: [description, explore_fraction]
    DIFFICULTY_LEVEL_MAP = {
        1: ["Easy", 0.66],
        2: ["Medium", 0.33],
        3: ["Hard", 0]
    }

    # Initialisation and Game Entry
    def __init__(self):
        """
        Initializes the CoinTowerTopple game with default settings.

        Defines:
        - default game settings: difficulty, topple height, possible actions
        - Main Menu options: option IDs, descriptions and callback methods
        """
        # Game settings
        self.difficulty_level = 1  # Key for DIFFICULTY_LEVEL_MAP
        self.topple_height = 21  # Number of coins that causes tower to topple
        self.possible_actions = [1, 2, 3]  # Sorted list of numbers (ascending)

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
        print(self._get_title_str())
        print(self._get_settings_str())
        self._run_main_menu()

    # Main Menu and Callbacks
    def _run_main_menu(self):
        """
        Starts the main menu loop.

        Displays the menu options and prompts the user to select one.
        - If the input is valid, the corresponding method is called
        - If the input is invalid, an error message is displayed and the user
        is prompted again.

        The loop continues until the user chooses the 'Quit' option.
        """
        print(self._get_main_menu_str())
        prompt = (
            f"Choose option (1 to {len(self.main_options)}): "
        )

        while True:
            try:
                # Display options and get user response
                response = int(input(prompt + "\n"))

                # Check response is valid main_options key
                if response not in self.main_options:
                    raise KeyError

            except (KeyError, ValueError):
                print(
                    "- INVALID ENTRY: "
                    "must be a whole number between 1 and "
                    f"{len(self.main_options)}\n"
                )
            else:
                # Call relevant function
                self.main_options[response][1]()

    def _play(self):
        """
        Runs the main game loop to allow a human player to compete against an
        AI opponent.

        The method:
        - Initializes an AI player and trains it using reinforcement learning
        with the current game settings.
        - Displays the 'Play Game' title screen and game settings
        - Determines which player (human or AI) has the first move and starts
        the game.
        - Alternates turns between the human and AI player, updating the tower
        height after each turn
        - Ends the game when the tower height reaches or exceeds the topple
        height and declares the winner.
        - Prompts the user about whether they want to play again. If so,
        starts a new game, otherwise returns to the main menu.
        """

        # Initialise AI with current game settings
        ai = AIPlayer(
            self.difficulty_level,
            self.topple_height,
            self.possible_actions
        )

        # Train AI (to get q_values)
        ai.train(10000)

        # Apply difficulty level setting to AI
        # (by stating probability that it makes a random decision)
        explore_fraction = self.DIFFICULTY_LEVEL_MAP[self.difficulty_level][1]

        # Begin loop for replaying the game
        replay = True
        while replay:
            print(
                "\n\n"
                "=========================== "
                "PLAY GAME "
                "==========================="
                "\n\n"
                f"{self._get_settings_str()}\n\n"
            )

            # Reset tower height and game state
            tower_height = 1
            game_state = -1

            # Choose which player starts - 0: human, 1: computer
            player = random.choice([0, 1])
            print(
                f"{'You' if player == 0 else 'Computer'} "
                "won the toss to take first move ..."
            )

            # Enter game loop
            while game_state < 0:
                # Display current coin count
                print(
                    "\nTower height: "
                    f"{tower_height} "
                    f"{'coin' if tower_height == 1 else 'coins'}"
                )

                # Get action
                if player == 0:  # Human's turn - ask for action and validate
                    add_coins = self._get_valid_action()
                else:  # AI's turn - choose best action
                    add_coins = ai.choose_action(
                        tower_height, explore_fraction
                    )
                    print(
                        f"- The computer chose to add {add_coins} "
                        f"{'coin' if add_coins == 1 else 'coins'}"
                    )

                # Update tower_height and update game_state if required
                tower_height += add_coins
                if tower_height >= self.topple_height:
                    game_state = 0 if player == 1 else 1

                # Switch player
                player = 1 if player == 0 else 0

            # Game End
            print("\nTOWER HAS TOPPLED!\n")

            if game_state == 0:  # Human player won
                print(
                    "====================== "
                    "GAME OVER - YOU WON "
                    "======================\n"
                )
            else:  # Computer won
                print(
                    "==================== "
                    "GAME OVER - COMPUTER WON "
                    "===================\n"
                )

            # Prompt user to play again
            response = self._get_valid_str(
                "Would you like to play again with the same settings?\n"
                "- Enter 'y' for yes or 'n' for no: ",
                ["y", "n"]
            )
            if response != "y":
                replay = False

        print(self._get_main_menu_str())

    def _change_settings(self):
        """
        Allows the user to modify the game settings by prompting for the
        difficulty level, topple height, and possible actions.

        If all inputs are valid, the updated configuration is displayed
        before returning to the main menu.
        """

        # Show introductory message
        print("""

====================== CHANGE GAME SETTINGS =====================

Difficulty Options
1. Easy
2. Medium
3. Hard

""")

        # Choose difficulty
        prompt = "Choose difficulty option (1, 2 or 3): "
        self.difficulty_level = self._get_valid_int(prompt, 1, 3)
        print("- OK\n")
        print(
            "-----------------------------------------------------------------"
            "\n"
        )

        # Choose topple height
        prompt = "Specify the Topple Height (between 10 and 100): "
        self.topple_height = self._get_valid_int(prompt, 10, 100)
        print("- OK\n")
        print(
            "-----------------------------------------------------------------"
            "\n"
        )

        # Write possible actions (list of numbers)
        print(
            "State the possible actions\n"
            "i.e. how many coins may be added to the tower on each turn\n")
        prompt = "Write a comma separated list of numbers (e.g. '1,3,4'): "
        self.possible_actions = self._get_valid_int_list(
            prompt, 1, self.topple_height
        )
        print("- OK\n")
        print(
            "-----------------------------------------------------------------"
            "\n"
        )

        # Write new settings
        print(f"{self._get_settings_str("NEW ")}\n")
        input("Press Enter to return to main menu: \n")
        print(
            "-----------------------------------------------------------------"
        )
        print(self._get_main_menu_str())

    def _show_rules(self):
        """
        Retrieves and displays the game rules, then waits for user confirmation
        before returning to the main menu.
        """
        print(self._get_rules_str())
        input("Press Enter to return to main menu: \n")
        print(
            "-----------------------------------------------------------------"
        )
        print(self._get_main_menu_str())

    def _quit(self):
        """
        Exits the game by displaying a farewell message and terminating
        the program.
        """
        print("\nThanks for playing!\nSee you next time.\n")
        sys.exit(0)

    # Helper functions for displays
    def _get_title_str(self):
        """
        Returns the welcome title as a formatted multiline string.
        """
        title_str = """
-----------------------------------------------------------------
---------------------- COIN TOWER TOPPLE ------------------------
-----------------------------------------------------------------
"""
        return title_str

    def _get_main_menu_str(self):
        """
        Returns a formatted string of the Main Menu.
        """
        main_options_str = "\n\n========== MAIN MENU ==========\n"
        for key, (description, _) in self.main_options.items():
            main_options_str += f"{key}. {description}\n"
        return main_options_str

    def _get_settings_str(self, prefix_title=""):
        """
        Returns a formatted string of the current game settings.

        Parameters:
        prefix_title (str, optional): A custom title prefix to prepend
        before "GAME SETTINGS". Defaults to an empty string.
        """
        settings_str = (
            f"{prefix_title}GAME SETTINGS\n"
            f"{'- Difficulty: ':<20} "
            f"{self.DIFFICULTY_LEVEL_MAP[self.difficulty_level][0]}\n"
            f"{'- Topple Height: ':<20} {self.topple_height}\n"
            f"{'- Possible Actions: ':<20} "
            f"{', '.join(map(str, self.possible_actions))}"
        )
        return settings_str

    def _get_rules_str(self):
        """
        Returns the game rules as a formatted multiline string.
        """
        rules_str = """

======================== RULES OF THE GAME ======================

Players take turns to add to a tower of coins until the tower
'topples'. This happens when the number of coins in the tower is
greater than or equal to the 'topple height'.

  1. The game starts with 1 coin in the tower.
     The player to take the first move is chosen at random.

  2. On their turn, each player chooses how many coins to add to
     the tower. They must choose one of the numbers in the
     Possible Actions list (defined in the game settings).

  3. A player wins the game if they force their opponent to topple
     the tower.

"""
        return rules_str

    # Helper Functions for getting valid user input
    def _get_valid_int(self, prompt, min, max):
        """
        Repeatedly prompts the user for an integer input until a valid
        response is provided.

        Ensures that the input is a number within the specified range
        [min, max]. Displays an error message for invalid entries.
        """
        while True:
            try:
                response = int(input(prompt + "\n"))
                if min <= response <= max:
                    return response
                raise ValueError
            except ValueError:
                print(
                    "- INVALID ENTRY: "
                    f"must be a whole number between {min} and {max}\n")

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
                response = input(prompt + "\n")
                nums = response.split(",")

                # Check enough items in list
                if len(nums) < 2:
                    raise CustomError(
                        "- INVALID ENTRY: "
                        "list must contain at least 2 numbers separated\n"
                        "                 by commas\n"
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

    def _get_valid_action(self):
        """
        Prompts the player to input a valid number of coins to add to the
        tower.

        The function:
        - Displays the available actions as a formatted list.
        - Repeatedly asks the user for input until a valid number is entered.
        - Ensures the chosen number is within the allowed set of possible
        actions.
        """
        # Get numbers as comma separated list
        possible_actions_str = ", ".join(
            map(str, self.possible_actions)
        )

        # Replace last comma with "or"
        parts = possible_actions_str.rsplit(",", 1)
        possible_actions_str = " or".join(parts)

        # Write prompt
        prompt = (
            "- How many coins would you like to add?\n"
            f"  Choose {possible_actions_str} coins: ")

        # Game loop
        while True:
            try:
                response = int(input(prompt + "\n"))
                if response in self.possible_actions:
                    return response
                raise ValueError
            except ValueError:
                print(
                    "- INVALID ENTRY: "
                    "please choose one of the numbers stated above\n"
                )

    def _get_valid_str(self, prompt, valid_options):
        """
        Repeatedly prompts the user for input until a valid response is
        provided.

        The user is required to enter a string that matches one of the
        items in the `valid_options` list (case-insensitive).

        Returns the input after converting to lowercase and stripping
        leading/trailing whitespace.
        """
        while True:
            try:
                response = input(prompt + "\n")
                response = response.strip().lower()
                if response in valid_options:
                    return response
                raise ValueError
            except ValueError:
                print(
                    "- INVALID ENTRY: "
                    "must enter either one of the following...\n"
                    f"  {','.join(valid_options)}\n"
                )


class AIPlayer:
    """
    Represents the computer player.
    """
    def __init__(self, difficulty_index, topple_height, possible_actions):
        self.difficulty_index = difficulty_index
        self.topple_height = topple_height
        self.possible_actions = possible_actions  # sorted in ascending order

        # Initialise q_values
        self.q_values = {
            (state, action): 0 for state in range(1, self.topple_height)
            for action in self.possible_actions
        }

    # Public methods
    def choose_action(self, state, explore_fraction):
        """
        Selects an action based on the current state and exploration factor.

        The `explore_fraction` parameter controls the balance between
        exploration and exploitation:
        - FULL EXPLORATION: `1.0` - Always chooses a random action
        (useful during AI training).
        - FULL EXPLOITATION: `0.0` - Always selects the action with the
        highest Q-value (useful for playing game on hardest difficulty).
        - BALANCE: Between `0.0` and `1.0` - Randomly chooses between
        exploration and exploitation (useful for playing game on lower
        difficulty level SETTINGS).
        """
        if random.random() < explore_fraction:
            # Choose random move
            return random.choice(self.possible_actions)
        else:
            # Choose move with highest q_value
            state_q_values = [
                self.q_values.get((state, action), 0)
                for action in self.possible_actions
            ]
            max_q_value = max(state_q_values)
            max_indices = [
                i for i, q_value in enumerate(state_q_values)
                if q_value == max_q_value
            ]
            random_max_index = random.choice(max_indices)
            return self.possible_actions[random_max_index]

    def train(self, num_training_games):
        """
        Trains the AI using reinforcement learning by simulating multiple
        games.

        The AI plays against itself for `num_training_games`, updating
        Q-values for all state-action pairs. Actions are chosen randomly
        to ensure comprehensive exploration of possible moves under the
        current game settings (topple height and possible actions).
        """
        print("\n\nTraining AI using current game settings...")

        EXPLORE_FRACTION = 1  # Full exploration

        for i in range(num_training_games):

            # Reset game
            state = 1  # height of tower
            game_over = False

            # Game loop
            while not game_over:

                # Choose (random) action
                action = self.choose_action(state, EXPLORE_FRACTION)

                # Get next_state that opponent will play from
                next_state = state + action

                # Get reward for updating q_value[(state, action)]
                if next_state >= self.topple_height:
                    # Lost game
                    reward = -1
                    game_over = True
                elif (
                    next_state + self.possible_actions[0] >= self.topple_height
                ):
                    # Won game (since opponent will lose on next turn)
                    reward = 1
                else:
                    reward = 0

                # Update q_values
                self.q_values[(state, action)] = \
                    self._update_q_value(state, action, reward)

                # Update state
                state = next_state

        print("AI training complete")

    # Helper functions
    def _update_q_value(self, state, action, reward):
        """
        Updates the Q-value for a given state-action pair using the Bellman
        equation.

        This function applies reinforcement learning principles to update the
        Q-value based on the reward received and the estimated future rewards.
        It considers the opponent's best possible action in the next state to
        anticipate future rewards.
        """
        # Define constants for Bellman Equation
        LEARNING_RATE = 0.8  # Weight of new experiences vs past experiences
        DISCOUNT = 0.5  # Weight of future rewards vs immediate rewards

        # Get opponents next state and predict next move (exploit strategy)
        opponent_state = state + action
        opponent_best_action = self.choose_action(opponent_state, 0)

        # Get expected next state and future reward
        expected_next_state = opponent_state + opponent_best_action
        expected_future_reward = \
            self._get_max_future_reward(expected_next_state)

        # Calculate new current_q_value using Bellman Equation
        current_q_value = self.q_values.get((state, action), 0)
        current_q_value += LEARNING_RATE * (
                reward + (DISCOUNT * expected_future_reward)
                - current_q_value
        )

        return current_q_value

    def _get_max_future_reward(self, next_state):
        """
        Computes the maximum possible future reward for a given state.

        This function retrieves the Q-values for all possible actions in
        the given next state and returns the highest value, representing
        the best expected future reward.
        """
        future_rewards = [
            self.q_values.get((next_state, action), 0)
            for action in self.possible_actions
        ]
        return max(future_rewards)
