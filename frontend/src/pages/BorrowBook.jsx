import {useState, useEffect} from 'react'
import {useParams} from 'react-router-dom'
import {getBook} from "../services/bookService.js";
import {get_user} from "../services/userServices.js";
import {issueBook, userBorrowDetails} from "../services/borrowServices.js";

const BorrowBook = () => {
    const [book, setBook] = useState([])
    const [searchUser, setSearchUser] = useState('')
    const [user, setUser] = useState('')
    const [borrow, setBorrow] = useState([])
    const [error, setError] = useState();
    const {book_id} = useParams()

    const fetchBooks = async () =>{

        try{
            const response = await getBook(book_id);
            setBook(response.data);
        }catch (error){
            console.error(error)
        }
    }




    useEffect(() => {
        fetchBooks()

    },[])

    const fetchUser = async (e) =>{
        e.preventDefault();
        try{
            const response = await get_user(searchUser)
            console.log(response)
            setUser(response)
            // checkBorrowedBookDetails(response.id)
        }catch (error){
            console.error(error)
        }
    }

    const checkBorrowedBookDetails = async (user_id) =>{
        try{
            const response = await userBorrowDetails(user_id, book_id);
            console.log(response)
            setBorrow(response.data);
        }catch (e) {
            console.error(e)

        }
    }

    const issueBookHandler = async (e) =>{
        e.preventDefault()
        try {
            const response = await issueBook(user.id, book_id);
            console.log(response.data);
            alert('Book issued successfully!');
            fetchBooks()
        } catch (error) {
            // console.error(error);
            if (error.response) {
                // alert(`Error: ${error.response.data.error}`);
                setError(error.response.data.error);
            } else {
                alert('Network or server error');
            }
        }
    }


    return (
        <div className="container">
            <div className="row mt-5">
                <div className="col-md-6">
                    {book && book.id && (
                        <div className="card shadow">
                            <div className="card-body">
                                <ul className="list-group">
                                    <li className="list-group-item">Title:{book.title}</li>
                                    <li className="list-group-item">Isbn:{book.isbn}</li>
                                    <li className="list-group-item">Author:{book.author.first_name} {book.author.last_name}</li>
                                    <li className="list-group-item">Genre:{book.genre.name}</li>
                                    <li className="list-group-item">publisher:{book.publisher}</li>
                                    <li className="list-group-item">language:{book.language.name}</li>
                                    <li className="list-group-item">pages:{book.pages}</li>
                                    <li className="list-group-item">price:{book.price}</li>
                                    <li className="list-group-item">Total stock:{book.total_stock}</li>
                                </ul>
                            </div>
                        </div>
                    )}
                </div>
                <div className="col-md-6">
                    <div className="card shadow">
                        <div className="card-body">
                            <form onSubmit={fetchUser}>
                                <div className="input-group mb-3">
                                    <input
                                        type="text"
                                        className="form-control"
                                        placeholder="email/phone/username"
                                        value={searchUser}
                                        onChange={(e)=>setSearchUser(e.target.value)}
                                           />
                                    <button className="btn btn-dark" type="submit"
                                            id="button-addon2">Search
                                    </button>
                                </div>
                            </form>
                            <div>
                                {user && (
                                    <>
                                    <ul className="list-group">
                                        <li className="list-group-item">UserName:{user.username}</li>
                                        <li className="list-group-item">Name:{user.first_name} {user.last_name}</li>
                                        <li className="list-group-item">Email:{user.email}</li>
                                        <li className="list-group-item">Borrow Status:</li>
                                    </ul>

                                    <form onSubmit={issueBookHandler}>
                                        {error && (error)}
                                        <div className="mt-3 d-flex align-items-center justify-content-center">
                                            <button type="submit" className="btn btn-dark btn-sm">Proceed to issue book</button>
                                        </div>

                                    </form>
                                    </>
                                )}


                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default BorrowBook;