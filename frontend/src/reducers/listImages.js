
export default (state = { uploading: false }, action) => {
    // console .log(action);

    switch (action.type) {

        case "GET_USER_IMAGES":
            return {
                ...state,
                images: action.payload
            }
        case "START_UPLOADING_IMAGE":
            console.log("start");

            return {
                ...state,
                uploading: true
            }
        case "FINISH_UPLOADING_IMAGE":
            console.log("end");

            return {
                ...state,
                uploading: false
            }

        default:
            return state
    }
}
