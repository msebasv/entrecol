import React from 'react'
import Sidebar from '../../components/Sidebar'

import './index.css'

const Movie = () => {
  return (
    <div className="container-movie">
      <Sidebar />
      <div className="content">
        <h2>MOVIE</h2>
      </div>
    </div>
  )
}

export default Movie
