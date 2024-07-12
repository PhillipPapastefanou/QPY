# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'full_model_c3.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1512, 856)
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AnimatedDocks)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(0, 750))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_main_separation = QtWidgets.QHBoxLayout()
        self.horizontalLayout_main_separation.setObjectName("horizontalLayout_main_separation")
        self.verticalLayout_climate_manip = QtWidgets.QVBoxLayout()
        self.verticalLayout_climate_manip.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_climate_manip.setObjectName("verticalLayout_climate_manip")
        self.groupBoxWorldmap = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxWorldmap.setEnabled(True)
        self.groupBoxWorldmap.setMinimumSize(QtCore.QSize(570, 270))
        self.groupBoxWorldmap.setMaximumSize(QtCore.QSize(800, 16777215))
        self.groupBoxWorldmap.setFlat(False)
        self.groupBoxWorldmap.setCheckable(False)
        self.groupBoxWorldmap.setObjectName("groupBoxWorldmap")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBoxWorldmap)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_worldmap_container = QtWidgets.QVBoxLayout()
        self.verticalLayout_worldmap_container.setObjectName("verticalLayout_worldmap_container")
        self.horizontalLayout_lon = QtWidgets.QHBoxLayout()
        self.horizontalLayout_lon.setObjectName("horizontalLayout_lon")
        self.label_lon = QtWidgets.QLabel(self.groupBoxWorldmap)
        self.label_lon.setObjectName("label_lon")
        self.horizontalLayout_lon.addWidget(self.label_lon)
        self.lineEdit_lon = QtWidgets.QLineEdit(self.groupBoxWorldmap)
        self.lineEdit_lon.setMinimumSize(QtCore.QSize(60, 0))
        self.lineEdit_lon.setMaximumSize(QtCore.QSize(60, 16777215))
        self.lineEdit_lon.setObjectName("lineEdit_lon")
        self.horizontalLayout_lon.addWidget(self.lineEdit_lon)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_lon.addItem(spacerItem)
        self.verticalLayout_worldmap_container.addLayout(self.horizontalLayout_lon)
        self.horizontalLayout_lat = QtWidgets.QHBoxLayout()
        self.horizontalLayout_lat.setObjectName("horizontalLayout_lat")
        self.label_lat = QtWidgets.QLabel(self.groupBoxWorldmap)
        self.label_lat.setObjectName("label_lat")
        self.horizontalLayout_lat.addWidget(self.label_lat)
        self.lineEdit_lat = QtWidgets.QLineEdit(self.groupBoxWorldmap)
        self.lineEdit_lat.setMinimumSize(QtCore.QSize(60, 0))
        self.lineEdit_lat.setMaximumSize(QtCore.QSize(60, 16777215))
        self.lineEdit_lat.setObjectName("lineEdit_lat")
        self.horizontalLayout_lat.addWidget(self.lineEdit_lat)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_lat.addItem(spacerItem1)
        self.verticalLayout_worldmap_container.addLayout(self.horizontalLayout_lat)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_worldmap_container.addItem(spacerItem2)
        self.horizontalLayout.addLayout(self.verticalLayout_worldmap_container)
        self.verticalLayout_worldmap_mpl = QtWidgets.QVBoxLayout()
        self.verticalLayout_worldmap_mpl.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_worldmap_mpl.setObjectName("verticalLayout_worldmap_mpl")
        self.horizontalLayout.addLayout(self.verticalLayout_worldmap_mpl)
        self.verticalLayout_climate_manip.addWidget(self.groupBoxWorldmap)
        self.groupBox_forcing_display = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_forcing_display.setMinimumSize(QtCore.QSize(570, 300))
        self.groupBox_forcing_display.setMaximumSize(QtCore.QSize(800, 16777215))
        self.groupBox_forcing_display.setObjectName("groupBox_forcing_display")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.groupBox_forcing_display)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_4 = QtWidgets.QLabel(self.groupBox_forcing_display)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_9.addWidget(self.label_4)
        self.comboBox_forcing_dataset = QtWidgets.QComboBox(self.groupBox_forcing_display)
        self.comboBox_forcing_dataset.setObjectName("comboBox_forcing_dataset")
        self.horizontalLayout_9.addWidget(self.comboBox_forcing_dataset)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_11 = QtWidgets.QLabel(self.groupBox_forcing_display)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_10.addWidget(self.label_11)
        self.lineEdit_first_year = QtWidgets.QLineEdit(self.groupBox_forcing_display)
        self.lineEdit_first_year.setEnabled(True)
        self.lineEdit_first_year.setMaximumSize(QtCore.QSize(40, 16777215))
        self.lineEdit_first_year.setReadOnly(True)
        self.lineEdit_first_year.setObjectName("lineEdit_first_year")
        self.horizontalLayout_10.addWidget(self.lineEdit_first_year)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_12 = QtWidgets.QLabel(self.groupBox_forcing_display)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_7.addWidget(self.label_12)
        self.lineEdit_last_year = QtWidgets.QLineEdit(self.groupBox_forcing_display)
        self.lineEdit_last_year.setEnabled(True)
        self.lineEdit_last_year.setMaximumSize(QtCore.QSize(40, 16777215))
        self.lineEdit_last_year.setReadOnly(True)
        self.lineEdit_last_year.setObjectName("lineEdit_last_year")
        self.horizontalLayout_7.addWidget(self.lineEdit_last_year)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_5 = QtWidgets.QLabel(self.groupBox_forcing_display)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_8.addWidget(self.label_5)
        self.lineEdit_resolution = QtWidgets.QLineEdit(self.groupBox_forcing_display)
        self.lineEdit_resolution.setEnabled(True)
        self.lineEdit_resolution.setMaximumSize(QtCore.QSize(40, 16777215))
        self.lineEdit_resolution.setReadOnly(True)
        self.lineEdit_resolution.setObjectName("lineEdit_resolution")
        self.horizontalLayout_8.addWidget(self.lineEdit_resolution)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem6)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_10 = QtWidgets.QLabel(self.groupBox_forcing_display)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_6.addWidget(self.label_10)
        self.lineEdit_offset = QtWidgets.QLineEdit(self.groupBox_forcing_display)
        self.lineEdit_offset.setMaximumSize(QtCore.QSize(40, 16777215))
        self.lineEdit_offset.setReadOnly(True)
        self.lineEdit_offset.setObjectName("lineEdit_offset")
        self.horizontalLayout_6.addWidget(self.lineEdit_offset)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem7)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem8)
        self.horizontalLayout_5.addLayout(self.verticalLayout)
        self.verticalLayout_forcing_display = QtWidgets.QVBoxLayout()
        self.verticalLayout_forcing_display.setObjectName("verticalLayout_forcing_display")
        self.horizontalLayout_5.addLayout(self.verticalLayout_forcing_display)
        self.verticalLayout_climate_manip.addWidget(self.groupBox_forcing_display)
        self.groupBox_manipulation_settings = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_manipulation_settings.setMinimumSize(QtCore.QSize(800, 320))
        self.groupBox_manipulation_settings.setMaximumSize(QtCore.QSize(850, 350))
        self.groupBox_manipulation_settings.setObjectName("groupBox_manipulation_settings")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox_manipulation_settings)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_manip = QtWidgets.QHBoxLayout()
        self.horizontalLayout_manip.setObjectName("horizontalLayout_manip")
        self.verticalLayout_manip_slider = QtWidgets.QVBoxLayout()
        self.verticalLayout_manip_slider.setObjectName("verticalLayout_manip_slider")
        self.verticalLayout_temp_change = QtWidgets.QVBoxLayout()
        self.verticalLayout_temp_change.setObjectName("verticalLayout_temp_change")
        self.label_temp_change = QtWidgets.QLabel(self.groupBox_manipulation_settings)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_temp_change.setFont(font)
        self.label_temp_change.setAlignment(QtCore.Qt.AlignCenter)
        self.label_temp_change.setObjectName("label_temp_change")
        self.verticalLayout_temp_change.addWidget(self.label_temp_change)
        self.horizontalLayout_temp_change = QtWidgets.QHBoxLayout()
        self.horizontalLayout_temp_change.setObjectName("horizontalLayout_temp_change")
        self.horizontalSlider_temp_change = QtWidgets.QSlider(self.groupBox_manipulation_settings)
        self.horizontalSlider_temp_change.setMinimumSize(QtCore.QSize(150, 0))
        self.horizontalSlider_temp_change.setMaximumSize(QtCore.QSize(200, 16777215))
        self.horizontalSlider_temp_change.setMinimum(-20)
        self.horizontalSlider_temp_change.setMaximum(20)
        self.horizontalSlider_temp_change.setSingleStep(1)
        self.horizontalSlider_temp_change.setPageStep(4)
        self.horizontalSlider_temp_change.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_temp_change.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.horizontalSlider_temp_change.setTickInterval(0)
        self.horizontalSlider_temp_change.setObjectName("horizontalSlider_temp_change")
        self.horizontalLayout_temp_change.addWidget(self.horizontalSlider_temp_change)
        self.lineEdit_temp_change = QtWidgets.QLineEdit(self.groupBox_manipulation_settings)
        self.lineEdit_temp_change.setEnabled(False)
        self.lineEdit_temp_change.setMinimumSize(QtCore.QSize(55, 0))
        self.lineEdit_temp_change.setMaximumSize(QtCore.QSize(55, 16777215))
        self.lineEdit_temp_change.setObjectName("lineEdit_temp_change")
        self.horizontalLayout_temp_change.addWidget(self.lineEdit_temp_change)
        self.label_2 = QtWidgets.QLabel(self.groupBox_manipulation_settings)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_temp_change.addWidget(self.label_2)
        self.lineEdit_temp_years = QtWidgets.QLineEdit(self.groupBox_manipulation_settings)
        self.lineEdit_temp_years.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lineEdit_temp_years.setObjectName("lineEdit_temp_years")
        self.horizontalLayout_temp_change.addWidget(self.lineEdit_temp_years)
        self.label_3 = QtWidgets.QLabel(self.groupBox_manipulation_settings)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_temp_change.addWidget(self.label_3)
        self.verticalLayout_temp_change.addLayout(self.horizontalLayout_temp_change)
        self.verticalLayout_manip_slider.addLayout(self.verticalLayout_temp_change)
        self.verticalLayout_rain_change = QtWidgets.QVBoxLayout()
        self.verticalLayout_rain_change.setObjectName("verticalLayout_rain_change")
        self.label_rain_change = QtWidgets.QLabel(self.groupBox_manipulation_settings)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_rain_change.setFont(font)
        self.label_rain_change.setAlignment(QtCore.Qt.AlignCenter)
        self.label_rain_change.setObjectName("label_rain_change")
        self.verticalLayout_rain_change.addWidget(self.label_rain_change)
        self.horizontalLayout_rain_change = QtWidgets.QHBoxLayout()
        self.horizontalLayout_rain_change.setObjectName("horizontalLayout_rain_change")
        self.horizontalSlider_rain_change = QtWidgets.QSlider(self.groupBox_manipulation_settings)
        self.horizontalSlider_rain_change.setMinimumSize(QtCore.QSize(150, 0))
        self.horizontalSlider_rain_change.setMaximumSize(QtCore.QSize(200, 16777215))
        self.horizontalSlider_rain_change.setMinimum(-100)
        self.horizontalSlider_rain_change.setMaximum(100)
        self.horizontalSlider_rain_change.setSingleStep(10)
        self.horizontalSlider_rain_change.setPageStep(25)
        self.horizontalSlider_rain_change.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_rain_change.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.horizontalSlider_rain_change.setObjectName("horizontalSlider_rain_change")
        self.horizontalLayout_rain_change.addWidget(self.horizontalSlider_rain_change)
        self.lineEdit_rain_change = QtWidgets.QLineEdit(self.groupBox_manipulation_settings)
        self.lineEdit_rain_change.setEnabled(False)
        self.lineEdit_rain_change.setMinimumSize(QtCore.QSize(55, 0))
        self.lineEdit_rain_change.setMaximumSize(QtCore.QSize(55, 16777215))
        self.lineEdit_rain_change.setObjectName("lineEdit_rain_change")
        self.horizontalLayout_rain_change.addWidget(self.lineEdit_rain_change)
        self.label_6 = QtWidgets.QLabel(self.groupBox_manipulation_settings)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_rain_change.addWidget(self.label_6)
        self.lineEdit_rain_years = QtWidgets.QLineEdit(self.groupBox_manipulation_settings)
        self.lineEdit_rain_years.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lineEdit_rain_years.setObjectName("lineEdit_rain_years")
        self.horizontalLayout_rain_change.addWidget(self.lineEdit_rain_years)
        self.label_8 = QtWidgets.QLabel(self.groupBox_manipulation_settings)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_rain_change.addWidget(self.label_8)
        self.verticalLayout_rain_change.addLayout(self.horizontalLayout_rain_change)
        self.verticalLayout_manip_slider.addLayout(self.verticalLayout_rain_change)
        self.verticalLayout_co2_change = QtWidgets.QVBoxLayout()
        self.verticalLayout_co2_change.setObjectName("verticalLayout_co2_change")
        self.label_co2_change = QtWidgets.QLabel(self.groupBox_manipulation_settings)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_co2_change.setFont(font)
        self.label_co2_change.setAlignment(QtCore.Qt.AlignCenter)
        self.label_co2_change.setObjectName("label_co2_change")
        self.verticalLayout_co2_change.addWidget(self.label_co2_change)
        self.horizontalLayout_co2_change = QtWidgets.QHBoxLayout()
        self.horizontalLayout_co2_change.setObjectName("horizontalLayout_co2_change")
        self.horizontalSlider_co2_change = QtWidgets.QSlider(self.groupBox_manipulation_settings)
        self.horizontalSlider_co2_change.setMinimumSize(QtCore.QSize(150, 0))
        self.horizontalSlider_co2_change.setMaximumSize(QtCore.QSize(200, 16777215))
        self.horizontalSlider_co2_change.setMinimum(-100)
        self.horizontalSlider_co2_change.setMaximum(400)
        self.horizontalSlider_co2_change.setSingleStep(50)
        self.horizontalSlider_co2_change.setPageStep(50)
        self.horizontalSlider_co2_change.setProperty("value", 0)
        self.horizontalSlider_co2_change.setSliderPosition(0)
        self.horizontalSlider_co2_change.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_co2_change.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.horizontalSlider_co2_change.setObjectName("horizontalSlider_co2_change")
        self.horizontalLayout_co2_change.addWidget(self.horizontalSlider_co2_change)
        self.lineEdit_co2_change = QtWidgets.QLineEdit(self.groupBox_manipulation_settings)
        self.lineEdit_co2_change.setEnabled(False)
        self.lineEdit_co2_change.setMinimumSize(QtCore.QSize(55, 0))
        self.lineEdit_co2_change.setMaximumSize(QtCore.QSize(55, 16777215))
        self.lineEdit_co2_change.setObjectName("lineEdit_co2_change")
        self.horizontalLayout_co2_change.addWidget(self.lineEdit_co2_change)
        self.label_9 = QtWidgets.QLabel(self.groupBox_manipulation_settings)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_co2_change.addWidget(self.label_9)
        self.lineEdit_co2_years = QtWidgets.QLineEdit(self.groupBox_manipulation_settings)
        self.lineEdit_co2_years.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lineEdit_co2_years.setObjectName("lineEdit_co2_years")
        self.horizontalLayout_co2_change.addWidget(self.lineEdit_co2_years)
        self.label_7 = QtWidgets.QLabel(self.groupBox_manipulation_settings)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_co2_change.addWidget(self.label_7)
        self.verticalLayout_co2_change.addLayout(self.horizontalLayout_co2_change)
        self.verticalLayout_manip_slider.addLayout(self.verticalLayout_co2_change)
        self.horizontalLayout_manip.addLayout(self.verticalLayout_manip_slider)
        self.verticalGroupBox_manip_display = QtWidgets.QGroupBox(self.groupBox_manipulation_settings)
        self.verticalGroupBox_manip_display.setMinimumSize(QtCore.QSize(250, 0))
        self.verticalGroupBox_manip_display.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.verticalGroupBox_manip_display.setObjectName("verticalGroupBox_manip_display")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalGroupBox_manip_display)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tabWidget_manip_display = QtWidgets.QTabWidget(self.verticalGroupBox_manip_display)
        self.tabWidget_manip_display.setObjectName("tabWidget_manip_display")
        self.tab_temp = QtWidgets.QWidget()
        self.tab_temp.setObjectName("tab_temp")
        self.tabWidget_manip_display.addTab(self.tab_temp, "")
        self.tab_rain = QtWidgets.QWidget()
        self.tab_rain.setObjectName("tab_rain")
        self.tabWidget_manip_display.addTab(self.tab_rain, "")
        self.verticalLayout_3.addWidget(self.tabWidget_manip_display)
        self.horizontalLayout_manip.addWidget(self.verticalGroupBox_manip_display)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_manip)
        self.verticalLayout_climate_manip.addWidget(self.groupBox_manipulation_settings)
        self.horizontalLayout_main_separation.addLayout(self.verticalLayout_climate_manip)
        self.verticalLayout_4.addLayout(self.horizontalLayout_main_separation)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1512, 37))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.dockWidget_status_bar = QtWidgets.QDockWidget(MainWindow)
        self.dockWidget_status_bar.setEnabled(True)
        self.dockWidget_status_bar.setMinimumSize(QtCore.QSize(613, 60))
        self.dockWidget_status_bar.setMaximumSize(QtCore.QSize(524287, 60))
        self.dockWidget_status_bar.setFloating(False)
        self.dockWidget_status_bar.setAllowedAreas(QtCore.Qt.NoDockWidgetArea)
        self.dockWidget_status_bar.setObjectName("dockWidget_status_bar")
        self.dockWidgetContents_1 = QtWidgets.QWidget()
        self.dockWidgetContents_1.setObjectName("dockWidgetContents_1")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.dockWidgetContents_1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton_run_model = QtWidgets.QPushButton(self.dockWidgetContents_1)
        self.pushButton_run_model.setMinimumSize(QtCore.QSize(75, 35))
        self.pushButton_run_model.setMaximumSize(QtCore.QSize(75, 16777215))
        self.pushButton_run_model.setObjectName("pushButton_run_model")
        self.horizontalLayout_4.addWidget(self.pushButton_run_model)
        self.pushButton_stop_model = QtWidgets.QPushButton(self.dockWidgetContents_1)
        self.pushButton_stop_model.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_stop_model.sizePolicy().hasHeightForWidth())
        self.pushButton_stop_model.setSizePolicy(sizePolicy)
        self.pushButton_stop_model.setMinimumSize(QtCore.QSize(75, 35))
        self.pushButton_stop_model.setMaximumSize(QtCore.QSize(75, 16777215))
        self.pushButton_stop_model.setObjectName("pushButton_stop_model")
        self.horizontalLayout_4.addWidget(self.pushButton_stop_model)
        self.label_14 = QtWidgets.QLabel(self.dockWidgetContents_1)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_4.addWidget(self.label_14)
        self.comboBox_PFT = QtWidgets.QComboBox(self.dockWidgetContents_1)
        self.comboBox_PFT.setObjectName("comboBox_PFT")
        self.horizontalLayout_4.addWidget(self.comboBox_PFT)
        self.label_13 = QtWidgets.QLabel(self.dockWidgetContents_1)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_4.addWidget(self.label_13)
        self.lineEdit_nyear_spinup = QtWidgets.QLineEdit(self.dockWidgetContents_1)
        self.lineEdit_nyear_spinup.setMaximumSize(QtCore.QSize(60, 16777215))
        self.lineEdit_nyear_spinup.setObjectName("lineEdit_nyear_spinup")
        self.horizontalLayout_4.addWidget(self.lineEdit_nyear_spinup)
        self.label = QtWidgets.QLabel(self.dockWidgetContents_1)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.progressBar_model_progress = QtWidgets.QProgressBar(self.dockWidgetContents_1)
        self.progressBar_model_progress.setMinimumSize(QtCore.QSize(100, 0))
        self.progressBar_model_progress.setProperty("value", 0)
        self.progressBar_model_progress.setObjectName("progressBar_model_progress")
        self.horizontalLayout_4.addWidget(self.progressBar_model_progress)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem9)
        self.dockWidget_status_bar.setWidget(self.dockWidgetContents_1)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockWidget_status_bar)
        self.dockWidget_output_1 = QtWidgets.QDockWidget(MainWindow)
        self.dockWidget_output_1.setEnabled(True)
        self.dockWidget_output_1.setAutoFillBackground(False)
        self.dockWidget_output_1.setObjectName("dockWidget_output_1")
        self.dockWidgetContents_output_mpl_1 = QtWidgets.QWidget()
        self.dockWidgetContents_output_mpl_1.setObjectName("dockWidgetContents_output_mpl_1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.dockWidgetContents_output_mpl_1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.cB_output_1 = QtWidgets.QComboBox(self.dockWidgetContents_output_mpl_1)
        self.cB_output_1.setObjectName("cB_output_1")
        self.horizontalLayout_11.addWidget(self.cB_output_1)
        self.label_15 = QtWidgets.QLabel(self.dockWidgetContents_output_mpl_1)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_11.addWidget(self.label_15)
        self.comboBox = QtWidgets.QComboBox(self.dockWidgetContents_output_mpl_1)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout_11.addWidget(self.comboBox)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem10)
        self.verticalLayout_2.addLayout(self.horizontalLayout_11)
        self.mpl_container_1 = QtWidgets.QVBoxLayout()
        self.mpl_container_1.setObjectName("mpl_container_1")
        self.verticalLayout_2.addLayout(self.mpl_container_1)
        self.dockWidget_output_1.setWidget(self.dockWidgetContents_output_mpl_1)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockWidget_output_1)
        self.dockWidget_output_2 = QtWidgets.QDockWidget(MainWindow)
        self.dockWidget_output_2.setObjectName("dockWidget_output_2")
        self.dockWidgetContents_output_mpl_2 = QtWidgets.QWidget()
        self.dockWidgetContents_output_mpl_2.setObjectName("dockWidgetContents_output_mpl_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.dockWidgetContents_output_mpl_2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.cB_output_2 = QtWidgets.QComboBox(self.dockWidgetContents_output_mpl_2)
        self.cB_output_2.setObjectName("cB_output_2")
        self.horizontalLayout_12.addWidget(self.cB_output_2)
        self.label_16 = QtWidgets.QLabel(self.dockWidgetContents_output_mpl_2)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_12.addWidget(self.label_16)
        self.comboBox_2 = QtWidgets.QComboBox(self.dockWidgetContents_output_mpl_2)
        self.comboBox_2.setObjectName("comboBox_2")
        self.horizontalLayout_12.addWidget(self.comboBox_2)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem11)
        self.verticalLayout_5.addLayout(self.horizontalLayout_12)
        self.mpl_container_2 = QtWidgets.QVBoxLayout()
        self.mpl_container_2.setObjectName("mpl_container_2")
        self.verticalLayout_5.addLayout(self.mpl_container_2)
        self.dockWidget_output_2.setWidget(self.dockWidgetContents_output_mpl_2)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockWidget_output_2)
        self.dockWidget_output_3 = QtWidgets.QDockWidget(MainWindow)
        self.dockWidget_output_3.setObjectName("dockWidget_output_3")
        self.dockWidgetContents_output_mpl_3 = QtWidgets.QWidget()
        self.dockWidgetContents_output_mpl_3.setObjectName("dockWidgetContents_output_mpl_3")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.dockWidgetContents_output_mpl_3)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.cB_output_3 = QtWidgets.QComboBox(self.dockWidgetContents_output_mpl_3)
        self.cB_output_3.setObjectName("cB_output_3")
        self.verticalLayout_7.addWidget(self.cB_output_3)
        self.mpl_container_3 = QtWidgets.QVBoxLayout()
        self.mpl_container_3.setObjectName("mpl_container_3")
        self.verticalLayout_7.addLayout(self.mpl_container_3)
        self.dockWidget_output_3.setWidget(self.dockWidgetContents_output_mpl_3)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockWidget_output_3)
        self.dockWidget_output_4 = QtWidgets.QDockWidget(MainWindow)
        self.dockWidget_output_4.setObjectName("dockWidget_output_4")
        self.dockWidgetContents_4 = QtWidgets.QWidget()
        self.dockWidgetContents_4.setObjectName("dockWidgetContents_4")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.dockWidgetContents_4)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.cB_output_4 = QtWidgets.QComboBox(self.dockWidgetContents_4)
        self.cB_output_4.setObjectName("cB_output_4")
        self.verticalLayout_9.addWidget(self.cB_output_4)
        self.mpl_container_4 = QtWidgets.QVBoxLayout()
        self.mpl_container_4.setObjectName("mpl_container_4")
        self.verticalLayout_9.addLayout(self.mpl_container_4)
        self.dockWidget_output_4.setWidget(self.dockWidgetContents_4)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockWidget_output_4)
        self.dockWidget_logger = QtWidgets.QDockWidget(MainWindow)
        self.dockWidget_logger.setMinimumSize(QtCore.QSize(98, 200))
        self.dockWidget_logger.setMaximumSize(QtCore.QSize(524287, 200))
        self.dockWidget_logger.setFloating(False)
        self.dockWidget_logger.setAllowedAreas(QtCore.Qt.NoDockWidgetArea)
        self.dockWidget_logger.setObjectName("dockWidget_logger")
        self.dockWidgetContents_logger = QtWidgets.QWidget()
        self.dockWidgetContents_logger.setObjectName("dockWidgetContents_logger")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.dockWidgetContents_logger)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.textBrowser_logger = QtWidgets.QTextBrowser(self.dockWidgetContents_logger)
        self.textBrowser_logger.setMaximumSize(QtCore.QSize(16777215, 200))
        self.textBrowser_logger.setObjectName("textBrowser_logger")
        self.horizontalLayout_2.addWidget(self.textBrowser_logger)
        self.dockWidget_logger.setWidget(self.dockWidgetContents_logger)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockWidget_logger)

        self.retranslateUi(MainWindow)
        self.tabWidget_manip_display.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBoxWorldmap.setTitle(_translate("MainWindow", "Worldmap"))
        self.label_lon.setText(_translate("MainWindow", "Lon:"))
        self.label_lat.setText(_translate("MainWindow", "Lat: "))
        self.groupBox_forcing_display.setTitle(_translate("MainWindow", "Forcing"))
        self.label_4.setText(_translate("MainWindow", "Forcing dataset:"))
        self.label_11.setText(_translate("MainWindow", "First year:  "))
        self.label_12.setText(_translate("MainWindow", "Lasy year:  "))
        self.label_5.setText(_translate("MainWindow", "Resolution:"))
        self.label_10.setText(_translate("MainWindow", "Offset:       "))
        self.groupBox_manipulation_settings.setTitle(_translate("MainWindow", "Climate manipulation"))
        self.label_temp_change.setText(_translate("MainWindow", "Temperature change "))
        self.label_2.setText(_translate("MainWindow", "over"))
        self.label_3.setText(_translate("MainWindow", "years"))
        self.label_rain_change.setText(_translate("MainWindow", "Rainfall change"))
        self.label_6.setText(_translate("MainWindow", "over"))
        self.label_8.setText(_translate("MainWindow", "years"))
        self.label_co2_change.setText(_translate("MainWindow", "CO2 change"))
        self.label_9.setText(_translate("MainWindow", "over"))
        self.label_7.setText(_translate("MainWindow", "years"))
        self.verticalGroupBox_manip_display.setTitle(_translate("MainWindow", "Manipulation display"))
        self.tabWidget_manip_display.setTabText(self.tabWidget_manip_display.indexOf(self.tab_temp), _translate("MainWindow", "Tab 1"))
        self.tabWidget_manip_display.setTabText(self.tabWidget_manip_display.indexOf(self.tab_rain), _translate("MainWindow", "Tab 2"))
        self.pushButton_run_model.setText(_translate("MainWindow", "Run"))
        self.pushButton_stop_model.setText(_translate("MainWindow", "Stop"))
        self.label_14.setText(_translate("MainWindow", "PFT:"))
        self.label_13.setText(_translate("MainWindow", "Spinup years:"))
        self.label.setText(_translate("MainWindow", "Progress:"))
        self.label_15.setText(_translate("MainWindow", "Res:"))
        self.label_16.setText(_translate("MainWindow", "Res:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
