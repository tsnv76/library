const BookItem = ({book}) => {
    return(
        <tr>
            <td>{book.text}</td>
            <td>{book.authors}</td>
        </tr>
    )
}

const BookList = ({books}) => {
    return (
        <table>
            <th>
                Название книги
            </th>
            <th>
                Автор
            </th>
            {books.map((book) => <BookItem book={book} />)}
        </table>
    )
}

export default BookList;