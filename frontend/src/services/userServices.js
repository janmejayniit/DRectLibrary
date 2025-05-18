import axios from 'axios';


const API_URL = 'http://127.0.0.1:8000/api/users/';

export const login = async (email, password) => {
    try{
        const response = await axios.post(`${API_URL}token/`, {email, password});
        return response.data;
    }catch(err){
        console.log(err);
    }
};

export const register = async ({username, first_name, last_name, email, password}) => {
    try {
        await axios.post(`${API_URL}register/`, {
            username,
            first_name,
            last_name,
            email,
            password,
        });
        // alert('Registration successful!');
    } catch (err) {
        // alert('Registration failed. Please try again.');
        console.error(err);
    }
}

export const get_user = async (search)=>{
    try{
        const response = await axios.get(`${API_URL}lookup/`, { params: { q: search} })
        return response.data;
        // console.log(response.data);
    }catch(err)  {
        console.error(err);
    }
}
// export const get_user = async (search) => await axios.get(`${API_URL}lookp/`,{params:{q:search}});