from Media import Movie
from collections import namedtuple
import fresh_tomatoes as site
import requests
import json

movies = []

# Web service adress from which to fetch relevant movie infos
SERVICE_URL = "http://www.omdbapi.com/?i={id}&plot=short&r=json"

# Youtube trailer URL
YT_URL = "https://www.youtube.com/watch?v={video_id}"

# Movie entry array field data indexes
YT_ID_INDEX = 1
IMDB_ID_INDEX = 0

# No JSON data error message
NO_JSON_DATA_RECEIVED = "No JSON data received for movie : {id}"
# Structure used to encapsulat Json fields
JSON_FIELDS = namedtuple("JSON_FIELDS", "POSTER RATING PLOT TITLE")
FIELDS = JSON_FIELDS("Poster", "imdbRating", "Plot", "Title")

# Movie data entry field delimiter
DELIMITER = ":"

# File to store every movie entry
FILE = "movies.dat"

# Build trailer URL according to youtube ID


def build_youtube__url(vid_id):
    """
    Get complete youtube video URL from video_id
    Parameters:
        vid_id: Standard Youtube video ID

    Returns complete and usable video URL
    """
    return YT_URL.format(video_id=vid_id)

# Get all json values from movie


def get_movie_json_data(movie_id):
    """
    Get movie information in json format using a web SERVICE
    Parameters:

     movie_id: the movie IMDB id to get data from in form ttXXXX

    Returns  movie json info
    """
    url = SERVICE_URL.format(id=movie_id)
    try:

        r = requests.get(url)
        result = json.loads(r.text)
    except valuesError:
        print(NO_JSON_DATA_RECEIVED.format(id=movie_id))
    return result


def build_movie_list_from_file(file):
    with open(file) as movie_file:
        for entry in movie_file:
            data = entry.split(DELIMITER)
            movie_json_info = get_movie_json_data(data[IMDB_ID_INDEX])
            current_movie = Movie(
                movie_json_info[FIELDS.TITLE],
                movie_json_info[FIELDS.PLOT],
                movie_json_info[FIELDS.POSTER],
                build_youtube__url(data[YT_ID_INDEX]),
                movie_json_info[FIELDS.RATING])
            movies.append(current_movie)

build_movie_list_from_file(FILE)
site.open_movies_page(movies)
