import cv2
import os
from pathlib import Path
import pandas as pd
import numpy as np
from tqdm import tqdm

def extract_frames_basic(video_path, output_dir, frame_interval=30):
    """
    Extract frames at regular intervals
    
    Args:
        video_path: Path to input video
        output_dir: Directory to save frames
        frame_interval: Extract every Nth frame (30 = ~1 frame per second at 30fps)
    """
    # Create output directory
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    
    # Open video
    cap = cv2.VideoCapture(video_path)
    
    # Get video properties
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    
    print(f"Video: {video_path}")
    print(f"Total frames: {total_frames}, FPS: {fps}")
    
    frame_count = 0
    saved_count = 0
    
    with tqdm(total=total_frames//frame_interval, desc="Extracting frames") as pbar:
        while True:
            ret, frame = cap.read()
            if not ret:
                break
                
            # Save frame at specified interval
            if frame_count % frame_interval == 0:
                frame_filename = f"frame_{saved_count:06d}.jpg"
                frame_path = os.path.join(output_dir, frame_filename)
                cv2.imwrite(frame_path, frame)
                saved_count += 1
                pbar.update(1)
            
            frame_count += 1
    
    cap.release()
    print(f"Extracted {saved_count} frames to {output_dir}")
    return saved_count

# Fix 2: Actually call the function at the end of your file
if __name__ == "__main__":
    # Set your output directory
    output_dir = "extracted_frames/example"
    
    # Call the function
    frame_count = extract_frames_basic(
        # input path to video you want to extract frames from
        video_path='insert path here',
        output_dir=output_dir,
        frame_interval=30  # Extract every 30th frame
    )
    
    print(f"Done! Extracted {frame_count} frames.")