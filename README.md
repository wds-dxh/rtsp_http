<!--
 * @Author: wds-dxh wdsnpshy@163.com
 * @Date: 2024-11-03 12:13:58
 * @LastEditors: wds-dxh wdsnpshy@163.com
 * @LastEditTime: 2024-11-03 12:16:14
 * @FilePath: /rtsp_http/README.md
 * @Description: 
 * 微信: 15310638214 
 * 邮箱：wdsnpshy@163.com 
 * Copyright (c) 2024 by ${wds-dxh}, All Rights Reserved. 
-->
### 使用说明

以下是在当前工作空间中使用 `main.py` 的指南：

1. **安装依赖库**：

   请确保已安装以下 Python 库：

   - Flask
   - OpenCV-Python
   - argparse

   您可以使用以下命令安装所需的库：

   ```bash
   pip install flask opencv-python
   ```

2. **运行程序**：

   在终端中，导航到 `main.py` 文件所在的目录。

   使用以下命令运行程序，注意将 `YOUR_RTSP_URL` 替换为实际的 RTSP 视频流地址：

   ```bash
   python main.py --url YOUR_RTSP_URL
   ```

   例如：

   ```bash
   python main.py --url rtsp://example.com/stream
   ```

3. **访问视频流**：

   在浏览器中输入以下地址：

   ```
   http://localhost:5001/
   ```

   您将看到转换后的视频流。

4. **注意事项**：

   - 确保 RTSP 流地址可用且网络连接正常。
   - 如果在服务器上运行并希望外部设备访问，请确保防火墙允许端口 `5001`，并将 `app.run()` 中的主机地址设置为可访问的 IP。

5. **修改端口或主机（可选）**：

   如果需要修改服务器的端口号或主机地址，可以编辑 `main.py` 中的以下部分：

   ```python
   if __name__ == '__main__':
       app.run(host='::', port=5001)
   ```

   将 `host` 和 `port` 参数修改为所需的值。

---

# rtsp_http
