## Define the Player class
class Player:
    def __init__(self, playerName, playerPosition):
        self.playerName = playerName
        self.playerPosition = playerPosition

# Define the NFLTeam class
class NFLTeam:
    def __init__(self, teamName, players):
        self.teamName = teamName
        self.players = players

    def show_team(self):
        print(f"Team: {self.teamName}")
        print("Players:")
        for player in self.players:
            print(f"{player.playerName} - {player.playerPosition}")

# Create players
player1 = Player("Odell Beckham Jr", "WR")
player2 = Player("Jaxon Dart", "QB")
player3 = Player("Derrick Henry", "RB")
player4 = Player("Brock Bowers", "TE")

# Add players to a list
playerList = [player1, player2, player3, player4]

# Create team with custom name
team = NFLTeam("Grand Rapids GoStars", playerList)

# Display team info
team.show_team()