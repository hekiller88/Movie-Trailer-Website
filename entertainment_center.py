import media
import web_generator


# Toy Story: movie title, storyline, poster image and movie trailer
toy_story = media.Movie("Toy Story",
                        "A story of a boy  and his toy that come to life",
                        "http://www.impawards.com/1995/posters/toy_story_ver1_xlg.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

# Avatar: movie title, storyline, poster image and movie trailer
avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://4.bp.blogspot.com/_1qPLMlz01yQ/SwTA3GFVzxI/AAAAAAAADts/irJykYj7hJs/s1600/MarketSaw_03+Nov.+18+23.51.jpg",  # NOQA
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

# Man on Fire: movie title, storyline, poster image and movie trailer
man_on_fire = media.Movie("Man on Fire",
                          "A cold blood revenge",
                          "https://i.pinimg.com/736x/e2/53/9a/e2539af69a7cb48e3c901a9b2392eca4--elderly-man-man-on-fire.jpg",  # NOQA
                          "https://www.youtube.com/watch?v=rb-ZEBBKolc")

# set the movies that will be passed to the media file
movies = [toy_story, avatar, man_on_fire]

# open the HTML file in a browser via the fresh_tomatoes.py file
web_generator.open_movies_page(movies)
