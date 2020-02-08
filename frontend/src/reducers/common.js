import {
    LOGIN,
    REGISTER,
    REGISTER_PAGE_UNLOADED,
    LOGOUT,
    APP_LOAD
} from "../constants/actionTypes"

const initialState = {
    token: null,
    currentUser: null,
}

export default (state = initialState, action) => {
    switch (action.type) {

        case APP_LOAD:
            return {
                ...state,
                token: action.token || null,
                appLoaded: true,
                currentUser: action.payload ? action.payload.user : null
            };

        case LOGOUT:
            return { 
                ...state, 
                redirectTo: '/', 
                token: null, 
                currentUser: null };

        case LOGIN:
        case REGISTER:
            return {
                ...state,
                redirectTo: action.error ? null : '/',
                token: action.error ? null : action.payload.user.token,
                currentUser: action.error ? null : action.payload.user
            };

        case REGISTER_PAGE_UNLOADED:
            return { ...state };

        default:
            return state
    }
}
