import cv2
import numpy as np
import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoTransformerBase, WebRtcMode

st.set_page_config(page_title="ChromaCloak AI", page_icon="🧙‍♂️", layout="centered")

st.title("ChromaCloak AI 🧙‍♂️✨")
st.write("Real-time Invisibility Cloak powered by OpenCV & WebRTC.")

class CloakTransformer(VideoTransformerBase):
    def __init__(self):
        self.bg_frame = None

    def transform(self, frame):
        # Convert WebRTC frame to OpenCV BGR format
        img = frame.to_ndarray(format="bgr24")
        img = np.flip(img, axis=1)

        # Automatically capture the initial baseline frame as background
        if self.bg_frame is None:
            self.bg_frame = img.copy()

        # HSV Color Transformation
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

       # Tightened Red HSV Thresholding to avoid skin tone overlap
        lower_red1, upper_red1 = np.array([0, 150, 100]), np.array([10, 255, 255])
        lower_red2, upper_red2 = np.array([170, 150, 100]), np.array([180, 255, 255])
        mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
        mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
        mask = mask1 + mask2

        # Morphological Noise Filtering
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        mask = cv2.dilate(mask, kernel, iterations=2)

        mask_inv = cv2.bitwise_not(mask)

        # Bitwise Compositing
        res_bg = cv2.bitwise_and(self.bg_frame, self.bg_frame, mask=mask)
        res_frame = cv2.bitwise_and(img, img, mask=mask_inv)

        return cv2.addWeighted(res_bg, 1, res_frame, 1, 0)

# Streamlit UI Controls
st.info("💡 Step away from the camera for 1 second when starting so the background locks cleanly!")

webrtc_streamer(
    key="chromacloak-stream",
    mode=WebRtcMode.SENDRECV,
    video_transformer_factory=CloakTransformer,
    media_stream_constraints={"video": True, "audio": False},
    async_transform=True,
)