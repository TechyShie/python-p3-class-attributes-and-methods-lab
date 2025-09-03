class Song:
    # Class attributes to track songs, genres, artists, and their counts
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        # Instance attributes
        self.name = name
        self.artist = artist
        self.genre = genre

        # Update total song count
        Song.count += 1

        # Track unique genres and artists
        if genre not in Song.genres:
            Song.genres.append(genre)
        if artist not in Song.artists:
            Song.artists.append(artist)

        # Increment per-genre and per-artist counts
        Song.genre_count[genre] = Song.genre_count.get(genre, 0) + 1
        Song.artist_count[artist] = Song.artist_count.get(artist, 0) + 1
