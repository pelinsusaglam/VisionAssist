# VisionAssist

# VisionAssist: Real-Time Audio Navigation for the Visually Impaired


**VisionAssist** is a real-time audio navigation system designed to assist visually impaired individuals in navigating their surroundings. It uses advanced object detection and tracking with the YOLO (You Only Look Once) model to identify and track objects, such as vehicles and pedestrians. It then provides real-time audio feedback to guide users safely through their environment.

## Features

- **Real-Time Object Detection**: Detects various objects, such as vehicles and pedestrians, in the camera feed using the YOLO model.
- **Audio Alerts**: Provides audio cues for detected objects, helping the user to understand the object's position relative to them.
- **Polygonal Zones**: Defines specific polygonal areas in the environment where the system can trigger alerts when an object enters the area.
- **Voice Feedback**: Utilizes text-to-speech to deliver audio feedback, ensuring that users are informed of potential obstacles and navigational cues.

## Requirements

To run **VisionAssist**, you need the following dependencies:

- Python 3.x
- `opencv-python`
- `numpy`
- `pyttsx3`
- `ultralytics` (for YOLO model)
- `imutils`

Install dependencies using pip:

```bash
pip install opencv-python numpy pyttsx3 ultralytics imutils
