import time
import board
import adafruit_ssd1306
from PIL import Image, ImageDraw

# Định nghĩa kích thước màn hình
WIDTH = 128
HEIGHT = 64  # Đối với màn hình 128x64
EYE_WIDTH = 30
EYE_HEIGHT = 40
EYE_SPACING = 20
EYE_Y = HEIGHT // 2 - EYE_HEIGHT // 2

# Tạo đối tượng I2C
i2c = board.I2C()

# Tạo đối tượng màn hình OLED
oled = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c)

def draw_rounded_rectangle(draw, xy, radius, outline=None, fill=None):
    x0, y0, x1, y1 = xy
    draw.rectangle([x0 + radius, y0, x1 - radius, y1], outline=outline, fill=fill)
    draw.rectangle([x0, y0 + radius, x1, y1 - radius], outline=outline, fill=fill)
    draw.pieslice([x0, y0, x0 + 2 * radius, y0 + 2 * radius], 180, 270, outline=outline, fill=fill)
    draw.pieslice([x1 - 2 * radius, y0, x1, y0 + 2 * radius], 270, 360, outline=outline, fill=fill)
    draw.pieslice([x0, y1 - 2 * radius, x0 + 2 * radius, y1], 90, 180, outline=outline, fill=fill)
    draw.pieslice([x1 - 2 * radius, y1 - 2 * radius, x1, y1], 0, 90, outline=outline, fill=fill)

def draw_eyes(draw, left_x, right_x, eye_state, radius=10):
    # Xóa hình ảnh bằng cách vẽ hình chữ nhật đen
    draw.rectangle((0, 0, oled.width, oled.height), outline=0, fill=0)
    
    if eye_state == 'open':
        # Vẽ mắt trái
        draw_rounded_rectangle(draw, (left_x, EYE_Y, left_x + EYE_WIDTH, EYE_Y + EYE_HEIGHT), radius, outline=255, fill=255)
        # Vẽ mắt phải
        draw_rounded_rectangle(draw, (right_x, EYE_Y, right_x + EYE_WIDTH, EYE_Y + EYE_HEIGHT), radius, outline=255, fill=255)
    elif eye_state == 'closed':
        # Vẽ mắt trái đóng
        draw.rectangle((left_x, EYE_Y + EYE_HEIGHT // 2 - 5, left_x + EYE_WIDTH, EYE_Y + EYE_HEIGHT // 2 + 5), outline=255, fill=255)
        # Vẽ mắt phải đóng
        draw.rectangle((right_x, EYE_Y + EYE_HEIGHT // 2 - 5, right_x + EYE_WIDTH, EYE_Y + EYE_HEIGHT // 2 + 5), outline=255, fill=255)

def main():
    left_eye_x = WIDTH // 4 - EYE_WIDTH // 2
    right_eye_x = 3 * WIDTH // 4 - EYE_WIDTH // 2

    image = Image.new('1', (oled.width, oled.height))
    draw = ImageDraw.Draw(image)

    while True:
        # Chớp mắt
        draw_eyes(draw, left_eye_x, right_eye_x, 'open')
        oled.image(image)
        oled.show()
        time.sleep(1)
        
        draw_eyes(draw, left_eye_x, right_eye_x, 'closed')
        oled.image(image)
        oled.show()
        time.sleep(0.5)
        
        draw_eyes(draw, left_eye_x, right_eye_x, 'open')
        oled.image(image)
        oled.show()
        time.sleep(1)
        draw_eyes(draw, left_eye_x, right_eye_x, 'closed')
        oled.image(image)
        oled.show()
        time.sleep(0.5)
        
        # Di chuyển mắt qua trái
        for i in range(10):
            draw_eyes(draw, left_eye_x - i * 2, right_eye_x - i * 2, 'open')
            oled.image(image)
            oled.show()
            time.sleep(0.05)

        draw_eyes(draw, left_eye_x - 10 * 2, right_eye_x - 10 * 2, 'closed')
        oled.image(image)
        oled.show()
        time.sleep(0.2)
        
        draw_eyes(draw, left_eye_x - 10 * 2, right_eye_x - 10 * 2, 'open')
        oled.image(image)
        oled.show()
        time.sleep(1)
        # Di chuyển mắt qua phải
        for i in range(10):
            draw_eyes(draw, left_eye_x - 20 + i * 2, right_eye_x - 20 + i * 2, 'open')
            oled.image(image)
            oled.show()
            time.sleep(0.05)
        draw_eyes(draw, left_eye_x - 20 + 10 * 2,  right_eye_x - 20 + 10 * 2, 'closed')
        oled.image(image)
        oled.show()
        time.sleep(0.2)
        
        draw_eyes(draw, left_eye_x - 20 + 10 * 2,  right_eye_x - 20 + 10 * 2, 'open')
        oled.image(image)
        oled.show()
        time.sleep(1)

                
        # Di chuyển mắt qua phải
        for i in range(10):
            draw_eyes(draw, left_eye_x  + i * 2, right_eye_x + i * 2, 'open')
            oled.image(image)
            oled.show()
            time.sleep(0.05)
        draw_eyes(draw, left_eye_x + i * 2,  right_eye_x + i * 2, 'closed')
        oled.image(image)
        oled.show()
        time.sleep(0.2)
        
        draw_eyes(draw,left_eye_x + i * 2,  right_eye_x + i * 2, 'open')
        oled.image(image)
        oled.show()
        time.sleep(1)
                
        # Di chuyển mắt qua trái
        for i in range(10):
            draw_eyes(draw, left_eye_x + i * 2, right_eye_x + i * 2, 'open')
            oled.image(image)
            oled.show()
            time.sleep(0.05)
        draw_eyes(draw, left_eye_x * 2, right_eye_x * 2, 'closed')
        oled.image(image)
        oled.show()
        time.sleep(0.2)
        
        draw_eyes(draw, left_eye_x * 2, right_eye_x * 2, 'open')
        oled.image(image)
        oled.show()
        time.sleep(1)

if __name__ == "__main__":
    main()
