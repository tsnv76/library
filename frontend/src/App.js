import React from 'react'
import {HashRouter, BrowserRouter, Routes, Route, Link, Redirect, Navigate, useLocation} from 'react-router-dom'
import AuthorList from "./components/AuthorList";
import BookList from "./components/BookList";
import AuthorBooks from "./components/AuthorBooks";
import LoginForm from "./components/LoginForm";
import BookForm from "./components/BookForm";
import axios from 'axios'


const NotFound = ({  }) => {
    let location = useLocation()
    return (
        <div>Page {location.pathname} not found</div>
    )
}


class App extends React.Component {
  constructor(prop) {
    super(prop)
    this.state = {
      'authors': [],
      'books': [],
      'token':  ''
    }
  }

  get_token(login, password) {
      axios
        .post('http://127.0.0.1:8000/api-token-auth/', {"username": login, "password": password})
        .then(response => {
          const token = response.data.token
            console.log(token)
            localStorage.setItem('token', token)
          this.setState({
            'token': token
          }, this.get_data)
        })
        .catch(error => console.log(error))
  }

  logout() {
      localStorage.setItem('token', '')
      this.setState({
          'token': ''
      }, this.get_data)
  }

  componentDidMount() {
      let token = localStorage.getItem('token')
      this.setState({
          'token': token
      }, this.get_data)
  }

  is_auth() {
      return !!this.state.token
  }

  get_headers() {
      if (this.is_auth()) {
          return {
              'Authorization': 'Token ' + this.state.token
          }
      }
      return {}
  }

  get_data() {
      let headers = this.get_headers()
    axios
        .get('http://127.0.0.1:8000/api/authors/', {headers})
        .then(response => {
          const authors = response.data
          this.setState({
            'authors': authors
          })
        })
        .catch(error => {
            console.log(error);
            this.setState({
                'authors': []
            })
        })

    axios
        .get('http://127.0.0.1:8000/api/books/', {headers})
        .then(response => {
          const books = response.data
          this.setState({
            'books': books
          })
        })
        .catch(error => {
            console.log(error);
            this.setState({
                'books': []
            })
        })
  }

    create_book(title, authors) {
      console.log(title, authors)
        let headers = this.get_headers()
        axios
            .post("http://127.0.0.1:8000/api/books/", {'text': title, 'authors': authors}, {headers})
            .then(response => {
              this.get_data();
            })
            .catch(error => {
                console.log(error);
            })
    }

    delete_book(id) {
          // console.log(id)
        let headers = this.get_headers()
        axios
            .delete(`http://127.0.0.1:8000/api/books/${id}`, {headers})
            .then(response => {
              const authors = response.data
              this.setState({
                'books': this.state.books.filter((book) => book.id != id)
              })
            })
            .catch(error => {
                console.log(error);
            })
    }



  render () {
    return (
        <div>
            <BrowserRouter>
                <nav>
                    <ul>
                        <li><Link to="/">Authors</Link></li>
                        <li><Link to="/books">Books</Link></li>
                        <li><Link to="/books/create">Create book</Link></li>
                        <li>
                            { this.is_auth() ? <button onClick={() => this.logout()}>Logout</button> : <Link to="/login">Login</Link> }
                        </li>
                    </ul>
                </nav>
                <Routes>
                    <Route exact path='/' element={<AuthorList authors={this.state.authors} /> } />
                    <Route exact path='/books'   element={<BookList books={this.state.books} delete_book={(id) => this.delete_book(id)}/> } />
                    <Route exact path='/books/create'   element={<BookForm authors={this.state.authors} create_book={(title, authors) => this.create_book(title, authors)}/> } />
                    <Route exact path='/login'   element={<LoginForm  get_token={(login, password) => this.get_token(login, password)}/> } />
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
