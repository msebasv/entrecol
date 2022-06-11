import React from 'react'
import Sidebar from '../../components/Sidebar'

import './index.css'

const Home = () => {
  return (
    <div className="container-home">
      <Sidebar />
      <div className="content">
        <h1>Welcome User!</h1>
      </div>
    </div>
  )
}

export default Home
