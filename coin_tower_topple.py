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

    def _play(self):
        print("PLAY THE GAME")

    def _change_settings(self):
        print("CHANGE GAME SETTINGS")

    def _show_rules(self):
        print("SHOW RULES")

    def _quit(self):
        print("QUIT")
