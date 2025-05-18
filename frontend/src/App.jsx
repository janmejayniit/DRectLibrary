import Login  from "./pages/Login.jsx";
import Register  from "./pages/Register.jsx";
import SearchBook from "./pages/SearchBook.jsx";
import { Route, RouterProvider, createBrowserRouter, createRoutesFromElements } from 'react-router-dom'
import {Layout} from "./components/Layout.jsx";
import BorrowBook from "./pages/BorrowBook.jsx";
import Home from "./pages/Home.jsx";


function App() {

    const router = createBrowserRouter(createRoutesFromElements(
        <Route  path='/' element={<Layout/>}>
            <Route path="/" element={<Home/>}/>
            <Route path="/login" element={<Login/>} />
            <Route path="/register" element={<Register/>} />
            <Route path="/searchbook" element={<SearchBook/>} />
            <Route path="/borrow/:book_id" element={<BorrowBook/>} />
        </Route>


    ));
  return (
    <>
        <RouterProvider router={router}></RouterProvider>
    </>
  )
}

export default App
