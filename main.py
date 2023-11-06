import streamlit as st

st.title("Mobile Camera Access with Streamlit")

html_code = """
<!DOCTYPE html>
<html>
<head>
    <title>Camera Access</title>
</head>
<body>
    <h1>Mobile Camera Access</h1>
    <video id="cameraFeed" autoplay></video>
    <button id="startButton">Start Camera</button>
    <button id="stopButton">Stop Camera</button>

    <script>
        const videoElement = document.getElementById('cameraFeed');
        const startButton = document.getElementById('startButton');
        const stopButton = document.getElementById('stopButton');

        async function startCamera() {
            try {
                const stream = await navigator.mediaDevices.getUserMedia({ video: true });
                videoElement.srcObject = stream;
            } catch (error) {
                console.error('Error accessing camera:', error);
            }
        }

        function stopCamera() {
            const stream = videoElement.srcObject;
            if (stream) {
                const tracks = stream.getTracks();
                tracks.forEach(track => track.stop());
                videoElement.srcObject = null;
            }
        }

        startButton.addEventListener('click', startCamera);
        stopButton.addEventListener('click', stopCamera);
    </script>
</body>
</html>
"""

st.components.v1.html(html_code)
