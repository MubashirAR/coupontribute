import React, { Suspense } from "react";
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";
import Navbar from "../Components/Navbar";
import Coupons from "./Coupons";
import Home from "./Home";

import Login from "./Login";
import Orders from "./Orders";
import Payments from "./Payments";
import Profile from "./Profile";
import Register from "./Register";


export default () => {
  return (
    <Router>
      <div className="full-height">
        <Navbar />
        {/* A <Switch> looks through its children <Route>s and
              renders the first one that matches the current URL. */}
        <Switch>
          <Route path="/profile">
            <Profile />
          </Route>
          <Route path="/coupons">
            <Coupons />
          </Route>
          <Route path="/payments">
            <Payments />
          </Route>
          <Route path="/orders">
            <Orders />
          </Route>
          <Route path="/register">
            <Register />
          </Route>
          <Route path="/login">
            <Login />
          </Route>
          <Route path="/">
            <Home />
          </Route>
        </Switch>
      </div>
    </Router>
  );
}
