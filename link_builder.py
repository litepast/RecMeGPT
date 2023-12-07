"""
Module in charge of creating a hyperlink to learn more about the recommendation. 
It will be redirected to a different website, appropriate to learn more about the recommendation.
"""
# It will not redirect to the recommendation entry on these sites, but to the search results
# In a full, not MVP, version of this application. I would use the API of each of these websites
# to return the first result of the exact link. Or even en scrapper if the site was 
# too good and it did not have an API

def get_rec_link(title, index):
    link_builder = {
        0: '<a href="https://open.spotify.com/search/{}/albums">Listen to the Album on Spotify</a>',
        1: '<a href="https://www.mobygames.com/search/?q={}">Check the videogame information on Mobygames</a>',        2: "",
        2: '<a href="https://www.youtube.com/results?search_query={}+trailer">Watch the movie trailer on Youtube</a>',
        3: '<a href="https://www.imdb.com/find/?s=tt&q={}&ref_=nv_sr_sm">Check the TV Show information on IMDB</a>',
        4: '<a href="https://www.goodreads.com/search?utf8=%E2%9C%93&query={}">Check the Book information on GoodReads</a>'
    }
    return link_builder[index].format(title)