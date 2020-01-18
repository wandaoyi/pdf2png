#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# =============================================================================
# @Time     : 2020/1/3 17:08
# @Author   : WanDaoYi
# @FileName : pdf_2_png.py
# ==============================================================================


import fitz
import os
from config import cfg


class Pdf2Png(object):

    def __init__(self):
        self.input_data_path = cfg.COMMON.INPUT_PATH
        self.output_info_path = cfg.COMMON.OUTPUT_PATH

        print(self.input_data_path)
        print(self.output_info_path)
        pass

    def pdf_2_png(self):
        # 读取文件夹内的文件名
        name_list = os.listdir(self.input_data_path)
        print(name_list)
        for name in name_list:
            # 获取文件路径
            data_path = os.path.join(self.input_data_path, name)
            print(data_path)
            data = fitz.open(data_path)

            for pg in range(0, data.pageCount):
                page = data[pg]
                # zoom = int(1000) 比 zoom = int(100) 高清
                zoom = int(cfg.COMMON.IMAGE_DEFINITION)
                rotate = int(0)
                trans = fitz.Matrix(zoom / 100.0, zoom / 100.0).preRotate(rotate)
                # alpha=True 为 png 背景透明，False 为白色背景
                pm = page.getPixmap(matrix=trans, alpha=cfg.COMMON.IMAGE_BACK_GROUND)
                image_name = str(pg + 1) + cfg.COMMON.IMAGE_STYLE
                output_path = os.path.join(self.output_info_path, image_name)
                pm.writePNG(output_path)
                pass
        pass


if __name__ == "__main__":

    demo = Pdf2Png()
    demo.pdf_2_png()
    print("It's over! ")
    pass


