import React from 'react'

interface Nav {
  _id: number;
  icon: string;
  name: string;
}

interface NavItemProps {
  nav: Nav;
}

function NavItem({ nav }: NavItemProps) {
  return (
    <li className='nav-item' key={nav._id}>
        <a className='nav-link collapsed' href="/">
            <i className={nav.icon}></i>
            <span>{nav.name}</span>
        </a>
    </li>
  )
}

export default NavItem