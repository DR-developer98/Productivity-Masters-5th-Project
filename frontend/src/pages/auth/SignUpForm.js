import React from "react";

const SignUpForm = () => {
  return (
    <Container className="mt-5">
      <Row className="justify-content-md-center">
        <Col md={6}>
          <h1 className="text-center mb-4">Sign Up</h1>
          <Form>
            <Form.Group controlId="formName" className="mb-3">
              <Form.Label>Username</Form.Label>
              <Form.Control type="text" placeholder="Enter your username" />
            </Form.Group>

            <Form.Group controlId="formPassword" className="mb-3">
              <Form.Label>Password</Form.Label>
              <Form.Control type="password" placeholder="Enter password" />
            </Form.Group>

            <Form.Group controlId="formConfirmPassword" className="mb-4">
              <Form.Label>Confirm Password</Form.Label>
              <Form.Control type="password" placeholder="Confirm password" />
            </Form.Group>

            <Button variant="primary" type="submit" className="w-100">
              Create Account
            </Button>
          </Form>
        </Col>
      </Row>
    </Container>
  );
};

export default SignUpForm;
