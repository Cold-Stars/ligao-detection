# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'home.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDoubleSpinBox,
    QFrame, QHBoxLayout, QLabel, QLayout,
    QMainWindow, QProgressBar, QPushButton, QScrollArea,
    QSizePolicy, QSlider, QSpacerItem, QSpinBox,
    QSplitter, QStackedWidget, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1258, 719)
        self.Main_QW = QWidget(MainWindow)
        self.Main_QW.setObjectName(u"Main_QW")
        self.horizontalLayout_14 = QHBoxLayout(self.Main_QW)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.Main_QF = QFrame(self.Main_QW)
        self.Main_QF.setObjectName(u"Main_QF")
        self.Main_QF.setStyleSheet(u"QFrame#Main_QF{\n"
"	background-color: qlineargradient(x0:0, y0:1, x1:1, y1:1,stop:0.4  rgb(0, 0, 100), stop:1 rgb(10, 50, 200));\n"
"border:0px solid red;\n"
"border-radius:30px\n"
"}")
        self.main_qframe = QHBoxLayout(self.Main_QF)
        self.main_qframe.setSpacing(0)
        self.main_qframe.setObjectName(u"main_qframe")
        self.main_qframe.setContentsMargins(0, 0, 0, 0)
        self.LeftMenuBg = QFrame(self.Main_QF)
        self.LeftMenuBg.setObjectName(u"LeftMenuBg")
        self.LeftMenuBg.setMinimumSize(QSize(68, 0))
        self.LeftMenuBg.setMaximumSize(QSize(68, 16777215))
        self.LeftMenuBg.setStyleSheet(u"QFrame#LeftMenuBg{\n"
"	background-color: rgba(255, 255, 255,0);\n"
"border:0px solid red;\n"
"border-radius:30px\n"
"}")
        self.LeftMenuBg.setFrameShape(QFrame.Shape.NoFrame)
        self.LeftMenuBg.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.LeftMenuBg)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, -1)
        self.ToggleBox = QFrame(self.LeftMenuBg)
        self.ToggleBox.setObjectName(u"ToggleBox")
        self.ToggleBox.setMinimumSize(QSize(200, 80))
        self.ToggleBox.setMaximumSize(QSize(200, 80))
        self.ToggleBox.setFrameShape(QFrame.Shape.NoFrame)
        self.ToggleBox.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.ToggleBox)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.ToggleBotton = QPushButton(self.ToggleBox)
        self.ToggleBotton.setObjectName(u"ToggleBotton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ToggleBotton.sizePolicy().hasHeightForWidth())
        self.ToggleBotton.setSizePolicy(sizePolicy)
        self.ToggleBotton.setMinimumSize(QSize(0, 45))
        self.ToggleBotton.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setFamilies([u"Nirmala UI"])
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        self.ToggleBotton.setFont(font)
        self.ToggleBotton.setCursor(QCursor(Qt.PointingHandCursor))
        self.ToggleBotton.setMouseTracking(True)
        self.ToggleBotton.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.ToggleBotton.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.ToggleBotton.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.ToggleBotton.setAutoFillBackground(False)
        self.ToggleBotton.setStyleSheet(u"QPushButton{\n"
"background-image: url(:/all/img/menu.png);\n"
"background-repeat: no-repeat;\n"
"background-position: left center;\n"
"border: none;\n"
"border-left: 23px solid transparent;\n"
"\n"
"text-align: center;\n"
"padding-left: 0px;\n"
"color: rgba(255, 255, 255, 199);\n"
"font: 700 12pt \"Nirmala UI\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgba(114, 129, 214, 59);\n"
"}")
        icon = QIcon(QIcon.fromTheme(u"zoom-out"))
        self.ToggleBotton.setIcon(icon)
        self.ToggleBotton.setAutoDefault(False)
        self.ToggleBotton.setFlat(False)

        self.verticalLayout_4.addWidget(self.ToggleBotton)


        self.verticalLayout_2.addWidget(self.ToggleBox)

        self.MenuBox = QFrame(self.LeftMenuBg)
        self.MenuBox.setObjectName(u"MenuBox")
        self.MenuBox.setMinimumSize(QSize(200, 0))
        self.MenuBox.setMaximumSize(QSize(200, 16777215))
        self.MenuBox.setFrameShape(QFrame.Shape.NoFrame)
        self.MenuBox.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.MenuBox)
        self.verticalLayout_5.setSpacing(15)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.src_file_button = QPushButton(self.MenuBox)
        self.src_file_button.setObjectName(u"src_file_button")
        self.src_file_button.setMinimumSize(QSize(0, 45))
        self.src_file_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.src_file_button.setStyleSheet(u"QPushButton{\n"
"background-image: url(:/all/img/file.png);\n"
"background-repeat: no-repeat;\n"
"background-position: left center;\n"
"border: none;\n"
"border-left: 23px solid transparent;\n"
"\n"
"text-align: center;\n"
"padding-left: 0px;\n"
"color: rgba(255, 255, 255, 199);\n"
"font: 700 12pt \"Nirmala UI\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgba(114, 129, 214, 59);\n"
"}")

        self.verticalLayout_5.addWidget(self.src_file_button)

        self.src_cam_button = QPushButton(self.MenuBox)
        self.src_cam_button.setObjectName(u"src_cam_button")
        self.src_cam_button.setMinimumSize(QSize(0, 45))
        self.src_cam_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.src_cam_button.setStyleSheet(u"QPushButton{\n"
"background-image: url(:/all/img/cam.png);\n"
"background-repeat: no-repeat;\n"
"background-position: left center;\n"
"border: none;\n"
"border-left: 23px solid transparent;\n"
"\n"
"text-align: center;\n"
"padding-left: 0px;\n"
"color: rgba(255, 255, 255, 199);\n"
"font: 700 12pt \"Nirmala UI\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgba(114, 129, 214, 59);\n"
"}")
        self.src_cam_button.setCheckable(False)

        self.verticalLayout_5.addWidget(self.src_cam_button)

        self.src_rtsp_button = QPushButton(self.MenuBox)
        self.src_rtsp_button.setObjectName(u"src_rtsp_button")
        self.src_rtsp_button.setMinimumSize(QSize(0, 45))
        self.src_rtsp_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.src_rtsp_button.setAutoFillBackground(False)
        self.src_rtsp_button.setStyleSheet(u"QPushButton{\n"
"background-image: url(:/all/img/RTSP.png);\n"
"background-repeat: no-repeat;\n"
"background-position: left center;\n"
"border: none;\n"
"border-left: 23px solid transparent;\n"
"\n"
"text-align: center;\n"
"padding-left: 0px;\n"
"color: rgba(255, 255, 255, 199);\n"
"font: 700 12pt \"Nirmala UI\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgba(114, 129, 214, 59);\n"
"}")

        self.verticalLayout_5.addWidget(self.src_rtsp_button)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.verticalLayout_5.setStretch(0, 1)

        self.verticalLayout_2.addWidget(self.MenuBox)

        self.VersionInfo = QFrame(self.LeftMenuBg)
        self.VersionInfo.setObjectName(u"VersionInfo")
        self.VersionInfo.setMinimumSize(QSize(235, 10))
        self.VersionInfo.setMaximumSize(QSize(250, 15))
        self.VersionInfo.setFrameShape(QFrame.Shape.StyledPanel)
        self.VersionInfo.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.VersionInfo)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(18, 0, -1, 0)
        self.VersionLabel = QLabel(self.VersionInfo)
        self.VersionLabel.setObjectName(u"VersionLabel")
        self.VersionLabel.setStyleSheet(u"font: 900 italic 10pt \"Segoe UI\";\n"
"color: rgba(255, 255, 255, 199);")
        self.VersionLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.VersionLabel)


        self.verticalLayout_2.addWidget(self.VersionInfo)


        self.main_qframe.addWidget(self.LeftMenuBg)

        self.ContentBox = QFrame(self.Main_QF)
        self.ContentBox.setObjectName(u"ContentBox")
        self.ContentBox.setStyleSheet(u"QFrame#ContentBox{\n"
"	background-color: rgb(245, 249, 254);\n"
"border:0px solid red;\n"
"border-radius:30px\n"
"}")
        self.ContentBox.setFrameShape(QFrame.Shape.StyledPanel)
        self.ContentBox.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.ContentBox)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.top = QFrame(self.ContentBox)
        self.top.setObjectName(u"top")
        self.top.setMinimumSize(QSize(0, 30))
        self.top.setMaximumSize(QSize(16777215, 30))
        self.top.setStyleSheet(u"QFrame#top{\n"
"background-color: rgba(255, 255, 255,0);\n"
"}")
        self.top.setFrameShape(QFrame.Shape.StyledPanel)
        self.top.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.top)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(20, 0, -1, 0)
        self.explain_title = QLabel(self.top)
        self.explain_title.setObjectName(u"explain_title")
        self.explain_title.setMinimumSize(QSize(0, 30))
        self.explain_title.setMaximumSize(QSize(16777215, 30))
        self.explain_title.setStyleSheet(u"font: 700 italic 11pt \"Segoe UI\";")
        self.explain_title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.explain_title)

        self.buttons_sf = QFrame(self.top)
        self.buttons_sf.setObjectName(u"buttons_sf")
        self.buttons_sf.setMinimumSize(QSize(120, 30))
        self.buttons_sf.setMaximumSize(QSize(120, 30))
        self.buttons_sf.setFrameShape(QFrame.Shape.StyledPanel)
        self.buttons_sf.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.buttons_sf)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.settings_button = QPushButton(self.buttons_sf)
        self.settings_button.setObjectName(u"settings_button")
        self.settings_button.setMinimumSize(QSize(0, 20))
        self.settings_button.setMaximumSize(QSize(16777215, 20))
        self.settings_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.settings_button.setStyleSheet(u"QPushButton{\n"
"background-image: url(:/all/img/set.png);\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"border: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"}")

        self.horizontalLayout_2.addWidget(self.settings_button)

        self.min_sf = QPushButton(self.buttons_sf)
        self.min_sf.setObjectName(u"min_sf")
        self.min_sf.setMinimumSize(QSize(14, 14))
        self.min_sf.setMaximumSize(QSize(14, 14))
        self.min_sf.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(4, 180, 0);\n"
