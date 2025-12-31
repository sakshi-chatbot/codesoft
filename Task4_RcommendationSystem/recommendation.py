movies = {
    "action": ["Avengers", "Batman", "Iron Man"],
    "romance": ["Titanic", "Notebook", "La La Land"],
    "comedy": ["Jumanji", "The Mask", "Hangover"],
    "horror": ["Conjuring", "Annabelle", "IT"]
}

print("Welcome to Movie Recommendation System 🎬")
print("Available genres: action, romance, comedy, horror")

choice = input("Enter your favorite genre: ").lower()

if choice in movies:
    print("Recommended movies for you:")
    for movie in movies[choice]:
        print("-", movie)
else:
    print("Sorry, genre not found!")
