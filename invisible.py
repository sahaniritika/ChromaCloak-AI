import cv2
import numpy as np

def run_fixed_cloak():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("[ERROR] Camera open nahi ho raha hai.")
        return

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    print("\n[SUCCESS] ChromaCloak AI - Instant Fix Active!")
    print("--------------------------------------------------")
    print("1. Camera start hone par bilkul side ho jayein.")
    print("2. Piche clear room dikhte hi keyboard par 'b' dabayein.")
    print("3. Phir kapda samne layein - 100% clean invisibility!")
    print("4. Exit karne ke liye 'q' dabayein.")
    print("--------------------------------------------------\n")

    bg_frame = None

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame = np.flip(frame, axis=1)

        # Keyboard Key Capture
        key = cv2.waitKey(1) & 0xFF

        # 'b' Key Dabane Se Exact Background Capture Hoga
        if key == ord('b'):
            bg_frame = frame.copy()
            print("[SUCCESS] Clean Background Captured Successfully!")

        # Agar Background Captured Hai Tab Invisibility Processing Hogi
        if bg_frame is not None:
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

            # High Saturation Red Mask
            lower_red1 = np.array([0, 120, 70])
            upper_red1 = np.array([10, 255, 255])
            mask1 = cv2.inRange(hsv, lower_red1, upper_red1)

            lower_red2 = np.array([170, 120, 70])
            upper_red2 = np.array([180, 255, 255])
            mask2 = cv2.inRange(hsv, lower_red2, upper_red2)

            mask = mask1 + mask2

            # Morphological Noise Filtering
            kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
            mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
            mask = cv2.dilate(mask, kernel, iterations=2)

            mask_inv = cv2.bitwise_not(mask)

            res_bg = cv2.bitwise_and(bg_frame, bg_frame, mask=mask)
            res_frame = cv2.bitwise_and(frame, frame, mask=mask_inv)

            final_output = cv2.addWeighted(res_bg, 1, res_frame, 1, 0)
        else:
            # jab tak 'b' nahi dabaya tab tak live camera dikhega aur text instruction aayegi
            final_output = frame.copy()
            cv2.putText(final_output, "Press 'b' to set background", (30, 40), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)

        cv2.imshow("ChromaCloak AI", final_output)

        if key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    run_fixed_cloak()