"border:1px solid rgba(113, 17, 15,50);\n"
"border-radius:6px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(139, 29, 31)\n"
"	\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(232, 59, 35);\n"
"}\n"
"")

        self.horizontalLayout_2.addWidget(self.min_sf)

        self.max_sf = QPushButton(self.buttons_sf)
        self.max_sf.setObjectName(u"max_sf")
        self.max_sf.setMinimumSize(QSize(14, 14))
        self.max_sf.setMaximumSize(QSize(14, 14))
        self.max_sf.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(227, 199, 0);\n"
"border:1px solid rgba(113, 17, 15,50);\n"
"border-radius:6px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(139, 29, 31)\n"
"	\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(232, 59, 35);\n"
"}\n"
"")

        self.horizontalLayout_2.addWidget(self.max_sf)

        self.close_button = QPushButton(self.buttons_sf)
        self.close_button.setObjectName(u"close_button")
        self.close_button.setMinimumSize(QSize(14, 14))
        self.close_button.setMaximumSize(QSize(14, 14))
        self.close_button.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(240, 108, 96);\n"
"border:1px solid rgba(113, 17, 15,50);\n"
"border-radius:6px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(139, 29, 31)\n"
"	\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(232, 59, 35);\n"
"}\n"
"")

        self.horizontalLayout_2.addWidget(self.close_button)


        self.horizontalLayout.addWidget(self.buttons_sf)


        self.verticalLayout_6.addWidget(self.top)

        self.content = QStackedWidget(self.ContentBox)
        self.content.setObjectName(u"content")
        self.content.setStyleSheet(u"")
        self.content.setFrameShape(QFrame.Shape.StyledPanel)
        self.content.setFrameShadow(QFrame.Shadow.Raised)
        self.Page0 = QWidget()
        self.Page0.setObjectName(u"Page0")
        self.Page0.setStyleSheet(u"background: transparent;")
        self.horizontalLayout_5 = QHBoxLayout(self.Page0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, 0, 0, 0)
        self.main_content = QVBoxLayout()
        self.main_content.setSpacing(5)
        self.main_content.setObjectName(u"main_content")
        self.Result_QF = QFrame(self.Page0)
        self.Result_QF.setObjectName(u"Result_QF")
        self.Result_QF.setStyleSheet(u"")
        self.Result_QF.setFrameShape(QFrame.Shape.StyledPanel)
        self.Result_QF.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.Result_QF)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.splitter = QSplitter(self.Result_QF)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setStyleSheet(u"#splitter::handle{background: 1px solid  rgba(200, 200, 200,100);}")
        self.splitter.setOrientation(Qt.Orientation.Horizontal)
        self.splitter.setHandleWidth(2)
        self.pre_video = QLabel(self.splitter)
        self.pre_video.setObjectName(u"pre_video")
        self.pre_video.setMinimumSize(QSize(200, 100))
        self.pre_video.setStyleSheet(u"background-color: rgb(238, 242, 255);\n"
"border:2px solid rgb(255, 255, 255);\n"
"border-radius:15px")
        self.pre_video.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.splitter.addWidget(self.pre_video)
        self.res_video = QLabel(self.splitter)
        self.res_video.setObjectName(u"res_video")
        self.res_video.setMinimumSize(QSize(200, 100))
        self.res_video.setStyleSheet(u"background-color: rgb(238, 242, 255);\n"
"border:2px solid rgb(255, 255, 255);\n"
"border-radius:15px")
        self.res_video.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.splitter.addWidget(self.res_video)

        self.verticalLayout_16.addWidget(self.splitter)


        self.main_content.addWidget(self.Result_QF)

        self.QF_Group = QFrame(self.Page0)
        self.QF_Group.setObjectName(u"QF_Group")
        self.QF_Group.setMinimumSize(QSize(0, 150))
        self.QF_Group.setMaximumSize(QSize(16777215, 150))
        self.QF_Group.setStyleSheet(u"QFrame#QF_Group{\n"
"background-color: rgb(238, 242, 255);\n"
"border:2px solid rgb(255, 255, 255);\n"
"border-radius:15px;\n"
"}")
        self.QF_Group.setFrameShape(QFrame.Shape.StyledPanel)
        self.QF_Group.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.QF_Group)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 9, -1, 15)
        self.scrollArea_2 = QScrollArea(self.QF_Group)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setMinimumSize(QSize(0, 150))
        self.scrollArea_2.setMaximumSize(QSize(16777215, 150))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 1153, 148))
        self.label_img_2 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_img_2.setObjectName(u"label_img_2")
        self.label_img_2.setGeometry(QRect(0, 0, 54, 130))
        self.label_img_2.setMinimumSize(QSize(0, 130))
        self.label_img_2.setMaximumSize(QSize(16777215, 130))
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.horizontalLayout_3.addWidget(self.scrollArea_2)


        self.main_content.addWidget(self.QF_Group)

        self.Pause_QF = QFrame(self.Page0)
        self.Pause_QF.setObjectName(u"Pause_QF")
        self.Pause_QF.setMinimumSize(QSize(0, 30))
        self.Pause_QF.setMaximumSize(QSize(16777215, 30))
        self.Pause_QF.setFrameShape(QFrame.Shape.StyledPanel)
        self.Pause_QF.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.Pause_QF)
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 3, 0)
        self.run_button = QPushButton(self.Pause_QF)
        self.run_button.setObjectName(u"run_button")
        self.run_button.setMinimumSize(QSize(0, 30))
        self.run_button.setMaximumSize(QSize(16777215, 30))
        self.run_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.run_button.setMouseTracking(True)
        self.run_button.setStyleSheet(u"QPushButton{\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"border: none;\n"
"}\n"
"QPushButton:hover{\n"
"\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/all/img/begin.png", QSize(), QIcon.Normal, QIcon.Off)
        icon1.addFile(u":/all/img/pause.png", QSize(), QIcon.Normal, QIcon.On)
        self.run_button.setIcon(icon1)
        self.run_button.setIconSize(QSize(30, 30))
        self.run_button.setCheckable(True)
        self.run_button.setChecked(False)

        self.horizontalLayout_4.addWidget(self.run_button)

        self.progress_bar = QProgressBar(self.Pause_QF)
        self.progress_bar.setObjectName(u"progress_bar")
        self.progress_bar.setMinimumSize(QSize(0, 20))
        self.progress_bar.setMaximumSize(QSize(16777215, 20))
        self.progress_bar.setStyleSheet(u"QProgressBar{ \n"
"font: 700 10pt \"Microsoft YaHei UI\";\n"
"color: rgb(253, 143, 134); \n"
"text-align:center; \n"
"border:3px solid rgb(255, 255, 255);\n"
"border-radius: 10px; \n"
"background-color: rgba(215, 215, 215,100);\n"
"} \n"
"\n"
"QProgressBar:chunk{ \n"
"border-radius:0px; \n"
"background: rgba(119, 111, 252, 200);\n"
"border-radius: 7px;\n"
"}")
        self.progress_bar.setMaximum(1000)
        self.progress_bar.setValue(0)

        self.horizontalLayout_4.addWidget(self.progress_bar)

        self.stop_button = QPushButton(self.Pause_QF)
        self.stop_button.setObjectName(u"stop_button")
        self.stop_button.setMinimumSize(QSize(0, 30))
        self.stop_button.setMaximumSize(QSize(16777215, 30))
        self.stop_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.stop_button.setStyleSheet(u"QPushButton{\n"
"background-image: url(:/all/img/stop.png);\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"border: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"}")

        self.horizontalLayout_4.addWidget(self.stop_button)


        self.main_content.addWidget(self.Pause_QF)


        self.horizontalLayout_5.addLayout(self.main_content)

        self.prm_page = QFrame(self.Page0)
        self.prm_page.setObjectName(u"prm_page")
        self.prm_page.setMinimumSize(QSize(0, 0))
        self.prm_page.setMaximumSize(QSize(0, 16777215))
        self.prm_page.setStyleSheet(u"QFrame#prm_page{\n"
"background-color: qradialgradient(cx:0, cy:0, radius:1, fx:0.1, fy:0.1, stop:0 rgb(0, 0, 100),  stop:1 rgb(10, 50, 200));\n"
"border-top-left-radius:30px;\n"
"border-top-right-radius:0px;\n"
"border-bottom-right-radius:0px;\n"
"border-bottom-left-radius:30px;\n"
"}")
        self.prm_page.setFrameShape(QFrame.Shape.StyledPanel)
        self.prm_page.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.prm_page)
        self.verticalLayout_22.setSpacing(15)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(15, 15, -1, -1)
        self.label = QLabel(self.prm_page)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"padding-left: 0px;\n"
