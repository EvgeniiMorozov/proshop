import React, { useState } from "react";
import { Button, Form, FormControl } from "react-bootstrap";
import { useNavigate } from "react-router-dom";

function SearchBox() {
  const navigate = useNavigate();

  const [keyword, setKeyword] = useState("");

  const submitHandler = (e) => {
    e.preventDefault();
    if (keyword) {
      navigate(`/?keyword=${keyword}`);
    } else {
      // navigate()
    }
  };
  return (
    <Form className="d-flex" onSubmit={submitHandler}>
      <FormControl
        type="search"
        placeholder="Search"
        className="me-2"
        aria-label="Search"
        onChange={(e) => setKeyword(e.target.value)}
      />
      <Button variant="outline-success">Search</Button>
    </Form>
  );
}

export default SearchBox;
