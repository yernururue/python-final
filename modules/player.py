class Player:
    def __init__(self, player_id, name, scores, dates):
        self.player_id = player_id
        self.name = name
        self.scores = scores
        self.dates = dates

    def add_score(self, score):
        #validation
        if isinstance(score, int):
            if score>=0:
                self.scores.append(score)
            else:
                print("Score must be positive")
        else:
            print("score must be integer")
    
    def get_average(self):
        length = len(self.scores)
        total_scores = 0
        for i in self.scores:
            total_scores += i
        if length == 0:
            return 0
        else:
            average_score = total_scores/length
        return average_score

    def get_best_score(self):
        max_score = 0
        for i in self.scores:
            if i>max_score:
                max_score = i
            else:
                continue
        return max_score
    
