import random

# Data structure to hold quiz questions and answers
quiz_questions = [
    {"prompt": "Who directed the movie 'Inception'?", "choices": ["Steven Spielberg", "Christopher Nolan", "Martin Scorsese", "James Cameron"], "correctAnswer": 1},
    {"prompt": "Which movie features the character Jack Dawson?", "choices": ["The Great Gatsby", "Catch Me If You Can", "Titanic", "Inception"], "correctAnswer": 2},
    {"prompt": "What is the highest-grossing film of all time?", "choices": ["Avatar", "Titanic", "Avengers: Endgame", "Star Wars: The Force Awakens"], "correctAnswer": 0},
    {"prompt": "Which film won the Best Picture Oscar in 1994?", "choices": ["Pulp Fiction", "Forrest Gump", "The Shawshank Redemption", "Jurassic Park"], "correctAnswer": 1},
    {"prompt": "Who played the Joker in the 2008 movie 'The Dark Knight'?", "choices": ["Heath Ledger", "Jack Nicholson", "Joaquin Phoenix", "Mark Hamill"], "correctAnswer": 0},
    {"prompt": "What year was the original 'Jurassic Park' movie released?", "choices": ["1990", "1993", "1996", "1999"], "correctAnswer": 1},
    {"prompt": "Which actress played the leading role in the movie 'La La Land'?", "choices": ["Emma Stone", "Emma Watson", "Anne Hathaway", "Natalie Portman"], "correctAnswer": 0},
    {"prompt": "Which movie features the quote, 'I see dead people'?", "choices": ["The Sixth Sense", "Ghost", "Poltergeist", "Casper"], "correctAnswer": 0},
    {"prompt": "Which film did Tom Hanks NOT star in?", "choices": ["Cast Away", "Saving Private Ryan", "Forrest Gump", "Inception"], "correctAnswer": 3},
    {"prompt": "What is the name of the fictional country where 'Black Panther' is set?", "choices": ["Genovia", "Wakanda", "Elbonia", "Latveria"], "correctAnswer": 1}
]

def display_question(question):
    """Display the current question and accept user input until it's valid."""
    print("\n" + question["prompt"])
    for idx, choice in enumerate(question["choices"]):
        print(f"{idx + 1}. {choice}")

    while True:
        try:
            answer = int(input("Choose the correct answer (1-4): "))
            if 1 <= answer <= 4:
                return answer
            else:
                print("Invalid input: Please choose a number between 1 and 4.")
        except ValueError:
            print("Invalid input: Please enter a valid number between 1 and 4.")

def start_quiz():
    """Shuffle questions, display them one by one, and tally the score."""
    random.shuffle(quiz_questions)
    score = 0

    for question in quiz_questions:
        answer = display_question(question)
        if answer == question["correctAnswer"] + 1:
            print("Correct!")
            score += 1
        else:
            print("Wrong!")
    
    print(f"\nQuiz completed! Your final score is: {score}/{len(quiz_questions)}")

if __name__ == "__main__":
    print("Welcome to the Movie Trivia Challenge!")
    start_quiz()
