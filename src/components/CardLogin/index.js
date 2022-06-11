import React, { useState, useRef } from 'react'

import ReCAPTCHA from 'react-google-recaptcha'
import { Container, Card, Form, FormGroup, Button } from 'react-bootstrap'
import { Navigate } from 'react-router-dom'
import './index.css'

const CardLogin = ({ dataLogin }) => {
  const [form, setForm] = useState({
    user: '',
    password: '',
  })
  const [isLogin, setIsLogin] = useState(false)
  const [captchaSelect, setCaptchaSelect] = useState(false)
  const [errorUser, setErrorUser] = useState(false)
  const [errorPassword, setErrorPassword] = useState(false)
  const captcha = useRef(null)

  const handleChangeRecaptcha = () => {
    if (captcha.current.getValue()) {
      setCaptchaSelect(true)
    } else {
      setCaptchaSelect(false)
    }
  }

  const handleChange = (e) => {
    setForm({
      ...form,
      [e.target.name]: e.target.value,
    })
  }

  const handleValidation = () => {
    if (!form.user) {
      setErrorUser(true)
    } else {
      setErrorUser(false)
    }
    if (!form.password) {
      setErrorPassword(true)
    } else {
      setErrorPassword(false)
    }
  }

  const handleSubmit = (e) => {
    handleValidation()
    if (
      dataLogin.find(
        (data) => data.user === form.user && data.password === form.password,
      ) &&
      captchaSelect === true
    ) {
      console.log('HOLA')
      setIsLogin(true)
    } else {
      setIsLogin(false)
    }
  }

  return (
    <Container fluid="sm" className="container-card">
      <Card className="card-login">
        <Card.Header className="title-login">
          <h2>EntreCOL+</h2>
        </Card.Header>
        <Card.Body className="card-body">
          <form className="form-login" onSubmit={handleSubmit}>
            <FormGroup className="form-group">
              <Form.Control
                className="input-user"
                name="user"
                type="text"
                placeholder="User"
                onChange={handleChange}
                value={form.user}
                onInvalid={handleValidation}
                required
              />
            </FormGroup>
            {errorUser ? (
              <span className="message-error-user">Usuario inválido</span>
            ) : (
              <span></span>
            )}
            <FormGroup className="form-group">
              <Form.Control
                className="input-password"
                name="password"
                type="password"
                placeholder="Password"
                onChange={handleChange}
                value={form.password}
                required
              />
            </FormGroup>
            {errorPassword ? (
              <span className="message-error-password">
                Contraseña inválida
              </span>
            ) : (
              <span></span>
            )}
            <FormGroup className="form-group">
              <div className="container-captcha">
                <ReCAPTCHA
                  className="recaptcha"
                  ref={captcha}
                  sitekey="6LdfIiAgAAAAAAsiTC1crac0IB51gacRjYMaW2Dl"
                  onChange={handleChangeRecaptcha}
                />
              </div>
            </FormGroup>
            <FormGroup>
              <Button
                className="button-login"
                variant="primary"
                type="button"
                onClick={handleSubmit}
              >
                Login
              </Button>
              {isLogin ? <Navigate to="/home" /> : null}
            </FormGroup>
          </form>
        </Card.Body>
      </Card>
    </Container>
  )
}

export default CardLogin