"padding-bottom: 2px;\n"
"color: rgba(255, 255, 255, 240);\n"
"font: 700 italic 16pt \"Segoe UI\";")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_22.addWidget(self.label)

        self.Model_QF_2 = QWidget(self.prm_page)
        self.Model_QF_2.setObjectName(u"Model_QF_2")
        self.Model_QF_2.setMinimumSize(QSize(190, 90))
        self.Model_QF_2.setMaximumSize(QSize(190, 90))
        self.Model_QF_2.setStyleSheet(u"QWidget#Model_QF_2{\n"
"border:2px solid rgba(255, 255, 255, 70);\n"
"border-radius:15px;\n"
"}")
        self.verticalLayout_21 = QVBoxLayout(self.Model_QF_2)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(9, 9, 9, 9)
        self.ToggleBotton_6 = QPushButton(self.Model_QF_2)
        self.ToggleBotton_6.setObjectName(u"ToggleBotton_6")
        sizePolicy.setHeightForWidth(self.ToggleBotton_6.sizePolicy().hasHeightForWidth())
        self.ToggleBotton_6.setSizePolicy(sizePolicy)
        self.ToggleBotton_6.setMinimumSize(QSize(0, 30))
        self.ToggleBotton_6.setMaximumSize(QSize(16777215, 30))
        font1 = QFont()
        font1.setFamilies([u"Nirmala UI"])
        font1.setPointSize(13)
        font1.setBold(True)
        font1.setItalic(False)
        self.ToggleBotton_6.setFont(font1)
        self.ToggleBotton_6.setCursor(QCursor(Qt.ArrowCursor))
        self.ToggleBotton_6.setMouseTracking(True)
        self.ToggleBotton_6.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.ToggleBotton_6.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.ToggleBotton_6.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.ToggleBotton_6.setAutoFillBackground(False)
        self.ToggleBotton_6.setStyleSheet(u"QPushButton{\n"
"background-image: url(:/all/img/model.png);\n"
"background-repeat: no-repeat;\n"
"background-position: left center;\n"
"border: none;\n"
"border-left: 20px solid transparent;\n"
"\n"
"text-align: left;\n"
"padding-left: 40px;\n"
"padding-bottom: 2px;\n"
"color: rgba(255, 255, 255, 199);\n"
"font: 700 13pt \"Nirmala UI\";\n"
"}")
        self.ToggleBotton_6.setIcon(icon)
        self.ToggleBotton_6.setAutoDefault(False)
        self.ToggleBotton_6.setFlat(False)

        self.verticalLayout_21.addWidget(self.ToggleBotton_6)

        self.model_box = QComboBox(self.Model_QF_2)
        self.model_box.setObjectName(u"model_box")
        self.model_box.setMinimumSize(QSize(170, 20))
        self.model_box.setMaximumSize(QSize(170, 20))
        self.model_box.setStyleSheet(u"\n"
"QComboBox {\n"
"            background-color: rgba(255,255,255,90);\n"
"			color: rgba(0, 0, 0, 200);\n"
"			font: 600 9pt \"Segoe UI\";\n"
"            border: 1px solid lightgray;\n"
"            border-radius: 10px;\n"
"            padding-left: 15px;\n"
"        }\n"
"        \n"
"        QComboBox:on {\n"
"            border: 1px solid #63acfb;\n"
"        }\n"
"\n"
"        QComboBox::drop-down {\n"
"            width: 22px;\n"
"            border-left: 1px solid lightgray;\n"
"            border-top-right-radius: 15px;\n"
"            border-bottom-right-radius: 15px;\n"
"        }\n"
"        \n"
"        QComboBox::drop-down:on {\n"
"            border-left: 1px solid #63acfb;\n"
"        }\n"
"\n"
"        QComboBox::down-arrow {\n"
"            width: 16px;\n"
"            height: 16px;\n"
"            image: url(:/all/img/box_down.png);\n"
"        }\n"
"\n"
"        QComboBox::down-arrow:on {\n"
"            image: url(:/all/img/box_up.png);\n"
"        }\n"
"\n"
"        QComboBox QAbstractI"
                        "temView {\n"
"            border: none;\n"
"            outline: none;\n"
"			padding: 10px;\n"
"            background-color: rgb(223, 188, 220);\n"
"        }\n"
"\n"
"\n"
"        QComboBox QScrollBar:vertical {\n"
"            width: 2px;\n"
"           background-color: rgba(255,255,255,150);\n"
"        }\n"
"\n"
"        QComboBox QScrollBar::handle:vertical {\n"
"            background-color: rgba(255,255,255,90);\n"
"        }")
        self.model_box.setInsertPolicy(QComboBox.InsertPolicy.NoInsert)
        self.model_box.setMinimumContentsLength(0)

        self.verticalLayout_21.addWidget(self.model_box)


        self.verticalLayout_22.addWidget(self.Model_QF_2)

        self.IOU_QF = QFrame(self.prm_page)
        self.IOU_QF.setObjectName(u"IOU_QF")
        self.IOU_QF.setMinimumSize(QSize(190, 90))
        self.IOU_QF.setMaximumSize(QSize(190, 90))
        self.IOU_QF.setStyleSheet(u"QFrame#IOU_QF{\n"
"border:2px solid rgba(255, 255, 255, 70);\n"
"border-radius:15px;\n"
"}")
        self.verticalLayout_15 = QVBoxLayout(self.IOU_QF)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.ToggleBotton_2 = QPushButton(self.IOU_QF)
        self.ToggleBotton_2.setObjectName(u"ToggleBotton_2")
        sizePolicy.setHeightForWidth(self.ToggleBotton_2.sizePolicy().hasHeightForWidth())
        self.ToggleBotton_2.setSizePolicy(sizePolicy)
        self.ToggleBotton_2.setMinimumSize(QSize(0, 30))
        self.ToggleBotton_2.setMaximumSize(QSize(16777215, 30))
        self.ToggleBotton_2.setFont(font1)
        self.ToggleBotton_2.setCursor(QCursor(Qt.ArrowCursor))
        self.ToggleBotton_2.setMouseTracking(True)
        self.ToggleBotton_2.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.ToggleBotton_2.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.ToggleBotton_2.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.ToggleBotton_2.setAutoFillBackground(False)
        self.ToggleBotton_2.setStyleSheet(u"QPushButton{\n"
"background-image: url(:/all/img/IOU.png);\n"
"background-repeat: no-repeat;\n"
"background-position: left center;\n"
"border: none;\n"
"border-left: 20px solid transparent;\n"
"\n"
"text-align: left;\n"
"padding-left: 40px;\n"
"padding-bottom: 4px;\n"
"color: rgba(255, 255, 255, 199);\n"
"font: 700 13pt \"Nirmala UI\";\n"
"}")
        self.ToggleBotton_2.setIcon(icon)
        self.ToggleBotton_2.setAutoDefault(False)
        self.ToggleBotton_2.setFlat(False)

        self.verticalLayout_15.addWidget(self.ToggleBotton_2)

        self.frame_3 = QFrame(self.IOU_QF)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy1)
        self.frame_3.setMinimumSize(QSize(0, 20))
        self.frame_3.setMaximumSize(QSize(16777215, 20))
        self.horizontalLayout_10 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_10.setSpacing(10)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(8, 0, 10, 0)
        self.iou_spinbox = QDoubleSpinBox(self.frame_3)
        self.iou_spinbox.setObjectName(u"iou_spinbox")
        self.iou_spinbox.setCursor(QCursor(Qt.PointingHandCursor))
        self.iou_spinbox.setStyleSheet(u"QDoubleSpinBox {\n"
"border: 0px solid lightgray;\n"
"border-radius: 2px;\n"
"background-color: rgba(255,255,255,90);\n"
"font: 600 9pt \"Segoe UI\";\n"
"}\n"
"        \n"
"QDoubleSpinBox::up-button {\n"
"width: 10px;\n"
"height: 9px;\n"
"margin: 0px 3px 0px 0px;\n"
"border-image: url(:/all/img/box_up.png);\n"
"}\n"
"QDoubleSpinBox::up-button:pressed {\n"
"margin-top: 1px;\n"
"}\n"
"            \n"
"QDoubleSpinBox::down-button {\n"
"width: 10px;\n"
"height: 9px;\n"
"margin: 0px 3px 0px 0px;\n"
"border-image: url(:/all/img/box_down.png);\n"
"}\n"
"QDoubleSpinBox::down-button:pressed {\n"
"margin-bottom: 1px;\n"
"}")
        self.iou_spinbox.setMinimum(0.010000000000000)
        self.iou_spinbox.setMaximum(1.000000000000000)
        self.iou_spinbox.setSingleStep(0.050000000000000)
        self.iou_spinbox.setValue(0.450000000000000)

        self.horizontalLayout_10.addWidget(self.iou_spinbox)

        self.iou_slider = QSlider(self.frame_3)
        self.iou_slider.setObjectName(u"iou_slider")
        self.iou_slider.setCursor(QCursor(Qt.PointingHandCursor))
        self.iou_slider.setStyleSheet(u"QSlider::groove:horizontal {\n"
"border: none;\n"
"height: 10px;\n"
"background-color: rgba(255,255,255,90);\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"width: 10px;\n"
"margin: -1px 0px -1px 0px;\n"
"border-radius: 3px;\n"
"background-color: white;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #59969b, stop:1 #04e7fa);\n"
"border-radius: 5px;\n"
"}")
        self.iou_slider.setMinimum(1)
        self.iou_slider.setMaximum(100)
        self.iou_slider.setValue(45)
        self.iou_slider.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout_10.addWidget(self.iou_slider)


        self.verticalLayout_15.addWidget(self.frame_3)


        self.verticalLayout_22.addWidget(self.IOU_QF)

        self.Conf_QF = QFrame(self.prm_page)
        self.Conf_QF.setObjectName(u"Conf_QF")
        self.Conf_QF.setMinimumSize(QSize(190, 90))
        self.Conf_QF.setMaximumSize(QSize(190, 90))
        self.Conf_QF.setStyleSheet(u"QFrame#Conf_QF{\n"
"border:2px solid rgba(255, 255, 255, 70);\n"
"border-radius:15px;\n"
"}")
        self.verticalLayout_18 = QVBoxLayout(self.Conf_QF)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.ToggleBotton_3 = QPushButton(self.Conf_QF)
        self.ToggleBotton_3.setObjectName(u"ToggleBotton_3")
        sizePolicy.setHeightForWidth(self.ToggleBotton_3.sizePolicy().hasHeightForWidth())
        self.ToggleBotton_3.setSizePolicy(sizePolicy)
        self.ToggleBotton_3.setMinimumSize(QSize(0, 30))
        self.ToggleBotton_3.setMaximumSize(QSize(16777215, 30))
        self.ToggleBotton_3.setFont(font1)
        self.ToggleBotton_3.setCursor(QCursor(Qt.ArrowCursor))
        self.ToggleBotton_3.setMouseTracking(True)
        self.ToggleBotton_3.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.ToggleBotton_3.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.ToggleBotton_3.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.ToggleBotton_3.setAutoFillBackground(False)
        self.ToggleBotton_3.setStyleSheet(u"QPushButton{\n"
"background-image: url(:/all/img/conf.png);\n"
"background-repeat: no-repeat;\n"
"background-position: left center;\n"
"border: none;\n"
"border-left: 20px solid transparent;\n"
"\n"
"text-align: left;\n"
"padding-left: 40px;\n"
"padding-bottom: 4px;\n"
"color: rgba(255, 255, 255, 199);\n"
"font: 700 13pt \"Nirmala UI\";\n"
"}")
        self.ToggleBotton_3.setIcon(icon)
        self.ToggleBotton_3.setAutoDefault(False)
        self.ToggleBotton_3.setFlat(False)

        self.verticalLayout_18.addWidget(self.ToggleBotton_3)

        self.frame = QFrame(self.Conf_QF)
        self.frame.setObjectName(u"frame")
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setMinimumSize(QSize(0, 20))
        self.frame.setMaximumSize(QSize(16777215, 20))
        self.horizontalLayout_11 = QHBoxLayout(self.frame)
        self.horizontalLayout_11.setSpacing(10)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(8, 0, 10, 0)
        self.conf_spinbox = QDoubleSpinBox(self.frame)
        self.conf_spinbox.setObjectName(u"conf_spinbox")
        self.conf_spinbox.setCursor(QCursor(Qt.PointingHandCursor))
        self.conf_spinbox.setStyleSheet(u"QDoubleSpinBox {\n"
"border: 0px solid lightgray;\n"
"border-radius: 2px;\n"
"background-color: rgba(255,255,255,90);\n"
"font: 600 9pt \"Segoe UI\";\n"
"}\n"
"        \n"
"QDoubleSpinBox::up-button {\n"
"width: 10px;\n"
"height: 9px;\n"
"margin: 0px 3px 0px 0px;\n"
"border-image: url(:/all/img/box_up.png);\n"
"}\n"
"QDoubleSpinBox::up-button:pressed {\n"
"margin-top: 1px;\n"
"}\n"
"            \n"
"QDoubleSpinBox::down-button {\n"
"width: 10px;\n"
"height: 9px;\n"
"margin: 0px 3px 0px 0px;\n"
"border-image: url(:/all/img/box_down.png);\n"
"}\n"
"QDoubleSpinBox::down-button:pressed {\n"
"margin-bottom: 1px;\n"
"}")
        self.conf_spinbox.setMinimum(0.010000000000000)
        self.conf_spinbox.setMaximum(1.000000000000000)
        self.conf_spinbox.setSingleStep(0.050000000000000)
        self.conf_spinbox.setValue(0.250000000000000)

        self.horizontalLayout_11.addWidget(self.conf_spinbox)

        self.conf_slider = QSlider(self.frame)
        self.conf_slider.setObjectName(u"conf_slider")
        self.conf_slider.setCursor(QCursor(Qt.PointingHandCursor))
        self.conf_slider.setStyleSheet(u"QSlider::groove:horizontal {\n"
"border: none;\n"
"height: 10px;\n"
"background-color: rgba(255,255,255,90);\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"width: 10px;\n"
"margin: -1px 0px -1px 0px;\n"
"border-radius: 3px;\n"
"background-color: white;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #59969b, stop:1 #04e7fa);\n"
"border-radius: 5px;\n"
"}")
        self.conf_slider.setMinimum(1)
        self.conf_slider.setMaximum(100)
        self.conf_slider.setValue(25)
        self.conf_slider.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout_11.addWidget(self.conf_slider)


        self.verticalLayout_18.addWidget(self.frame)


        self.verticalLayout_22.addWidget(self.Conf_QF)

        self.Delay_QF = QFrame(self.prm_page)
        self.Delay_QF.setObjectName(u"Delay_QF")
        self.Delay_QF.setMinimumSize(QSize(190, 90))
        self.Delay_QF.setMaximumSize(QSize(190, 90))
        self.Delay_QF.setStyleSheet(u"QFrame#Delay_QF{\n"
"border:2px solid rgba(255, 255, 255, 70);\n"
"border-radius:15px;\n"
"}")
        self.verticalLayout_19 = QVBoxLayout(self.Delay_QF)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.ToggleBotton_4 = QPushButton(self.Delay_QF)
        self.ToggleBotton_4.setObjectName(u"ToggleBotton_4")
        sizePolicy.setHeightForWidth(self.ToggleBotton_4.sizePolicy().hasHeightForWidth())
        self.ToggleBotton_4.setSizePolicy(sizePolicy)
        self.ToggleBotton_4.setMinimumSize(QSize(0, 30))
        self.ToggleBotton_4.setMaximumSize(QSize(16777215, 30))
        self.ToggleBotton_4.setFont(font1)
        self.ToggleBotton_4.setCursor(QCursor(Qt.ArrowCursor))
        self.ToggleBotton_4.setMouseTracking(True)
        self.ToggleBotton_4.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.ToggleBotton_4.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.ToggleBotton_4.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.ToggleBotton_4.setAutoFillBackground(False)
        self.ToggleBotton_4.setStyleSheet(u"QPushButton{\n"
"background-image: url(:/all/img/delay.png);\n"
"background-repeat: no-repeat;\n"
"background-position: left center;\n"
"border: none;\n"
"border-left: 20px solid transparent;\n"
"\n"
"text-align: left;\n"
"padding-left: 40px;\n"
"padding-bottom: 2px;\n"
"color: rgba(255, 255, 255, 199);\n"
"font: 700 13pt \"Nirmala UI\";\n"
"}")
        self.ToggleBotton_4.setIcon(icon)
        self.ToggleBotton_4.setAutoDefault(False)
        self.ToggleBotton_4.setFlat(False)

        self.verticalLayout_19.addWidget(self.ToggleBotton_4)

        self.frame_2 = QFrame(self.Delay_QF)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.frame_2.setMinimumSize(QSize(0, 20))
        self.frame_2.setMaximumSize(QSize(16777215, 20))
        self.horizontalLayout_12 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_12.setSpacing(10)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(8, 0, 10, 0)
        self.speed_spinbox = QSpinBox(self.frame_2)
        self.speed_spinbox.setObjectName(u"speed_spinbox")
        self.speed_spinbox.setStyleSheet(u"QSpinBox {\n"
"border: 0px solid lightgray;\n"
"border-radius: 2px;\n"
"background-color: rgba(255,255,255,90);\n"
"font: 600 9pt \"Segoe UI\";\n"
"}\n"
"        \n"
"QSpinBox::up-button {\n"
"width: 10px;\n"
"height: 9px;\n"
"margin: 0px 3px 0px 0px;\n"
"border-image: url(:/all/img/box_up.png);\n"
"}\n"
"QSpinBox::up-button:pressed {\n"
"margin-top: 1px;\n"
"}\n"
"            \n"
"QSpinBox::down-button {\n"
"width: 10px;\n"
"height: 9px;\n"
"margin: 0px 3px 0px 0px;\n"
"border-image: url(:/all/img/box_down.png);\n"
"}\n"
"QSpinBox::down-button:pressed {\n"
"margin-bottom: 1px;\n"
"}")
        self.speed_spinbox.setMaximum(50)
        self.speed_spinbox.setValue(10)

        self.horizontalLayout_12.addWidget(self.speed_spinbox)

        self.speed_slider = QSlider(self.frame_2)
        self.speed_slider.setObjectName(u"speed_slider")
        self.speed_slider.setCursor(QCursor(Qt.PointingHandCursor))
        self.speed_slider.setStyleSheet(u"QSlider::groove:horizontal {\n"
"border: none;\n"
"height: 10px;\n"
"background-color: rgba(255,255,255,90);\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"width: 10px;\n"
"margin: -1px 0px -1px 0px;\n"
"border-radius: 3px;\n"
"background-color: white;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"background-color: qradialgradient(cx:0, cy:0, radius:1, fx:0.1, fy:0.1, stop:0 rgb(253, 139, 133),  stop:1 rgb(248, 194, 152));\n"
"border-radius: 5px;\n"
"}")
        self.speed_slider.setMaximum(50)
        self.speed_slider.setValue(10)
        self.speed_slider.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout_12.addWidget(self.speed_slider)


        self.verticalLayout_19.addWidget(self.frame_2)


        self.verticalLayout_22.addWidget(self.Delay_QF)

        self.Save_QF = QFrame(self.prm_page)
        self.Save_QF.setObjectName(u"Save_QF")
        self.Save_QF.setMinimumSize(QSize(190, 120))
        self.Save_QF.setMaximumSize(QSize(190, 120))
        self.Save_QF.setStyleSheet(u"QFrame#Save_QF{\n"
"border:2px solid rgba(255, 255, 255, 70);\n"
"border-radius:15px;\n"
"}")
        self.verticalLayout_20 = QVBoxLayout(self.Save_QF)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(9, 9, 9, 9)
        self.ToggleBotton_5 = QPushButton(self.Save_QF)
        self.ToggleBotton_5.setObjectName(u"ToggleBotton_5")
        sizePolicy.setHeightForWidth(self.ToggleBotton_5.sizePolicy().hasHeightForWidth())
        self.ToggleBotton_5.setSizePolicy(sizePolicy)
        self.ToggleBotton_5.setMinimumSize(QSize(0, 30))
        self.ToggleBotton_5.setMaximumSize(QSize(16777215, 30))
        self.ToggleBotton_5.setFont(font1)
        self.ToggleBotton_5.setCursor(QCursor(Qt.ArrowCursor))
        self.ToggleBotton_5.setMouseTracking(True)
        self.ToggleBotton_5.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.ToggleBotton_5.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.ToggleBotton_5.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.ToggleBotton_5.setAutoFillBackground(False)
        self.ToggleBotton_5.setStyleSheet(u"QPushButton{\n"
"background-image: url(:/all/img/save.png);\n"
"background-repeat: no-repeat;\n"
"background-position: left center;\n"
"border: none;\n"
"border-left: 20px solid transparent;\n"
"\n"
"text-align: left;\n"
"padding-left: 40px;\n"
"padding-bottom: 2px;\n"
"color: rgba(255, 255, 255, 199);\n"
"font: 700 13pt \"Nirmala UI\";\n"
"}")
        self.ToggleBotton_5.setIcon(icon)
        self.ToggleBotton_5.setAutoDefault(False)
        self.ToggleBotton_5.setFlat(False)

        self.verticalLayout_20.addWidget(self.ToggleBotton_5)

        self.save_res_button = QCheckBox(self.Save_QF)
        self.save_res_button.setObjectName(u"save_res_button")
        self.save_res_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.save_res_button.setStyleSheet(u"QCheckBox {\n"
"color: rgba(255, 255, 255, 199);\n"
"font: 590 10pt \"Nirmala UI\";\n"
"        }\n"
"\n"
"        QCheckBox::indicator {\n"
"            padding-top: 1px;\n"
"padding-left: 10px;\n"
"            width: 40px;\n"
"            height: 30px;\n"
"            border: none;\n"
"        }\n"
"\n"
"        QCheckBox::indicator:unchecked {\n"
"            image: url(:/all/img/check_no.png);\n"
"        }\n"
"\n"
"        QCheckBox::indicator:checked {\n"
"            image: url(:/all/img/check_yes.png);\n"
"        }")

        self.verticalLayout_20.addWidget(self.save_res_button)

        self.save_txt_button = QCheckBox(self.Save_QF)
        self.save_txt_button.setObjectName(u"save_txt_button")
        self.save_txt_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.save_txt_button.setStyleSheet(u"QCheckBox {\n"
"color: rgba(255, 255, 255, 199);\n"
"font: 590 10pt \"Nirmala UI\";\n"
"        }\n"
"\n"
"        QCheckBox::indicator {\n"
"            padding-top: 1px;\n"
"padding-left: 10px;\n"
"            width: 40px;\n"
"            height: 30px;\n"
"            border: none;\n"
"        }\n"
"\n"
"        QCheckBox::indicator:unchecked {\n"
"            image: url(:/all/img/check_no.png);\n"
"        }\n"
"\n"
"        QCheckBox::indicator:checked {\n"
"            image: url(:/all/img/check_yes.png);\n"
"        }")

        self.verticalLayout_20.addWidget(self.save_txt_button)


        self.verticalLayout_22.addWidget(self.Save_QF)

        self.verticalSpacer_2 = QSpacerItem(20, 13, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_22.addItem(self.verticalSpacer_2)


        self.horizontalLayout_5.addWidget(self.prm_page)

        self.content.addWidget(self.Page0)
        self.page1 = QWidget()
        self.page1.setObjectName(u"page1")
        sizePolicy1.setHeightForWidth(self.page1.sizePolicy().hasHeightForWidth())
        self.page1.setSizePolicy(sizePolicy1)
        self.page1.setStyleSheet(u"background: transparent;")
        self.horizontalLayout_24 = QHBoxLayout(self.page1)
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(-1, 0, 0, 0)
        self.main_content_cam = QVBoxLayout()
        self.main_content_cam.setSpacing(5)
        self.main_content_cam.setObjectName(u"main_content_cam")
        self.Result_QF_cam = QFrame(self.page1)
        self.Result_QF_cam.setObjectName(u"Result_QF_cam")
        self.Result_QF_cam.setStyleSheet(u"")
        self.Result_QF_cam.setFrameShape(QFrame.Shape.StyledPanel)
        self.Result_QF_cam.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.Result_QF_cam)
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.splitter_cam = QSplitter(self.Result_QF_cam)
        self.splitter_cam.setObjectName(u"splitter_cam")
        self.splitter_cam.setStyleSheet(u"#splitter_cam::handle{background: 1px solid  rgba(200, 200, 200,100);}")
        self.splitter_cam.setOrientation(Qt.Orientation.Horizontal)
        self.splitter_cam.setHandleWidth(2)
        self.pre_cam = QLabel(self.splitter_cam)
        self.pre_cam.setObjectName(u"pre_cam")
        self.pre_cam.setMinimumSize(QSize(200, 100))
        self.pre_cam.setStyleSheet(u"background-color: rgb(238, 242, 255);\n"
"border:2px solid rgb(255, 255, 255);\n"
"border-radius:15px")
        self.pre_cam.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.splitter_cam.addWidget(self.pre_cam)
        self.res_cam = QLabel(self.splitter_cam)
        self.res_cam.setObjectName(u"res_cam")
        self.res_cam.setMinimumSize(QSize(200, 100))
        self.res_cam.setStyleSheet(u"background-color: rgb(238, 242, 255);\n"
"border:2px solid rgb(255, 255, 255);\n"
"border-radius:15px")
        self.res_cam.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.splitter_cam.addWidget(self.res_cam)

        self.verticalLayout_30.addWidget(self.splitter_cam)


        self.main_content_cam.addWidget(self.Result_QF_cam)

        self.QF_Group_cam = QFrame(self.page1)
        self.QF_Group_cam.setObjectName(u"QF_Group_cam")
        self.QF_Group_cam.setMinimumSize(QSize(0, 150))
        self.QF_Group_cam.setMaximumSize(QSize(16777215, 150))
        self.QF_Group_cam.setStyleSheet(u"QFrame#QF_Group_cam{\n"
"background-color: rgb(238, 242, 255);\n"
"border:2px solid rgb(255, 255, 255);\n"
"border-radius:15px;\n"
"}")
        self.QF_Group_cam.setFrameShape(QFrame.Shape.StyledPanel)
        self.QF_Group_cam.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.QF_Group_cam)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(-1, 9, -1, 15)
        self.scrollArea = QScrollArea(self.QF_Group_cam)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMinimumSize(QSize(0, 150))
        self.scrollArea.setMaximumSize(QSize(16777215, 150))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1153, 148))
        self.label_img = QLabel(self.scrollAreaWidgetContents)
        self.label_img.setObjectName(u"label_img")
        self.label_img.setGeometry(QRect(0, 0, 81, 130))
        self.label_img.setMinimumSize(QSize(0, 130))
        self.label_img.setMaximumSize(QSize(16777215, 130))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_15.addWidget(self.scrollArea)


        self.main_content_cam.addWidget(self.QF_Group_cam)

        self.Pause_QF_cam = QFrame(self.page1)
        self.Pause_QF_cam.setObjectName(u"Pause_QF_cam")
        self.Pause_QF_cam.setMinimumSize(QSize(0, 30))
        self.Pause_QF_cam.setMaximumSize(QSize(16777215, 30))
        self.Pause_QF_cam.setFrameShape(QFrame.Shape.StyledPanel)
        self.Pause_QF_cam.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.Pause_QF_cam)
        self.horizontalLayout_20.setSpacing(10)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 3, 0)
        self.run_button_cam = QPushButton(self.Pause_QF_cam)
        self.run_button_cam.setObjectName(u"run_button_cam")
        self.run_button_cam.setMinimumSize(QSize(0, 30))
        self.run_button_cam.setMaximumSize(QSize(16777215, 30))
        self.run_button_cam.setCursor(QCursor(Qt.PointingHandCursor))
        self.run_button_cam.setMouseTracking(True)
        self.run_button_cam.setStyleSheet(u"QPushButton{\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"border: none;\n"
"}\n"
"QPushButton:hover{\n"
"\n"
"}")
        self.run_button_cam.setIcon(icon1)
        self.run_button_cam.setIconSize(QSize(30, 30))
        self.run_button_cam.setCheckable(True)
        self.run_button_cam.setChecked(False)

        self.horizontalLayout_20.addWidget(self.run_button_cam)

        self.progress_bar_cam = QProgressBar(self.Pause_QF_cam)
        self.progress_bar_cam.setObjectName(u"progress_bar_cam")
        self.progress_bar_cam.setMinimumSize(QSize(0, 20))
        self.progress_bar_cam.setMaximumSize(QSize(16777215, 20))
        self.progress_bar_cam.setStyleSheet(u"QProgressBar{ \n"
"font: 700 10pt \"Microsoft YaHei UI\";\n"
"color: rgb(253, 143, 134); \n"
"text-align:center; \n"
"border:3px solid rgb(255, 255, 255);\n"
"border-radius: 10px; \n"
"background-color: rgba(215, 215, 215,100);\n"
"} \n"
"\n"
"QProgressBar:chunk{ \n"
"border-radius:0px; \n"
"background: rgba(119, 111, 252, 200);\n"
"border-radius: 7px;\n"
"}")
        self.progress_bar_cam.setMaximum(1000)
        self.progress_bar_cam.setValue(0)

        self.horizontalLayout_20.addWidget(self.progress_bar_cam)

        self.stop_button_cam = QPushButton(self.Pause_QF_cam)
        self.stop_button_cam.setObjectName(u"stop_button_cam")
        self.stop_button_cam.setMinimumSize(QSize(0, 30))
        self.stop_button_cam.setMaximumSize(QSize(16777215, 30))
        self.stop_button_cam.setCursor(QCursor(Qt.PointingHandCursor))
        self.stop_button_cam.setStyleSheet(u"QPushButton{\n"
"background-image: url(:/all/img/stop.png);\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"border: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"}")

        self.horizontalLayout_20.addWidget(self.stop_button_cam)


        self.main_content_cam.addWidget(self.Pause_QF_cam)


        self.horizontalLayout_24.addLayout(self.main_content_cam)

        self.prm_page_cam = QFrame(self.page1)
        self.prm_page_cam.setObjectName(u"prm_page_cam")
        self.prm_page_cam.setMinimumSize(QSize(0, 0))
        self.prm_page_cam.setMaximumSize(QSize(0, 16777215))
        self.prm_page_cam.setStyleSheet(u"QFrame#prm_page_cam{\n"
"background-color: qradialgradient(cx:0, cy:0, radius:1, fx:0.1, fy:0.1, stop:0 rgb(0, 0, 100),  stop:1 rgb(10, 50, 200));\n"
"border-top-left-radius:30px;\n"
"border-top-right-radius:0px;\n"
"border-bottom-right-radius:0px;\n"
"border-bottom-left-radius:30px;\n"
"}")
        self.prm_page_cam.setFrameShape(QFrame.Shape.StyledPanel)
        self.prm_page_cam.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.prm_page_cam)
        self.verticalLayout_31.setSpacing(15)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(15, 15, -1, -1)
        self.label_cam = QLabel(self.prm_page_cam)
        self.label_cam.setObjectName(u"label_cam")
        self.label_cam.setStyleSheet(u"padding-left: 0px;\n"
"padding-bottom: 2px;\n"
"color: rgba(255, 255, 255, 240);\n"
"font: 700 italic 16pt \"Segoe UI\";")
        self.label_cam.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_31.addWidget(self.label_cam)

        self.Model_QF_cam_2 = QWidget(self.prm_page_cam)
        self.Model_QF_cam_2.setObjectName(u"Model_QF_cam_2")
        self.Model_QF_cam_2.setMinimumSize(QSize(190, 90))
        self.Model_QF_cam_2.setMaximumSize(QSize(190, 90))
        self.Model_QF_cam_2.setStyleSheet(u"QWidget#Model_QF_cam_2{\n"
"border:2px solid rgba(255, 255, 255, 70);\n"
"border-radius:15px;\n"
"}")
        self.verticalLayout_32 = QVBoxLayout(self.Model_QF_cam_2)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(9, 9, 9, 9)
        self.ToggleBotton_10 = QPushButton(self.Model_QF_cam_2)
        self.ToggleBotton_10.setObjectName(u"ToggleBotton_10")
        sizePolicy.setHeightForWidth(self.ToggleBotton_10.sizePolicy().hasHeightForWidth())
        self.ToggleBotton_10.setSizePolicy(sizePolicy)
        self.ToggleBotton_10.setMinimumSize(QSize(0, 30))
        self.ToggleBotton_10.setMaximumSize(QSize(16777215, 30))
        self.ToggleBotton_10.setFont(font1)
        self.ToggleBotton_10.setCursor(QCursor(Qt.ArrowCursor))
        self.ToggleBotton_10.setMouseTracking(True)
        self.ToggleBotton_10.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.ToggleBotton_10.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.ToggleBotton_10.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.ToggleBotton_10.setAutoFillBackground(False)
        self.ToggleBotton_10.setStyleSheet(u"QPushButton{\n"
"background-image: url(:/all/img/model.png);\n"
"background-repeat: no-repeat;\n"
"background-position: left center;\n"
"border: none;\n"
"border-left: 20px solid transparent;\n"
"\n"
"text-align: left;\n"
"padding-left: 40px;\n"
"padding-bottom: 2px;\n"
"color: rgba(255, 255, 255, 199);\n"
"font: 700 13pt \"Nirmala UI\";\n"
"}")
        self.ToggleBotton_10.setIcon(icon)
        self.ToggleBotton_10.setAutoDefault(False)
        self.ToggleBotton_10.setFlat(False)

        self.verticalLayout_32.addWidget(self.ToggleBotton_10)

        self.model_box_cam = QComboBox(self.Model_QF_cam_2)
        self.model_box_cam.setObjectName(u"model_box_cam")
        self.model_box_cam.setMinimumSize(QSize(170, 20))
        self.model_box_cam.setMaximumSize(QSize(170, 20))
        self.model_box_cam.setStyleSheet(u"\n"
"QComboBox {\n"
"            background-color: rgba(255,255,255,90);\n"
"			color: rgba(0, 0, 0, 200);\n"
"			font: 600 9pt \"Segoe UI\";\n"
"            border: 1px solid lightgray;\n"
"            border-radius: 10px;\n"
"            padding-left: 15px;\n"
"        }\n"
"        \n"
"        QComboBox:on {\n"
"            border: 1px solid #63acfb;\n"
"        }\n"
"\n"
"        QComboBox::drop-down {\n"
"            width: 22px;\n"
"            border-left: 1px solid lightgray;\n"
"            border-top-right-radius: 15px;\n"
"            border-bottom-right-radius: 15px;\n"
"        }\n"
"        \n"
"        QComboBox::drop-down:on {\n"
"            border-left: 1px solid #63acfb;\n"
"        }\n"
"\n"
"        QComboBox::down-arrow {\n"
"            width: 16px;\n"
"            height: 16px;\n"
"            image: url(:/all/img/box_down.png);\n"
"        }\n"
"\n"
"        QComboBox::down-arrow:on {\n"
"            image: url(:/all/img/box_up.png);\n"
"        }\n"
"\n"
"        QComboBox QAbstractI"
                        "temView {\n"
"            border: none;\n"
"            outline: none;\n"
"			padding: 10px;\n"
"            background-color: rgb(223, 188, 220);\n"
"        }\n"
"\n"
"\n"
"        QComboBox QScrollBar:vertical {\n"
"            width: 2px;\n"
"           background-color: rgba(255,255,255,150);\n"
"        }\n"
"\n"
"        QComboBox QScrollBar::handle:vertical {\n"
"            background-color: rgba(255,255,255,90);\n"
"        }")
        self.model_box_cam.setInsertPolicy(QComboBox.InsertPolicy.NoInsert)
        self.model_box_cam.setMinimumContentsLength(0)

        self.verticalLayout_32.addWidget(self.model_box_cam)


        self.verticalLayout_31.addWidget(self.Model_QF_cam_2)

        self.IOU_QF_cam = QFrame(self.prm_page_cam)
        self.IOU_QF_cam.setObjectName(u"IOU_QF_cam")
        self.IOU_QF_cam.setMinimumSize(QSize(190, 90))
        self.IOU_QF_cam.setMaximumSize(QSize(190, 90))
        self.IOU_QF_cam.setStyleSheet(u"QFrame#IOU_QF_cam{\n"
"border:2px solid rgba(255, 255, 255, 70);\n"
"border-radius:15px;\n"
"}")
        self.verticalLayout_33 = QVBoxLayout(self.IOU_QF_cam)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.ToggleBotton_9 = QPushButton(self.IOU_QF_cam)
        self.ToggleBotton_9.setObjectName(u"ToggleBotton_9")
        sizePolicy.setHeightForWidth(self.ToggleBotton_9.sizePolicy().hasHeightForWidth())
        self.ToggleBotton_9.setSizePolicy(sizePolicy)
        self.ToggleBotton_9.setMinimumSize(QSize(0, 30))
        self.ToggleBotton_9.setMaximumSize(QSize(16777215, 30))
        self.ToggleBotton_9.setFont(font1)
        self.ToggleBotton_9.setCursor(QCursor(Qt.ArrowCursor))
        self.ToggleBotton_9.setMouseTracking(True)
        self.ToggleBotton_9.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.ToggleBotton_9.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.ToggleBotton_9.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.ToggleBotton_9.setAutoFillBackground(False)
        self.ToggleBotton_9.setStyleSheet(u"QPushButton{\n"
"background-image: url(:/all/img/IOU.png);\n"
"background-repeat: no-repeat;\n"
"background-position: left center;\n"
"border: none;\n"
"border-left: 20px solid transparent;\n"
"\n"
"text-align: left;\n"
"padding-left: 40px;\n"
"padding-bottom: 4px;\n"
"color: rgba(255, 255, 255, 199);\n"
"font: 700 13pt \"Nirmala UI\";\n"
"}")
        self.ToggleBotton_9.setIcon(icon)
        self.ToggleBotton_9.setAutoDefault(False)
        self.ToggleBotton_9.setFlat(False)

        self.verticalLayout_33.addWidget(self.ToggleBotton_9)

        self.frame_4 = QFrame(self.IOU_QF_cam)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy1.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy1)
        self.frame_4.setMinimumSize(QSize(0, 20))
        self.frame_4.setMaximumSize(QSize(16777215, 20))
        self.horizontalLayout_21 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_21.setSpacing(10)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(8, 0, 10, 0)
        self.iou_spinbox_cam = QDoubleSpinBox(self.frame_4)
        self.iou_spinbox_cam.setObjectName(u"iou_spinbox_cam")
        self.iou_spinbox_cam.setCursor(QCursor(Qt.PointingHandCursor))
        self.iou_spinbox_cam.setStyleSheet(u"QDoubleSpinBox {\n"
"border: 0px solid lightgray;\n"
"border-radius: 2px;\n"
"background-color: rgba(255,255,255,90);\n"
"font: 600 9pt \"Segoe UI\";\n"
"}\n"
"        \n"
"QDoubleSpinBox::up-button {\n"
"width: 10px;\n"
"height: 9px;\n"
"margin: 0px 3px 0px 0px;\n"
"border-image: url(:/all/img/box_up.png);\n"
"}\n"
"QDoubleSpinBox::up-button:pressed {\n"
"margin-top: 1px;\n"
"}\n"
"            \n"
"QDoubleSpinBox::down-button {\n"
"width: 10px;\n"
"height: 9px;\n"
"margin: 0px 3px 0px 0px;\n"
"border-image: url(:/all/img/box_down.png);\n"
"}\n"
"QDoubleSpinBox::down-button:pressed {\n"
"margin-bottom: 1px;\n"
"}")
        self.iou_spinbox_cam.setMinimum(0.010000000000000)
        self.iou_spinbox_cam.setMaximum(1.000000000000000)
        self.iou_spinbox_cam.setSingleStep(0.050000000000000)
        self.iou_spinbox_cam.setValue(0.450000000000000)

        self.horizontalLayout_21.addWidget(self.iou_spinbox_cam)

        self.iou_slider_cam = QSlider(self.frame_4)
        self.iou_slider_cam.setObjectName(u"iou_slider_cam")
        self.iou_slider_cam.setCursor(QCursor(Qt.PointingHandCursor))
        self.iou_slider_cam.setStyleSheet(u"QSlider::groove:horizontal {\n"
"border: none;\n"
"height: 10px;\n"
"background-color: rgba(255,255,255,90);\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"width: 10px;\n"
"margin: -1px 0px -1px 0px;\n"
"border-radius: 3px;\n"
"background-color: white;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #59969b, stop:1 #04e7fa);\n"
"border-radius: 5px;\n"
"}")
        self.iou_slider_cam.setMinimum(1)
        self.iou_slider_cam.setMaximum(100)
        self.iou_slider_cam.setValue(45)
        self.iou_slider_cam.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout_21.addWidget(self.iou_slider_cam)


        self.verticalLayout_33.addWidget(self.frame_4)


        self.verticalLayout_31.addWidget(self.IOU_QF_cam)

        self.Conf_QF_cam = QFrame(self.prm_page_cam)
        self.Conf_QF_cam.setObjectName(u"Conf_QF_cam")
        self.Conf_QF_cam.setMinimumSize(QSize(190, 90))
        self.Conf_QF_cam.setMaximumSize(QSize(190, 90))
        self.Conf_QF_cam.setStyleSheet(u"QFrame#Conf_QF_cam{\n"
"border:2px solid rgba(255, 255, 255, 70);\n"
"border-radius:15px;\n"
"}")
        self.verticalLayout_34 = QVBoxLayout(self.Conf_QF_cam)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.ToggleBotton_7 = QPushButton(self.Conf_QF_cam)
        self.ToggleBotton_7.setObjectName(u"ToggleBotton_7")
        sizePolicy.setHeightForWidth(self.ToggleBotton_7.sizePolicy().hasHeightForWidth())
        self.ToggleBotton_7.setSizePolicy(sizePolicy)
        self.ToggleBotton_7.setMinimumSize(QSize(0, 30))
        self.ToggleBotton_7.setMaximumSize(QSize(16777215, 30))
        self.ToggleBotton_7.setFont(font1)
        self.ToggleBotton_7.setCursor(QCursor(Qt.ArrowCursor))
        self.ToggleBotton_7.setMouseTracking(True)
        self.ToggleBotton_7.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.ToggleBotton_7.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.ToggleBotton_7.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.ToggleBotton_7.setAutoFillBackground(False)
        self.ToggleBotton_7.setStyleSheet(u"QPushButton{\n"
"background-image: url(:/all/img/conf.png);\n"
"background-repeat: no-repeat;\n"
"background-position: left center;\n"
"border: none;\n"
"border-left: 20px solid transparent;\n"
"\n"
"text-align: left;\n"
"padding-left: 40px;\n"
"padding-bottom: 4px;\n"
"color: rgba(255, 255, 255, 199);\n"
"font: 700 13pt \"Nirmala UI\";\n"
"}")
        self.ToggleBotton_7.setIcon(icon)
        self.ToggleBotton_7.setAutoDefault(False)
        self.ToggleBotton_7.setFlat(False)

        self.verticalLayout_34.addWidget(self.ToggleBotton_7)

        self.frame_5 = QFrame(self.Conf_QF_cam)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy1.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy1)
        self.frame_5.setMinimumSize(QSize(0, 20))
        self.frame_5.setMaximumSize(QSize(16777215, 20))
        self.horizontalLayout_22 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_22.setSpacing(10)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(8, 0, 10, 0)
        self.conf_spinbox_cam = QDoubleSpinBox(self.frame_5)
        self.conf_spinbox_cam.setObjectName(u"conf_spinbox_cam")
        self.conf_spinbox_cam.setCursor(QCursor(Qt.PointingHandCursor))
        self.conf_spinbox_cam.setStyleSheet(u"QDoubleSpinBox {\n"
"border: 0px solid lightgray;\n"
"border-radius: 2px;\n"
"background-color: rgba(255,255,255,90);\n"
"font: 600 9pt \"Segoe UI\";\n"
"}\n"
"        \n"
"QDoubleSpinBox::up-button {\n"
"width: 10px;\n"
"height: 9px;\n"
"margin: 0px 3px 0px 0px;\n"
"border-image: url(:/all/img/box_up.png);\n"
"}\n"
"QDoubleSpinBox::up-button:pressed {\n"
"margin-top: 1px;\n"
"}\n"
"            \n"
"QDoubleSpinBox::down-button {\n"
"width: 10px;\n"
"height: 9px;\n"
"margin: 0px 3px 0px 0px;\n"
"border-image: url(:/all/img/box_down.png);\n"
"}\n"
"QDoubleSpinBox::down-button:pressed {\n"
"margin-bottom: 1px;\n"
"}")
        self.conf_spinbox_cam.setMinimum(0.010000000000000)
        self.conf_spinbox_cam.setMaximum(1.000000000000000)
        self.conf_spinbox_cam.setSingleStep(0.050000000000000)
        self.conf_spinbox_cam.setValue(0.250000000000000)

        self.horizontalLayout_22.addWidget(self.conf_spinbox_cam)

        self.conf_slider_cam = QSlider(self.frame_5)
        self.conf_slider_cam.setObjectName(u"conf_slider_cam")
        self.conf_slider_cam.setCursor(QCursor(Qt.PointingHandCursor))
        self.conf_slider_cam.setStyleSheet(u"QSlider::groove:horizontal {\n"
"border: none;\n"
"height: 10px;\n"
"background-color: rgba(255,255,255,90);\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"width: 10px;\n"
"margin: -1px 0px -1px 0px;\n"
"border-radius: 3px;\n"
"background-color: white;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #59969b, stop:1 #04e7fa);\n"
"border-radius: 5px;\n"
"}")
        self.conf_slider_cam.setMinimum(1)
        self.conf_slider_cam.setMaximum(100)
        self.conf_slider_cam.setValue(25)
        self.conf_slider_cam.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout_22.addWidget(self.conf_slider_cam)


        self.verticalLayout_34.addWidget(self.frame_5)


        self.verticalLayout_31.addWidget(self.Conf_QF_cam)

        self.Delay_QF_cam = QFrame(self.prm_page_cam)
        self.Delay_QF_cam.setObjectName(u"Delay_QF_cam")
        self.Delay_QF_cam.setMinimumSize(QSize(190, 90))
        self.Delay_QF_cam.setMaximumSize(QSize(190, 90))
        self.Delay_QF_cam.setStyleSheet(u"QFrame#Delay_QF_cam{\n"
"border:2px solid rgba(255, 255, 255, 70);\n"
"border-radius:15px;\n"
"}")
        self.verticalLayout_35 = QVBoxLayout(self.Delay_QF_cam)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.ToggleBotton_8 = QPushButton(self.Delay_QF_cam)
        self.ToggleBotton_8.setObjectName(u"ToggleBotton_8")
        sizePolicy.setHeightForWidth(self.ToggleBotton_8.sizePolicy().hasHeightForWidth())
        self.ToggleBotton_8.setSizePolicy(sizePolicy)
        self.ToggleBotton_8.setMinimumSize(QSize(0, 30))
        self.ToggleBotton_8.setMaximumSize(QSize(16777215, 30))
        self.ToggleBotton_8.setFont(font1)
        self.ToggleBotton_8.setCursor(QCursor(Qt.ArrowCursor))
        self.ToggleBotton_8.setMouseTracking(True)
        self.ToggleBotton_8.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.ToggleBotton_8.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.ToggleBotton_8.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.ToggleBotton_8.setAutoFillBackground(False)
        self.ToggleBotton_8.setStyleSheet(u"QPushButton{\n"
"background-image: url(:/all/img/delay.png);\n"
"background-repeat: no-repeat;\n"
"background-position: left center;\n"
"border: none;\n"
"border-left: 20px solid transparent;\n"
"\n"
"text-align: left;\n"
"padding-left: 40px;\n"
"padding-bottom: 2px;\n"
"color: rgba(255, 255, 255, 199);\n"
"font: 700 13pt \"Nirmala UI\";\n"
"}")
        self.ToggleBotton_8.setIcon(icon)
        self.ToggleBotton_8.setAutoDefault(False)
        self.ToggleBotton_8.setFlat(False)

        self.verticalLayout_35.addWidget(self.ToggleBotton_8)

        self.frame_6 = QFrame(self.Delay_QF_cam)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy1.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy1)
        self.frame_6.setMinimumSize(QSize(0, 20))
        self.frame_6.setMaximumSize(QSize(16777215, 20))
        self.horizontalLayout_23 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_23.setSpacing(10)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(8, 0, 10, 0)
        self.speed_spinbox_cam = QSpinBox(self.frame_6)
        self.speed_spinbox_cam.setObjectName(u"speed_spinbox_cam")
        self.speed_spinbox_cam.setStyleSheet(u"QSpinBox {\n"
"border: 0px solid lightgray;\n"
"border-radius: 2px;\n"
"background-color: rgba(255,255,255,90);\n"
"font: 600 9pt \"Segoe UI\";\n"
"}\n"
"        \n"
"QSpinBox::up-button {\n"
"width: 10px;\n"
"height: 9px;\n"
"margin: 0px 3px 0px 0px;\n"
"border-image: url(:/all/img/box_up.png);\n"
"}\n"
"QSpinBox::up-button:pressed {\n"
"margin-top: 1px;\n"
"}\n"
"            \n"
"QSpinBox::down-button {\n"
"width: 10px;\n"
"height: 9px;\n"
"margin: 0px 3px 0px 0px;\n"
"border-image: url(:/all/img/box_down.png);\n"
"}\n"
"QSpinBox::down-button:pressed {\n"
"margin-bottom: 1px;\n"
"}")
        self.speed_spinbox_cam.setMaximum(50)
        self.speed_spinbox_cam.setValue(10)

        self.horizontalLayout_23.addWidget(self.speed_spinbox_cam)

        self.speed_slider_cam = QSlider(self.frame_6)
        self.speed_slider_cam.setObjectName(u"speed_slider_cam")
        self.speed_slider_cam.setCursor(QCursor(Qt.PointingHandCursor))
        self.speed_slider_cam.setStyleSheet(u"QSlider::groove:horizontal {\n"
"border: none;\n"
"height: 10px;\n"
"background-color: rgba(255,255,255,90);\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"width: 10px;\n"
"margin: -1px 0px -1px 0px;\n"
"border-radius: 3px;\n"
"background-color: white;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"background-color: qradialgradient(cx:0, cy:0, radius:1, fx:0.1, fy:0.1, stop:0 rgb(253, 139, 133),  stop:1 rgb(248, 194, 152));\n"
"border-radius: 5px;\n"
"}")
        self.speed_slider_cam.setMaximum(50)
        self.speed_slider_cam.setValue(10)
        self.speed_slider_cam.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout_23.addWidget(self.speed_slider_cam)


        self.verticalLayout_35.addWidget(self.frame_6)


        self.verticalLayout_31.addWidget(self.Delay_QF_cam)

        self.Save_QF_cam = QFrame(self.prm_page_cam)
        self.Save_QF_cam.setObjectName(u"Save_QF_cam")
        self.Save_QF_cam.setMinimumSize(QSize(190, 120))
        self.Save_QF_cam.setMaximumSize(QSize(190, 120))
        self.Save_QF_cam.setStyleSheet(u"QFrame#Save_QF_cam{\n"
"border:2px solid rgba(255, 255, 255, 70);\n"
"border-radius:15px;\n"
"}")
        self.verticalLayout_36 = QVBoxLayout(self.Save_QF_cam)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(9, 9, 9, 9)
        self.ToggleBotton_11 = QPushButton(self.Save_QF_cam)
        self.ToggleBotton_11.setObjectName(u"ToggleBotton_11")
        sizePolicy.setHeightForWidth(self.ToggleBotton_11.sizePolicy().hasHeightForWidth())
        self.ToggleBotton_11.setSizePolicy(sizePolicy)
        self.ToggleBotton_11.setMinimumSize(QSize(0, 30))
        self.ToggleBotton_11.setMaximumSize(QSize(16777215, 30))
        self.ToggleBotton_11.setFont(font1)
        self.ToggleBotton_11.setCursor(QCursor(Qt.ArrowCursor))
        self.ToggleBotton_11.setMouseTracking(True)
        self.ToggleBotton_11.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.ToggleBotton_11.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.ToggleBotton_11.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.ToggleBotton_11.setAutoFillBackground(False)
        self.ToggleBotton_11.setStyleSheet(u"QPushButton{\n"
"background-image: url(:/all/img/save.png);\n"
"background-repeat: no-repeat;\n"
"background-position: left center;\n"
"border: none;\n"
"border-left: 20px solid transparent;\n"
"\n"
"text-align: left;\n"
"padding-left: 40px;\n"
"padding-bottom: 2px;\n"
"color: rgba(255, 255, 255, 199);\n"
"font: 700 13pt \"Nirmala UI\";\n"
"}")
        self.ToggleBotton_11.setIcon(icon)
        self.ToggleBotton_11.setAutoDefault(False)
        self.ToggleBotton_11.setFlat(False)

        self.verticalLayout_36.addWidget(self.ToggleBotton_11)

        self.save_res_button_cam = QCheckBox(self.Save_QF_cam)
        self.save_res_button_cam.setObjectName(u"save_res_button_cam")
        self.save_res_button_cam.setCursor(QCursor(Qt.PointingHandCursor))
        self.save_res_button_cam.setStyleSheet(u"QCheckBox {\n"
"color: rgba(255, 255, 255, 199);\n"
"font: 590 10pt \"Nirmala UI\";\n"
"        }\n"
"\n"
"        QCheckBox::indicator {\n"
"            padding-top: 1px;\n"
"padding-left: 10px;\n"
"            width: 40px;\n"
"            height: 30px;\n"
"            border: none;\n"
"        }\n"
"\n"
"        QCheckBox::indicator:unchecked {\n"
"            image: url(:/all/img/check_no.png);\n"
"        }\n"
"\n"
"        QCheckBox::indicator:checked {\n"
"            image: url(:/all/img/check_yes.png);\n"
"        }")

        self.verticalLayout_36.addWidget(self.save_res_button_cam)

        self.save_txt_button_cam = QCheckBox(self.Save_QF_cam)
        self.save_txt_button_cam.setObjectName(u"save_txt_button_cam")
        self.save_txt_button_cam.setCursor(QCursor(Qt.PointingHandCursor))
        self.save_txt_button_cam.setStyleSheet(u"QCheckBox {\n"
"color: rgba(255, 255, 255, 199);\n"
"font: 590 10pt \"Nirmala UI\";\n"
"        }\n"
"\n"
"        QCheckBox::indicator {\n"
"            padding-top: 1px;\n"
"padding-left: 10px;\n"
"            width: 40px;\n"
"            height: 30px;\n"
"            border: none;\n"
"        }\n"
"\n"
"        QCheckBox::indicator:unchecked {\n"
"            image: url(:/all/img/check_no.png);\n"
"        }\n"
"\n"
"        QCheckBox::indicator:checked {\n"
"            image: url(:/all/img/check_yes.png);\n"
"        }")

        self.verticalLayout_36.addWidget(self.save_txt_button_cam)


        self.verticalLayout_31.addWidget(self.Save_QF_cam)

        self.verticalSpacer_3 = QSpacerItem(20, 13, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_31.addItem(self.verticalSpacer_3)


        self.horizontalLayout_24.addWidget(self.prm_page_cam)

        self.content.addWidget(self.page1)

        self.verticalLayout_6.addWidget(self.content)

        self.below = QFrame(self.ContentBox)
        self.below.setObjectName(u"below")
        self.below.setMinimumSize(QSize(0, 30))
        self.below.setMaximumSize(QSize(16777215, 30))
        self.below.setFrameShape(QFrame.Shape.StyledPanel)
        self.below.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.below)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(20, 2, 0, 4)
        self.status_bar = QLabel(self.below)
        self.status_bar.setObjectName(u"status_bar")
        self.status_bar.setStyleSheet(u"font: 700 11pt \"Segoe UI\";\n"
"color: rgba(0, 0, 0, 140);")

        self.horizontalLayout_13.addWidget(self.status_bar)

        self.frame_size_grip = QFrame(self.below)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setStyleSheet(u"border-radius:30px;")
        self.frame_size_grip.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_size_grip.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_13.addWidget(self.frame_size_grip)


        self.verticalLayout_6.addWidget(self.below)

        self.content.raise_()
        self.top.raise_()
        self.below.raise_()

        self.main_qframe.addWidget(self.ContentBox)


        self.horizontalLayout_14.addWidget(self.Main_QF)

        MainWindow.setCentralWidget(self.Main_QW)

        self.retranslateUi(MainWindow)

        self.ToggleBotton.setDefault(False)
        self.content.setCurrentIndex(0)
        self.ToggleBotton_6.setDefault(False)
        self.ToggleBotton_2.setDefault(False)
        self.ToggleBotton_3.setDefault(False)
        self.ToggleBotton_4.setDefault(False)
        self.ToggleBotton_5.setDefault(False)
        self.ToggleBotton_10.setDefault(False)
        self.ToggleBotton_9.setDefault(False)
        self.ToggleBotton_7.setDefault(False)
        self.ToggleBotton_8.setDefault(False)
        self.ToggleBotton_11.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.ToggleBotton.setText(QCoreApplication.translate("MainWindow", u"\u9690\u85cf\u8fb9\u680f", None))
        self.src_file_button.setText(QCoreApplication.translate("MainWindow", u"\u52a0\u8f7d\u6587\u4ef6", None))
        self.src_cam_button.setText(QCoreApplication.translate("MainWindow", u"\u6444\u50cf\u5934", None))
        self.src_rtsp_button.setText(QCoreApplication.translate("MainWindow", u"RTSP", None))
        self.VersionLabel.setText(QCoreApplication.translate("MainWindow", u"Version: 2.0-Beta", None))
        self.explain_title.setText(QCoreApplication.translate("MainWindow", u"\u529b\u9ad8\u8bc6\u522b", None))
        self.settings_button.setText("")
        self.min_sf.setText("")
        self.max_sf.setText("")
        self.close_button.setText("")
        self.pre_video.setText("")
        self.res_video.setText("")
        self.label_img_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.run_button.setText("")
        self.stop_button.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e", None))
        self.ToggleBotton_6.setText(QCoreApplication.translate("MainWindow", u"\u6a21\u578b", None))
        self.model_box.setPlaceholderText("")
        self.ToggleBotton_2.setText(QCoreApplication.translate("MainWindow", u"IoU\u9608\u503c", None))
        self.ToggleBotton_3.setText(QCoreApplication.translate("MainWindow", u"\u7f6e\u4fe1\u5ea6\u9608\u503c", None))
        self.ToggleBotton_4.setText(QCoreApplication.translate("MainWindow", u"\u5ef6\u8fdf(ms)", None))
        self.ToggleBotton_5.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58", None))
        self.save_res_button.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58 MP4/JPG", None))
        self.save_txt_button.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58 Labels(.txt)", None))
        self.pre_cam.setText("")
        self.res_cam.setText("")
        self.label_img.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.run_button_cam.setText("")
        self.stop_button_cam.setText("")
        self.label_cam.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.ToggleBotton_10.setText(QCoreApplication.translate("MainWindow", u"\u6a21\u578b", None))
        self.model_box_cam.setPlaceholderText("")
        self.ToggleBotton_9.setText(QCoreApplication.translate("MainWindow", u"IoU\u9608\u503c", None))
        self.ToggleBotton_7.setText(QCoreApplication.translate("MainWindow", u"\u7f6e\u4fe1\u5ea6\u9608\u503c", None))
        self.ToggleBotton_8.setText(QCoreApplication.translate("MainWindow", u"\u5ef6\u8fdf(ms)", None))
        self.ToggleBotton_11.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.save_res_button_cam.setText(QCoreApplication.translate("MainWindow", u"Save MP4/JPG", None))
        self.save_txt_button_cam.setText(QCoreApplication.translate("MainWindow", u"Save Labels(.txt)", None))
        self.status_bar.setText(QCoreApplication.translate("MainWindow", u"Welcome!", None))
    # retranslateUi

