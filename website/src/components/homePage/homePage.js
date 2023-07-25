import './HomePage.css'
import axios from 'axios'
import react, {useState, useEffect} from 'react'

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
        setData(helper.hits)
        console.log(helper.hits)
      }
    ).catch((error) => {
      console.error('Error Fetching Data', error);
      setData([{}])
    });
  }

  function displaySearchResults() {
    if(data != null) {
    return <div>

    </div>
    }
  }


  return (
    <div className="app">
      <h1 className="headerTitle">Learn Languages From Music</h1>
        <div className="search-bar-container">
          <input type="text" className="search-input" 
          placeholder="Enter Song Title Here" id="searchBar" onChange={onSearchBarChange}/>
          <button className="searchButton" onClick={searchSongs}>Search</button>
        </div>
        {data.length > 0 ? (
          data.map((item, index) => (
            <div key={index}>
              <h2>{item.result?.title}</h2>
            </div>
          ))
          ) : (
            <p>Loading Data...</p>
          )
        }
        {/* Other components and content */}
    </div>
    );
}

export default HomePage;