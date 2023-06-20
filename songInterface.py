import lyricsgenius as lg

def searchSong():
    genius = genius = lg.Genius('h3DHLVgmdDgLzNvSAEa602VcnqfNC7akNaXOs1TLErJL2beimrlHIOCCnY2QNpMn',  # Client access token from Genius Client API page
                             skip_non_songs=True, excluded_terms=["(Remix)", "(Live)"],
                             remove_section_headers=True)
    song = genius.search_songs("明日も", 3)
    print("Artist: " + song['hits'][0]['result']['artist_names'] + " || Song: " + song['hits'][0]['result']['title'])
    print("Artist: " + song['hits'][1]['result']['artist_names'] + " || Song: " + song['hits'][1]['result']['title'])
    print("Artist: " + song['hits'][2]['result']['artist_names'] + " || Song: " + song['hits'][2]['result']['title'])

if __name__ == "__main__":
    song = searchSong()