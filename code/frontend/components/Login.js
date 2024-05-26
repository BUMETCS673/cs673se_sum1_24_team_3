import React, {useState} from 'react';
import axios from 'axios';

const Login = ({history}) => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const {data} = await axios.post('/api/auth/login/', {
                username,
                password,
            });
            localStorage.setItem('access', data.access);
            localStorage.setItem('refresh', data.refresh);
            history.push('/dashboard'); // Redirect to the dashboard or any protected route
        } catch (error) {
            setError('Invalid credentials');
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
            <input
                type="password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                placeholder="Password"
                required
            />
            <button type="submit">Login</button>
            {error && <p>{error}</p>}
        </form>
    );
};

export default Login;

/**
 The Login component is a simple form with fields for username and password.
 It uses the useState hook to manage the form state and the axios library
 to make a POST request to the backend API. If the login is successful,
 the access and refresh tokens are stored in the local storage,
 and the user is redirected to the dashboard. If there is an error,
 an error message is displayed to the user.
 **/

