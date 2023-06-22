import lyricsgenius as lg

def searchSong(songTitle):
    genius = genius = lg.Genius('h3DHLVgmdDgLzNvSAEa602VcnqfNC7akNaXOs1TLErJL2beimrlHIOCCnY2QNpMn',  # Client access token from Genius Client API page
                             skip_non_songs=True, excluded_terms=["(Remix)", "(Live)"],
                             remove_section_headers=True)
    if len(songTitle) == 0:
        songTitle = "明日も"
    searchResults = genius.search_songs(songTitle, 9)
    return searchResults

def selectSong(searchResults):
    i: int = 0
    while i < 10 and i < len(song['hits'][i]):
        print(str(i + 1) + ". Artist: " + searchResults['hits'][i]['result']['artist_names'] + " || Song: " + 
              searchResults['hits'][i]['result']['title'])
        i += 1
    print("Do You See Your Desired Song? If Yes, Input its respective number, if not type no")
    foundSongResponse = input()
    if(foundSongResponse.isdigit() == True and foundSongResponse > int(0)):
        try:
            chosenSong = searchResults['hits'][int(foundSongResponse) - 1]['result']['title']
            print("Your song is " + chosenSong)
        except:
            print("Not Valid")
    elif(foundSongResponse.lower()== "no" or foundSongResponse == "N"):
        print("Please Reenter the Song to Search again, Including the artist can help narrow down search results.")
        newSearchTerm = input()
        newSearchResults = searchSong(newSearchTerm)
        selectSong(newSearchResults)
    else:
        print("Invalid Response")
    

    

if __name__ == "__main__":
    song = searchSong("")
    selectSong(song)