def make_album(artist_name, album_title, song_number=None):
    album = {
        'artist': artist_name,
        'album': album_title
    }
    if song_number:
        album['songs'] = song_number
    return album

# Main loop
def album_collection():
    print("🎵 Album Collector")
    print("Type 'quit' at any prompt to exit.\n")

    albums = []

    while True:
        artist = input("Enter artist name: ")
        if artist.lower() == 'quit':
            break

        title = input("Enter album title: ")
        if title.lower() == 'quit':
            break

        song_input = input("Enter number of songs (or press Enter to skip): ")
        if song_input.lower() == 'quit':
            break

        song_number = int(song_input) if song_input.isdigit() else None

        album = make_album(artist, title, song_number)
        albums.append(album)
        print(f"✅ Album added: {album}\n")

    print("\n📚 Your Album Collection:")
    for idx, a in enumerate(albums, 1):
        print(f"{idx}. {a}")

# Run the interactive loop
album_collection()
