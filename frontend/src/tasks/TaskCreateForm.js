import React, { useState } from "react";
import { Form, Button, Container, Row, Col } from "react-bootstrap";
import btnStyles from "../styles/Button.module.css";
import styles from "../styles/TaskCreateForm.module.css";

const TaskCreateForm = () => {
  const [taskData, setTaskData] = useState({
    title: "",
    description: "",
    due_date: "",
    priority: "medium",
    state: "open",
    category: "",
    owners: [],
  });

  const {title, description, due_date, priority, state, category, owners} = taskData

  const handleChange = (event) => {
    setTaskData({
        ...taskData,
        [event.target.name]: event.target.value
    })
  }

  return (
    <Container className={"mt-2"}>
      <Row className="justify-content-md-center">
        <Col md={6}>
          <h1 className="text-center">Create a new task</h1>
          <Form>
            <Form.Group controlId="title">
              <Form.Label className="d-none">Title</Form.Label>
              <Form.Control
                type="text"
                name="title"
                value={title}
                required
                placeholder="Enter a title"
                onChange = {handleChange}
              />
            </Form.Group>
            <Form.Group controlId="description">
              <Form.Label className="d-none">Description</Form.Label>
              <Form.Control
                as="textarea"
                rows={3}
                value={description}
                name="description"
                placeholder="Description of the task"
                required
                onChange = {handleChange}
              />
            </Form.Group>
            <Form.Group controlId="due_date">
              <Form.Label>Due Date</Form.Label>
              <Form.Control
                value={due_date}
                type="datetime-local"
                name="due_date"
                required
                onChange = {handleChange}
              />
            </Form.Group>
            <Form.Group controlId="priority">
              <Form.Label>Priority</Form.Label>
              <Form.Control
                value={priority}
                as="select"
                name="priority"
                onChange = {handleChange}
              >
                <option value="high">High</option>
                <option value="medium">Medium</option>
                <option value="low">Low</option>
              </Form.Control>
            </Form.Group>

            <Form.Group controlId="state">
              <Form.Label>Status</Form.Label>
              <Form.Control value={state} as="select" name="state" onChange = {handleChange}>
                <option value="open">Open</option>
                <option value="in_progress">In progress</option>
                <option value="done">Complete</option>
                <option value="overdue">Overdue</option>
              </Form.Control>
            </Form.Group>
            <Form.Group controlId="category">
              <Form.Label>Category</Form.Label>
              <Form.Control
                value={category}
                as="select"
                name="category"
                onChange = {handleChange}
              >
                <option value="category1">Category 1</option>
                <option value="category2">Category 2</option>
                <option value="category3">Category 3</option>
                <option value="category4">Category 4</option>
              </Form.Control>
            </Form.Group>
            <Form.Group controlId="owners">
              <Form.Label>Owners</Form.Label>
              <Form.Control
                as="select"
                multiple
                name="owners"
                value={owners}
                onChange = {handleChange}
              >
                <option value="owner1">Owner1</option>
                <option value="owner2">Owner2</option>
              </Form.Control>
            </Form.Group>
            <div className="d-flex gap-2 mt-3">
              <Button className={`${btnStyles.Btn} ${styles.CancelBtn} mr-1`}>
                Cancel
              </Button>
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
