'''
Author: wds-dxh wdsnpshy@163.com
Date: 2024-01-11 16:00:42
LastEditors: wds-dxh wdsnpshy@163.com
LastEditTime: 2024-11-03 11:52:14
FilePath: /推流/main.py
Description: 
微信: 15310638214 
邮箱：wdsnpshy@163.com 
Copyright (c) 2024 by ${wds-dxh}, All Rights Reserved. 
'''
from flask import Flask, render_template, Response
import cv2
import threading

app = Flask(__name__)

# 定义全局变量保存最新帧
global_frame = None

def update_frame():
    global global_frame
    # 使用OpenCV捕获摄像头
    url = "rtsp://cloud-5plus.dxh-wds.top:8555/stream"  # 替换为你的视频流地址
    camera = cv2.VideoCapture(url)
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            # 将帧编码为JPEG格式
            # frame = cv2.resize(frame, (640, 480))
            ret, buffer = cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 80])
            global_frame = buffer.tobytes()

# 在应用启动时启动后台线程
threading.Thread(target=update_frame, daemon=True).start()

def generate_frames():
    while True:
        if global_frame is None:
            continue
        # 使用生成器函数输出帧
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + global_frame + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    # 使用Response对象包装生成器函数，以便将其作为视频流输出
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    # app.run(debug=True)
    #让外部可以访问
    app.run( host='::' ,port=5001)
    # app.run( host='0.0.0.0' ,port=5001)
