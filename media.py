import webbrowser

class Movie():
    """This class provides a way to store my favourite movies"""

    def __init__(self,movie_title, movie_storyline, poster_image, trailer_youtube):
        """This function stores movie information
        Args and parameters: movie title, storyline, poster and trailer"""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """This functions opens the movie trailers in a youtube link
        args: self"""
        webbrowser.open(self.trailer_youtube_url)
