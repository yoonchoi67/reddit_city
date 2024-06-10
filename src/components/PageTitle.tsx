import React from 'react';
import '../css/pageTitle.css';

interface PageTitleProps {
  page: string;
}

function PageTitle({page}: PageTitleProps) {
  return (
    <div className='pagetitle'>
      <h1>{page}</h1>
      <nav>
        <ol className='breadcrumb'>
          <li className='breadcrumb-item'>
            <a href='/'>
              <i className='bi bi-house-door'></i>
            </a>
          </li>
          <li className='breadcrumb-item active'>{page}</li>
        </ol>
      </nav>
    </div>
  )
}

export default PageTitle
