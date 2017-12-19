# -*- coding: utf-8 -*-
"""
__author__ = 'Sunny'
__mtime__ = '6/22/2016'

                ┏┓     ┏┓
              ┏┛┻━━━┛┻┓
             ┃     ☃     ┃
             ┃ ┳┛  ┗┳  ┃
            ┃     ┻     ┃
            ┗━┓     ┏━┛
               ┃     ┗━━━┓
              ┃  神兽保佑   ┣┓
             ┃　永无BUG！  ┏┛
            ┗┓┓┏━┳┓┏┛
             ┃┫┫  ┃┫┫
            ┗┻┛  ┗┻┛
"""
if __name__ == '__main__':
    from PyInstaller.__main__ import run
    """
    -F, --onefilePy代码只有一个文件
    -D, --onedirPy代码放在一个目录中（默认是这个）
    -K, --tk包含TCL/TK
    -d, --debug生成debug模式的exe文件
    -w, --windowed, --noconsole窗体exe文件(Windows Only)
    -c, --nowindowed, --console控制台exe文件(Windows Only)
    -X, --upx使用upx压缩exe文件(压缩是不用打命令只要将upx.exe加到Python安装目录下就好了)
    -o DIR, --out=DIR设置spec文件输出的目录，默认在PyInstaller同目录
    -i <FILE.ICO>,--icon=<FILE.ICO>加入图标（Windows Only）
    -v FILE, --version=FILE加入版本信息文件
    """
    opts=['run.py','-n=store1.6.0','-w','-i=项目3.ico','--additional-hooks-dir=.']
    # opts=['t.py','-F','-n=demo','-i=logo1.ico']
    run(opts)

