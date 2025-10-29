import React from "react";
import { Form, Button, Container, Row, Col } from "react-bootstrap";
import btnStyles from "../styles/Button.module.css";

const TaskCreateForm = () => {
  return (
    <Container className={"mt-5"}>
      <Row className="justify-content-md-center">
        <Col md={6}>
          <h1>Create a new task</h1>
          <Form>
            <Form.Group controlId="title">
              <Form.Label className="d-none">Title</Form.Label>
              <Form.Control
                type="text"
                name="title"
                required
                placeholder="Enter a title"
              />
            </Form.Group>
            <Form.Group controlId="description">
              <Form.Label className="d-none">Description</Form.Label>
              <Form.Control
                as="textarea"
                rows={3}
                name="description"
                placeholder="Description of the task"
                required
              />
            </Form.Group>
            <Form.Group controlId="due_date">
              <Form.Label>Due Date</Form.Label>
              <Form.Control type="datetime-local" name="due_date" required />
            </Form.Group>
            <Form.Group controlId="priority">
              <Form.Label>Priority</Form.Label>
              <Form.Control as="select" name="priority">
                <option value="high">High</option>
                <option value="medium">Medium</option>
                <option value="low">Low</option>
              </Form.Control>
            </Form.Group>

            <Form.Group controlId="state">
              <Form.Label>Status</Form.Label>
              <Form.Control as="select" name="state">
                <option value="open">Open</option>
                <option value="in_progress">In progress</option>
                <option value="done">Complete</option>
                <option value="overdue">Overdue</option>
              </Form.Control>
            </Form.Group>
            <div className="d-flex gap-2 mt-3">
              <Button className={`${btnStyles.Btn} mr-1`}>Cancel</Button>
              <Button className={`${btnStyles.Btn} ml-1`} type="submit">
                Create Task
              </Button>
            </div>
          </Form>
        </Col>
      </Row>
    </Container>
  );
};

export default TaskCreateForm;
