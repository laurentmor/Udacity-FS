class Movie:
    def __init__(self, title, storyline, poster, trailer, rating=0):
        """
        Constructor:
        ============
        Parameters :
                    title - Movie title
                    storyline - Small movie description
                    poster - Official movie poster URL
                    trailer - Movie trailer URL
                    rating - Movie rating from 0 t0 10
        """
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster
        self.trailer_youtube_url = trailer
        self.rating = rating

    def __repr__(self):
        """
            Returns Class information representation
        """
        return str(self.title) + " : " + str(self.storyline)
