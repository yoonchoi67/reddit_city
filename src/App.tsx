import React, {createContext, useEffect, useState} from 'react';
import 'bootstrap-icons/font/bootstrap-icons.css'
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.min.js';

import './App.css';
import Header from './components/Header'
import SideBar from './components/SideBar';
import Main from './components/Main';
// import { MarkerDataProvider } from './MarkerDataProvider'; // Import MarkerDataProvider


function App(): React.ReactElement {

  return (
    <>
      {/* <MarkerDataProvider> */}
      <Header />
      <SideBar />
      <Main />
      {/* </MarkerDataProvider> */}
    </>
  )  
  // return <Header />
}

export default App;
