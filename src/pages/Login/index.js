import React, { useState } from 'react'

import CardLogin from '../../components/CardLogin'

import './index.css'

const loginDB = [
  {
    id: 1,
    user: 'user',
    password: '123456',
  },
  {
    id: 2,
    user: 'user1',
    password: '123456',
  },
]
const Login = () => {
  const [dataLogin, setDataLogin] = useState(loginDB)

  return (
    <div className="container-login">
      <CardLogin dataLogin={dataLogin} />
    </div>
  )
}

export default Login
