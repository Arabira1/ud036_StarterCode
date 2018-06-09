class Media():
    def __init__(self, title, intruduce):
        self.title = title;
        self.story_line = intruduce;

class Movie(Media):
    def __init__(self, title, intruduce, image_url, trailer_url, release):
        Media.__init__(self, title, intruduce);
        self.poster_image_url = image_url;
        self.trailer_youtube_url = trailer_url;
        self.release = release