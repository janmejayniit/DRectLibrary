import axios from 'axios';

const API_URL = 'http://127.0.0.1:8000/api/borrow/';
export const borrowList = async ()=>{
    try{
        const response=await axios.get(`${API_URL}borrows/`);
        return response;
    }catch (error){
        throw error;
    }

}

export const userBorrowDetails = async (user_id, book_id)=>{
    try{
        const response = await axios.get(`${API_URL}${user_id}/${book_id}/`)
        return response.data;
    }catch(error){
        console.log(error);
    }

}

export const issueBook = async (user_id, book_id)=>{
    try {
        const response = await axios.post(`${API_URL}${user_id}/${book_id}/issue/`);

        console.log(response.data);
        return response.data;
    } catch (error) {
       console.log(error);
    }
}