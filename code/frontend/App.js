import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Login from './components/Login';
import Register from './components/Register';
import Dashboard from './components/Dashboard';

const App = () => {
    return (
        <Router>
            <Routes>
                <Route path="/login" element={<Login />} />
                <Route path="/register" element={<Register />} />
                <Route path="/dashboard" element={<Dashboard />} />
                {/* Add other routes as needed */}
            </Routes>
        </Router>
    );
};

export default App;


/**
 The App component is the main component that sets up the routing for the application.
 It uses the BrowserRouter component from react-router-dom to enable client-side routing.
 The Switch component is used to render the first child Route that matches the current location.
 The Route components define the paths and components to render for each route.
 In this example, the Login, Register, and Dashboard components are set up as routes.
 **/
