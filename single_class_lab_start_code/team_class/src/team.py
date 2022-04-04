class Team:
    def __init__(self, input_name, input_players, input_coach):
        self.name = input_name
        self.players = input_players
        self.coach = input_coach
        self.points = 0

    def update_coach(self):
        self.coach = "John Candy"

    def add_player(self, player):
        self.players.append(player)
    
    def has_player(self, player):
        for guy in self.players:
            if guy == player:
                return True
        return False

    def has_points(self):
        return self.points

    def play_game(self, result):
        if result == True:
            self.points += 3

        