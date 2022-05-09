import React from "react";
import { Container, Navbar, Nav, Row } from "react-bootstrap";

function header() {
  return (
    <header>
      <Navbar bg="dark" variant="dark" expand="lg" collapseOnSelect>
        <Container>
          <Navbar.Brand href="/">ProShop</Navbar.Brand>
          <Navbar.Toggle aria-controls="basic-navbar-nav" />
          <Navbar.Collapse id="basic-navbar-nav">
            <Nav className="me-auto">
              <Nav.Link href="/cart">
                <i className="fas fa-shopping-cart"></i>
                &nbsp;Cart
              </Nav.Link>
              <Nav.Link href="/login">
                <i className="fas fa-user"></i>
                &nbsp;Login
              </Nav.Link>
            </Nav>
          </Navbar.Collapse>
        </Container>
      </Navbar>
    </header>
  );
}

export default header;
