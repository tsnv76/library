import React from 'react'
import AuthorList from "./components/AuthorList";
import axios from 'axios'


class App extends React.Component {
  constructor(prop) {
    super(prop)
    this.state = {
      'authors': []
    }
  }

  componentDidMount() {
    axios
        .get('http://127.0.0.1:8000/api/authors/')
        .then(response => {
          const authors = response.data
          this.setState({
            'authors': authors
          })
        })
        .catch(error => console.log())
  }

  render () {
    return (
        <div>
         <AuthorList authors={this.state.authors} ></AuthorList>
        </div>
    )
  }
}

export default App;
