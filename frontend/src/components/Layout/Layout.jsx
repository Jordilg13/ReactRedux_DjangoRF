import React, { useEffect } from 'react';
import Drawer from '@material-ui/core/Drawer';
import AppBar from '@material-ui/core/AppBar';
import CssBaseline from '@material-ui/core/CssBaseline';
import Toolbar from '@material-ui/core/Toolbar';
import List from '@material-ui/core/List';
import Typography from '@material-ui/core/Typography';
import Divider from '@material-ui/core/Divider';
import ListItem from '@material-ui/core/ListItem';
import ListItemIcon from '@material-ui/core/ListItemIcon';
import ListItemText from '@material-ui/core/ListItemText';
import InboxIcon from '@material-ui/icons/MoveToInbox';
import MailIcon from '@material-ui/icons/Mail';
import { Switch, Route } from 'react-router-dom';
import { Button, IconButton, Menu, MenuItem, withStyles, Link, Badge, InputBase } from '@material-ui/core';
import AccountCircle from '@material-ui/icons/AccountCircle';
import { connect } from 'react-redux';
import { push } from 'react-router-redux';
import agent from '../../agent';
import useStyles from "./styles"
import ListPhotos from '../Photos/ListPhotos';
import PhotoSizeSelectActualOutlinedIcon from '@material-ui/icons/PhotoSizeSelectActualOutlined';
import SearchIcon from '@material-ui/icons/Search';
import UploadPhoto from '../Photos/UploadPhoto';



function Layout(props) {
    const classes = props.classes
    const [anchorEl, setAnchorEl] = React.useState(null);
    const open = Boolean(anchorEl);

    const handleMenu = event => {
        setAnchorEl(event.currentTarget);
    };

    const handleClose = () => {
        setAnchorEl(null);
    };

    useEffect(() => {
        // componentWillMount
        const token = window.localStorage.getItem("jwt")
        if (token) {
            agent.setToken(token);
        }
        props.onLoad(token ? agent.Auth.current() : null, token)
    }, [])


    return (
        <div className={classes.root}>
            <CssBaseline />
            <AppBar position="fixed" className={classes.appBar}>
                <Toolbar >
                    <Typography variant="h6" noWrap >
                        <Link href="/" color="inherit" style={{ textDecoration: 'none', marginLeft: "35px" }}>
                            Jordilg Photos
                    </Link>
                    </Typography>
                    <div className={classes.search}>
                        <div className={classes.searchIcon}>
                            <SearchIcon />
                        </div>
                        <InputBase
                            placeholder="Search…"
                            classes={{
                                root: classes.inputRoot,
                                input: classes.inputInput,
                            }}
                            inputProps={{ 'aria-label': 'search' }}
                        />
                    </div>

                   <UploadPhoto></UploadPhoto>


                    <div className={classes.sectionDesktop}>

                        {
                            props.token ? (
                                // LOGGED USER
                                <>

                                    <Typography variant="h6" style={{ marginTop: "7px" }} >{props.currentUser.username}</Typography>
                                    <div>
                                        <IconButton
                                            aria-label="account of current user"
                                            aria-controls="menu-appbar"
                                            aria-haspopup="true"
                                            onClick={handleMenu}
                                            color="inherit"
                                        >
                                            <AccountCircle />
                                        </IconButton>
                                        <Menu
                                            id="menu-appbar"
                                            anchorEl={anchorEl}
                                            anchorOrigin={{
                                                vertical: 'top',
                                                horizontal: 'right',
                                            }}
                                            keepMounted
                                            transformOrigin={{
                                                vertical: 'top',
                                                horizontal: 'right',
                                            }}
                                            open={open}
                                            onClose={handleClose}
                                        >
                                            <MenuItem onClick={handleClose}>Profile</MenuItem>
                                            <MenuItem onClick={handleClose}>My account</MenuItem>
                                            <MenuItem onClick={handleClose} onClick={props.logout}>Logout</MenuItem>
                                        </Menu>
                                    </div></>)
                                :
                                // NOT LOGGED
                                <Button onClick={() => props.goTo("/login")} color="inherit" >Login</Button>
                        }
                    </div>
                </Toolbar>
            </AppBar>
            <Drawer
                className={classes.drawer}
                variant="permanent"
                classes={{
                    paper: classes.drawerPaper,
                }}
            >
                <div className={classes.toolbar} />
                <List>
                    <ListItem button key="1" onClick={() => props.goTo("/photos")}>
                        <ListItemIcon><PhotoSizeSelectActualOutlinedIcon /></ListItemIcon>
                        <ListItemText primary="Photos" />
                    </ListItem>
                </List>
                <Divider />
                <List>
                    {['All mail', 'Trash', 'Spam'].map((text, index) => (
                        <ListItem button key={text}>
                            <ListItemIcon>{index % 2 === 0 ? <InboxIcon /> : <MailIcon />}</ListItemIcon>
                            <ListItemText primary={text} />
                        </ListItem>
                    ))}
                </List>
            </Drawer>
            <main className={classes.content}>
                <div className={classes.toolbar} />

                <Switch>
                    <Route path="/photos" component={ListPhotos}></Route>
                    {/* <Route path="/register" component={Register}></Route> */}
                </Switch>

            </main>
        </div>
    );
}
const mapStateToProps = (state) => ({
    ...state.common,
})

const mapDispatchToProps = dispatch => ({
    goTo: (url) =>
        dispatch(push(url)),
    onLoad: (payload, token) =>
        dispatch({ type: "APP_LOAD", payload, token }),
    logout: () =>
        dispatch({ type: "LOGOUT" })

})


export default connect(mapStateToProps, mapDispatchToProps)(withStyles(useStyles)(Layout))