import lyricsgenius as lg
from janome.tokenizer import Tokenizer
class SongInterface:
    
    def __init__(self) -> None:
        self.genius = lg.Genius('h3DHLVgmdDgLzNvSAEa602VcnqfNC7akNaXOs1TLErJL2beimrlHIOCCnY2QNpMn',
                             skip_non_songs=True, excluded_terms=["(Remix)", "(Live)"],
                             remove_section_headers=True)
        self.t = Tokenizer()
    
    
    def searchSong(self, songTitle: str):
        if(len(songTitle) == 0):
            return {"Invalid Search Query"}
        searchResults = self.genius.search_songs(songTitle, 9)
        return searchResults
    