# mini playlist project

playlist = {
    "rock": [
        "Bohemian Rhapsody - Queen",
        "Stairway to Heaven - Led Zeppelin",
        "Hotel California - Eagles",
        "Sweet Child O' Mine - Guns N' Roses",
        "Back In Black - AC/DC",
    ],
    "pop": [
        "Thriller - Michael Jackson",
        "Like a Prayer - Madonna",
        "Shape of You - Ed Sheeran",
        "Firework - Katy Perry",
        "Uptown Funk - Mark Ronson ft. Bruno Mars",
    ],
    "jazz": [
        "Take Five - Dave Brubeck",
        "So What - Miles Davis",
        "My Favorite Things - John Coltrane",
        "What a Wonderful World - Louis Armstrong",
        "Feeling Good - Nina Simone",
    ],
    "classical": [
        "Symphony No. 5 - Beethoven",
        "Canon in D - Pachelbel",
        "The Four Seasons - Vivaldi",
        "Clair de Lune - Debussy",
        "Swan Lake - Tchaikovsky",
    ],
}

while True:
    print(
        """
Welcome to the Playlist!
1. View Playlist
2. Add Song
3. Delete Song
4. Exit
"""
    )

    user_choice = input("Select an option: ").strip()

    if user_choice == "1":
        print("Here is your playlist: 😃")
        for genre, songs in playlist.items():
            print(f"{genre.title()}: ")
            for index, song in enumerate(songs, start=1):
                print(f"{index}: {song}")
            print()

    elif user_choice == "2":
        print("Adding your music: ❤️")
        user_genre = input("Enter your genre:   ").strip().lower()
        user_song = input("Enter your song:        ").title()
        if user_genre in playlist.keys():
            playlist[user_genre].append(user_song)
        else:
            playlist[user_genre] = [user_song]

    elif user_choice == "3":
        print("We are still working on this functionality.")

    elif user_choice == "4":
        print("Thank you for using the Playlist app. Goodbye! 👋")
        break
    else:
        print("Invalid input. Please select a valid option.")
