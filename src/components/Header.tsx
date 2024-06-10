import React from 'react';
import '../css/header.css';
import Logo from './Logo';
import SearchBar from './SearchBar';

function Header(): React.ReactElement {
  return (
    <header id='header' className='header fixed-top d-flex align-items-center'>
      <Logo />
      <SearchBar/>
    </header>
  )
}

export default Header
