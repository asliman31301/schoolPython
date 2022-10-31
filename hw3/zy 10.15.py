#Ahmad SLiman 1898612

class Team:
    def __init__(self):
        self.name = 'none'
        self.wins = 0
        self.losses = 0

    def get_win_percentage(self):
        if self.wins + self.losses == 0:
            return 0.0
        else:
            return float(self.wins / (self.wins + self.losses))

    def print_standing(self):
        ratio = self.get_win_percentage()
        if ratio < 0.5:
            print(f'Team {self.name} has a losing average.')
        else:
            print(f'Congratulations, Team {self.name} has a winning average!')


if __name__ == "__main__":
    team = Team()

    user_name = str(input())
    user_wins = float(input())
    user_losses = float(input())

    team.name = user_name
    team.wins = user_wins
    team.losses = user_losses
    team.print_standing()
