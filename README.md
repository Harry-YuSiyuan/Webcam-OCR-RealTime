# 🚀 1. Webcam-OCR-RealTime	实时摄像头 OCR 识别工具
Real-time OCR with USB external computer camera &amp; OpenCV &amp; Tesseract, supporting Chinese/English/numbers

带USB外接电脑摄像头&OpenCV&Tesseract实时OCR，支持中文/英文/数字
# 📚 2. Introduction	项目介绍
This is a real-time text recognition tool based on OpenCV and Tesseract OCR engine that captures images by calling a USB external computer camera, recognizes Chinese, English, and numbers in the images in real time, and displays the recognition results on the screen.
Core features:
- Real - time performance: The camera footage is processed in real - time with low recognition latency. - Multilingual support: It supports the recognition of Chinese (Simplified), English, and numbers simultaneously.
- Multilingual support: Supports the recognition of Chinese (Simplified), English, and numbers simultaneously.
- Lightweight deployment: fewer dependent libraries, and no need for an internet connection for local operation.
- Extensible: Supports custom image preprocessing (such as noise reduction, threshold adjustment) to optimize the recognition effect.

这是一个基于 OpenCV 和 Tesseract OCR 引擎的实时文字识别工具，通过调用USB外接的电脑摄像头捕获画面，实时识别画面中的中文、英文和数字，并在屏幕上显示识别结果。
核心特点：
- 实时性：摄像头画面实时处理，识别延迟低
- 多语言支持：同时支持中文（简体）、英文和数字识别
- 轻量部署：依赖库少，本地运行无需联网
- 可扩展：支持自定义图像预处理（如降噪、阈值调整）优化识别效果

# 🎥 3. Demo	演示
![enter image description here](DEMO.gif)

# 🛠️ 4. Prerequisites 环境依赖
#### Required Environment - Python 3.9
-   Dependent libraries: - OpenCV (for camera capture and image processing)
-   pytesseract (Python interface for Tesseract)
-   Tesseract OCR engine (core recognition tool, needs to be installed separately)

#### Tesseract Special Configuration  
Tesseract may not include Chinese language packs by default and needs to be installed manually:
-   Download address:[Tesseract official download](https://github.com/tesseract-ocr/tesseract) (or according to the system selection: Windows with exe installation, Linux with `sudo apt install tesseract-ocr `)
-   Chinese language pack: Check `chi_sim` (Simplified Chinese) when installing, or download [tessdata language pack](https://github.com/tesseract-ocr/tessdata) later and put it in the`tessdata `directory of Tesseract.

#### 必备环境 - Python 3.9
- 依赖库： - OpenCV（用于摄像头捕获和图像处理） 
- pytesseract（Tesseract 的 Python 接口） 
- Tesseract OCR 引擎（核心识别工具，需单独安装） 

#### Tesseract 特殊配置 
Tesseract 默认可能不包含中文语言包，需手动安装： 
- 下载地址：[Tesseract 官方下载](https://github.com/tesseract-ocr/tesseract)（或根据系统选择：Windows 用 exe 安装，Linux 用 `sudo apt install tesseract-ocr`） 
- 中文语言包：安装时勾选 `chi_sim`（简体中文），或后期下载 [tessdata 语言包](https://github.com/tesseract-ocr/tessdata) 并放到 Tesseract 的 `tessdata` 目录下。

# 🎯 5. Improvement Directions	改进方向
### 1.  Performance optimization 性能优化
- **Problem description	问题描述**：
Limited by CPU-intensive calculations (especially image preprocessing and Tesseract OCR recognition), the frame rate on low-end devices is relatively low (about 10 - 15 FPS), resulting in less smooth real-time display.
  受限于 CPU 密集型计算（尤其是图像预处理和 Tesseract OCR 识别），在低配设备上帧率较低（约 10-15 FPS），导致实时显示不够流畅。
### 2. Raspberry Pi Porting Plan	树莓派移植计划
- **Goal	目标**：
Supports running on Raspberry Pi 4B (and above) to create a portable OCR device.
支持在 Raspberry Pi 4B（及以上）运行，打造便携 OCR 设备。

- **Challenge	挑战**：  
 - The CPU performance of Raspberry Pi is limited, and the algorithm complexity needs to be optimized.
 树莓派 CPU 性能有限，需优化算法复杂度  
 - The official Tesseract library is complex to install on the ARM architecture.
 官方 Tesseract 库在 ARM 架构上安装复杂  
  
# 📄 6.License	许可证
This project is open-sourced under the MIT license, as detailed in the [LICENSE] (LICENSE) file.
本项目基于 MIT 许可证开源，详情见 [LICENSE](LICENSE) 文件。
