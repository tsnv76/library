import React from 'react'
import {HashRouter, BrowserRouter, Routes, Route, Link, Redirect, Navigate} from 'react-router-dom'
import AuthorList from "./components/AuthorList";
import BookList from "./components/BookList";
import AuthorBooks from "./components/AuthorBooks";
import axios from 'axios'


const NotFound = ({  }) => {
    return (
        <div>Page  not found</div>
    )
}


class App extends React.Component {
  constructor(prop) {
    super(prop)
    this.state = {
      'authors': [],
      'books': []
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

    axios
        .get('http://127.0.0.1:8000/api/books/')
        .then(response => {
          const books = response.data
          this.setState({
            'books': books
          })
        })
        .catch(error => console.log())
  }

  render () {
    return (
        <div>
            <BrowserRouter>
                <nav>
                    <ul>
                        <li><Link to="">Authors</Link></li>
                        <li><Link to="/books">Books</Link></li>
                    </ul>
                </nav>
                <Routes>
                    <Route exact path='/' element={<AuthorList authors={this.state.authors} /> } />
                    <Route exact path='/books'   element={<BookList books={this.state.books} /> } />
                    <Route path="/authors" element={<Navigate to="/" />} />
                    <Route path='/author/:id'   element={<AuthorBooks books={this.state.books} /> } />
                    <Route path="*" element={<NotFound /> } />
                </Routes>
            </BrowserRouter>
        </div>
    )
  }
}

export default App;
