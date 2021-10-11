#!/usr/bin/env python
# coding:utf-8

"""
惬意办工
v0.1 实现壁纸切换功能
v0.2 实现简单的番茄钟
"""

import os
import sys
import win32api
import win32con
import win32gui
import random
import configparser
from functools import partial
from PySide2.QtCore import QDir, QTimer
from PySide2.QtGui import QIcon, QCursor
from PySide2.QtWidgets import QApplication, QMainWindow, QSystemTrayIcon, QMenu, QAction, QFileDialog, QMessageBox

import resources_rc
from tomato_dialog import TomatoDialog
from calendar_dialog import CalendarDialog


class MainWindow(QMainWindow):
    """
    主窗口类
    """

    def __init__(self):
        """
        主窗口的构造函数

        :param cfg: 配置项
        """

        super(MainWindow, self).__init__()
        self.hide()

        # 壁纸
        self.wallpapers = self.get_wallpapers()
        self.cur_classify = ""
        self.cur_wallpaper = ""
        self.switch_timer = None
        self.show_paper("")

        # 托盘图标
        self.sys_tray = QSystemTrayIcon(self)  # 创建托盘
        self.sys_tray.setIcon(QIcon(":res/cozy_office.ico"))  # 设置托盘图标
        self.sys_tray.setToolTip("惬意办工")
        self.sys_tray.show()

        # 番茄钟
        self.tomato_dlg = TomatoDialog()

        # 托盘菜单
        self.menu = None
        self.sys_tray.activated.connect(self.show_menu)

    def get_wallpapers(self):
        """取得壁纸列表"""

        if qApp.cfg["wallpaper"]["path"]:
            ret = {}

            for root, dirs, files in os.walk(qApp.cfg["wallpaper"]["path"]):
                for dir in dirs:
                    ret[dir] = []
                for file in files:
                    ret[root[len(qApp.cfg["wallpaper"]["path"]) + 1:]].append(os.path.join(root, file))

            return ret
        else:
            return {}

    def create_menu(self):
        """创建菜单"""

        menu = QMenu()

        # 壁纸
        wallpaper = menu.addMenu(QIcon(":res/wallpaper.png"), "壁纸")
        if self.wallpapers:
            # 换一张
            next = wallpaper.addMenu("换一张")
            all = QAction("全部", self)
            next.addAction(all)
            all.triggered.connect(lambda: self.show_paper(""))

            # 分隔
            next.addSeparator()

            # 分类
            for key in self.wallpapers:
                classify = QAction(key, self)
                next.addAction(classify)
                classify.triggered.connect(partial(self.show_paper, key))       # 此处若使用lambda，槽函数接收到的参数永远是最后一项

            # 自动切换
            auto = QAction("自动切换", self)
            auto.setCheckable(True)
            auto.setChecked(True if self.switch_timer else False)
            wallpaper.addAction(auto)
            auto.triggered.connect(self.auto_switch)

            # 分隔
            wallpaper.addSeparator()

            # 删除当前壁纸
            if self.cur_wallpaper:
                del_ = QAction("删除当前壁纸", self)
                wallpaper.addAction(del_)
                del_.triggered.connect(self.del_cur_wallpaper)
        else:
            setup = QAction("设置壁纸路径", self)
            wallpaper.addAction(setup)
            setup.triggered.connect(self.set_wallpaper_path)

        # 番茄钟
        tomato = QAction(QIcon(":res/tomato.png"), "番茄钟", self)
        tomato.triggered.connect(self.show_tomato_dialog)
        menu.addAction(tomato)

        # 记事本
        note = QAction(QIcon(":res/note.png"), "记事本", self)
        note.triggered.connect(self.show_calendar_dialog)
        menu.addAction(note)

        # 分隔
        menu.addSeparator()

        # 退出
        exit = QAction(QIcon(":res/exit.png"), "退出", self)
        exit.triggered.connect(qApp.quit)
        menu.addAction(exit)

        return menu

    def show_menu(self, reason):
        """显示托盘菜单"""

        # 重新创建菜单
        self.menu = self.create_menu()
        self.sys_tray.setContextMenu(self.menu)

        # 显示菜单
        self.sys_tray.contextMenu().popup(QCursor.pos())

    def set_wallpaper_path(self):
        """设置壁纸路径"""

        # 选择目录
        self.cfg["wallpaper"]["path"] = QFileDialog.getExistingDirectory(self, "设置壁纸路径", QDir.currentPath())

        if self.cfg["wallpaper"]["path"]:
            # 读取壁纸列表
            self.wallpapers = self.get_wallpapers()

            # 保存到配置文件
            config = configparser.ConfigParser()
            config.read_dict(self.cfg)
            config.write(open(self.cfg_path, "w"))

    def show_paper(self, classify=""):
        """显示一张壁纸"""

        if not self.wallpapers:
            return

        if classify == "":
            classify = random.choice(list(self.wallpapers.keys()))

        self.cur_classify = classify
        self.cur_wallpaper = random.choice(self.wallpapers[classify])

        # 1.打开注册表键
        key = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER, "Control Panel\\Desktop", 0, win32con.KEY_SET_VALUE)

        # 2.设置壁纸风格：0=居中 1=平铺 2=拉伸
        win32api.RegSetValueEx(key, "WallpaperStyle", 0, win32con.REG_SZ, "2")

        # 3.设置壁纸是否缩放：0=缩放 1=原图
        win32api.RegSetValueEx(key, "TileWallpaper", 0, win32con.REG_SZ, "0")

        # 4.设置壁纸
        win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, self.cur_wallpaper, 3)

        # 5.关闭注册表键
        win32api.RegCloseKey(key)

        if self.switch_timer:
            # 重启定时器
            self.end_switch()
            self.start_switch()

    def start_switch(self):
        """开始自动切换"""

        self.switch_timer = QTimer()
        self.switch_timer.start(self.cfg["wallpaper"]["interval"] * 1000 * 60)
        self.switch_timer.timeout.connect(self.show_paper)

    def end_switch(self):
        """停止自动切换"""

        self.switch_timer.stop()
        self.switch_timer = None

    def auto_switch(self):
        """开始、停止自动切换"""

        if self.switch_timer:
            self.end_switch()
        else:
            self.start_switch()

    def del_cur_wallpaper(self):
        """删除当前壁纸"""

        if QMessageBox.question(self, '确认', '是否删除当前壁纸？') == QMessageBox.StandardButton.Yes:
            self.wallpapers[self.cur_classify].remove(self.cur_wallpaper)
            os.remove(self.cur_wallpaper)
            self.show_paper()

    def show_tomato_dialog(self):
        """显示番茄钟对话框"""

        self.tomato_dlg.show()

    def show_calendar_dialog(self):
        """显示记事本对话框"""

        dlg = CalendarDialog()
        dlg.exec_()


