import React, { Component } from 'react'
import PublishIcon from '@material-ui/icons/Publish';
import { Button } from '@material-ui/core';
import { connect } from 'react-redux'
import agent from '../../agent';
import { SnackbarProvider, useSnackbar, withSnackbar } from 'notistack';
import { Snackbar } from "../Common/SnackBar"


class UploadPhoto extends Component {
    constructor() {
        super()

        this.state = {

        }


        this.onChange = (e) => {
            this.props.enqueueSnackbar("Uploading...")
            var formData = new FormData()
            formData.append("image", e.target.files[0])
            // agent.Images.send(formData)
            this.props.uploadImage(formData)


        }
    }

    // componentDidMount() {
    //     console.log("DIDMOUNT");
    // }
    // replaces componentWillReceiveProps that is deprecated
    static getDerivedStateFromProps(nextProps, prevProps) {

        // if is uploaded shows the success snackbar
        if (nextProps.uploading !== prevProps.uploading && nextProps.uploading) {
            nextProps.enqueueSnackbar("Succesfully uploaded", {
                variant: 'success',
            })
        }
        return nextProps
    }

    render() {
        return (
            <div>
                <Button
                    variant="text"
                    component="label"
                    color="inherit"
                >
                    <PublishIcon></PublishIcon>
                    Upload File
                    <input
                        type="file"
                        style={{ display: "none" }}
                        // onChange={this.onChange}
                        onChange={this.onChange}
                        encType="multipart/form-data"
                    />
                </Button>
            </div>
        )
    }
}

const mapStateToProps = (state) => ({
    ...state.listimages
})

const mapDispatchToProps = dispatch => ({
    uploadImage: (formdata) =>
        dispatch({
            type: "UPLOAD_IMAGE",
            image: agent.Images.send(formdata)
        }),
    getImages: () =>
        dispatch({
            type: "GET_USER_IMAGES",
            payload: agent.Images.list()
        }),
})

export default connect(mapStateToProps, mapDispatchToProps)(withSnackbar(UploadPhoto))
