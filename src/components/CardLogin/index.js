import React, { useRef } from 'react'

import ReCAPTCHA from 'react-google-recaptcha'
import { Container, Card, Form, FormGroup, Button } from 'react-bootstrap'

import './index.css'

const CardLogin = () => {
  const captcha = useRef(null)

  const handleChange = () => {
    if (captcha.current.getValue()) {
      console.log('No es un robot')
    }
  }

  return (
    <Container fluid="sm" className="container-card">
      <Card className="card-login">
        <Card.Header className="title-login">
          <h2>EntreCOL+</h2>
        </Card.Header>
        <Card.Body className="card-body">
          <Form className="form-login">
            <FormGroup className="form-group">
              <Form.Control
                className="input-user"
                type="text"
                placeholder="User"
              />
            </FormGroup>
            <FormGroup className="form-group">
              <Form.Control
                className="input-password"
                type="password"
                placeholder="Password"
              />
            </FormGroup>
            <FormGroup className="form-group">
              <div className="container-captcha">
                <ReCAPTCHA
                  className="recaptcha"
                  ref={captcha}
                  sitekey="6LdfIiAgAAAAAAsiTC1crac0IB51gacRjYMaW2Dl"
                  onChange={handleChange}
                />
              </div>
            </FormGroup>
            <FormGroup>
              <Button className="button-login" variant="primary" type="button">
                Login
              </Button>
            </FormGroup>
          </Form>
        </Card.Body>
      </Card>
    </Container>
  )
}

export default CardLogin
