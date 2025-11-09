import requests
import webbrowser

try:
    movieName = input("Enter a movie title: ")

    url = f"https://imdb.iamidiotareyoutoo.com/search?q={movieName}"

    response = requests.get(url)
    response.raise_for_status()

    data = response.json()

    if "description" in data and len(data["description"]) > 0:
        movie = data["description"][0]

        movie_title = movie.get("#TITLE", "Couldn't find the title")
        released_year = movie.get("#YEAR", "Couldn't find the release year")
        rank = movie.get("#RANK", "Couldn't find the rank")
        actors = movie.get("#ACTORS", "Couldn't find the actors")
        movie_id = movie.get("#IMDB_ID", "Couldn't find the IMDB ID")
        image_url = movie.get("IMG_POSTER", None)

        print(f"Movie Title: {movie_title}")
        print(f"Released Year: {released_year}")
        print(f"Rank: {rank}")
        print(f"Actors: {actors}")
        print(f"IMDB ID: {movie_id}")

        if image_url:
            webbrowser.open(image_url)
        else:
            print("No poster available.")
    else:
        print("No movie found with that title.")

except requests.exceptions.RequestException as e:
    print(f"Network error: {e}")

except (KeyError, IndexError, ValueError) as e:
    print(f"Data error: {e}")

except Exception as e:
    print(f"Unexpected error: {e}")

