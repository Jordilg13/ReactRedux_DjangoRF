import superagentPromise from 'superagent-promise';
import _superagent from 'superagent';

const superagent = superagentPromise(_superagent, global.Promise);

const API_ROOT = "http://0.0.0.0:8000/api";

// const encode = encodeURIComponent;
const responseBody = res => res.body;

let token = null;
const tokenPlugin = req => {

    if (token) {
        req.set('authorization', `Token ${token}`);
    }
}

const requests = {
    post: (url, body) =>
        superagent.post(`${API_ROOT}${url}`, body).use(tokenPlugin).then(responseBody),
    get: url =>
        superagent.get(`${API_ROOT}${url}`).use(tokenPlugin).then(responseBody),
}

const Auth = {
    current: () =>
        requests.get('/user'),
    login: (email, password) =>
        requests.post("/users/login", { user: { email, password } }),
    register: (username, email, password) =>
        requests.post("/users/register", { user: { username, email, password } })
}


export default {
    Auth,
    setToken: _token => { token = _token; }
}
