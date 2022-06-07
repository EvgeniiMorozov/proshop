import React, { useState } from "react";
import { Button, Form } from "react-bootstrap";
import { useLocation, useNavigate } from "react-router-dom";

function SearchBox() {
  const navigate = useNavigate();
  const location = useLocation();

  const [keyword, setKeyword] = useState("");

  const submitHandler = (e) => {
    e.preventDefault();
    if (keyword) {
      navigate(`/?keyword=${keyword}`);
    } else {
      navigate(navigate(location.pathname));
    }
  };
  return (
    <Form className="d-flex" onSubmit={submitHandler}>
      <Form.Control
        type="text"
        name="searchBox"
        placeholder="Search"
        className="me-2"
        onChange={(e) => setKeyword(e.target.value)}
      ></Form.Control>
      <Button type="submit" variant="outline-success">
        Search
      </Button>
    </Form>
  );
}

export default SearchBox;
