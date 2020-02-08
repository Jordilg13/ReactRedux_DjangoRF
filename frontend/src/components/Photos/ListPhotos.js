import React, { Component, useEffect, useState } from 'react'
import { connect, useSelector } from 'react-redux'
import Gallery from 'react-grid-gallery';
import { Input, Button } from '@material-ui/core';
import agent from '../../agent';


const mapStateToProps = (state) => ({ ...state.listimages });

// TODO: loader until images are llisted
const mapDispatchToProps = (dispatch) => ({
    getImages: () =>
        dispatch({
            type: "GET_USER_IMAGES",
            payload: agent.Images.list()
        })
});

function ListPhotos(props) {

    // const [ph, setph] = useState(props.images)
    console.log(props);

    useEffect(() => {
        const token = window.localStorage.getItem("jwt")
        if (token) {
            agent.setToken(token);
        }
        props.getImages()

    }, [])

    if (props.hasOwnProperty("images")) {
        var images = []
        var tags = []
        for (let i of props.images.results) {
            tags = []
            for (const tag of i.tags) {
                tags.push({
                    value: tag,
                    title: tag
                })

            }

            images.push({
                src: `data:image/png;base64,${i.base64_image}`,
                thumbnail: `data:image/png;base64,${i.base64_image}`,
                thumbnailWidth: i.size.width / 2,
                thumbnailHeight: i.size.height / 2,
                tags:tags
            })
            console.log(images);

        }
    }

    // let ph = [{
    //     src: "https://c2.staticflickr.com/9/8356/28897120681_3b2c0f43e0_b.jpg",
    //     thumbnail: "https://c2.staticflickr.com/9/8356/28897120681_3b2c0f43e0_b.jpg",
    //     thumbnailWidth: 320,
    //     thumbnailHeight: 174,
    //     isSelected: true,
    //     caption: "After Rain (Jeshu John - designerspics.com)"
    // },
    // {
    //     src: "https://c2.staticflickr.com/9/8356/28897120681_3b2c0f43e0_b.jpg",
    //     thumbnail: "https://c2.staticflickr.com/9/8356/28897120681_3b2c0f43e0_n.jpg",
    //     thumbnailWidth: 320,
    //     thumbnailHeight: 212,
    //     tags: [{ value: "Ocean", title: "Ocean" }, { value: "People", title: "People" }],
    //     caption: "Boats (Jeshu John - designerspics.com)"
    // },

    // {
    //     src: "https://c4.staticflickr.com/9/8887/28897124891_98c4fdd82b_b.jpg",
    //     thumbnail: "https://c4.staticflickr.com/9/8887/28897124891_98c4fdd82b_n.jpg",
    //     thumbnailWidth: 320,
    //     thumbnailHeight: 212
    // }]

    console.log(props.images)
    return (
        <div>
            <h1>Photos</h1>
            {
                props.hasOwnProperty("images") && props.images.count > 0 ? (
                    // <h1>{(images)}</h1>
                    <Gallery images={images} key="sad"></Gallery>
                ) : (
                        <h3>You don't have any images, you can upload one clicking at the button on the topside.</h3>
                    )
            }

        </div>
    )
}



export default connect(mapStateToProps, mapDispatchToProps)(ListPhotos)
