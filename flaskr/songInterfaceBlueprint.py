from flask import Blueprint, request
from flaskr.songInterface import SongInterface

def constructBlueprint(songInterface: SongInterface) -> Blueprint:
    songInterfaceBlueprint = Blueprint("sibp", __name__)
    
    @songInterfaceBlueprint.route("/search", methods=["POST"])
    def searchForSong():
        if request.json is not None:
            searchQuery = request.json["searchQuery"]
            print(searchQuery)
            results = songInterface.searchSong(searchQuery)
            return results
        return {"Error": "Invalid Search"}
    
    return songInterfaceBlueprint