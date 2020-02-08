import React, { Component } from 'react'
import PublishIcon from '@material-ui/icons/Publish';
import { Button } from '@material-ui/core';
import { connect } from 'react-redux'
import agent from '../../agent';

export class UploadPhoto extends Component {
    constructor(props) {
        super(props)

        this.onChange = (e) => {
            var formData = new FormData()
            formData.append("image", e.target.files[0])
            agent.Images.send(formData)
        }
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
                        onChange={this.onChange}
                        encType="multipart/form-data"
                    />
                </Button>
            </div>
        )
    }
}

const mapStateToProps = (state) => ({
    ...state
})

const mapDispatchToProps = dispatch => ({
    // upladImage: (image) =>
    //     dispatch({
    //         type: "UPLOAD_IMAGE",
    //         image
    //     })
})

export default connect(mapStateToProps, mapDispatchToProps)(UploadPhoto)
