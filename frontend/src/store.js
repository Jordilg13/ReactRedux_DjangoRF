import { applyMiddleware, createStore } from 'redux';
import { promiseMiddleware, localStorageMiddleware } from './middleware';
import reducer from './reducer';
// import createHistory from 'history/createBrowserHistory';
import { createBrowserHistory as createHistory } from 'history'
import { routerMiddleware } from 'react-router-redux'

export const history = createHistory();
const myRouterMiddleware = routerMiddleware(history);

const getMiddleware = () => {
  return applyMiddleware(myRouterMiddleware, promiseMiddleware, localStorageMiddleware)
};

export const store = createStore(
  reducer, getMiddleware());

