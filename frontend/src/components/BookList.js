const BookItem = ({book, delete_book}) => {
    return(
        <tr>
            <td>{book.text}</td>
            <td>{book.authors}</td>
            <td><button onClick={()=>delete_book(book.id)} type="button">Delete</button> </td>
        </tr>
    )
}

const BookList = ({books, delete_book}) => {
    return (
        <table>
            <th>
                Название книги
            </th>
            <th>
                Автор
            </th>
            <th>

            </th>
            {books.map((book) => <BookItem book={book} delete_book={delete_book}/>)}
        </table>
    )
}

export default BookList;