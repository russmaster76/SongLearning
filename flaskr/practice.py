import lyricsgenius as lg
from janome.tokenizer import Tokenizer

genius = lg.Genius('h3DHLVgmdDgLzNvSAEa602VcnqfNC7akNaXOs1TLErJL2beimrlHIOCCnY2QNpMn',  # Client access token from Genius Client API page
                             skip_non_songs=True, excluded_terms=["(Remix)", "(Live)"],
                             remove_section_headers=True)

t = Tokenizer()

def searchSong(songTitle):
    if len(songTitle) == 0:
        songTitle = "明日も"
    searchResults = genius.search_songs(songTitle, 9)
    return searchResults

def selectSong(searchResults):
    i: int = 0
    while i < 10 and i < len(searchResults['hits'][0]) + 1:
        print(str(i + 1) + ". Artist: " + searchResults['hits'][i]['result']['artist_names'] + " || Song: " + 
              searchResults['hits'][i]['result']['title'])
        i += 1
    print("Do You See Your Desired Song? If Yes, Input its respective number, if not type no")
    foundSongResponse = input()
    if(foundSongResponse.isdigit() == True and int(foundSongResponse) > 0):
        try:
            chosenSong = searchResults['hits'][int(foundSongResponse) - 1]['result']['title']
            chosenSongArtist = searchResults['hits'][int(foundSongResponse) - 1]['result']['artist_names']
            print("Your song is " + chosenSong + " by " + chosenSongArtist)
            return(searchResults['hits'][int(foundSongResponse) - 1]['result'])
        except:
                print("That was an invalid response, Please select a song by typing its number or typing No")
                selectSong(searchResults)
    elif(foundSongResponse.lower()== "no" or foundSongResponse.lower() == "n"):
        print("Please Reenter the Song to Search again, Including the artist can help narrow down search results.")
        newSearchTerm = input()
        newSearchResults = searchSong(newSearchTerm)
        selectSong(newSearchResults)
    else:
        print("That was an invalid response, Please select a song by typing its number or typing No")
        selectSong(searchResults)

def getLyrics(songData):
    print(songData)
    lyrics = genius.lyrics(song_url=songData["url"])
    print(type(lyrics))
    print(lyrics)
    return lyrics

def tokenizeLyrics(lyrics):
    for token in t.tokenize(lyrics):
        print(token)

    

if __name__ == "__main__":
    searchResults = searchSong("")
    chosenSong = selectSong(searchResults)
    lyrics = getLyrics(chosenSong)
    tokenizeLyrics(lyrics)