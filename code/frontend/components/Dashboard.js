// code/frontend/components/Dashboard.js

import React from 'react';

const Dashboard = () => {
    return (
        <div>
            <h1>Dashboard</h1>
            <p>Welcome to your dashboard!</p>
        </div>
    );
};

export default Dashboard;


/**
 The Dashboard component is a simple component that displays a welcome message
 to the user. It can be used as a protected route that requires the user to be authenticated
 before accessing it. The component can be added to the App component to create a route
 that redirects users to the dashboard after successful login.
 **/
