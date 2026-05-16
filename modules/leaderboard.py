class Leaderboard:
    def __init__(self, players):
        self.players = players

    def add_player(self, Player):
        current_id = Player.player_id
        players[current_id] = Player
    