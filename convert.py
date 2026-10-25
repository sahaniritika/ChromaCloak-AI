import cv2
import imageio.v2 as imageio
import os
import glob

# OneDrive folder mein saari video files dhoondo
onedrive_path = os.path.expanduser('~\\OneDrive')
search_patterns = [os.path.join(onedrive_path, '**\\*.mp4'), os.path.join(onedrive_path, '**\\*.gif')]

files = []
for p in search_patterns:
    files.extend(glob.glob(p, recursive=True))

if not files:
    print('Error: OneDrive mein koi video/gif nahi mili!')
else:
    # Sabse nayi (latest) file uthao
    latest_file = max(files, key=os.path.getmtime)
    print(f'Found latest file in OneDrive: {latest_file}')
    
    cap = cv2.VideoCapture(latest_file)
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
