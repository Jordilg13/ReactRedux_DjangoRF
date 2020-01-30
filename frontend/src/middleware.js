import agent from './agent';
import {
  ASYNC_START,
  ASYNC_END,
  LOGIN,
  LOGOUT,
  REGISTER
} from './constants/actionTypes';
import { push } from 'react-router-redux';

// Promise middleware, sets the state in progress while the promise is not solved
const promiseMiddleware = store => next => action => {

  if (isPromise(action.payload)) {
    console.log(action);
    
    store.dispatch({ type: ASYNC_START, subtype: action.type });

    const currentView = store.getState().viewChangeCounter;  
    const skipTracking = action.skipTracking;

    action.payload.then(
      res => {        
        console.log('RESULT', res);
        const currentState = store.getState()
        if (!skipTracking && currentState.viewChangeCounter !== currentView) {
          return
        }

        action.payload = res;
        store.dispatch({ type: ASYNC_END, promise: action.payload });
        store.dispatch(action);
        // redirect to home
        if (action.type === "LOGIN" || action.type === "REGISTER") {
          store.dispatch(push("/"))
          
        }
        
      },
      error => {
        console.log('ERROR', error);
        const currentState = store.getState()
        if (!skipTracking && currentState.viewChangeCounter !== currentView) {
          return
        }
        action.error = true;
        action.payload = error.response.body;
        if (!action.skipTracking) {
          store.dispatch({ type: ASYNC_END, promise: action.payload });
        }
        store.dispatch(action);
      }
    );

    return;
  }

  next(action);
};

const localStorageMiddleware = store => next => action => {

  if (action.type === REGISTER || action.type === LOGIN) {
    if (!action.error) {
      window.localStorage.setItem('jwt', action.payload.user.token);
      agent.setToken(action.payload.user.token);
    }
  } else if (action.type === LOGOUT) {
    window.localStorage.setItem('jwt', '');
    agent.setToken(null);
  }

  next(action);
};

function isPromise(v) { 
  return v && typeof v.then === 'function';
}


export { promiseMiddleware, localStorageMiddleware }
