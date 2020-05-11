# from captcha.image import ImageCaptcha
from my_captcha.image import ImageCaptcha
import random

from flask import make_response
from io import BytesIO


def random_captcha_text(num):
    # 验证码列表
    captcha_text = '1234567890QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm'

    # 从list中随机获取 num 个元素，作为一个片断返回
    example = random.sample(captcha_text, num)
    # verification_code = random.sample(captcha_text, num)
    # 将列表里的片段变为字符串并返回
    verification_code = ''.join(example)
    return verification_code


# def generate_captcha_image():
#     num_name = 4
#     width = 20
#     height = 5
#     image = ImageCaptcha(width=width, height=height)
#     # 获得随机生成的验证码
#     captcha_text = random_captcha_text(num_name)
#     # 生成验证码
#     path = './static/verify_code/'
#     # 保存图片
#     image.write(captcha_text, path + captcha_text + '.png')
#     return captcha_text


def generate_captcha_image_url():
    num_name = 4
    width = 80
    height = 34
    image = ImageCaptcha(width=width, height=height, fonts=None, font_sizes=(22, 20, 26))
    # 获得随机生成的验证码
    captcha_text = random_captcha_text(num_name)
    # 生成图片
    out = BytesIO()
    image.write(captcha_text, out)
    out.seek(0)
    resp = make_response(out.read())
    resp.content_type = 'image/png'
    return resp, captcha_text
