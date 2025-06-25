from PIL import Image, ImageDraw, ImageFont

# 创建图片
img = Image.new('RGB', (640, 360), color=(36, 103, 194))
draw = ImageDraw.Draw(img)

# 渐变背景
for y in range(360):
    r = 36 + int((255-36) * y / 360 * 0.25)
    g = 103 + int((255-103) * y / 360 * 0.25)
    b = 194 + int((255-194) * y / 360 * 0.25)
    draw.line([(0, y), (640, y)], fill=(r, g, b))

# 画一个简笔直升机（右上角）
heli_x, heli_y = 420, 60
# 机身
draw.ellipse([heli_x, heli_y, heli_x+100, heli_y+40], outline="white", width=4)
# 旋翼
draw.line([(heli_x+50, heli_y-20), (heli_x+50, heli_y+10)], fill="white", width=4)
draw.line([(heli_x+15, heli_y-10), (heli_x+85, heli_y-10)], fill="white", width=4)
# 尾翼
draw.line([(heli_x+100, heli_y+20), (heli_x+130, heli_y+10)], fill="white", width=4)
draw.line([(heli_x+130, heli_y+10), (heli_x+130, heli_y+30)], fill="white", width=4)
draw.line([(heli_x+130, heli_y+30), (heli_x+100, heli_y+20)], fill="white", width=4)
# 起落架
draw.line([(heli_x+30, heli_y+40), (heli_x+70, heli_y+55)], fill="white", width=4)

# 文字内容
lines = [
    "柬埔寨直升机/机票/旅游一站式服务",
    "7x24小时中文客服，欢迎咨询",
    "直升机包机、景区观光、商务接送、私人订制"
]

# 尝试加载支持中文的字体
font_path = None
for path in [
    "C:/Windows/Fonts/msyh.ttc",   # 微软雅黑
    "C:/Windows/Fonts/simhei.ttf", # 黑体
    "C:/Windows/Fonts/simsun.ttc", # 宋体
]:
    try:
        font = ImageFont.truetype(path, 28)
        font_path = path
        break
    except:
        continue

if not font_path:
    font = ImageFont.load_default()
    print("警告：未找到中文字体，可能会出现方块字。")

# 计算文字整体高度
bbox = draw.textbbox((0, 0), lines[0], font=font)
line_height = bbox[3] - bbox[1] + 10
block_height = line_height * len(lines)

# 居中绘制
for i, line in enumerate(lines):
    bbox = draw.textbbox((0, 0), line, font=font)
    w = bbox[2] - bbox[0]
    h = bbox[3] - bbox[1]
    x = (640 - w) // 2
    y = (360 - block_height) // 2 + i * line_height
    draw.text((x, y), line, font=font, fill=(255, 255, 255))

# 保存图片
img.save("service_banner.png")
print("图片已生成，文件名为 service_banner.png")