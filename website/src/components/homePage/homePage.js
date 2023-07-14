import './HomePage.css'
import axios from 'axios'
import react, {useState} from 'react'

function HomePage() {
  
  const [data, setData] = useState([{}])
  var  searchBarContent = ""

  function onSearchBarChange(e) {
    e.preventDefault()
    searchBarContent = e.target.value
    console.log(e.target.value)
  }

  function searchSongs() {
    console.log(searchBarContent)
    let queryObj = {
      searchQuery: searchBarContent
    }

    axios.post('http://127.0.0.1:5000/search', queryObj)
    .then(
      response => response.data
    ).then(
      helper => {
        setData(helper)
        console.log(helper)
      }
    )
  }
  return (
    <div className="app">
      <h1 className="headerTitle">Learn Languages From Music</h1>
        <div className="search-bar-container">
          <input type="text" className="search-input" 
          placeholder="Enter Song Title Here" id="searchBar" onChange={onSearchBarChange}/>
          <button className="searchButton" onClick={searchSongs}>Search</button>
        </div>
        {/* Other components and content */}
    </div>
    );
}

export default HomePage;