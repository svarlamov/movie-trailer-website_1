'''
Created on Mar 7, 2015

@author: sashavarlamov.com
'''
import media
import fresh_tomatoes
def load_page():
    # Create some movie objects to later insert into our page
    # Instantiate a movie object
    the_hangover = media.Movie("The Hangover", 
                               "Three buddies wake up from a bachelor party in Las Vegas, with no memory of the previous night and the bachelor missing. They make their way around the city in order to find their friend before his wedding.",
                               "http://upload.wikimedia.org/wikipedia/en/b/b9/Hangoverposter09.jpg",
                               "https://www.youtube.com/watch?v=tcdUhdOlz9M")
    # Instantiate a movie object
    the_interview = media.Movie("The Interview",
                                "Dave Skylark and producer Aaron Rapoport run the celebrity tabloid show \"Skylark Tonight.\" When they land an interview with a surprise fan, North Korean dictator Kim Jong-un, they are recruited by the CIA to turn their trip to Pyongyang into an assassination mission.",
                                "http://upload.wikimedia.org/wikipedia/en/2/27/The_Interview_2014_poster.jpg",
                                "https://www.youtube.com/watch?v=frsvWVEHowg")
    # Instantiate a movie object
    south_park = media.Movie("South Park: Bigger Longer & Uncut",
                                "When the four boys see an R-rated movie featuring Canadians Terrance & Phillip, they are pronounced \"corrupted\", and their parents pressure the United States to wage war against Canada.",
                                "http://upload.wikimedia.org/wikipedia/en/8/83/SouthParkbiggerlongeruncut.jpg",
                                "https://www.youtube.com/watch?v=PbMl6DjhJ1I")
    # Add all of my movies into an array of movies called, movies
    movies = [the_hangover, the_interview, south_park]
    # Generate the my movies page, with the all of the movie objects that were instantiated above
    fresh_tomatoes.open_movies_page(movies)
