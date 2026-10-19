import streamlit as st
import cv2
import numpy as np
from streamlit_webrtc import webrtc_streamer, RTCConfiguration, VideoProcessorBase

st.set_page_config(page_title="ChromaCloak AI", page_icon="🧙‍♂️", layout="centered")

st.title("ChromaCloak AI 🧙‍♂️✨")
st.write("Real-time Invisibility Cloak powered by OpenCV & WebRTC.")

st.info("💡 Step away from the camera for 1 second when starting so the background locks cleanly!")

# Google STUN server configuration for stable WebRTC connection
RTC_CONFIGURATION = RTCConfiguration(
    {"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]}
)

class VideoProcessor(VideoProcessorBase):
    def __init__(self):
        self.background = None

    def recv(self, frame):
        img = frame.to_ndarray(format="bgr24")

        # Capture first frame as background baseline
        if self.background is None:
            self.background = img.copy()

        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        # Ultra-strict Red HSV Thresholds to prevent skin bleeding
        lower_red1, upper_red1 = np.array([0, 175, 130]), np.array([6, 255, 255])
        lower_red2, upper_red2 = np.array([174, 175, 130]), np.array([180, 255, 255])

        mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
        mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
        mask = mask1 + mask2

        # Morphological operations for noise reduction
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))
        mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE, np.ones((3, 3), np.uint8))

        mask_inv = cv2.bitwise_not(mask)

        # Segmenting red areas and replacing with background
        res1 = cv2.bitwise_and(img, img, mask=mask_inv)
        res2 = cv2.bitwise_and(self.background, self.background, mask=mask)

        final_output = cv2.addWeighted(res1, 1, res2, 1, 0)

        return frame.from_ndarray(final_output, format="bgr24")

webrtc_streamer(
    key="chromacloak",
    video_processor_factory=VideoProcessor,
    rtc_configuration=RTC_CONFIGURATION,
    media_stream_constraints={"video": True, "audio": False},
)