#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# =============================================================================
# @Time     : 2020/1/3 17:12
# @Author   : WanDaoYi
# @FileName : config.py
# ==============================================================================

from easydict import EasyDict as edict
import os


__C = edict()

cfg = __C

# common options
__C.COMMON = edict()

__C.COMMON.BASE_PATH = os.path.abspath(os.path.dirname(__file__))

# os.path.join(self.input_data_path, name)
__C.COMMON.INPUT_PATH = os.path.join(__C.COMMON.BASE_PATH, "input_pdf")
__C.COMMON.OUTPUT_PATH = os.path.join(__C.COMMON.BASE_PATH, "output_png")

# 输出的图片格式
__C.COMMON.IMAGE_STYLE = ".png"
# 白色背景为 False；透明背景为 True
__C.COMMON.IMAGE_BACK_GROUND = False

# 清晰度，高清度。数值大，则清晰度高
__C.COMMON.IMAGE_DEFINITION = 500





