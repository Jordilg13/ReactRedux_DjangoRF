import {LOGIN,REGISTER} from "../constants/actionTypes"
const initialState = {
    token: null
}

export default (state = initialState, action) => {
    console.log("common");

    switch (action.type) {

        case LOGIN:
        case REGISTER:
            
            console.log(action);
            return {
                ...state,
                redirectTo: action.error ? null : '/',
                token: action.error ? null : action.payload.user.token,
                currentUser: action.error ? null : action.payload.user
            };

        default:
            return state
    }
}
