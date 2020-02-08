
export default (state = {}, action) => {
    // console .log(action);

    switch (action.type) {

        case "GET_USER_IMAGES":
            return {
                ...state,
                images: action.payload
            }

        default:
            return state
    }
}
