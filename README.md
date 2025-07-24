# 1. Webcam-OCR-RealTime	实时摄像头 OCR 识别工具
Real-time OCR with OpenCV &amp; Tesseract, supporting Chinese/English/numbers
# 2. Introduction	项目介绍
This is a real-time text recognition tool based on OpenCV and Tesseract OCR engine that captures images by calling a computer camera, recognizes Chinese, English, and numbers in the images in real time, and displays the recognition results on the screen.
Core features:
- Real - time performance: The camera footage is processed in real - time with low recognition latency. - Multilingual support: It supports the recognition of Chinese (Simplified), English, and numbers simultaneously.
- Lightweight deployment: fewer dependent libraries, and no need for an internet connection for local operation
- Extensible: Supports custom image preprocessing (such as noise reduction, threshold adjustment) to optimize the recognition effect.

这是一个基于 OpenCV 和 Tesseract OCR 引擎的实时文字识别工具，通过调用电脑摄像头捕获画面，实时识别画面中的中文、英文和数字，并在屏幕上显示识别结果。
核心特点：
- 实时性：摄像头画面实时处理，识别延迟低； - 多语言支持：同时支持中文（简体）、英文和数字识别
- 轻量部署：依赖库少，本地运行无需联网
- 可扩展：支持自定义图像预处理（如降噪、阈值调整）优化识别效果

# 3. Demo	演示
![enter image description here](C:%5CUsers%5C24013%5CDesktop%演示.gif)

# 4. Prerequisites 环境依赖
#### Required Environment - Python 3.9
-   Dependent libraries: - OpenCV (for camera capture and image processing)
-   pytesseract (Python interface for Tesseract)
-   Tesseract OCR engine (core recognition tool, needs to be installed separately)

#### Tesseract Special Configuration  
Tesseract may not include Chinese language packs by default and needs to be installed manually:
-   Download address: [Tesseract official download]([https://github.com/tesseract-ocr/tesseract](https://github.com/tesseract-ocr/tesseract)) (or according to the system selection: Windows with exe installation, Linux with `sudo apt install tesseract-ocr `)
-   Chinese language pack: Check `chi_sim` (Simplified Chinese) when installing, or download [tessdata language pack]([https://github.com/tesseract-ocr/tessdata](https://github.com/tesseract-ocr/tessdata)) later and put it in the`tessdata `directory of Tesseract.

#### 必备环境 - Python 3.9
- 依赖库： - OpenCV（用于摄像头捕获和图像处理） 
- pytesseract（Tesseract 的 Python 接口） 
- Tesseract OCR 引擎（核心识别工具，需单独安装） 

#### Tesseract 特殊配置 
Tesseract 默认可能不包含中文语言包，需手动安装： 
- 下载地址：[Tesseract 官方下载](https://github.com/tesseract-ocr/tesseract)（或根据系统选择：Windows 用 exe 安装，Linux 用 `sudo apt install tesseract-ocr`） 
- 中文语言包：安装时勾选 `chi_sim`（简体中文），或后期下载 [tessdata 语言包](https://github.com/tesseract-ocr/tessdata) 并放到 Tesseract 的 `tessdata` 目录下。
# 5.License	许可证
本项目基于 MIT 许可证开源，详情见 [LICENSE](LICENSE) 文件。
