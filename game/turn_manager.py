SKIPPED_TURN = "SKIPPED_TURN"


class TurnManager:
    """A class to manage the turn order of the players."""

    def __init__(self, players):
        self.players = players
        self.turn_state = {player: None for player in players}

    def take_turn(self, player, content=None):
        """Take a turn for the given player."""
        if self.turn_state[player]:
            raise RuntimeError(f"Player {player} has already taken a turn.")
        self.turn_state[player] = content if content is not None else SKIPPED_TURN

    def reset(self):
        """Reset the turn state."""
        self.turn_state = {player: None for player in self.players}

    def who_can_take_a_turn(self):
        """Return a list of players who can take a turn."""
        players_who_can_take_a_turn = [
            player for player, taken in self.turn_state.items() if taken is None
        ]
        # If no players can take a turn, return None
        if players_who_can_take_a_turn:
            return players_who_can_take_a_turn

    def format_turn_for_llm(self):
        """Return a string of the current turn state."""
        return "\n".join(
            f"{player}: {content}"
            for player, content in self.turn_state.items()
            if content != SKIPPED_TURN
        )
