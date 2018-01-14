# -*- coding: utf-8 -*-
"""
__author__ = 'sunny'
__mtime__ = '2017/3/31'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
                   ┏┓      ┏┓
                ┏┛┻━━━┛┻┓
               ┃      ☃      ┃
              ┃  ┳┛  ┗┳  ┃
             ┃      ┻      ┃
            ┗━┓      ┏━┛
               ┃      ┗━━━┓
              ┃              ┣┓
             ┃　            ┏┛
            ┗┓┓┏━┳┓┏┛
             ┃┫┫  ┃┫┫
            ┗┻┛  ┗┻┛
"""
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from PyQt5.QtPrintSupport import QPrinterInfo, QPrinter


class Printer:
    # 打印机列表
    @staticmethod
    def printer_list():
        printer = []
        printer_info = QPrinterInfo()
        print('availablePrinterNames', printer_info.availablePrinterNames())
        print('defaultPrinterName', printer_info.defaultPrinterName())

        for item in printer_info.availablePrinters():
            printer.append(item.printerName())
        return printer

    # 打印任务
    @staticmethod
    def printing(printerName, html, pageHeight):

        printer = QPrinter(QPrinter.HighResolution)
        # p.setPaperSize(QPrinter.A4)

        text_document = QTextDocument()
        text_document.setHtml(html)
        # 调整纸张大小，否则字体会因为不同的驱动变形
        # textDocument.setPageSize(QSizeF(p.logicalDpiX()*(240/25.4),p.logicalDpiY()*(297/25.4)))
        text_document.setDocumentMargin(35)
        # height = 300+((page-1)*200)
        # printer.setPaperSize(QSizeF(printer.logicalDpiX()*(86/25.4),height),QPrinter.Point)
        # textDocument.setPageSize(QSizeF(printer.logicalDpiX()*(86/25.4),height))
        printer.setPaperSize(QSizeF(581, pageHeight), QPrinter.Point)
        text_document.setPageSize(QSizeF(581, pageHeight))
        text_op = QTextOption()
        text_op.setWrapMode(QTextOption.WrapAnywhere)
        text_op.setAlignment(Qt.AlignCenter)
        text_document.setDefaultTextOption(text_op)
        printer.setOutputFormat(QPrinter.NativeFormat)
        text_document.print(printer)

    @staticmethod
    def printing_22(printer, context):
        printer_info = QPrinterInfo()
        p = QPrinter()

        for item in printer_info.availablePrinters():
            if printer == item.printerName():
                p = QPrinter(item)

        doc = QTextDocument()
        doc.setHtml(u'%s' % context)
        doc.setPageSize(QSizeF(p.logicalDpiX() * (80 / 25.4),
                               p.logicalDpiY() * (297 / 25.4)))
        p.setOutputFormat(QPrinter.NativeFormat)
        doc.print_(p)
