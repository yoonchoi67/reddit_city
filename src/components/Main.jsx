import React from 'react';
import '../css/main.css';
import PageTitle from './PageTitle';
import Dashboard from './Dashboard';

function Main() {
  return (
    <main id='main' className='main'>
        <PageTitle page='dashboard'/>
        <Dashboard />
    </main>
      
    
  )
}

export default Main