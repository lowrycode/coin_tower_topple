class CoinTowerTopple:
    """
    Implements the logic for the Coin Tower Topple game, including:
    - menu navigation and user input validation
    - main game-play logic

    Use the start() method to launch the app
    """

    DIFFICULTY_DESCRIPTION_MAP = {1: "Easy", 2: "Medium", 3: "Hard"}

    def __init__(self):
        # Game settings
        self.difficulty_level = 1
        self.topple_height = 21
        self.possible_actions = [1, 2, 3]

    def start(self):
        """
        Launches the app.

        Displays the game title and default game settings before starting the
        Main Menu loop.
        """
        print("\n\n#### COIN TOWER TOPPLE ####\n")
        print(self._get_settings_str())

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
