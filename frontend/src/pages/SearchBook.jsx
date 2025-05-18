import {useState} from "react";
import {searchBooks} from "../services/bookService.js";
import { Link } from 'react-router-dom'

const SearchBook = () => {
    const [query, setQuery] = useState("");
    const [results, setResults] = useState([]);

    const handleSearch = async (e) => {
        e.preventDefault();
        try {
            const response = await searchBooks(query);
            setResults(response.data);
        } catch (err) {
            console.error('Search failed:', err);
        }
    };

    return (
        <div className="container mt-5">
            <div className="row ">
                <div className="col-md-6">
                    <form onSubmit={handleSearch} style={{display: 'flex', alignItems: 'center', gap: '0.5rem'}}>
                        <input
                            type="text"
                            placeholder="Search books..."
                            value={query}
                            onChange={(e) => setQuery(e.target.value)}
                        />
                        <button type="submit" className="btn btn-dark btn-sm">Search</button>
                    </form>
                </div>
                <div className="col-md-6">
                    {results.length > 0 ?
                        <ul style={{marginTop: '1rem'}}>
                            {results.map((book) => (
                                <li key={book.id}>
                                    <strong>{book.title}</strong> by {book.author.first_name}
                                    <Link to={`/borrow/${book.id}`} className="btn btn-default"><i className="fa fa-check-circle"></i> Issue</Link>
                                </li>
                            ))}
                        </ul>:
                        <>
                        No books found
                        </>

                    }

                </div>
            </div>
        </div>
    )
}
export default SearchBook;