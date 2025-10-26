import React from "react";
import { Link } from "react-router-dom";
import styles from "../../styles/SignInUpForm.module.css";
import appStyles from "../../App.module.css";
import btnStyles from "../../styles/Button.module.css";
import { Form, Button, Col, Row, Container } from "react-bootstrap";

const SignUpForm = () => {
  return (
    <Container className={`${styles.Container} mt-5`}>
      <Row className="justify-content-md-center">
        <Col md={6}>
          <h1 className={styles.Header}>Sign Up</h1>
          <Form>
            <Form.Group controlId="username" className="mb-3">
              <Form.Label className="d-none">Username</Form.Label>
              <Form.Control className={styles.Input} type="text" placeholder="Enter username" name="username" />
            </Form.Group>

            <Form.Group controlId="password1" className="mb-3">
              <Form.Label className="d-none">Password</Form.Label>
              <Form.Control className={styles.Input} type="password" placeholder="Enter password" name="password1"/>
            </Form.Group>

            <Form.Group controlId="password2" className="mb-4">
              <Form.Label className="d-none">Confirm Password</Form.Label>
              <Form.Control className={styles.Input} type="password" placeholder="Confirm password" name="password2"/>
            </Form.Group>

            <Button className={btnStyles.Btn} type="submit">
              Create Account
            </Button>
          </Form>
          <Container className={`mt-3 ${appStyles.Content}`}>
            {/* ↓↓↓ CREDIT: Code Institute Moments Project ↓↓↓*/}
          <Link class={styles.Link} to="/signin">
            Already have an account? <span>Sign in</span>
          </Link>
          {/* ↑↑↑ CREDIT: Code Institute Moments Project ↑↑↑*/}
        </Container>
        </Col>
      </Row>
    </Container>
  );
};

export default SignUpForm;
