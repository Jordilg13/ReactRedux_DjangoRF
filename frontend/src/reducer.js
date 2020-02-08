import auth from './reducers/auth';
import { combineReducers } from 'redux';
import common from './reducers/common';
import listimages from "./reducers/listImages"
// import { routerReducer } from 'react-router-redux';

export default combineReducers({
  auth,
  common,
  listimages,
  // router: routerReducer
});
