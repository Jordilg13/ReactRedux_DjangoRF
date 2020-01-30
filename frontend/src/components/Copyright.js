import React from 'react'
import { Typography, Link } from "@material-ui/core";

export default function Copyright() {
    return (
        <Typography variant="body2" color="textSecondary" align="center">
            {'Copyright © '}
            <Link color="inherit" href="http://0.0.0.0:8000/">
                Jordilg Photos
        </Link>{' '}
            {new Date().getFullYear()}
            {'.'}
        </Typography>
    );
}