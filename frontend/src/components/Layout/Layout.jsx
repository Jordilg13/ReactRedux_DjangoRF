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
import { Switch } from 'react-router-dom';
import { Button, IconButton, Menu, MenuItem, withStyles } from '@material-ui/core';
import AccountCircle from '@material-ui/icons/AccountCircle';
import { connect } from 'react-redux';
import { push } from 'react-router-redux';
import agent from '../../agent';
import useStyles from "./styles"




function ClippedDrawer(props) {
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
        props.onLoad(token ? agent.Auth.current(): null, token)
    },[])


    return (
        <div className={classes.root}>
            <CssBaseline />
            <AppBar position="fixed" className={classes.appBar}>
                <Toolbar>
                    <Typography variant="h6" noWrap>Jordilg Photos</Typography>
                    <div className={classes.toolbarButtons}>
                        {
                            props.token ? (
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
                                </div>)
                                :
                                <Button onClick={() => props.goToLogin()} color="inherit" >Login</Button>
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
                    {['Inbox', 'Starred', 'Send email', 'Drafts'].map((text, index) => (
                        <ListItem button key={text}>
                            <ListItemIcon>{index % 2 === 0 ? <InboxIcon /> : <MailIcon />}</ListItemIcon>
                            <ListItemText primary={text} />
                        </ListItem>
                    ))}
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

                </Switch>

            </main>
        </div>
    );
}
const mapStateToProps = (state) => ({
    ...state.common,
})

const mapDispatchToProps = dispatch => ({
    goToLogin: () =>
        dispatch(push("/login")),
    onLoad: (payload, token) =>
        dispatch({ type: "APP_LOAD", payload, token, skipTracking: true }),
    logout: () =>
        dispatch({type: "LOGOUT"})

})


export default connect(mapStateToProps, mapDispatchToProps)(withStyles(useStyles)(ClippedDrawer))