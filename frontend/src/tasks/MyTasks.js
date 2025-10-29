import React from 'react';
import { Container, Row, Col } from 'react-bootstrap';
import styles from '../styles/MyTasks.module.css';

const MyTasks = () => {
  return (
    <Container className={styles.Container}>
        <h1 className="text-center">My tasks</h1>
      <Row>
        <Col className={styles.Column}><h3 className={styles.Header}>To do</h3></Col>
        <Col className={styles.Column}><h3 className={styles.Header}>In progress</h3></Col>
        <Col className={styles.Column}><h3 className={styles.Header}>Complete</h3></Col>
        <Col className={styles.Column}><h3 className={styles.Header}>Overdue</h3></Col>
      </Row>
    </Container>
  )
}

export default MyTasks