import {useState, useEffect} from 'react'
import {borrowList} from "../services/borrowServices.js";

const Home = ()=>{
    const[borrowDetails, setBorrowDetails] = useState([])


    const fetchBorrowDetails = async ()=>{

        try{
            const response = await borrowList()
            setBorrowDetails(response.data)
            console.log(response.data)
        }catch (error) {
            console.log(error)
        }
    }

    useEffect(()=>{
        fetchBorrowDetails()
    },[])

    return (
        <div className="container">
            <div className="row">
                <div className="col-12">
                    <div className="card shadow">
                        <div className="card-header">
                            <h5>Books Borrow List</h5>
                        </div>
                        <div className="card-body">
                            <div className="row">
                                <div className="col-12">
                                    <table className="table table-striped">
                                        <thead>
                                             <tr>
                                                 <th>S.N</th>
                                                 <th>Borrower Name</th>
                                                 <th>Book Title</th>
                                                 <th>Issue Date</th>
                                                 <th>Due Date</th>
                                                 <th>Return Date</th>
                                                 <th>Fine(if any)</th>
                                                 <th>Actions</th>
                                             </tr>
                                        </thead>
                                        <tbody>
                                        {
                                            borrowDetails.map((borrow, index)=>{
                                                return (
                                                    <tr key={borrow.book.id}>
                                                        <td>{index + 1}</td>
                                                        <td>{borrow.user.first_name} {borrow.user.last_name}</td>
                                                        <td>{borrow.book.title}</td>
                                                        <td>{borrow.borrow_date}</td>
                                                        <td>{borrow.due_date}</td>
                                                        <td>{borrow.return_date}</td>
                                                        <td>{borrow.fine}</td>
                                                        <td>
                                                            <button className="btn btn-dark btn-sm">Return</button>
                                                        </td>
                                                    </tr>
                                                )

                                            })
                                        }
                                        </tbody>
                                    </table>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default Home;