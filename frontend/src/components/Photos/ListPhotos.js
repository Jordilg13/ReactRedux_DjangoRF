import React, { Component, useEffect, useState } from 'react'
import { connect, useSelector } from 'react-redux'
import Gallery from 'react-grid-gallery';
import { Input, Button } from '@material-ui/core';
import agent from '../../agent';
import { push } from 'react-router-redux';
import toastr from 'toastr'
import 'toastr/build/toastr.min.css'



const mapStateToProps = (state) => ({ ...state.listimages });

// TODO: loader until images are llisted
const mapDispatchToProps = (dispatch) => ({
    getImages: () =>
        dispatch({
            type: "GET_USER_IMAGES",
            payload: agent.Images.list()
        }),
    goTo: (url) =>
        dispatch(push(url))
});

function ListPhotos(props) {

    // similar to componentwillmount with functional components
    useEffect(() => {
        console.log(props);

        const token = window.localStorage.getItem("jwt")
        if (token) {
            agent.setToken(token);
            props.getImages()
        } else {
            toastr.error(`You should be logged to see the images`)
            props.goTo("/login")
        }
    }, [props.uploading]) // checks if there are any new photo to reload the list

    function myTileViewportStyleFn(index) {
        console.log(this._gallery.children[index+1]);
    }


    let printPhotos = () => {
        if (props.hasOwnProperty("images")) {
            if (props.images !== null) {
                return <Gallery
                    images={images}
                    key="sad"
                    backdropClosesModal={true}
                    lightboxWillOpen={myTileViewportStyleFn}
                ></Gallery>
            }
        }
        return <h3>You don't have any images, you can upload one clicking the button on the topside.</h3>
    }


    // check if the images are setted in the store
    if (props.hasOwnProperty("images")) {
        if (props.images !== null) {


            var images = []
            var tags = []
            // generate the data in the gallery format
            for (let i of props.images.results) {
                tags = []
                // data of tags
                for (const tag of i.tags) {
                    tags.push({
                        value: tag,
                        title: tag
                    })
                }

                // data of the images
                // TODO: change the extension of the image, but still working
                images.push({
                    src: `data:image/png;base64,${i.base64_image}`,
                    thumbnail: `data:image/png;base64,${i.base64_image}`,
                    thumbnailWidth: i.size.width / 2,
                    thumbnailHeight: i.size.height / 2,
                    tags: tags,
                    papaaaa: true,
                })

            }
        }

    }

    return (
        <div>
            <h1>Photos</h1>
            {
                printPhotos()
            }

        </div>
    )
}


export default connect(mapStateToProps, mapDispatchToProps)(ListPhotos)
