import React from 'react';
import './App.css';
import { Route, Switch } from 'react-router-dom';
import Login from "./components/Auth/Login"
import Register from './components/Auth/Register';
import Home from "./components/Home"
import Layout from "./components/Layout/Layout"

function App() {
  return (
    <div>
      <Switch>
        <Route path="/login" component={Login}></Route>
        <Route path="/register" component={Register}></Route>
        <Route path="/" component={Layout}></Route>
      </Switch>
      {/* <Layout></Layout> */}

    </div>
  );
}

export default App;
