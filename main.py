'''
Author: wds-dxh wdsnpshy@163.com
Date: 2024-01-11 16:00:42
LastEditors: wds-dxh wdsnpshy@163.com
LastEditTime: 2024-11-03 13:47:04
FilePath: /rtsp_http/main.py
Description: 
微信: 15310638214 
邮箱：wdsnpshy@163.com 
Copyright (c) 2024 by ${wds-dxh}, All Rights Reserved. 
'''
from flask import Flask, render_template, Response
import cv2
import threading
import argparse  # 新增导入

app = Flask(__name__)

# 定义全局变量保存最新帧
global_frames = {}  # 用于存储多个视频流的最新帧

def update_frame1(video_url):
    global global_frames
    camera = cv2.VideoCapture(video_url)
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 80])
            global_frames[1] = buffer.tobytes()

def update_frame2(video_url):
    global global_frames
    camera = cv2.VideoCapture(video_url)
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 80])
            global_frames[2] = buffer.tobytes()

def update_frame3(video_url):
    global global_frames
    camera = cv2.VideoCapture(video_url)
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 80])
            global_frames[3] = buffer.tobytes()

def update_frame4(video_url):
    global global_frames
    camera = cv2.VideoCapture(video_url)
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 80])
            global_frames[4] = buffer.tobytes()

# 解析命令行参数
parser = argparse.ArgumentParser(description='RTSP to HTTP video streaming')
parser.add_argument('--urls', nargs=4, required=True, help='RTSP video stream URLs')
args = parser.parse_args()

# 为每个视频流启动一个线程
threading.Thread(target=update_frame1, args=(args.urls[0],), daemon=True).start()
threading.Thread(target=update_frame2, args=(args.urls[1],), daemon=True).start()
threading.Thread(target=update_frame3, args=(args.urls[2],), daemon=True).start()
threading.Thread(target=update_frame4, args=(args.urls[3],), daemon=True).start()

def generate_frames(stream_id):
    while True:
        if stream_id not in global_frames or global_frames[stream_id] is None:
            continue
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + global_frames[stream_id] + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed1')
def video_feed1():
    return Response(generate_frames(1),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video_feed2')
def video_feed2():
    return Response(generate_frames(2),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video_feed3')
def video_feed3():
    return Response(generate_frames(3),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video_feed4')
def video_feed4():
    return Response(generate_frames(4),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='::', port=5001)