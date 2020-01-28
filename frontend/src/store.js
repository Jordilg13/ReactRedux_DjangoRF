import { applyMiddleware, createStore } from 'redux';
import { promiseMiddleware, localStorageMiddleware } from './middleware';
import reducer from './reducer';

const getMiddleware = () => {
  return applyMiddleware(promiseMiddleware, localStorageMiddleware)
};

export const store = createStore(
  reducer, getMiddleware());

