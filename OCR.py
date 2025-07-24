import cv2
import numpy as np
import pytesseract
from PIL import Image, ImageDraw, ImageFont

##########
wigth = 640
height = 480
brightness = 150
##########

### 函数定义
def preprocess_frame(frame):
    # 转换为灰度图
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # 中值滤波去噪，对椒盐噪声有较好效果
    blurred = cv2.medianBlur(gray, 3)
    # 自适应阈值处理，增强数字与背景对比度
    thresh = cv2.adaptiveThreshold(
        blurred, 255, 
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY_INV, 11, 2
    )
    # 形态学操作，去除小的噪声点
    kernel = np.ones((2, 2), np.uint8)
    thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
    
    return blurred,thresh

def cv2ImgText(img, text, x, y, font_path='simhei.ttf', font_size=20, color=(0, 0, 255)):
    try:
        img_pil = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))  # 转PIL格式
        draw = ImageDraw.Draw(img_pil)
        font = ImageFont.truetype(font_path, font_size)  # 加载中文字体
        draw.text((x, y), text, font=font, fill=color)    # 绘制文字
        return cv2.cvtColor(np.array(img_pil), cv2.COLOR_RGB2BGR)  # 转回OpenCV格式
    except Exception as e:
        print(f"绘制文本时出错: {e}")
        return img

def stackImages(scale, imgArray):
    # Handle the case where imgArray is empty
    if not imgArray:
        return np.zeros((0, 0, 3), np.uint8)
    
    rowsAvailable = isinstance(imgArray[0], list)
    
    # Dynamically get the reference image
    if rowsAvailable:
        ref_img = next((img for row in imgArray for img in row if img is not None), None)
    else:
        ref_img = next((img for img in imgArray if img is not None), None)
    
    if ref_img is None:
        return np.zeros((0, 0, 3), np.uint8)
    
    width = ref_img.shape[1]
    height = ref_img.shape[0]
    
    if rowsAvailable:
        processed_rows = []
        max_cols = max(len(row) for row in imgArray)
        for row in imgArray:
            processed_row = []
            for img in row:
                if img is None:
                    img = np.zeros((height, width, 3), np.uint8)
                # Resize the image to the reference size and then scale it
                img = cv2.resize(img, (width, height), None, scale, scale)
                if len(img.shape) == 2:
                    img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
                processed_row.append(img)
            # Handle the case where the number of images in the row is inconsistent
            while len(processed_row) < max_cols:
                processed_row.append(np.zeros((height, width, 3), np.uint8))
            processed_rows.append(np.hstack(processed_row))
        return np.vstack(processed_rows)
    else:
        processed_imgs = []
        for img in imgArray:
            if img is None:
                img = np.zeros((height, width, 3), np.uint8)
            # Resize the image to the reference size and then scale it
            img = cv2.resize(img, (width, height), None, scale, scale)
            if len(img.shape) == 2:
                img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
            processed_imgs.append(img)
        return np.hstack(processed_imgs)

### 主函数

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
cap=cv2.VideoCapture(0)
cap.set(3,wigth)#宽
cap.set(4,height)#高
cap.set(10,brightness)#亮度

print("按 'q' 键退出")
while True:
    success, frame = cap.read()
    if not success:
        break
    frameCopy = frame.copy()
    blurred,thresh = preprocess_frame(frameCopy)
    boxes = pytesseract.image_to_data(thresh, lang='chi_sim')
    for x, b in enumerate(boxes.splitlines()):
        b = b.split()
        if x != 0:  # 跳过表头行（第一行是列名）
            if len(b) == 12 and float(b[10]) >80:
                # 解析坐标和文字
                x_coord, y_coord, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
                text = b[11]
                print(f"识别到文本: {text}，置信度：{b[10]}，位置: ({x_coord}, {y_coord}, {w}, {h})")
                # 绘制矩形框和文字
                cv2.rectangle(frameCopy, (x_coord, y_coord), (x_coord + w, y_coord + h), (0, 255, 0), 2)
                # 检查坐标范围
                if x_coord >= 0 and y_coord - 10 >= 0:
                    # 尝试使用对比度较高的颜色
                    frameCopy = cv2ImgText(frameCopy, text, x_coord, y_coord - 10, font_path=r'C:\Windows\Fonts\simhei.ttf', color=(255, 0, 0))
                else:
                    print(f"坐标超出范围,x: {x_coord}, y: {y_coord - 10}")
    
    frameStacked = stackImages(0.4, [[frame, blurred], [thresh, frameCopy]])
    cv2.imshow("OCR Detection", frameStacked)
    # 按 'q' 键退出
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 释放摄像头资源并关闭所有窗口
cap.release()
cv2.destroyAllWindows()