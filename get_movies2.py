import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tmdb_proj2.settings")

import django
django.setup()

from django.core.management import call_command

import requests
from tmdb_projapp2.models import Movie

from dotenv import load_dotenv

# TMDb API URL and API key
API = os.getenv("API")
URL = 'https://api.themoviedb.org/3/discover/movie'

import gzip
import json

def fetch_and_save_movies():
    # Fetch data from the API
    response = requests.get(URL, params={'api_key': API})
    data = response.json()

    for movie_data in data.get('results', []):
        movie_id = movie_data.get('id')
        # Check if the movie already exists
        if not Movie.objects.filter(movie_id=movie_id).exists():
            Movie.objects.create(
                movie_id=movie_id,  # Mapping 'id' from API to 'movie_id'
                metadata=movie_data  # Save the entire movie data as JSON
            )
        else:
            print(f"Movie with ID {movie_id} already exists. Skipping.")

    print("Movies have been successfully saved to the database!")

# Run the function
if __name__ == "__main__":
    fetch_and_save_movies()
