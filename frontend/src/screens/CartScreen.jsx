import React, { useEffect } from "react";
import { Link, useParams, useLocation, useNavigate } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";
import {
  Col,
  Row,
  ListGroup,
  Image,
  Form,
  Button,
  Card,
} from "react-bootstrap";
import Message from "../components/Message";
import { addToCart } from "../actions/cartActions";

function CartScreen() {
  const location = useLocation();
  const navigate = useNavigate();
  const params = useParams();
  const productId = params.id;
  const qty = location.search;
  console.log(qty);

  return <div>Cart</div>;
}

export default CartScreen;
