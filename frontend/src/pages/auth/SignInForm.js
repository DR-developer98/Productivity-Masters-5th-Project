import React, { useState } from "react";
import { Link, useHistory } from "react-router-dom";
import styles from "../../styles/SignInUpForm.module.css";
import appStyles from "../../App.module.css";
import btnStyles from "../../styles/Button.module.css";
import { Form, Button, Col, Row, Container } from "react-bootstrap";
import axios from "axios";

const SignInForm = () => {
  const [signInData, setSignInData] = useState({
    username: "",
    password: "",
  });

  const { username, password } = signInData;

  const history = useHistory();

  const handleChange = (event) => {
    setSignInData({
      ...signInData,
      [event.target.name]: event.target.value,
    });
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      await axios.post("/dj-rest-auth/login/", signInData);
      history.push("/");
    } catch (err) {
    }
  };

  return (
    <Container className={`${styles.Container} mt-5`}>
      <Row className="justify-content-md-center">
        <Col md={6}>
          <h1 className={styles.Header}>Sign In</h1>
          <Form onSubmit={handleSubmit}>
            <Form.Group controlId="username" className="mb-3">
              <Form.Label className="d-none">Username</Form.Label>
              <Form.Control
                className={styles.Input}
                type="text"
                placeholder="Enter username"
                name="username"
                value={username}
                onChange={handleChange}
              />
            </Form.Group>

            <Form.Group controlId="password" className="mb-4">
              <Form.Label className="d-none">Password</Form.Label>
              <Form.Control
                className={styles.Input}
                type="password"
                placeholder="Enter Password"
                name="password"
                value={password}
                onChange={handleChange}
              />
            </Form.Group>

            <Button className={btnStyles.Btn} type="submit">
              Sign in
            </Button>

          </Form>
          <Container className={`mt-3 ${appStyles.Content}`}>
            <Link class={styles.Link} to="/signup">
              Haven't registered yet? <span>Sign up</span>
            </Link>
          </Container>
        </Col>
      </Row>
    </Container>
  );
}

export default SignInForm