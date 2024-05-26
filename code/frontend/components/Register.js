// code/frontend/components/Register.js

import React, {useState} from 'react';
import axios from 'axios';

const Register = ({history}) => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [phoneNumber, setPhoneNumber] = useState('');
    const [dateOfBirth, setDateOfBirth] = useState('');
    const [errors, setErrors] = useState({});

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            await axios.post('/api/auth/register/', {
                username,
                password,
                phone_number: phoneNumber,
                date_of_birth: dateOfBirth,
            });
            alert('User registered');
            history.push('/login');
        } catch (error) {
            setErrors(error.response.data);
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            <input
                type="text"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
                placeholder="Username"
                required
            />
            {errors.username && <p>{errors.username}</p>}
            <input
                type="password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                placeholder="Password"
                required
            />
            {errors.password && <p>{errors.password}</p>}
            <input
                type="text"
                value={phoneNumber}
                onChange={(e) => setPhoneNumber(e.target.value)}
                placeholder="Phone Number"
            />
            {errors.phone_number && <p>{errors.phone_number}</p>}
            <input
                type="date"
                value={dateOfBirth}
                onChange={(e) => setDateOfBirth(e.target.value)}
                placeholder="Date of Birth"
            />
            {errors.date_of_birth && <p>{errors.date_of_birth}</p>}
            <button type="submit">Register</button>
        </form>
    );
};

export default Register;

/**
 The Register component is similar to the Login component,
 but with additional fields for phone number and date of birth.
 The component also includes error handling to display validation errors from the backend.
 **/

