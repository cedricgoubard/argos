import React from 'react';
import Webcam from "react-webcam";
import Container from '@material-ui/core/Container';
import AppBar from '@material-ui/core/AppBar';
import IconButton from '@material-ui/core/IconButton';
import MenuIcon from '@material-ui/icons/Menu'
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';
import Box from '@material-ui/core/Box';
import './App.css';


function uploadImage(img_str) {
  var url_txt = process.env.REACT_APP_BACK_URL + '/webcam';
  var url = new URL(url_txt, window.location.href);

    fetch(url, {
        method: 'POST',
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          img: img_str
        })
    })
    .catch((error) => {
      console.log("Error while fetching :" + error.message);
    });
}

function App() {
  const webcamRef = React.useRef(null);
  const capture = React.useCallback(
    () => {
      const screenshot = webcamRef.current.getScreenshot();
      uploadImage(screenshot)
    },
    [webcamRef]
  );

  return (
    <>
    <Container maxWidth="sm">
      <AppBar position="absolute">
        <Toolbar>
          {/* <IconButton edge="start" color="inherit" aria-label="menu">
            <MenuIcon />
          </IconButton> */}
          <Typography variant="h6" color="inherit" noWrap>
            Argos
          </Typography>
        </Toolbar>
      </AppBar>
      <Box my={4}>
        {/* <Webcam
        audio={false}
        ref={webcamRef}
        screenshotFormat="image/jpeg"
        /> */}

        <button onClick={capture}>Capture photo</button>
      </Box>
    </Container>
      </>
  );
}

export default App;
