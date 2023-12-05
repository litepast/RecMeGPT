"""Module in charge of creating an hyperlink to learn more about the recommendation.
It wil redirect to a different website, appropiate to learn more about the recommendation.
"""

def movie_link_builder(title):    
    youtube_link = f"https://www.youtube.com/results?search_query={title}+trailer"
    return f'<a href="{youtube_link}">Watch the movie trailer on Youtube</a>'

def album_link_builder(title):
    spotify_link = f"https://open.spotify.com/search/{title}/albums"
    return f'<a href="{spotify_link}">Listen to the Album on Spotify</a>'

def videogame_link_builder(title):
    moby_link = f"https://www.mobygames.com/search/?q={title}"
    return f'<a href="{moby_link}">Check the videogame information on Mobygames</a>'

def tv_link_builder(title):
    imdb_link = f"https://www.imdb.com/find/?s=tt&q={title}&ref_=nv_sr_sm"
    return f'<a href="{imdb_link}">Check the TV Show information on IMDB</a>'

def book_link_builder(title):
    goodreads_link = f"https://www.goodreads.com/search?utf8=%E2%9C%93&query={title}"
    return f'<a href="{goodreads_link}">Check the Book information on GoodReads</a>'

link_builder = {
    0: album_link_builder,
    1: videogame_link_builder,
    2: movie_link_builder,
    3: tv_link_builder,
    4: book_link_builder,
}

def get_rec_link(title, index):
    """
    Gets the link to learn more about the recommendation.
    Args:
    - title (str): Recommendation title.
    - index (int): The index of the media.
    Returns:
    - str: The anchor html tag to go to a website to learn about the recommendation.
    """
    return link_builder.get(index)(title)