class CozyOffice(QApplication):
    """应用主类"""

    def __init__(self, argv):
        """
        构造函数

        :param argv: 启动参数
        """

        super().__init__(argv)

        # 配置文件
        self.cfg_path = "config.ini"
        self.cfg = self.read_config()

    def read_config(self):
        """读取配置文件"""

        cfg = {
            "tomato": {
                "work": 25,
                "rest": 5
            },
            "wallpaper": {
                "path": "",
                "interval": 10
            }
        }

        if os.path.exists(self.cfg_path):
            config = configparser.ConfigParser()
            config.read(self.cfg_path)

            if config.has_option("tomato", "work"):
                cfg["tomato"]["work"] = config.getint("tomato", "work")

            if config.has_option("tomato", "rest"):
                cfg["tomato"]["rest"] = config.getint("tomato", "rest")

            if config.has_option("wallpaper", "path"):
                cfg["wallpaper"]["path"] = config.get("wallpaper", "path")

            if config.has_option("wallpaper", "interval"):
                cfg["wallpaper"]["interval"] = config.getint("wallpaper", "interval")
        else:
            self.save_config(cfg)

        return cfg

    def save_config(self, default=None):
        """保存配置文件"""

        config = configparser.ConfigParser()
        if default:
            config.read_dict(default)
        else:
            config.read_dict(self.cfg)
            
        config.write(open(self.cfg_path, "w"))


def main():
    """主函数"""

    app = CozyOffice(sys.argv)
    app.setQuitOnLastWindowClosed(False)
    dlg = MainWindow()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
