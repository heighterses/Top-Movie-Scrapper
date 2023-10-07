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

rev_list_of_movies = list_of_Movies[::-1]

file = "movies.txt"

with open(file, "w", encoding="utf-8") as file:
    for prn in rev_list_of_movies:
        print(prn)
        file.write(prn + "\n")


