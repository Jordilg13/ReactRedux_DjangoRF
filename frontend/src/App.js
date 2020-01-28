import React from 'react';
import './App.css';
import { Route, Switch } from 'react-router-dom';
import Login from "./components/Login/Login"
import Register from './components/Register';
import Home from "./components/Home"
import Layout from "./components/Layout/Layout"

function App() {
  return (
    <div>
      <Switch>
        <Route exact path="/" component={Layout}></Route>
        <Route path="/login" component={Login}></Route>
        <Route path="/register" component={Register}></Route>
      </Switch>

    </div>
  );
}

export default App;
