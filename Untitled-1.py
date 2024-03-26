class Football_team():
    def __init__(self, name, score, champion):
        self.name = name
        self.score = score
        self.champion = champion 
        
    def compare_score(self, other_team):
        if self.score > other_team.score:
            print(f"{self.name} has a higher score than {other_team.name}")
        elif self.score < other_team.score:
            print(f"{self.name} has a lower score than {other_team.name}")
        else:
            print(f"{self.name} and {other_team.name} have the same score")
    
    def champion_rate(self, champion_team):
        self.champion += champion_team
        print(f"{self.name}, we got {self.champion} championships")

team_1_name = input("Enter  name of team 1: ")
team_1_score = int(input("Enter  score of team 1: "))



team_2_name = input("Enter the name of team 2: ")
team_2_score = int(input("Enter the score of team 2: "))

team_1 = Football_team(team_1_name, team_1_score)
team_2 = Football_team(team_2_name, team_2_score)

team_1.compare_score(team_2)
