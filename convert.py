import cv2
import imageio.v2 as imageio
import os

video_path = os.path.expanduser('~\\Downloads\\demo.gif.mp4')
if not os.path.exists(video_path):
    print(f'Error: {video_path} nahi mila!')
else:
    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    fps = fps if fps and fps > 0 else 10
    
    frames = []
    while True:
        success, frame = cap.read()
        if not success:
            break
        frames.append(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    
    cap.release()
    
    if len(frames) > 0:
        os.makedirs('assets', exist_ok=True)
        imageio.mimsave('assets/demo.gif', frames, fps=int(fps))
        print('SUCCESS: GIF successfully generated in assets folder!')
    else:
        print('Error: Video frames read nahi ho paye.')
