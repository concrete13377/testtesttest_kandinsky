FROM python:3.10.12
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
RUN pip install 'git+https://github.com/ai-forever/Kandinsky-2.git' 'git+https://github.com/openai/CLIP.git' opencv-python
