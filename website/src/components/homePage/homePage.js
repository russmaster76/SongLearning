import './HomePage.css'
import axios from 'axios'

function HomePage() {
  var  searchBarContent = ""

  function onSearchBarChange(e) {
    e.preventDefault()
    searchBarContent = e.target.value
    console.log(e.target.value)
  }

  function onSearchButtonClick(e) {
    console.log(searchBarContent)
  }

  function searchSongs() {
    let queryObj = {
      searchQuery: searchBarContent
    }

    axios.post('http://127.0.0.1:5000/search', queryObj)
    .then(
      response => response.data
    )
    .then(
      
    )
  }
  return (
    <div className="app">
      <h1 className="headerTitle">Learn Languages From Music</h1>
        <div className="search-bar-container">
          <input type="text" className="search-input" 
          placeholder="Enter Song Title Here" id="searchBar" onChange={onSearchBarChange}/>
          <button className="searchButton" onClick={onSearchButtonClick}>Search</button>
        </div>
        {/* Other components and content */}
    </div>
    );
}

export default HomePage;