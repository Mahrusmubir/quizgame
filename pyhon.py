from abc import ABC, abstractmethod

class Game(ABC):
    @abstractmethod
    def run_game(self):
        pass

class QuestionGame(Game):
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
    
    def run_game(self):
        print("Welcome to the Question Game!")
        play_game = input("Would you like to play? (yes or no): ")
        
        if play_game.lower() != "yes":
            print("Okay, maybe another time!")
            return
        
        print("Let's begin!")
        for question, answer in self.questions.items():
            user_answer = input(question + " ")
            if user_answer.lower() == answer.lower():
                print("Correct!")
                self.score += 1
            else:
                print("Incorrect.")
        
        print("Game over! Your final score is {} out of {}. That's {:.0f}% correct!".format(
            self.score, len(self.questions), (self.score/len(self.questions))*100))


questions = {
    "What is the capital of France? ": "Paris",
    "What is the largest mammal on Earth? ": "Blue Whale",
    "What year was Python created? ": "1989",
    "What is the tallest mountain in the world? ": "Mount Everest",
    "What is the currency of Japan? ": "Yen"
}


game = QuestionGame(questions)
game.run_game()
