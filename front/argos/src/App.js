import React from 'react';
import Webcam from "react-webcam";
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
  const [imgSrc, setImgSrc] = React.useState(null);
  const capture = React.useCallback(
    () => {
      const screenshot = webcamRef.current.getScreenshot();
      setImgSrc(screenshot);
      uploadImage(screenshot)
    },
    [webcamRef, setImgSrc]
  );

  return (
    <>
    <Webcam
        audio={false}
        ref={webcamRef}
        screenshotFormat="image/jpeg"
      />
      <button onClick={capture}>Capture photo</button>
      {
        imgSrc && (
          <img src={imgSrc}/>
        )
      }
      </>
  );
}

export default App;
