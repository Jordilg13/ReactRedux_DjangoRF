import React, { Component } from 'react'
import { connect } from 'react-redux'
import Gallery from 'react-grid-gallery';
import { Input, Button } from '@material-ui/core';

export class ListPhotos extends Component {
    constructor() {
        super();
        this.state = {
            pictures: {}
        };
    }

    onChange = (pictures) => this.setState({pictures});

    render() {

        let ph = [{
            src: "https://c2.staticflickr.com/9/8356/28897120681_3b2c0f43e0_b.jpg",
            thumbnail: "https://c2.staticflickr.com/9/8356/28897120681_3b2c0f43e0_b.jpg",
            thumbnailWidth: 320,
            thumbnailHeight: 174,
            isSelected: true,
            caption: "After Rain (Jeshu John - designerspics.com)"
        },
        {
            src: "https://c2.staticflickr.com/9/8356/28897120681_3b2c0f43e0_b.jpg",
            thumbnail: "https://c2.staticflickr.com/9/8356/28897120681_3b2c0f43e0_n.jpg",
            thumbnailWidth: 320,
            thumbnailHeight: 212,
            tags: [{ value: "Ocean", title: "Ocean" }, { value: "People", title: "People" }],
            caption: "Boats (Jeshu John - designerspics.com)"
        },

        {
            src: "https://c4.staticflickr.com/9/8887/28897124891_98c4fdd82b_b.jpg",
            thumbnail: "https://c4.staticflickr.com/9/8887/28897124891_98c4fdd82b_n.jpg",
            thumbnailWidth: 320,
            thumbnailHeight: 212
        }]
        return (
            <div>
                <h1>List Photos</h1>


                
                <Gallery images={ph}></Gallery>
            </div>
        )
    }
}

const mapStateToProps = (state) => ({
    ...state
})

const mapDispatchToProps = {

}

export default connect(mapStateToProps, mapDispatchToProps)(ListPhotos)
