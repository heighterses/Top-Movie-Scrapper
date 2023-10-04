import requests
from bs4 import BeautifulSoup

web_url = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

web_data = requests.get(url=web_url)
web_data_text_format = web_data.text
soup = BeautifulSoup(web_data_text_format, "html.parser")

list_of_Movies = []

Movie_Names = soup.find_all(name="h3", class_="title")
for list_of_names in Movie_Names:
    names_text = list_of_names.getText()
    list_of_Movies.append(names_text)

top_movie = min(list_of_Movies)
low_movie = max(list_of_Movies)
print(top_movie,low_movie)

file = "movies.txt"

with open("movies.txt", "w") as file:
    for movie in list_of_Movies:
        file.write(movie)