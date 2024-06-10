import React from 'react';
import '../css/SideBar.css';
import navList from '../static_data/navItem';
import NavItem from './NavItem';

function SideBar(): React.ReactElement {
    
    return (
        <aside id='sidebar' className='sidebar'>
            <ul className='sidebar-nav' id='sidebar-nav'>
                <li className='nav-heading'> Pages</li>
                {navList.map(nav => (
                    <NavItem key={nav._id} nav={nav}/>
                ))}
            </ul>

        </aside>
    )
}

export default SideBar

