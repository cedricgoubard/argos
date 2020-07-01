import React from 'react';
import Webcam from "react-webcam";
import './App.css';

function App() {
  const webcamRef = React.useRef(null);
  const [imgSrc, setImgSrc] = React.useState(null);
  const capture = React.useCallback(
    () => {
      const screenshot = webcamRef.current.getScreenshot();
      setImgSrc(screenshot);
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
