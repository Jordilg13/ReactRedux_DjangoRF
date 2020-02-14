import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import * as serviceWorker from './serviceWorker';

import { Provider } from 'react-redux';

import { store, history } from './store';
import { Route, Switch, Router } from 'react-router-dom';
import { SnackbarProvider } from 'notistack';
// import ConnectedRouter from 'react-router-redux';


ReactDOM.render((

    <Provider store={store}>
        <Router history={history}>
            <Switch>
                <SnackbarProvider maxSnack={2}>
                    <Route path="/" component={App} />
                </SnackbarProvider>
            </Switch>
        </Router>
    </Provider>

), document.getElementById('root')
);

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
