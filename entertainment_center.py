import media
import fresh_tomatoes

#beginning creating instances for my favorite movies

interstellar = media.Movie("Interstellar",
                           "A team of explorers travel through a wormhole in space",
                           "http://www.joblo.com/posters/images/full/interstellar_ver8_xlg.jpg",
                           "https://www.youtube.com/watch?v=ePbKGoIGAXY")


dark_knight = media.Movie("Batman: Dark Knight",
                          "When the menace known as the Joker wreaks havoc and chaos on the people of Gotham",
                          "https://s-media-cache-ak0.pinimg.com/736x/b3/fe/d0/b3fed0f179ae1749204c767aff03c646.jpg",
                          "https://www.youtube.com/watch?v=yQ5U8suTUw0")

fight_club = media.Movie("Fight Club",
                         "An insomniac office worker, looking for a way to change his life, "
                         "crosses paths with a devil-may-care soap maker",
                         "http://imgc.allpostersimages.com/images/P-473-488-90/8"
                         "0/8083/JYI2300Z/posters/anna-malkin-fight-club-watercolor.jpg",
                         "https://www.youtube.com/watch?v=SUXWAEX2jlg")

matrix = media.Movie("The Matrix",
                     "A computer hacker learns from mysterious rebels about the true nature of his reality",
                     "http://imgc.allpostersimages.com/images/P-473-488-90/38/38"
                     "98/ZFPJF00Z/posters/the-matrix-reloaded.jpg",
                     "https://www.youtube.com/watch?v=m8e-FF8MsqU")


inception = media.Movie("Inception",
                        "A thief, who steals corporate secrets through use of dream-sharing technology",
                        "http://images.moviepostershop.com/inception-movie-poster-2010-1010547301.jpg",
                        "https://www.youtube.com/watch?v=66TuSJo4dZM")

forrest_gump = media.Movie("Forrest Gump",
                           "Forrest Gump, while not intelligent, has accidentally "
                           "been present at many historic moments",
                           "https://ca.movieposter.com/posters/archive/main/5/A70-2717",
                           "https://www.youtube.com/watch?v=uPIEn0M8su0")

#begin to create a list and store all my instances of my favorite movies
movies = [interstellar, dark_knight, fight_club, inception, matrix, forrest_gump]

#call open_movies_page function in fresh_tomatoes to open the static webpage
fresh_tomatoes.open_movies_page(movies)
