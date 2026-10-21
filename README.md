# ChromaCloak AI 🧙‍♂️✨

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://chromacloak-ai.streamlit.app)
![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green?style=for-the-badge&logo=opencv)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

A real-time, automated "Invisibility Cloak" web application built using Python, OpenCV, and Streamlit. By utilizing HSV color-space transformation, dual-range masking, and morphological filtering, **ChromaCloak AI** isolates specific color thresholds and seamlessly overlays a static background stream to achieve a smooth invisibility effect.

## 🚀 Live Web Demo
Experience the application directly in your web browser: **[chromacloak-ai.streamlit.app](https://chromacloak-ai.streamlit.app)**

---

## 🎬 Demo Preview

![ChromaCloak AI Demo](assets/demo.gif)

---

## 🌟 Key Features

- **Live WebRTC Video Streaming:** Low-latency, browser-based camera frame processing using `streamlit-webrtc`.
- **Instant Background Capture:** Dynamic baseline calibration to lock clean room backgrounds upon application initialization.
- **Dual-Threshold HSV Masking:** Optimized color boundary detection designed to prevent skin/clothing overlap and reduce ghosting artifacts.
- **Morphological Noise Cleanup:** Advanced erosion, dilation, and Gaussian blurring applied to eliminate frame flicker and edge bleeding.
- **Cross-Platform Compatibility:** Runs both locally via OpenCV window and on the web via Streamlit Community Cloud.

---

## 🛠️ Tech Stack

- **Language:** Python 3.x
- **Libraries & Frameworks:** 
  - `streamlit` & `streamlit-webrtc` (Interactive web dashboard & browser video streaming)
  - `opencv-python-headless` (Real-time video processing & matrix operations)
  - `numpy` (Array processing & bitwise manipulation)

---

## 🚀 Getting Started

### 1. Prerequisites

Ensure you have Python installed on your system. Install all dependencies using:

```bash
pip install -r requirements.txt