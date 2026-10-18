# ChromaCloak AI 🧙‍♂️✨

A real-time, automated "Invisibility Cloak" implementation built using Python and OpenCV. By utilizing HSV color-space transformation, dual-range masking, and morphological filtering, **ChromaCloak AI** isolates specific color thresholds and seamlessly overlays a static background stream to achieve a smooth invisibility effect.

---

## 🌟 Key Features

- **Instant Background Capture:** Dynamic 1-key baseline calibration (`'b'`) to lock clean room backgrounds without manual slider tuning.
- **Dual-Threshold HSV Masking:** Optimized color boundary detection designed to prevent skin/clothing overlap and reduce ghosting artifacts.
- **Morphological Noise Cleanup:** Advanced erosion, dilation, and Gaussian blurring applied to eliminate frame flicker and edge bleeding.
- **High-FPS Performance:** Lightweight single-file frame processing loop optimized for live webcam feeds.

---

## 🛠️ Tech Stack

- **Language:** Python 3.x
- **Libraries:** 
  - `opencv-python` (Real-time video processing & matrix operations)
  - `numpy` (Array processing & bitwise manipulation)

---

## 🚀 Getting Started

### Prerequisites

Ensure you have Python installed on your system. Install the required dependencies using `pip`:

```bash
pip install opencv-python numpy