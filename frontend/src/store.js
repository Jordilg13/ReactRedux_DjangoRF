import { applyMiddleware, createStore } from 'redux';
import { promiseMiddleware, localStorageMiddleware } from './middleware';
import { composeWithDevTools } from 'redux-devtools-extension/developmentOnly';
import reducer from './reducer';
import { createBrowserHistory as createHistory } from 'history'
import { routerMiddleware } from 'react-router-redux'


export const history = createHistory();
const myRouterMiddleware = routerMiddleware(history);

export const store = createStore(
  reducer,
  composeWithDevTools(applyMiddleware(myRouterMiddleware, promiseMiddleware, localStorageMiddleware)),
  
);

