# Favorite-Movie-Trailers-PYTHON
Server-side code to store a list of my favorite movies. Serves this data to open as a static web page

![Alt text](http://i.imgur.com/ABktyHu.png "preview")

Class Movie in media.py provides a template for storing movie titles and its information

entertain_center.py imports media.py and creates instances of the Movie class and creates the movies with its specific information

fresh_tomatoes.py takes the media.py and entertainment_center and opens the static webpage with its open_movies_page along with JS, HTML and CSS.

The application will be executed by the entertainment_centre.py file because it calls the open_movies_page function in fresh tomatoes.
Program can be run by any python IDE (IDLE, Pycharm etc). Have all files in one folder and execute the entertainment_centre.py file. Upon execution it should open a static web page on your default browswer with a list of my favorite movies.
