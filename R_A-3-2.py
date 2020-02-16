
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QIcon
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys,time
from PyQt4.QtCore import *
import xml.etree.ElementTree as ET
import resource





class Module:

    Containers = []

    def __init__(self, XmlFilePath):
        self.XmlFilePath = XmlFilePath

    def GetModuleName(self):
        tree = ET.parse(self.XmlFilePath)   #parse the file
        for node in tree.iter():    #iterate on all tree nodes
            if(node.tag == "{http://autosar.org/3.2.1}Module"):
                for child in node:
                    if(child.tag == "{http://autosar.org/3.2.1}Short_Name"):
                        return child.text



    def GetContainerName(self):
        tree = ET.parse(self.XmlFilePath)   #parse the file
        Containers = []
        for node in tree.iter():    #iterate on all tree nodes
            if(node.tag == "{http://autosar.org/3.2.1}Containers"):
                for child in node:
                    if(child.tag == "{http://autosar.org/3.2.1}Container"):
                        for grandchild in child:
                            if(grandchild.tag == "{http://autosar.org/3.2.1}Short_Name"):
                                Containers.append(grandchild.text)
        return Containers

    def GetSubContainerName(self,Container):
        tree = ET.parse(self.XmlFilePath)   #parse the file
        SubContainers = []
        for node in tree.iter():    #iterate on all tree node
                if(node.tag == "{http://autosar.org/3.2.1}Container"):
                    flag=False
                    for child in node:
                        if((child.tag == "{http://autosar.org/3.2.1}Short_Name") and (flag == False)):
                            if(child.text == Container):
                                flag =True
                                continue
                               
                        if((child.tag == "{http://autosar.org/3.2.1}Parameters") and (flag == True)) :
                            for grandchild in child:
                                if(grandchild.tag == "{http://autosar.org/3.2.1}subContainer"):
                                    for subContainerName in grandchild:
                                        if(subContainerName.tag == "{http://autosar.org/3.2.1}Short_Name"):
                                            SubContainers.append(subContainerName.text)
        return SubContainers





    def GetParamName(self,Container):
        tree = ET.parse(self.XmlFilePath)   #parse the file
        Parameters = []

        for node in tree.iter():    #iterate on all tree node
                if(node.tag == "{http://autosar.org/3.2.1}Container"):
                    flag=False
                    for child in node:
                        if((child.tag == "{http://autosar.org/3.2.1}Short_Name") and (flag == False)):
                            if(child.text == Container):
                                flag =True
                                continue
                               
                        if((child.tag == "{http://autosar.org/3.2.1}Parameters") and (flag == True)) :
                            for grandchild in child:
                                if(grandchild.tag == "{http://autosar.org/3.2.1}Param"):
                                    for parName in grandchild:
                                        if(parName.tag == "{http://autosar.org/3.2.1}Short_Name"):
                                            Parameters.append(parName.text)

        return Parameters


    def Modify(self,param,value):
        ET.register_namespace("", "http://autosar.org/3.2.1")

        tree = ET.parse(self.XmlFilePath)   #parse the file
        for node in tree.iter():
            if(node.tag == "{http://autosar.org/3.2.1}Param"):
                flag=False

                for child in node:
                    if((child.tag == "{http://autosar.org/3.2.1}Short_Name") and (child.text == param) and (flag == False)):
                        flag = True
                        continue

                    if((child.tag == "{http://autosar.org/3.2.1}Value") and (flag == True)):
                        child.text=value
        tree.write('can_xml_1.xml')

    def GetValue(self,param):
        ET.register_namespace("", "http://autosar.org/3.2.1")

        tree = ET.parse(self.XmlFilePath)   #parse the file
        for node in tree.iter():
            if(node.tag == "{http://autosar.org/3.2.1}Param"):
                flag=False

                for child in node:
                    if((child.tag == "{http://autosar.org/3.2.1}Short_Name") and (child.text == param) and (flag == False)):
                        flag = True
                        continue

                    if((child.tag == "{http://autosar.org/3.2.1}Value") and (flag == True)):
                        return child.text



    def GetNames(self):
        tree = ET.parse(self.XmlFilePath)   #parse the file

        for node in tree.iter():
            print(node.tag)

    

    def Subcontainer_param(self,subContainer):
        tree=ET.parse(self.XmlFilePath)
        Subcontainer_param=[]
        for element in tree.iter():
            if(element.tag=="{http://autosar.org/3.2.1}subContainer"):
                found=False
                for child in element:
                    if((child.tag=="{http://autosar.org/3.2.1}Short_Name")and(found==False)):
                        if(child.text==subContainer):
                            found=True
                            continue
                    if((child.tag=="{http://autosar.org/3.2.1}Param")and(found==True)):
                        for grandchild in child:
                            if(grandchild.tag=="{http://autosar.org/3.2.1}Short_Name"):
                                Subcontainer_param.append(grandchild.text)

        return Subcontainer_param  

    def Subsubcontainer_param(self,subsubContainer):
        tree=ET.parse(self.XmlFilePath)
        Subsubcontainer_param=[]
        for element in tree.iter():
            if(element.tag=="{http://autosar.org/3.2.1}subsubContainer"):
                found=False
                for child in element:
                    if((child.tag=="{http://autosar.org/3.2.1}Short_Name")and(found==False)):
                        if(child.text==subsubContainer):
                            found=True
                            continue
                    if((child.tag=="{http://autosar.org/3.2.1}Parameters")and(found==True)):
                        for grandchild in child:
                            if(grandchild.tag=="{http://autosar.org/3.2.1}Param"):  
                                for lastchild in grandchild:
                                    if(lastchild.tag=="{http://autosar.org/3.2.1}Short_Name"):
                                        Subsubcontainer_param.append(lastchild.text)                                                  
        return Subsubcontainer_param

    def Subcontainer_no(self,subContainer):
        tree=ET.parse(self.XmlFilePath)
        count=0
        for element in tree.iter():
            if(element.tag=="{http://autosar.org/3.2.1}subContainer"):
                found=False
                for child in element:
                    if((child.tag=="{http://autosar.org/3.2.1}Short_Name")and(found==False)):
                        if(subContainer in child.text):
                            count=count+1
                            

        return count

    def Subsubcontainer_no(self,subsubContainer):
        tree=ET.parse(self.XmlFilePath)
        count=0
        for element in tree.iter():
            if(element.tag=="{http://autosar.org/3.2.1}subsubContainer"):
                for child in element:
                    if(child.tag=="{http://autosar.org/3.2.1}Short_Name"):
                        if(subsubContainer in child.text):
                            count =count+1
        return count

    
    def no_HTH_HRH(self,Type):
        tree=ET.parse(self.XmlFilePath)
        count=0
        for element in tree.iter():
            if(element.tag=="{http://autosar.org/3.2.1}subContainer"):
                found=False
                for child in element:
                    if((child.tag=="{http://autosar.org/3.2.1}Short_Name")and(found==False)):
                        if('CanHardwareObject' in child.text):
                            found=True
                            continue
                    if((child.tag=="{http://autosar.org/3.2.1}Param")and(found==True)):
                        for grandchild in child:
                            if((grandchild.tag=="{http://autosar.org/3.2.1}Value") and (grandchild.text==Type)):
                                count =count+1
                         
                             
        return count

    def HW_object_Type(self,HW_Object):
        tree=ET.parse(self.XmlFilePath)
        for element in tree.iter():
            if(element.tag=="{http://autosar.org/3.2.1}subContainer"):
                found=False
                for child in element:
                    if((child.tag=="{http://autosar.org/3.2.1}Short_Name")and(found==False)):
                        if(child.text==HW_Object):
                            found=True
                            continue
                    if((child.tag=="{http://autosar.org/3.2.1}Param")and(found==True)):
                        for grandchild in child:
                            if((grandchild.tag=="{http://autosar.org/3.2.1}Value") and (grandchild.text=='TRANSMIT' or grandchild.text=='RECEIVE')):
                                return grandchild.text
                        


def check(value):
        if(value == 'True'):
            return True
        else:
            return False

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_CanTool(object):
    path_1=""
    def setupUi(self, CanTool):
        CanTool.setObjectName(_fromUtf8("CanTool"))

        CanTool.resize(1058,700)
        self.centralwidget = QtGui.QWidget(CanTool)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.treeWidget = QtGui.QTreeWidget(self.centralwidget)
        self.treeWidget.setGeometry(QtCore.QRect(0, 0, 260, 800))
        self.treeWidget.setObjectName(_fromUtf8("treeWidget"))
        item_0 = QtGui.QTreeWidgetItem(self.treeWidget)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_2 = QtGui.QTreeWidgetItem(item_1)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_3 = QtGui.QTreeWidgetItem(item_1)
        item_4 = QtGui.QTreeWidgetItem(item_3)
        item_15 = QtGui.QTreeWidgetItem(item_4)
        item_16 = QtGui.QTreeWidgetItem(item_3)
        item_17 = QtGui.QTreeWidgetItem(item_16)
        #item_4 = QtGui.QTreeWidgetItem(item_3)
        item_5 = QtGui.QTreeWidgetItem(item_1)
        item_7 = QtGui.QTreeWidgetItem(item_5)
        item_8 = QtGui.QTreeWidgetItem(item_7)
        item_9 = QtGui.QTreeWidgetItem(item_5)
        item_10= QtGui.QTreeWidgetItem(item_9)
        item_11= QtGui.QTreeWidgetItem(item_5)
        item_12= QtGui.QTreeWidgetItem(item_11)
        item_13= QtGui.QTreeWidgetItem(item_5)
        item_14= QtGui.QTreeWidgetItem(item_13)
        #item_6 = QtGui.QTreeWidgetItem(item_5) #CanHWFilter
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(270, 0, 780, 700))
        self.groupBox.setStyleSheet(_fromUtf8("background-image: url(:/img/edited.jpg);"))
        self.groupBox.setAutoFillBackground(True)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.groupBox.setVisible(False)
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(30, 70, 71, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(30, 120, 161, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(30, 170, 121, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(30, 220, 171, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(30, 270, 141, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(30, 320, 121, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(30, 370, 111, 16))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(30, 420, 101, 16))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(30, 470, 111, 16))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.Can_Index = QtGui.QLineEdit(self.groupBox)
        self.Can_Index.setGeometry(QtCore.QRect(290, 70, 113, 20))
        self.Can_Index.setObjectName(_fromUtf8("Can_Index"))
        self.Can_main_fn_Mode_period = QtGui.QLineEdit(self.groupBox)
        self.Can_main_fn_Mode_period.setGeometry(QtCore.QRect(290, 120, 113, 20))
        self.Can_main_fn_Mode_period.setObjectName(_fromUtf8("Can_main_fn_Mode_period"))
        self.Can_Timeout_Duration = QtGui.QLineEdit(self.groupBox)
        self.Can_Timeout_Duration.setGeometry(QtCore.QRect(290, 170, 113, 20))
        self.Can_Timeout_Duration.setObjectName(_fromUtf8("Can_Timeout_Duration"))
        self.Can_Main_Fn_Wakeup = QtGui.QLineEdit(self.groupBox)
        self.Can_Main_Fn_Wakeup.setGeometry(QtCore.QRect(290, 220, 113, 20))
        self.Can_Main_Fn_Wakeup.setObjectName(_fromUtf8("Can_Main_Fn_Wakeup"))
        self.Can_mul_transmission = QtGui.QCheckBox(self.groupBox)
        self.Can_mul_transmission.setGeometry(QtCore.QRect(290, 270, 70, 17))
        self.Can_mul_transmission.setText(_fromUtf8(""))
        self.Can_mul_transmission.setObjectName(_fromUtf8("Can_mul_transmission"))
        self.Can_Public_icom_support = QtGui.QCheckBox(self.groupBox)
        self.Can_Public_icom_support.setGeometry(QtCore.QRect(290, 320, 70, 17))
        self.Can_Public_icom_support.setText(_fromUtf8(""))
        self.Can_Public_icom_support.setObjectName(_fromUtf8("Can_Public_icom_support"))
        self.Can_version_info = QtGui.QCheckBox(self.groupBox)
        self.Can_version_info.setGeometry(QtCore.QRect(290, 370, 70, 17))
        self.Can_version_info.setText(_fromUtf8(""))
        self.Can_version_info.setObjectName(_fromUtf8("Can_version_info"))
        self.Can_Dev_error = QtGui.QCheckBox(self.groupBox)
        self.Can_Dev_error.setGeometry(QtCore.QRect(290, 420, 70, 17))
        self.Can_Dev_error.setText(_fromUtf8(""))
        self.Can_Dev_error.setObjectName(_fromUtf8("Can_Dev_error"))
        self.Can_Set_baudrate_API = QtGui.QCheckBox(self.groupBox)
        self.Can_Set_baudrate_API.setGeometry(QtCore.QRect(290,470, 70, 17))
        self.Can_Set_baudrate_API.setText(_fromUtf8(""))
        self.Can_Set_baudrate_API.setObjectName(_fromUtf8("Can_Set_baudrate_API"))



        ###################################################### Can_Controller_GroupBox

        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(270, 0, 780, 700))
        self.groupBox_2.setStyleSheet(_fromUtf8("background-image: url(:/img/edited.jpg);"))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox"))
        self.groupBox_2.setVisible(False)
        self.label_10 = QtGui.QLabel(self.groupBox_2)
        self.label_10.setGeometry(QtCore.QRect(30, 70, 161, 21))
        self.label_10.setObjectName(_fromUtf8("label"))
        self.label_20 = QtGui.QLabel(self.groupBox_2)
        self.label_20.setGeometry(QtCore.QRect(30, 120, 161, 16))
        self.label_20.setObjectName(_fromUtf8("label_2"))
        self.label_30 = QtGui.QLabel(self.groupBox_2)
        self.label_30.setGeometry(QtCore.QRect(30, 170, 111, 16))
        self.label_30.setObjectName(_fromUtf8("label_3"))
        self.label_40 = QtGui.QLabel(self.groupBox_2)
        self.label_40.setGeometry(QtCore.QRect(30, 220, 101, 16))
        self.label_40.setObjectName(_fromUtf8("label_4"))
        self.label_50 = QtGui.QLabel(self.groupBox_2)
        self.label_50.setGeometry(QtCore.QRect(30, 270, 121, 16))
        self.label_50.setObjectName(_fromUtf8("label_5"))
        self.label_60 = QtGui.QLabel(self.groupBox_2)
        self.label_60.setGeometry(QtCore.QRect(30, 320, 131, 16))
        self.label_60.setObjectName(_fromUtf8("label_6"))
        self.label_70 = QtGui.QLabel(self.groupBox_2)
        self.label_70.setGeometry(QtCore.QRect(30, 370, 141, 16))
        self.label_70.setObjectName(_fromUtf8("label_7"))
        self.label_80 = QtGui.QLabel(self.groupBox_2)
        self.label_80.setGeometry(QtCore.QRect(30, 420, 121, 16))
        self.label_80.setObjectName(_fromUtf8("label_8"))
        self.label_90 = QtGui.QLabel(self.groupBox_2)
        self.label_90.setGeometry(QtCore.QRect(30, 470, 151, 16))
        self.label_90.setObjectName(_fromUtf8("label_9"))
        self.Can_Controller_ID = QtGui.QLineEdit(self.groupBox_2)
        self.Can_Controller_ID.setGeometry(QtCore.QRect(290, 70, 113, 20))
        self.Can_Controller_ID.setObjectName(_fromUtf8("Can_Controller_ID"))
        self.Can_Controller_Base_Address = QtGui.QLineEdit(self.groupBox_2)
        self.Can_Controller_Base_Address.setGeometry(QtCore.QRect(290, 120, 113, 20))
        self.Can_Controller_Base_Address.setObjectName(_fromUtf8("Can_Controller_Base_Address"))
        self.Can_Tx_Processing = QtGui.QComboBox(self.groupBox_2)
        self.Can_Tx_Processing.setGeometry(QtCore.QRect(290, 170, 111, 22))
        self.Can_Tx_Processing.setObjectName(_fromUtf8("Can_Tx_Processing"))
        self.Can_Tx_Processing.addItem('INTERRUPT')
        self.Can_Tx_Processing.addItem('POLLING')
        self.Can_Rx_Processing = QtGui.QComboBox(self.groupBox_2)
        self.Can_Rx_Processing.setGeometry(QtCore.QRect(290, 220, 111, 22))
        self.Can_Rx_Processing.setObjectName(_fromUtf8("Can_Rx_Processing"))
        self.Can_Rx_Processing.addItem('INTERRUPT')
        self.Can_Rx_Processing.addItem('POLLING')
        self.can_bus_off = QtGui.QComboBox(self.groupBox_2)
        self.can_bus_off.setGeometry(QtCore.QRect(290, 270, 111, 22))
        self.can_bus_off.setObjectName(_fromUtf8("can_bus_off"))
        self.can_bus_off.addItem('INTERRUPT')
        self.can_bus_off.addItem('POLLING')
        self.can_wakeup = QtGui.QComboBox(self.groupBox_2)
        self.can_wakeup.setGeometry(QtCore.QRect(290, 320, 111, 22))
        self.can_wakeup.setObjectName(_fromUtf8("can_wakeup"))
        self.can_wakeup.addItem('INTERRUPT')
        self.can_wakeup.addItem('POLLING')
        self.can_controller_activation = QtGui.QCheckBox(self.groupBox_2)
        self.can_controller_activation.setGeometry(QtCore.QRect(290, 370, 70, 17))
        self.can_controller_activation.setText(_fromUtf8(""))
        self.can_controller_activation.setObjectName(_fromUtf8("can_controller_activation"))
        self.can_wakeup_support = QtGui.QCheckBox(self.groupBox_2)
        self.can_wakeup_support.setGeometry(QtCore.QRect(290, 420, 70, 17))
        self.can_wakeup_support.setText(_fromUtf8(""))
        self.can_wakeup_support.setObjectName(_fromUtf8("can_wakeup_support"))
        self.can_wakeup_API = QtGui.QCheckBox(self.groupBox_2)
        self.can_wakeup_API.setGeometry(QtCore.QRect(290, 470, 70, 17))
        self.can_wakeup_API.setText(_fromUtf8(""))
        self.can_wakeup_API.setObjectName(_fromUtf8("can_wakeup_API"))
       ########################################################################


        ################################################################# CanContollerBaudRate
        self.groupBox_3 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(270, 0, 780, 700))
        self.groupBox_3.setStyleSheet(_fromUtf8("background-image: url(:/img/edited.jpg);"))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.groupBox_3.setVisible(False)
        self.label_2000 = QtGui.QLabel(self.groupBox_3)
        self.label_2000.setGeometry(QtCore.QRect(30, 120, 141, 16))
        self.label_2000.setObjectName(_fromUtf8("label_2000"))
        self.label_3000 = QtGui.QLabel(self.groupBox_3)
        self.label_3000.setGeometry(QtCore.QRect(30, 170, 151, 16))
        self.label_3000.setObjectName(_fromUtf8("label_3000"))
        self.label_4000 = QtGui.QLabel(self.groupBox_3)
        self.label_4000.setGeometry(QtCore.QRect(30, 220, 111, 16))
        self.label_4000.setObjectName(_fromUtf8("label_4000"))
        self.label_5000 = QtGui.QLabel(self.groupBox_3)
        self.label_5000.setGeometry(QtCore.QRect(30, 270, 101, 16))
        self.label_5000.setObjectName(_fromUtf8("label_5000"))
        self.label_1000 = QtGui.QLabel(self.groupBox_3)
        self.label_1000.setGeometry(QtCore.QRect(30, 70, 181, 21))
        self.label_1000.setObjectName(_fromUtf8("label_1000"))
        self.label_6000 = QtGui.QLabel(self.groupBox_3)
        self.label_6000.setGeometry(QtCore.QRect(30, 320, 191, 16))
        self.label_6000.setObjectName(_fromUtf8("label_6000"))
        self.BaudRate_config_ID = QtGui.QLineEdit(self.groupBox_3)
        self.BaudRate_config_ID.setGeometry(QtCore.QRect(290, 70, 113, 20))
        self.BaudRate_config_ID.setObjectName(_fromUtf8("BaudRate_config_ID"))
        self.BaudRate = QtGui.QLineEdit(self.groupBox_3)
        self.BaudRate.setGeometry(QtCore.QRect(290, 120, 113, 20))
        self.BaudRate.setObjectName(_fromUtf8("BaudRate"))
        self.Prop_seg = QtGui.QLineEdit(self.groupBox_3)
        self.Prop_seg.setGeometry(QtCore.QRect(290, 170, 113, 20))
        self.Prop_seg.setObjectName(_fromUtf8("Prop_seg"))
        self.Prop_seg1 = QtGui.QLineEdit(self.groupBox_3)
        self.Prop_seg1.setGeometry(QtCore.QRect(290, 220, 113, 20))
        self.Prop_seg1.setObjectName(_fromUtf8("Prop_seg1"))
        self.Prop_seg2 = QtGui.QLineEdit(self.groupBox_3)
        self.Prop_seg2.setGeometry(QtCore.QRect(290, 270, 113, 20))
        self.Prop_seg2.setObjectName(_fromUtf8("Prop_seg2"))
        self.Sync_jumpwidth = QtGui.QLineEdit(self.groupBox_3)
        self.Sync_jumpwidth.setGeometry(QtCore.QRect(290, 320, 113, 20))
        self.Sync_jumpwidth.setObjectName(_fromUtf8("Sync_jumpwidth"))
       #############################################################################################

         ###################################################### Can_Controller_2_GroupBox

        self.groupBox_12 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_12.setGeometry(QtCore.QRect(270, 0, 780, 700))
        self.groupBox_12.setStyleSheet(_fromUtf8("background-image: url(:/img/edited.jpg);"))
        self.groupBox_12.setObjectName(_fromUtf8("groupBox_11"))
        self.groupBox_12.setVisible(False)
        self.label_10_2 = QtGui.QLabel(self.groupBox_12)
        self.label_10_2.setGeometry(QtCore.QRect(30, 70, 161, 21))
        self.label_10_2.setObjectName(_fromUtf8("label_10_2"))
        self.label_20_2 = QtGui.QLabel(self.groupBox_12)
        self.label_20_2.setGeometry(QtCore.QRect(30, 120, 161, 16))
        self.label_20_2.setObjectName(_fromUtf8("label_20_2"))
        self.label_30_2 = QtGui.QLabel(self.groupBox_12)
        self.label_30_2.setGeometry(QtCore.QRect(30, 170, 111, 16))
        self.label_30_2.setObjectName(_fromUtf8("label_30_2"))
        self.label_40_2 = QtGui.QLabel(self.groupBox_12)
        self.label_40_2.setGeometry(QtCore.QRect(30, 220, 101, 16))
        self.label_40_2.setObjectName(_fromUtf8("label_40_2"))
        self.label_50_2 = QtGui.QLabel(self.groupBox_12)
        self.label_50_2.setGeometry(QtCore.QRect(30, 270, 121, 16))
        self.label_50_2.setObjectName(_fromUtf8("label_50_2"))
        self.label_60_2= QtGui.QLabel(self.groupBox_12)
        self.label_60_2.setGeometry(QtCore.QRect(30, 320, 131, 16))
        self.label_60_2.setObjectName(_fromUtf8("label_60_2"))
        self.label_70_2 = QtGui.QLabel(self.groupBox_12)
        self.label_70_2.setGeometry(QtCore.QRect(30, 370, 141, 16))
        self.label_70_2.setObjectName(_fromUtf8("label_70_2"))
        self.label_80_2 = QtGui.QLabel(self.groupBox_12)
        self.label_80_2.setGeometry(QtCore.QRect(30, 420, 121, 16))
        self.label_80_2.setObjectName(_fromUtf8("label_80_2"))
        self.label_90_2 = QtGui.QLabel(self.groupBox_12)
        self.label_90_2.setGeometry(QtCore.QRect(30, 470, 151, 16))
        self.label_90_2.setObjectName(_fromUtf8("label_90_2"))
        self.Can_Controller_ID_2 = QtGui.QLineEdit(self.groupBox_12)
        self.Can_Controller_ID_2.setGeometry(QtCore.QRect(290, 70, 113, 20))
        self.Can_Controller_ID_2.setObjectName(_fromUtf8("Can_Controller_ID_2"))
        self.Can_Controller_Base_Address_2 = QtGui.QLineEdit(self.groupBox_12)
        self.Can_Controller_Base_Address_2.setGeometry(QtCore.QRect(290, 120, 113, 20))
        self.Can_Controller_Base_Address_2.setObjectName(_fromUtf8("Can_Controller_Base_Address_2"))
        self.Can_Tx_Processing_2 = QtGui.QComboBox(self.groupBox_12)
        self.Can_Tx_Processing_2.setGeometry(QtCore.QRect(290, 170, 111, 22))
        self.Can_Tx_Processing_2.setObjectName(_fromUtf8("Can_Tx_Processing_2"))
        self.Can_Tx_Processing_2.addItem('INTERRUPT')
        self.Can_Tx_Processing_2.addItem('POLLING')
        self.Can_Rx_Processing_2 = QtGui.QComboBox(self.groupBox_12)
        self.Can_Rx_Processing_2.setGeometry(QtCore.QRect(290, 220, 111, 22))
        self.Can_Rx_Processing_2.setObjectName(_fromUtf8("Can_Rx_Processing_2"))
        self.Can_Rx_Processing_2.addItem('INTERRUPT')
        self.Can_Rx_Processing_2.addItem('POLLING')
        self.can_bus_off_2 = QtGui.QComboBox(self.groupBox_12)
        self.can_bus_off_2.setGeometry(QtCore.QRect(290, 270, 111, 22))
        self.can_bus_off_2.setObjectName(_fromUtf8("can_bus_off_2"))
        self.can_bus_off_2.addItem('INTERRUPT')
        self.can_bus_off_2.addItem('POLLING')
        self.can_wakeup_2= QtGui.QComboBox(self.groupBox_12)
        self.can_wakeup_2.setGeometry(QtCore.QRect(290, 320, 111, 22))
        self.can_wakeup_2.setObjectName(_fromUtf8("can_wakeup_2"))
        self.can_wakeup_2.addItem('INTERRUPT')
        self.can_wakeup_2.addItem('POLLING')
        self.can_controller_activation_2 = QtGui.QCheckBox(self.groupBox_12)
        self.can_controller_activation_2.setGeometry(QtCore.QRect(290, 370, 70, 17))
        self.can_controller_activation_2.setText(_fromUtf8(""))
        self.can_controller_activation_2.setObjectName(_fromUtf8("can_controller_activation_2"))
        self.can_wakeup_support_2 = QtGui.QCheckBox(self.groupBox_12)
        self.can_wakeup_support_2.setGeometry(QtCore.QRect(290, 420, 70, 17))
        self.can_wakeup_support_2.setText(_fromUtf8(""))
        self.can_wakeup_support_2.setObjectName(_fromUtf8("can_wakeup_support_2"))
        self.can_wakeup_API_2 = QtGui.QCheckBox(self.groupBox_12)
        self.can_wakeup_API_2.setGeometry(QtCore.QRect(290, 470, 70, 17))
        self.can_wakeup_API_2.setText(_fromUtf8(""))
        self.can_wakeup_API_2.setObjectName(_fromUtf8("can_wakeup_API_2"))
       ########################################################################


        ################################################################# CanContoller_2_BaudRate
        self.groupBox_13 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_13.setGeometry(QtCore.QRect(270, 0, 780, 700))
        self.groupBox_13.setStyleSheet(_fromUtf8("background-image: url(:/img/edited.jpg);"))
        self.groupBox_13.setObjectName(_fromUtf8("groupBox_12"))
        self.groupBox_13.setVisible(False)
        self.label_2000_2 = QtGui.QLabel(self.groupBox_13)
        self.label_2000_2.setGeometry(QtCore.QRect(30, 120, 141, 16))
        self.label_2000_2.setObjectName(_fromUtf8("label_2000_2"))
        self.label_3000_2 = QtGui.QLabel(self.groupBox_13)
        self.label_3000_2.setGeometry(QtCore.QRect(30, 170, 151, 16))
        self.label_3000_2.setObjectName(_fromUtf8("label_3000_2"))
        self.label_4000_2 = QtGui.QLabel(self.groupBox_13)
        self.label_4000_2.setGeometry(QtCore.QRect(30, 220, 111, 16))
        self.label_4000_2.setObjectName(_fromUtf8("label_4000_2"))
        self.label_5000_2 = QtGui.QLabel(self.groupBox_13)
        self.label_5000_2.setGeometry(QtCore.QRect(30, 270, 101, 16))
        self.label_5000_2.setObjectName(_fromUtf8("label_5000_2"))
        self.label_1000_2 = QtGui.QLabel(self.groupBox_13)
        self.label_1000_2.setGeometry(QtCore.QRect(30, 70, 181, 21))
        self.label_1000_2.setObjectName(_fromUtf8("label_1000_2"))
        self.label_6000_2 = QtGui.QLabel(self.groupBox_13)
        self.label_6000_2.setGeometry(QtCore.QRect(30, 320, 191, 16))
        self.label_6000_2.setObjectName(_fromUtf8("label_6000_2"))
        self.BaudRate_config_ID_2 = QtGui.QLineEdit(self.groupBox_13)
        self.BaudRate_config_ID_2.setGeometry(QtCore.QRect(290, 70, 113, 20))
        self.BaudRate_config_ID_2.setObjectName(_fromUtf8("BaudRate_config_ID_2"))
        self.BaudRate_2 = QtGui.QLineEdit(self.groupBox_13)
        self.BaudRate_2.setGeometry(QtCore.QRect(290, 120, 113, 20))
        self.BaudRate_2.setObjectName(_fromUtf8("BaudRate_2"))
        self.Prop_seg_2= QtGui.QLineEdit(self.groupBox_13)
        self.Prop_seg_2.setGeometry(QtCore.QRect(290, 170, 113, 20))
        self.Prop_seg_2.setObjectName(_fromUtf8("Prop_seg_2"))
        self.Prop_seg1_2 = QtGui.QLineEdit(self.groupBox_13)
        self.Prop_seg1_2.setGeometry(QtCore.QRect(290, 220, 113, 20))
        self.Prop_seg1_2.setObjectName(_fromUtf8("Prop_seg1_2"))
        self.Prop_seg2_2 = QtGui.QLineEdit(self.groupBox_13)
        self.Prop_seg2_2.setGeometry(QtCore.QRect(290, 270, 113, 20))
        self.Prop_seg2_2.setObjectName(_fromUtf8("Prop_seg2_2"))
        self.Sync_jumpwidth_2 = QtGui.QLineEdit(self.groupBox_13)
        self.Sync_jumpwidth_2.setGeometry(QtCore.QRect(290, 320, 113, 20))
        self.Sync_jumpwidth_2.setObjectName(_fromUtf8("Sync_jumpwidth_2"))
       #############################################################################################

       #############################################################################################CanHardwareObject_1
        self.groupBox_4 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(270, 0, 780, 700))
        self.groupBox_4.setStyleSheet(_fromUtf8("background-image: url(:/img/edited.jpg);"))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.groupBox_4.setVisible(False)
        self.label_10000_1 = QtGui.QLabel(self.groupBox_4)
        self.label_10000_1.setGeometry(QtCore.QRect(30, 70, 181, 21))
        self.label_10000_1.setObjectName(_fromUtf8("label"))
        self.label_20000_1 = QtGui.QLabel(self.groupBox_4)
        self.label_20000_1.setGeometry(QtCore.QRect(30, 120, 111, 16))
        self.label_20000_1.setObjectName(_fromUtf8("label_2"))
        self.label_30000_1 = QtGui.QLabel(self.groupBox_4)
        self.label_30000_1.setGeometry(QtCore.QRect(30, 170, 91, 16))
        self.label_30000_1.setObjectName(_fromUtf8("label_3"))
        self.label_40000_1 = QtGui.QLabel(self.groupBox_4)
        self.label_40000_1.setGeometry(QtCore.QRect(30, 220, 101, 16))
        self.label_40000_1.setObjectName(_fromUtf8("label_4"))
        self.label_50000_1 = QtGui.QLabel(self.groupBox_4)
        self.label_50000_1.setGeometry(QtCore.QRect(30, 270, 91, 16))
        self.label_50000_1.setObjectName(_fromUtf8("label_5"))
        self.label_60000_1 = QtGui.QLabel(self.groupBox_4)
        self.label_60000_1.setGeometry(QtCore.QRect(30, 320, 141, 16))
        self.label_60000_1.setObjectName(_fromUtf8("label_6"))
        self.label_70000_1 = QtGui.QLabel(self.groupBox_4)
        self.label_70000_1.setGeometry(QtCore.QRect(30, 370, 141, 16))
        self.label_70000_1.setObjectName(_fromUtf8("label_7"))
        self.Can_Object_Id_1 = QtGui.QLineEdit(self.groupBox_4)
        self.Can_Object_Id_1.setGeometry(QtCore.QRect(290, 70, 113, 20))
        self.Can_Object_Id_1.setObjectName(_fromUtf8("Can_Object_Id"))
        self.Can_Fd_Padding_Value_1 = QtGui.QLineEdit(self.groupBox_4)
        self.Can_Fd_Padding_Value_1.setGeometry(QtCore.QRect(290, 120, 113, 20))
        self.Can_Fd_Padding_Value_1.setObjectName(_fromUtf8("Can_Fd_Padding_Value"))
        self.Can_Object_Type_1 = QtGui.QComboBox(self.groupBox_4)
        self.Can_Object_Type_1.setGeometry(QtCore.QRect(290, 170, 111, 22))
        self.Can_Object_Type_1.setObjectName(_fromUtf8("Can_Object_Type"))
        self.Can_Object_Type_1.addItem('TRANSMIT')
        self.Can_Object_Type_1.addItem('RECEIVE')
        self.Can_HandleType_1= QtGui.QComboBox(self.groupBox_4)
        self.Can_HandleType_1.setGeometry(QtCore.QRect(290, 220, 111, 22))
        self.Can_HandleType_1.setObjectName(_fromUtf8("Can_HandleType"))
        self.Can_HandleType_1.addItem('BASIC')
        self.Can_HandleType_1.addItem('FULL')
        self.Can_Id_Type_1 = QtGui.QComboBox(self.groupBox_4)
        self.Can_Id_Type_1.setGeometry(QtCore.QRect(290, 270, 111, 22))
        self.Can_Id_Type_1.setObjectName(_fromUtf8("Can_Id_Type"))
        self.Can_Id_Type_1.addItem('STANDARD')
        self.Can_Id_Type_1.addItem('EXTENDED')
        self.Can_Id_Type_1.addItem('MIXED')
        self.Can_Trigger_Transmit_Enable_1 = QtGui.QCheckBox(self.groupBox_4)
        self.Can_Trigger_Transmit_Enable_1.setGeometry(QtCore.QRect(290, 320, 70, 17))
        self.Can_Trigger_Transmit_Enable_1.setText(_fromUtf8(""))
        self.Can_Trigger_Transmit_Enable_1.setObjectName(_fromUtf8("Can_Trigger_Transmit_Enable"))
        self.Can_Controller_ref_1 = QtGui.QComboBox(self.groupBox_4)
        self.Can_Controller_ref_1.setGeometry(QtCore.QRect(290, 370, 111, 22))
        self.Can_Controller_ref_1.setObjectName(_fromUtf8("Can_Controller_ref"))
        self.Can_Controller_ref_1.addItem('Controller 0')
        self.Can_Controller_ref_1.addItem('Controller 1')
       
        #######################################################################################################

        ##################################################################################CanHWFilter_1
        self.groupBox_5 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_5.setGeometry(QtCore.QRect(270, 0, 780, 700))
        self.groupBox_5.setStyleSheet(_fromUtf8("background-image: url(:/img/edited.jpg);"))
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.groupBox_5.setVisible(False)
        self.label_100000_1 = QtGui.QLabel(self.groupBox_5)
        self.label_100000_1.setGeometry(QtCore.QRect(30, 70, 181, 21))
        self.label_100000_1.setObjectName(_fromUtf8("label_100000_1"))
        self.label_200000_1 = QtGui.QLabel(self.groupBox_5)
        self.label_200000_1.setGeometry(QtCore.QRect(30, 120, 111, 16))
        self.label_200000_1.setObjectName(_fromUtf8("label_200000_1"))
        self.Can_Hw_Filter_Mask_1= QtGui.QLineEdit(self.groupBox_5)
        self.Can_Hw_Filter_Mask_1.setGeometry(QtCore.QRect(290, 70, 113, 20))
        self.Can_Hw_Filter_Mask_1.setObjectName(_fromUtf8("Can_Hw_Filter_Mask_1"))
        self.Can_Hw_Filter_Code_1 = QtGui.QLineEdit(self.groupBox_5)
        self.Can_Hw_Filter_Code_1.setGeometry(QtCore.QRect(290, 120, 113, 20))
        self.Can_Hw_Filter_Code_1.setObjectName(_fromUtf8("Can_Hw_Filter_Code_1"))
        #####################################################################################################

        #############################################################################################CanHardwareObject_2
        self.groupBox_6 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_6.setGeometry(QtCore.QRect(270, 0, 780, 700))
        self.groupBox_6.setStyleSheet(_fromUtf8("background-image: url(:/img/edited.jpg);"))
        self.groupBox_6.setObjectName(_fromUtf8("groupBox_6"))
        self.groupBox_6.setVisible(False)
        self.label_10000_2 = QtGui.QLabel(self.groupBox_6)
        self.label_10000_2.setGeometry(QtCore.QRect(30, 70, 181, 21))
        self.label_10000_2.setObjectName(_fromUtf8("label_10000_2"))
        self.label_20000_2 = QtGui.QLabel(self.groupBox_6)
        self.label_20000_2.setGeometry(QtCore.QRect(30, 120, 111, 16))
        self.label_20000_2.setObjectName(_fromUtf8("label_20000_2"))
        self.label_30000_2 = QtGui.QLabel(self.groupBox_6)
        self.label_30000_2.setGeometry(QtCore.QRect(30, 170, 91, 16))
        self.label_30000_2.setObjectName(_fromUtf8("label_30000_2"))
        self.label_40000_2 = QtGui.QLabel(self.groupBox_6)
        self.label_40000_2.setGeometry(QtCore.QRect(30, 220, 101, 16))
        self.label_40000_2.setObjectName(_fromUtf8("label_40000_2"))
        self.label_50000_2 = QtGui.QLabel(self.groupBox_6)
        self.label_50000_2.setGeometry(QtCore.QRect(30, 270, 91, 16))
        self.label_50000_2.setObjectName(_fromUtf8("label_50000_2"))
        self.label_60000_2 = QtGui.QLabel(self.groupBox_6)
        self.label_60000_2.setGeometry(QtCore.QRect(30, 320, 141, 16))
        self.label_60000_2.setObjectName(_fromUtf8("label_60000_2"))
        self.label_70000_2 = QtGui.QLabel(self.groupBox_6)
        self.label_70000_2.setGeometry(QtCore.QRect(30, 370, 141, 16))
        self.label_70000_2.setObjectName(_fromUtf8("label_70000_2"))
        self.Can_Object_Id_2 = QtGui.QLineEdit(self.groupBox_6)
        self.Can_Object_Id_2.setGeometry(QtCore.QRect(290, 70, 113, 20))
        self.Can_Object_Id_2.setObjectName(_fromUtf8("Can_Object_Id_2"))
        self.Can_Fd_Padding_Value_2 = QtGui.QLineEdit(self.groupBox_6)
        self.Can_Fd_Padding_Value_2.setGeometry(QtCore.QRect(290, 120, 113, 20))
        self.Can_Fd_Padding_Value_2.setObjectName(_fromUtf8("Can_Fd_Padding_Value_2"))
        self.Can_Object_Type_2 = QtGui.QComboBox(self.groupBox_6)
        self.Can_Object_Type_2.setGeometry(QtCore.QRect(290, 170, 111, 22))
        self.Can_Object_Type_2.setObjectName(_fromUtf8("Can_Object_Type_2"))
        self.Can_Object_Type_2.addItem('TRANSMIT')
        self.Can_Object_Type_2.addItem('RECEIVE')
        self.Can_HandleType_2= QtGui.QComboBox(self.groupBox_6)
        self.Can_HandleType_2.setGeometry(QtCore.QRect(290, 220, 111, 22))
        self.Can_HandleType_2.setObjectName(_fromUtf8("Can_HandleType_2"))
        self.Can_HandleType_2.addItem('BASIC')
        self.Can_HandleType_2.addItem('FULL')
        self.Can_Id_Type_2 = QtGui.QComboBox(self.groupBox_6)
        self.Can_Id_Type_2.setGeometry(QtCore.QRect(290, 270, 111, 22))
        self.Can_Id_Type_2.setObjectName(_fromUtf8("Can_Id_Type_2"))
        self.Can_Id_Type_2.addItem('STANDARD')
        self.Can_Id_Type_2.addItem('EXTENDED')
        self.Can_Id_Type_2.addItem('MIXED')
        self.Can_Trigger_Transmit_Enable_2 = QtGui.QCheckBox(self.groupBox_6)
        self.Can_Trigger_Transmit_Enable_2.setGeometry(QtCore.QRect(290, 320, 70, 17))
        self.Can_Trigger_Transmit_Enable_2.setText(_fromUtf8(""))
        self.Can_Trigger_Transmit_Enable_2.setObjectName(_fromUtf8("Can_Trigger_Transmit_Enable_2"))
        self.Can_Controller_ref_2 = QtGui.QComboBox(self.groupBox_6)
        self.Can_Controller_ref_2.setGeometry(QtCore.QRect(290, 370, 111, 22))
        self.Can_Controller_ref_2.setObjectName(_fromUtf8("Can_Controller_ref_2"))
        self.Can_Controller_ref_2.addItem('Controller 0')
        self.Can_Controller_ref_2.addItem('Controller 1')
        #######################################################################################################

        ##################################################################################CanHWFilter_2
        self.groupBox_7 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_7.setGeometry(QtCore.QRect(270, 0, 780, 700))
        self.groupBox_7.setStyleSheet(_fromUtf8("background-image: url(:/img/edited.jpg);"))
        self.groupBox_7.setObjectName(_fromUtf8("groupBox_7"))
        self.groupBox_7.setVisible(False)
        self.label_100000_2 = QtGui.QLabel(self.groupBox_7)
        self.label_100000_2.setGeometry(QtCore.QRect(30, 70, 181, 21))
        self.label_100000_2.setObjectName(_fromUtf8("label_100000_2"))
        self.label_200000_2 = QtGui.QLabel(self.groupBox_7)
        self.label_200000_2.setGeometry(QtCore.QRect(30, 120, 111, 16))
        self.label_200000_2.setObjectName(_fromUtf8("label_100000_2"))
        self.Can_Hw_Filter_Mask_2= QtGui.QLineEdit(self.groupBox_7)
        self.Can_Hw_Filter_Mask_2.setGeometry(QtCore.QRect(290, 70, 113, 20))
        self.Can_Hw_Filter_Mask_2.setObjectName(_fromUtf8("Can_Hw_Filter_Mask_2"))
        self.Can_Hw_Filter_Code_2 = QtGui.QLineEdit(self.groupBox_7)
        self.Can_Hw_Filter_Code_2.setGeometry(QtCore.QRect(290, 120, 113, 20))
        self.Can_Hw_Filter_Code_2.setObjectName(_fromUtf8("Can_Hw_Filter_Code_2"))
        #####################################################################################################

        #############################################################################################CanHardwareObject_3
        self.groupBox_8 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_8.setGeometry(QtCore.QRect(270, 0, 780, 700))
        self.groupBox_8.setStyleSheet(_fromUtf8("background-image: url(:/img/edited.jpg);"))
        self.groupBox_8.setObjectName(_fromUtf8("groupBox_4"))
        self.groupBox_8.setVisible(False)
        self.label_10000_3 = QtGui.QLabel(self.groupBox_8)
        self.label_10000_3.setGeometry(QtCore.QRect(30, 70, 181, 21))
        self.label_10000_3.setObjectName(_fromUtf8("label"))
        self.label_20000_3 = QtGui.QLabel(self.groupBox_8)
        self.label_20000_3.setGeometry(QtCore.QRect(30, 120, 111, 16))
        self.label_20000_3.setObjectName(_fromUtf8("label_2"))
        self.label_30000_3 = QtGui.QLabel(self.groupBox_8)
        self.label_30000_3.setGeometry(QtCore.QRect(30, 170, 91, 16))
        self.label_30000_3.setObjectName(_fromUtf8("label_3"))
        self.label_40000_3 = QtGui.QLabel(self.groupBox_8)
        self.label_40000_3.setGeometry(QtCore.QRect(30, 220, 101, 16))
        self.label_40000_3.setObjectName(_fromUtf8("label_4"))
        self.label_50000_3 = QtGui.QLabel(self.groupBox_8)
        self.label_50000_3.setGeometry(QtCore.QRect(30, 270, 91, 16))
        self.label_50000_3.setObjectName(_fromUtf8("label_5"))
        self.label_60000_3 = QtGui.QLabel(self.groupBox_8)
        self.label_60000_3.setGeometry(QtCore.QRect(30, 320, 141, 16))
        self.label_60000_3.setObjectName(_fromUtf8("label_6"))
        self.label_70000_3 = QtGui.QLabel(self.groupBox_8)
        self.label_70000_3.setGeometry(QtCore.QRect(30, 370, 141, 16))
        self.label_70000_3.setObjectName(_fromUtf8("label_7"))
        self.Can_Object_Id_3 = QtGui.QLineEdit(self.groupBox_8)
        self.Can_Object_Id_3.setGeometry(QtCore.QRect(290, 70, 113, 20))
        self.Can_Object_Id_3.setObjectName(_fromUtf8("Can_Object_Id"))
        self.Can_Fd_Padding_Value_3 = QtGui.QLineEdit(self.groupBox_8)
        self.Can_Fd_Padding_Value_3.setGeometry(QtCore.QRect(290, 120, 113, 20))
        self.Can_Fd_Padding_Value_3.setObjectName(_fromUtf8("Can_Fd_Padding_Value"))
        self.Can_Object_Type_3 = QtGui.QComboBox(self.groupBox_8)
        self.Can_Object_Type_3.setGeometry(QtCore.QRect(290, 170, 111, 22))
        self.Can_Object_Type_3.setObjectName(_fromUtf8("Can_Object_Type"))
        self.Can_Object_Type_3.addItem('TRANSMIT')
        self.Can_Object_Type_3.addItem('RECEIVE')
        self.Can_HandleType_3= QtGui.QComboBox(self.groupBox_8)
        self.Can_HandleType_3.setGeometry(QtCore.QRect(290, 220, 111, 22))
        self.Can_HandleType_3.setObjectName(_fromUtf8("Can_HandleType"))
        self.Can_HandleType_3.addItem('BASIC')
        self.Can_HandleType_3.addItem('FULL')
        self.Can_Id_Type_3 = QtGui.QComboBox(self.groupBox_8)
        self.Can_Id_Type_3.setGeometry(QtCore.QRect(290, 270, 111, 22))
        self.Can_Id_Type_3.setObjectName(_fromUtf8("Can_Id_Type"))
        self.Can_Id_Type_3.addItem('STANDARD')
        self.Can_Id_Type_3.addItem('EXTENDED')
        self.Can_Id_Type_3.addItem('MIXED')
        self.Can_Trigger_Transmit_Enable_3 = QtGui.QCheckBox(self.groupBox_8)
        self.Can_Trigger_Transmit_Enable_3.setGeometry(QtCore.QRect(290, 320, 70, 17))
        self.Can_Trigger_Transmit_Enable_3.setText(_fromUtf8(""))
        self.Can_Trigger_Transmit_Enable_3.setObjectName(_fromUtf8("Can_Trigger_Transmit_Enable"))
        self.Can_Controller_ref_3 = QtGui.QComboBox(self.groupBox_8)
        self.Can_Controller_ref_3.setGeometry(QtCore.QRect(290, 370, 111, 22))
        self.Can_Controller_ref_3.setObjectName(_fromUtf8("Can_Controller_ref_3"))
        self.Can_Controller_ref_3.addItem('Controller 0')
        self.Can_Controller_ref_3.addItem('Controller 1')
        #######################################################################################################

        ##################################################################################CanHWFilter_3
        self.groupBox_9 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_9.setGeometry(QtCore.QRect(270, 0, 780, 700))
        self.groupBox_9.setStyleSheet(_fromUtf8("background-image: url(:/img/edited.jpg);"))
        self.groupBox_9.setObjectName(_fromUtf8("groupBox_9"))
        self.groupBox_9.setVisible(False)
        self.label_100000_3 = QtGui.QLabel(self.groupBox_9)
        self.label_100000_3.setGeometry(QtCore.QRect(30, 70, 181, 21))
        self.label_100000_3.setObjectName(_fromUtf8("label_100000_3"))
        self.label_200000_3 = QtGui.QLabel(self.groupBox_9)
        self.label_200000_3.setGeometry(QtCore.QRect(30, 120, 111, 16))
        self.label_200000_3.setObjectName(_fromUtf8("label_200000_3"))
        self.Can_Hw_Filter_Mask_3= QtGui.QLineEdit(self.groupBox_9)
        self.Can_Hw_Filter_Mask_3.setGeometry(QtCore.QRect(290, 70, 113, 20))
        self.Can_Hw_Filter_Mask_3.setObjectName(_fromUtf8("Can_Hw_Filter_Mask_3"))
        self.Can_Hw_Filter_Code_3 = QtGui.QLineEdit(self.groupBox_9)
        self.Can_Hw_Filter_Code_3.setGeometry(QtCore.QRect(290, 120, 113, 20))
        self.Can_Hw_Filter_Code_3.setObjectName(_fromUtf8("Can_Hw_Filter_Code_3"))
        #####################################################################################################

        #############################################################################################CanHardwareObject_4
        self.groupBox_10 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_10.setGeometry(QtCore.QRect(270, 0, 780, 700))
        self.groupBox_10.setStyleSheet(_fromUtf8("background-image: url(:/img/edited.jpg);"))
        self.groupBox_10.setObjectName(_fromUtf8("groupBox_4"))
        self.groupBox_10.setVisible(False)
        self.label_10000_4 = QtGui.QLabel(self.groupBox_10)
        self.label_10000_4.setGeometry(QtCore.QRect(30, 70, 181, 21))
        self.label_10000_4.setObjectName(_fromUtf8("label_10000_4"))
        self.label_20000_4 = QtGui.QLabel(self.groupBox_10)
        self.label_20000_4.setGeometry(QtCore.QRect(30, 120, 111, 16))
        self.label_20000_4.setObjectName(_fromUtf8("label_20000_4"))
        self.label_30000_4 = QtGui.QLabel(self.groupBox_10)
        self.label_30000_4.setGeometry(QtCore.QRect(30, 170, 91, 16))
        self.label_30000_4.setObjectName(_fromUtf8("label_30000_4"))
        self.label_40000_4 = QtGui.QLabel(self.groupBox_10)
        self.label_40000_4.setGeometry(QtCore.QRect(30, 220, 101, 16))
        self.label_40000_4.setObjectName(_fromUtf8("label_40000_4"))
        self.label_50000_4 = QtGui.QLabel(self.groupBox_10)
        self.label_50000_4.setGeometry(QtCore.QRect(30, 270, 91, 16))
        self.label_50000_4.setObjectName(_fromUtf8("label_50000_4"))
        self.label_60000_4 = QtGui.QLabel(self.groupBox_10)
        self.label_60000_4.setGeometry(QtCore.QRect(30, 320, 141, 16))
        self.label_60000_4.setObjectName(_fromUtf8("label_60000_4"))
        self.label_70000_4 = QtGui.QLabel(self.groupBox_10)
        self.label_70000_4.setGeometry(QtCore.QRect(30, 370, 141, 16))
        self.label_70000_4.setObjectName(_fromUtf8("label_70000_4"))
        self.Can_Object_Id_4 = QtGui.QLineEdit(self.groupBox_10)
        self.Can_Object_Id_4.setGeometry(QtCore.QRect(290, 70, 113, 20))
        self.Can_Object_Id_4.setObjectName(_fromUtf8("Can_Object_Id_4"))
        self.Can_Fd_Padding_Value_4 = QtGui.QLineEdit(self.groupBox_10)
        self.Can_Fd_Padding_Value_4.setGeometry(QtCore.QRect(290, 120, 113, 20))
        self.Can_Fd_Padding_Value_4.setObjectName(_fromUtf8("Can_Fd_Padding_Value_4"))
        self.Can_Object_Type_4 = QtGui.QComboBox(self.groupBox_10)
        self.Can_Object_Type_4.setGeometry(QtCore.QRect(290, 170, 111, 22))
        self.Can_Object_Type_4.setObjectName(_fromUtf8("Can_Object_Type_4"))
        self.Can_Object_Type_4.addItem('TRANSMIT')
        self.Can_Object_Type_4.addItem('RECEIVE')
        self.Can_HandleType_4= QtGui.QComboBox(self.groupBox_10)
        self.Can_HandleType_4.setGeometry(QtCore.QRect(290, 220, 111, 22))
        self.Can_HandleType_4.setObjectName(_fromUtf8("Can_HandleType_4"))
        self.Can_HandleType_4.addItem('BASIC')
        self.Can_HandleType_4.addItem('FULL')
        self.Can_Id_Type_4 = QtGui.QComboBox(self.groupBox_10)
        self.Can_Id_Type_4.setGeometry(QtCore.QRect(290, 270, 111, 22))
        self.Can_Id_Type_4.setObjectName(_fromUtf8("Can_Id_Type_4"))
        self.Can_Id_Type_4.addItem('STANDARD')
        self.Can_Id_Type_4.addItem('EXTENDED')
        self.Can_Id_Type_4.addItem('MIXED')
        self.Can_Trigger_Transmit_Enable_4 = QtGui.QCheckBox(self.groupBox_10)
        self.Can_Trigger_Transmit_Enable_4.setGeometry(QtCore.QRect(290, 320, 70, 17))
        self.Can_Trigger_Transmit_Enable_4.setText(_fromUtf8(""))
        self.Can_Trigger_Transmit_Enable_4.setObjectName(_fromUtf8("Can_Trigger_Transmit_Enable_4"))
        self.Can_Controller_ref_4 = QtGui.QComboBox(self.groupBox_10)
        self.Can_Controller_ref_4.setGeometry(QtCore.QRect(290, 370, 111, 22))
        self.Can_Controller_ref_4.setObjectName(_fromUtf8("Can_Controller_ref_4"))
        self.Can_Controller_ref_4.addItem('Controller 0')
        self.Can_Controller_ref_4.addItem('Controller 1')
        #######################################################################################################

        ##################################################################################CanHWFilter_4
        self.groupBox_11 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_11.setGeometry(QtCore.QRect(270, 0, 780, 700))
        self.groupBox_11.setStyleSheet(_fromUtf8("background-image: url(:/img/edited.jpg);"))
        self.groupBox_11.setObjectName(_fromUtf8("groupBox_11"))
        self.groupBox_11.setVisible(False)
        self.label_100000_4 = QtGui.QLabel(self.groupBox_11)
        self.label_100000_4.setGeometry(QtCore.QRect(30, 70, 181, 21))
        self.label_100000_4.setObjectName(_fromUtf8("label_100000_4"))
        self.label_200000_4 = QtGui.QLabel(self.groupBox_11)
        self.label_200000_4.setGeometry(QtCore.QRect(30, 120, 111, 16))
        self.label_200000_4.setObjectName(_fromUtf8("label_200000_4"))
        self.Can_Hw_Filter_Mask_4= QtGui.QLineEdit(self.groupBox_11)
        self.Can_Hw_Filter_Mask_4.setGeometry(QtCore.QRect(290, 70, 113, 20))
        self.Can_Hw_Filter_Mask_4.setObjectName(_fromUtf8("Can_Hw_Filter_Mask_4"))
        self.Can_Hw_Filter_Code_4 = QtGui.QLineEdit(self.groupBox_11)
        self.Can_Hw_Filter_Code_4.setGeometry(QtCore.QRect(290, 120, 113, 20))
        self.Can_Hw_Filter_Code_4.setObjectName(_fromUtf8("Can_Hw_Filter_Code_4"))
        #####################################################################################################

        
        
        CanTool.setCentralWidget(self.centralwidget)
        
        self.menubar = QtGui.QMenuBar(CanTool)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 751, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        CanTool.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(CanTool)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        CanTool.setStatusBar(self.statusbar)
        self.actionOpen = QtGui.QAction(CanTool)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        
        self.actionOpen.triggered.connect(self.file_open)
        
        self.actionSave_Changes = QtGui.QAction(CanTool)
        self.actionSave_Changes.setObjectName(_fromUtf8("actionSave_Changes"))
        self.actionSave_Changes.setEnabled(False)

        self.actionSave_Changes.triggered.connect(self.save_xml)


        self.actionExit = QtGui.QAction(CanTool)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionExit_2 = QtGui.QAction(CanTool)
        self.actionExit_2.setObjectName(_fromUtf8("actionExit_2"))
        self.actionGenerate_Header_file = QtGui.QAction(CanTool)
        self.actionGenerate_Header_file.setObjectName(_fromUtf8("actionGenerate_Header_file"))
        self.actionGenerate_Header_file.setEnabled(False)

        self.actionGenerate_Header_file.triggered.connect(self.Generate)


        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave_Changes)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit_2)
        self.menuEdit.addAction(self.actionGenerate_Header_file)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())


        ############################ dialog box ########################
        self.dlg =QtGui.QInputDialog()                 
        self.dlg.setInputMode( QtGui.QInputDialog.TextInput) 
        self.dlg.setLabelText("Please enter can object name")
        self.dlg.setWindowTitle('Warning')
        self.dlg.resize(300,200)
        
        

        self.treeWidget.connect(self.treeWidget, SIGNAL("itemClicked(QTreeWidgetItem*, int)"),self.choose)

        self.retranslateUi(CanTool)
        QtCore.QMetaObject.connectSlotsByName(CanTool)

    

    


    def retranslateUi(self, CanTool):
        CanTool.setWindowTitle(_translate("CanTool", "Can Tool", None))
        self.treeWidget.headerItem().setText(0, _translate("CanTool", "", None))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("CanTool", "Can", None))
        self.treeWidget.topLevelItem(0).child(0).setText(0, _translate("CanTool", "Can General", None))
        self.treeWidget.topLevelItem(0).child(0).child(0).setText(0, _translate("CanTool", "Can Main Function RW Periods", None))
        self.treeWidget.topLevelItem(0).child(1).setText(0, _translate("CanTool", "Can Configuration Set", None))
        self.treeWidget.topLevelItem(0).child(1).child(0).setText(0, _translate("CanTool", "Can Controllers", None))
        self.treeWidget.topLevelItem(0).child(1).child(1).setText(0, _translate("CanTool", "Can Hardware Objects", None))
        self.treeWidget.topLevelItem(0).child(1).child(1).child(0).setText(0, _translate("CanTool", "Can Hardware Object_1", None))
        self.treeWidget.topLevelItem(0).child(1).child(1).child(0).child(0).setText(0, _translate("CanTool", "Can Hw Filter_1", None))
        self.treeWidget.topLevelItem(0).child(1).child(1).child(1).setText(0, _translate("CanTool", "Can Hardware Object_2", None))
        self.treeWidget.topLevelItem(0).child(1).child(1).child(1).child(0).setText(0, _translate("CanTool", "Can Hw Filter_2", None))
        self.treeWidget.topLevelItem(0).child(1).child(1).child(2).setText(0, _translate("CanTool", "Can Hardware Object_3", None))
        self.treeWidget.topLevelItem(0).child(1).child(1).child(2).child(0).setText(0, _translate("CanTool", "Can Hw Filter_3", None))
        self.treeWidget.topLevelItem(0).child(1).child(1).child(3).setText(0, _translate("CanTool", "Can Hardware Object_4", None))
        self.treeWidget.topLevelItem(0).child(1).child(1).child(3).child(0).setText(0, _translate("CanTool", "Can Hw Filter_4", None))
        self.treeWidget.topLevelItem(0).child(1).child(0).child(0).setText(0, _translate("CanTool", "Can Controller_1", None))
        self.treeWidget.topLevelItem(0).child(1).child(0).child(0).child(0).setText(0, _translate("CanTool", "Can Controller Baudrate config1", None))
        self.treeWidget.topLevelItem(0).child(1).child(0).child(1).setText(0, _translate("CanTool", "Can Controller_2", None))
        self.treeWidget.topLevelItem(0).child(1).child(0).child(1).child(0).setText(0, _translate("CanTool", "Can Controller Baudrate config2", None))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.groupBox.setTitle(_translate("CanTool", "Can General", None))
        self.label.setText(_translate("CanTool", "Can Index", None))
        self.label_2.setText(_translate("CanTool", "Can Main Function Mode Period", None))
        self.label_3.setText(_translate("CanTool", "Can TimeOut Duration", None))
        self.label_4.setText(_translate("CanTool", "Can Main Function WakeUp Period", None))
        self.label_5.setText(_translate("CanTool", "Can Multiplexed Transmission", None))
        self.label_6.setText(_translate("CanTool", "Can Public Icom Support", None))
        self.label_7.setText(_translate("CanTool", "Can Set BaudRate API", None))
        self.label_8.setText(_translate("CanTool", "Can Version Info API", None))
        self.label_9.setText(_translate("CanTool", "Can Dev Error Detect", None))
        self.menuFile.setTitle(_translate("CanTool", "File", None))
        self.menuEdit.setTitle(_translate("CanTool", "Generate", None))
        self.actionOpen.setText(_translate("CanTool", "Open", None))
        self.actionSave_Changes.setText(_translate("CanTool", "Save Changes", None))
        self.actionExit.setText(_translate("CanTool", "Exit", None))
        self.actionExit_2.setText(_translate("CanTool", "Exit", None))
        self.actionGenerate_Header_file.setText(_translate("CanTool", "Generate Files", None))

        ###########################################################Can_Controller
        self.groupBox_2.setTitle(_translate("MainWindow", "Can Controller", None))
        self.label_10.setText(_translate("MainWindow", "Can Controller ID", None))
        self.label_20.setText(_translate("MainWindow", "Can Controller Base Address", None))
        self.label_30.setText(_translate("MainWindow", "Can Tx Processing", None))
        self.label_40.setText(_translate("MainWindow", "Can Rx Processing", None))
        self.label_50.setText(_translate("MainWindow", "Can Bus off Processing", None))
        self.label_60.setText(_translate("MainWindow", "Can Wakeup Processing", None))
        self.label_70.setText(_translate("MainWindow", "Can Controller Activation", None))
        self.label_80.setText(_translate("MainWindow", "Can Wakeup Support", None))
        self.label_90.setText(_translate("MainWindow", "Can Wakeup Functionality API", None))
        ##########################################################################################
        
        #######################################################################################CanControllerBaudRate
        self.groupBox_3.setTitle(_translate("MainWindow", "Can BaudRate Config", None))
        self.label_2000.setText(_translate("MainWindow", "Can Controller BaudRate", None))
        self.label_3000.setText(_translate("MainWindow", "Can Controller Prop Seg", None))
        self.label_4000.setText(_translate("MainWindow", "Can Controller Seg1", None))
        self.label_5000.setText(_translate("MainWindow", "Can Controller Seg2", None))
        self.label_1000.setText(_translate("MainWindow", "Can Controller BaudRate Config ID", None))
        self.label_6000.setText(_translate("MainWindow", "Can Controller Sync JumpWidth", None))
        ##################################################################################################

        ###########################################################Can_Controller2
        self.groupBox_12.setTitle(_translate("MainWindow", "Can Controller", None))
        self.label_10_2.setText(_translate("MainWindow", "Can Controller ID", None))
        self.label_20_2.setText(_translate("MainWindow", "Can Controller Base Address", None))
        self.label_30_2.setText(_translate("MainWindow", "Can Tx Processing", None))
        self.label_40_2.setText(_translate("MainWindow", "Can Rx Processing", None))
        self.label_50_2.setText(_translate("MainWindow", "Can Bus off Processing", None))
        self.label_60_2.setText(_translate("MainWindow", "Can Wakeup Processing", None))
        self.label_70_2.setText(_translate("MainWindow", "Can Controller Activation", None))
        self.label_80_2.setText(_translate("MainWindow", "Can Wakeup Support", None))
        self.label_90_2.setText(_translate("MainWindow", "Can Wakeup Functionality API", None))
        ##########################################################################################
        
        #######################################################################################CanController_2_BaudRate
        self.groupBox_13.setTitle(_translate("MainWindow", "Can BaudRate Config", None))
        self.label_2000_2.setText(_translate("MainWindow", "Can Controller BaudRate", None))
        self.label_3000_2.setText(_translate("MainWindow", "Can Controller Prop Seg", None))
        self.label_4000_2.setText(_translate("MainWindow", "Can Controller Seg1", None))
        self.label_5000_2.setText(_translate("MainWindow", "Can Controller Seg2", None))
        self.label_1000_2.setText(_translate("MainWindow", "Can Controller BaudRate Config ID", None))
        self.label_6000_2.setText(_translate("MainWindow", "Can Controller Sync JumpWidth", None))
        ##################################################################################################

        #########################################################################################CanHardwareObject_1
        self.groupBox_4.setTitle(_translate("MainWindow", "Can Hardware Object", None))
        self.label_10000_1.setText(_translate("MainWindow", "Can Object ID", None))
        self.label_20000_1.setText(_translate("MainWindow", "Can Fd Padding Value", None))
        self.label_30000_1.setText(_translate("MainWindow", "Can Object Type", None))
        self.label_40000_1.setText(_translate("MainWindow", "Can Handle Type", None))
        self.label_50000_1.setText(_translate("MainWindow", "Can ID Type", None))
        self.label_60000_1.setText(_translate("MainWindow", "Can Trigger Transmit Enable", None))
        self.label_70000_1.setText(_translate("MainWindow", "Can Controller Ref", None))
        ################################################################################################

        #########################################################################################CanHWFilter_1
        self.groupBox_5.setTitle(_translate("MainWindow", "Can Hw Filter", None))
        self.label_100000_1.setText(_translate("MainWindow", "Can Hw Filter Mask", None))
        self.label_200000_1.setText(_translate("MainWindow", "Can Hw Filter Code", None))
        #############################################################################################
        
        #########################################################################################CanHardwareObject_2
        self.groupBox_6.setTitle(_translate("MainWindow", "Can Hardware Object", None))
        self.label_10000_2.setText(_translate("MainWindow", "Can Object ID", None))
        self.label_20000_2.setText(_translate("MainWindow", "Can Fd Padding Value", None))
        self.label_30000_2.setText(_translate("MainWindow", "Can Object Type", None))
        self.label_40000_2.setText(_translate("MainWindow", "Can Handle Type", None))
        self.label_50000_2.setText(_translate("MainWindow", "Can ID Type", None))
        self.label_60000_2.setText(_translate("MainWindow", "Can Trigger Transmit Enable", None))
        self.label_70000_2.setText(_translate("MainWindow", "Can Controller Ref", None))

        ################################################################################################

        #########################################################################################CanHWFilter_2
        self.groupBox_7.setTitle(_translate("MainWindow", "Can Hw Filter", None))
        self.label_100000_2.setText(_translate("MainWindow", "Can Hw Filter Mask", None))
        self.label_200000_2.setText(_translate("MainWindow", "Can Hw Filter Code", None))
        #############################################################################################

        #########################################################################################CanHardwareObject_3
        self.groupBox_8.setTitle(_translate("MainWindow", "Can Hardware Object", None))
        self.label_10000_3.setText(_translate("MainWindow", "Can Object ID", None))
        self.label_20000_3.setText(_translate("MainWindow", "Can Fd Padding Value", None))
        self.label_30000_3.setText(_translate("MainWindow", "Can Object Type", None))
        self.label_40000_3.setText(_translate("MainWindow", "Can Handle Type", None))
        self.label_50000_3.setText(_translate("MainWindow", "Can ID Type", None))
        self.label_60000_3.setText(_translate("MainWindow", "Can Trigger Transmit Enable", None))
        self.label_70000_3.setText(_translate("MainWindow", "Can Controller Ref", None))

        ################################################################################################

        #########################################################################################CanHWFilter_3
        self.groupBox_9.setTitle(_translate("MainWindow", "Can Hw Filter", None))
        self.label_100000_3.setText(_translate("MainWindow", "Can Hw Filter Mask", None))
        self.label_200000_3.setText(_translate("MainWindow", "Can Hw Filter Code", None))
        #############################################################################################

        #########################################################################################CanHardwareObject_4
        self.groupBox_10.setTitle(_translate("MainWindow", "Can Hardware Object", None))
        self.label_10000_4.setText(_translate("MainWindow", "Can Object ID", None))
        self.label_20000_4.setText(_translate("MainWindow", "Can Fd Padding Value", None))
        self.label_30000_4.setText(_translate("MainWindow", "Can Object Type", None))
        self.label_40000_4.setText(_translate("MainWindow", "Can Handle Type", None))
        self.label_50000_4.setText(_translate("MainWindow", "Can ID Type", None))
        self.label_60000_4.setText(_translate("MainWindow", "Can Trigger Transmit Enable", None))
        self.label_70000_4.setText(_translate("MainWindow", "Can Controller Ref", None))

        ################################################################################################

        #########################################################################################CanHWFilter_4
        self.groupBox_11.setTitle(_translate("MainWindow", "Can Hw Filter", None))
        self.label_100000_4.setText(_translate("MainWindow", "Can Hw Filter Mask", None))
        self.label_200000_4.setText(_translate("MainWindow", "Can Hw Filter Code", None))
        #############################################################################################
        
    def file_open(self):
        self.actionSave_Changes.setEnabled(True)
        self.actionGenerate_Header_file.setEnabled(True)
        path = QtGui.QFileDialog.getOpenFileName(None,'Open File')
        self.path_1 =path
        parser = Module(path)
        self.read_inputs(parser.GetValue('CanIndex'),parser.GetValue('CanMainFunctionModePeriod'),\
        parser.GetValue('CanMainFunctionWakeupPeriod'),parser.GetValue('CanTimeoutDuration'),\
        check(parser.GetValue('CanMultiplexedTransmission')),check(parser.GetValue('CanPublicIcomSupport')),\
        check(parser.GetValue('CanSetBaudrateApi')),check(parser.GetValue('CanVersionInfoApi')),\
        check(parser.GetValue('CanDevErrorDetect')),parser.GetValue('CanControllerId_1'),\
        parser.GetValue('CanControllerBaseAddress_1'),parser.GetValue('CanTxProcessing_1'),\
        parser.GetValue('CanRxProcessing_1'),parser.GetValue('CanBusoffProcessing_1'),parser.GetValue('CanWakeupProcessing_1'),\
        check(parser.GetValue('CanControllerActivation_1')),check(parser.GetValue('CanWakeupSupport_1')),\
        check(parser.GetValue('CanWakeupFunctionalityAPI_1')),parser.GetValue('CanControllerId_2'),\
        parser.GetValue('CanControllerBaseAddress_2'),parser.GetValue('CanTxProcessing_2'),\
        parser.GetValue('CanRxProcessing_2'),parser.GetValue('CanBusoffProcessing_2'),parser.GetValue('CanWakeupProcessing_2'),\
        check(parser.GetValue('CanControllerActivation_2')),check(parser.GetValue('CanWakeupSupport_2')),\
        check(parser.GetValue('CanWakeupFunctionalityAPI_2')),parser.GetValue('CanControllerBaudRateConfigID_1'),\
        parser.GetValue('CanControllerBaudRate_1'),parser.GetValue('CanControllerPropSeg_1'),\
        parser.GetValue('CanControllerSeg1_1'),parser.GetValue('CanControllerSeg2_1'),parser.GetValue('CanControllerSyncJumpWidth_1'),\
        parser.GetValue('CanControllerBaudRateConfigID_2'),parser.GetValue('CanControllerBaudRate_2'),\
        parser.GetValue('CanControllerPropSeg_2'),parser.GetValue('CanControllerSeg1_2'),parser.GetValue('CanControllerSeg2_2'),\
        parser.GetValue('CanControllerSyncJumpWidth_2'),parser.GetValue('CanObjectId_1'),parser.GetValue('CanFdPaddingValue_1'),\
        parser.GetValue('CanObjectType_1'),parser.GetValue('CanHandleType_1'),parser.GetValue('CanIdType_1'),\
        check(parser.GetValue('CanTriggerTransmitEnable_1')),parser.GetValue('CanControllerRef_1'),parser.GetValue('CanObjectId_2'),parser.GetValue('CanFdPaddingValue_2'),\
        parser.GetValue('CanObjectType_2'),parser.GetValue('CanHandleType_2'),parser.GetValue('CanIdType_2'),\
        check(parser.GetValue('CanTriggerTransmitEnable_2')),parser.GetValue('CanControllerRef_2'),parser.GetValue('CanObjectId_3'),parser.GetValue('CanFdPaddingValue_3'),\
        parser.GetValue('CanObjectType_3'),parser.GetValue('CanHandleType_3'),parser.GetValue('CanIdType_3'),\
        check(parser.GetValue('CanTriggerTransmitEnable_3')),parser.GetValue('CanControllerRef_3'),parser.GetValue('CanObjectId_4'),parser.GetValue('CanFdPaddingValue_4'),\
        parser.GetValue('CanObjectType_4'),parser.GetValue('CanHandleType_4'),parser.GetValue('CanIdType_4'),\
        check(parser.GetValue('CanTriggerTransmitEnable_4')),parser.GetValue('CanControllerRef_4'),parser.GetValue('CanHwFilterMask_1'),parser.GetValue('CanHwFilterCode_1'),\
        parser.GetValue('CanHwFilterMask_2'),parser.GetValue('CanHwFilterCode_2'),parser.GetValue('CanHwFilterMask_3'),\
        parser.GetValue('CanHwFilterCode_3'),parser.GetValue('CanHwFilterMask_4'),parser.GetValue('CanHwFilterCode_4'))




    def choose(self):
        selected_item=self.treeWidget.selectedItems()
        base_node=selected_item[0]
        getchild=base_node.text(0)
        if(getchild == "Can General"):
            self.groupBox.setVisible(True)
            self.groupBox_2.setVisible(False)
            self.groupBox_3.setVisible(False)
            self.groupBox_4.setVisible(False)
            self.groupBox_5.setVisible(False)
            self.groupBox_6.setVisible(False)
            self.groupBox_7.setVisible(False)
            self.groupBox_8.setVisible(False)
            self.groupBox_9.setVisible(False)
            self.groupBox_10.setVisible(False)
            self.groupBox_11.setVisible(False)
            self.groupBox_12.setVisible(False)
            self.groupBox_13.setVisible(False)
        if(getchild == "Can Controller_1"):
            self.groupBox_2.setVisible(True)
            self.groupBox.setVisible(False)
            self.groupBox_3.setVisible(False)
            self.groupBox_4.setVisible(False)
            self.groupBox_5.setVisible(False)
            self.groupBox_6.setVisible(False)
            self.groupBox_7.setVisible(False)
            self.groupBox_8.setVisible(False)
            self.groupBox_9.setVisible(False)
            self.groupBox_10.setVisible(False)
            self.groupBox_11.setVisible(False)
            self.groupBox_12.setVisible(False)
            self.groupBox_13.setVisible(False)
        if(getchild == "Can Controller Baudrate config1"):
            self.groupBox_3.setVisible(True)
            self.groupBox_2.setVisible(False)
            self.groupBox.setVisible(False)
            self.groupBox_4.setVisible(False)
            self.groupBox_5.setVisible(False)
            self.groupBox_6.setVisible(False)
            self.groupBox_7.setVisible(False)
            self.groupBox_8.setVisible(False)
            self.groupBox_9.setVisible(False)
            self.groupBox_10.setVisible(False)
            self.groupBox_11.setVisible(False)
            self.groupBox_12.setVisible(False)
            self.groupBox_13.setVisible(False)

        if(getchild == "Can Controller_2"):
            self.groupBox_12.setVisible(True)
            self.groupBox_11.setVisible(False)
            self.groupBox_2.setVisible(False)
            self.groupBox.setVisible(False)
            self.groupBox_3.setVisible(False)
            self.groupBox_4.setVisible(False)
            self.groupBox_5.setVisible(False)
            self.groupBox_6.setVisible(False)
            self.groupBox_7.setVisible(False)
            self.groupBox_8.setVisible(False)
            self.groupBox_9.setVisible(False)
            self.groupBox_10.setVisible(False) 
            self.groupBox_13.setVisible(False)
        if(getchild == "Can Controller Baudrate config2"):
            self.groupBox_13.setVisible(True)
            self.groupBox_12.setVisible(False)
            self.groupBox_3.setVisible(False)
            self.groupBox_2.setVisible(False)
            self.groupBox.setVisible(False)
            self.groupBox_4.setVisible(False)
            self.groupBox_5.setVisible(False)
            self.groupBox_6.setVisible(False)
            self.groupBox_7.setVisible(False)
            self.groupBox_8.setVisible(False)
            self.groupBox_9.setVisible(False)
            self.groupBox_10.setVisible(False)
            self.groupBox_11.setVisible(False)
        if(getchild == "Can Hardware Object_1"):
            self.groupBox_4.setVisible(True)
            self.groupBox_3.setVisible(False)
            self.groupBox_2.setVisible(False)
            self.groupBox.setVisible(False)
            self.groupBox_5.setVisible(False)
            self.groupBox_6.setVisible(False)
            self.groupBox_7.setVisible(False)
            self.groupBox_8.setVisible(False)
            self.groupBox_9.setVisible(False)
            self.groupBox_10.setVisible(False)
            self.groupBox_11.setVisible(False)
            self.groupBox_12.setVisible(False)
            self.groupBox_13.setVisible(False)
        if(getchild == "Can Hw Filter_1"):
            self.groupBox_5.setVisible(True)
            self.groupBox_4.setVisible(False)
            self.groupBox_3.setVisible(False)
            self.groupBox_2.setVisible(False)
            self.groupBox.setVisible(False)
            self.groupBox_6.setVisible(False)
            self.groupBox_7.setVisible(False)
            self.groupBox_8.setVisible(False)
            self.groupBox_9.setVisible(False)
            self.groupBox_10.setVisible(False)
            self.groupBox_11.setVisible(False)
            self.groupBox_12.setVisible(False)
            self.groupBox_13.setVisible(False)
        if(getchild == "Can Hardware Object_2"):
            self.groupBox_6.setVisible(True)
            self.groupBox_4.setVisible(False)
            self.groupBox_3.setVisible(False)
            self.groupBox_2.setVisible(False)
            self.groupBox.setVisible(False)
            self.groupBox_5.setVisible(False)
            self.groupBox_7.setVisible(False)
            self.groupBox_8.setVisible(False)
            self.groupBox_9.setVisible(False)
            self.groupBox_10.setVisible(False)
            self.groupBox_11.setVisible(False)
            self.groupBox_12.setVisible(False)
            self.groupBox_13.setVisible(False)
        if(getchild == "Can Hw Filter_2"):
            self.groupBox_7.setVisible(True)
            self.groupBox_5.setVisible(False)
            self.groupBox_4.setVisible(False)
            self.groupBox_3.setVisible(False)
            self.groupBox_2.setVisible(False)
            self.groupBox.setVisible(False)
            self.groupBox_6.setVisible(False)
            self.groupBox_8.setVisible(False)
            self.groupBox_9.setVisible(False)
            self.groupBox_10.setVisible(False)
            self.groupBox_11.setVisible(False)
            self.groupBox_12.setVisible(False)
            self.groupBox_13.setVisible(False)
        if(getchild == "Can Hardware Object_3"):
            self.groupBox_8.setVisible(True)
            self.groupBox_6.setVisible(False)
            self.groupBox_4.setVisible(False)
            self.groupBox_3.setVisible(False)
            self.groupBox_2.setVisible(False)
            self.groupBox.setVisible(False)
            self.groupBox_5.setVisible(False)
            self.groupBox_7.setVisible(False)
            self.groupBox_9.setVisible(False)
            self.groupBox_10.setVisible(False)
            self.groupBox_11.setVisible(False)
            self.groupBox_12.setVisible(False)
            self.groupBox_13.setVisible(False)
        if(getchild == "Can Hw Filter_3"):
            self.groupBox_9.setVisible(True)
            self.groupBox_7.setVisible(False)
            self.groupBox_5.setVisible(False)
            self.groupBox_4.setVisible(False)
            self.groupBox_3.setVisible(False)
            self.groupBox_2.setVisible(False)
            self.groupBox.setVisible(False)
            self.groupBox_6.setVisible(False)
            self.groupBox_8.setVisible(False)
            self.groupBox_10.setVisible(False)
            self.groupBox_11.setVisible(False)
            self.groupBox_12.setVisible(False)
            self.groupBox_13.setVisible(False)
        if(getchild == "Can Hardware Object_4"):
            self.groupBox_10.setVisible(True)
            self.groupBox_8.setVisible(False)
            self.groupBox_6.setVisible(False)
            self.groupBox_4.setVisible(False)
            self.groupBox_3.setVisible(False)
            self.groupBox_2.setVisible(False)
            self.groupBox.setVisible(False)
            self.groupBox_5.setVisible(False)
            self.groupBox_7.setVisible(False)
            self.groupBox_9.setVisible(False)
            self.groupBox_11.setVisible(False)
            self.groupBox_12.setVisible(False)
            self.groupBox_13.setVisible(False)
        if(getchild == "Can Hw Filter_4"):
            self.groupBox_11.setVisible(True)
            self.groupBox_9.setVisible(False)
            self.groupBox_7.setVisible(False)
            self.groupBox_5.setVisible(False)
            self.groupBox_4.setVisible(False)
            self.groupBox_3.setVisible(False)
            self.groupBox_2.setVisible(False)
            self.groupBox.setVisible(False)
            self.groupBox_6.setVisible(False)
            self.groupBox_8.setVisible(False)
            self.groupBox_10.setVisible(False)
            self.groupBox_12.setVisible(False)
            self.groupBox_13.setVisible(False)
            
            
            

    def read_inputs(self,Can_index='',Can_MainFunctionModePeriod='',Can_MainFunctionWakeUpPeriod='',Can_TimeoutDuration='',\
    Can_MultiplexedTransmission=False,Can_PublicIcomSupport=False,Can_SetBaudrateApi=False,Can_VersionInfoApi=False,\
    Can_DevErrorDetect=False,Can_Controller_ID='',Can_Controller_Base_Address='',Can_Tx_Processing='',Can_Rx_Processing='',\
    can_bus_off='',can_wakeup='',can_controller_activation=False,can_wakeup_support=False,can_wakeup_API=False,\
    Can_Controller_ID_2='',Can_Controller_Base_Address_2='',Can_Tx_Processing_2='',Can_Rx_Processing_2='',\
    can_bus_off_2='',can_wakeup_2='',can_controller_activation_2=False,can_wakeup_support_2=False,can_wakeup_API_2=False,\
    BaudRate_config_ID='',BaudRate='',Prop_seg='',Prop_seg1='',Prop_seg2='',Sync_jumpwidth='',BaudRate_config_ID_2='',\
    BaudRate_2='',Prop_seg_2='',Prop_seg1_2='',Prop_seg2_2='',Sync_jumpwidth_2='',\
    Can_Object_Id_1='',Can_Fd_Padding_Value_1='',Can_Object_Type_1='',Can_HandleType_1='',Can_Id_Type_1='',Can_Trigger_Transmit_Enable_1=False,CanControllerRef_1='',\
    Can_Object_Id_2='',Can_Fd_Padding_Value_2='',Can_Object_Type_2='',Can_HandleType_2='',Can_Id_Type_2='',Can_Trigger_Transmit_Enable_2=False,CanControllerRef_2='',\
    Can_Object_Id_3='',Can_Fd_Padding_Value_3='',Can_Object_Type_3='',Can_HandleType_3='',Can_Id_Type_3='',Can_Trigger_Transmit_Enable_3=False,CanControllerRef_3='',\
    Can_Object_Id_4='',Can_Fd_Padding_Value_4='',Can_Object_Type_4='',Can_HandleType_4='',Can_Id_Type_4='',Can_Trigger_Transmit_Enable_4=False,CanControllerRef_4='',\
    Can_Hw_Filter_Mask_1='',Can_Hw_Filter_Code_1='',Can_Hw_Filter_Mask_2='',Can_Hw_Filter_Code_2='',\
    Can_Hw_Filter_Mask_3='',Can_Hw_Filter_Code_3='',Can_Hw_Filter_Mask_4='',Can_Hw_Filter_Code_4=''):
        self.Can_Index.setText(str(Can_index))
        self.Can_main_fn_Mode_period.setText(str(Can_MainFunctionModePeriod))
        self.Can_Timeout_Duration.setText(str(Can_TimeoutDuration))
        self.Can_Main_Fn_Wakeup.setText(str(Can_MainFunctionWakeUpPeriod))
        self.Can_mul_transmission.setChecked(Can_MultiplexedTransmission)
        self.Can_Public_icom_support.setChecked(Can_PublicIcomSupport)
        self.Can_Set_baudrate_API.setChecked(Can_SetBaudrateApi)
        self.Can_version_info.setChecked(Can_VersionInfoApi)
        self.Can_Dev_error.setChecked(Can_DevErrorDetect)

        ########################## show in Can controller 1 group box ################################
        self.Can_Controller_ID.setText(Can_Controller_ID)
        self.Can_Controller_Base_Address.setText(Can_Controller_Base_Address)
        self.Can_Tx_Processing.setCurrentIndex(self.Can_Tx_Processing.findText(Can_Tx_Processing, QtCore.Qt.MatchFixedString))
        self.Can_Rx_Processing.setCurrentIndex(self.Can_Rx_Processing.findText(Can_Rx_Processing,QtCore.Qt.MatchFixedString))
        self.can_bus_off.setCurrentIndex(self.can_bus_off.findText(can_bus_off,QtCore.Qt.MatchFixedString))
        self.can_wakeup.setCurrentIndex(self.can_wakeup.findText(can_wakeup,QtCore.Qt.MatchFixedString))
        self.can_controller_activation.setChecked(can_controller_activation)
        self.can_wakeup_support.setChecked(can_wakeup_support)
        self.can_wakeup_API.setChecked(can_wakeup_API)

        ########################## show in Can BauseRate Config 1 #####################################

        self.BaudRate_config_ID.setText(BaudRate_config_ID)
        self.BaudRate.setText(BaudRate)
        self.Prop_seg.setText(Prop_seg)
        self.Prop_seg1.setText(Prop_seg1)
        self.Prop_seg2.setText(Prop_seg2)
        self.Sync_jumpwidth.setText(Sync_jumpwidth)

        ########################## show in Can controller 2 group box ##################################
        self.Can_Controller_ID_2.setText(Can_Controller_ID_2)
        self.Can_Controller_Base_Address_2.setText(Can_Controller_Base_Address_2)
        self.Can_Tx_Processing_2.setCurrentIndex(self.Can_Tx_Processing_2.findText(Can_Tx_Processing_2, QtCore.Qt.MatchFixedString))
        self.Can_Rx_Processing_2.setCurrentIndex(self.Can_Rx_Processing_2.findText(Can_Rx_Processing_2,QtCore.Qt.MatchFixedString))
        self.can_bus_off_2.setCurrentIndex(self.can_bus_off_2.findText(can_bus_off_2,QtCore.Qt.MatchFixedString))
        self.can_wakeup_2.setCurrentIndex(self.can_wakeup_2.findText(can_wakeup_2,QtCore.Qt.MatchFixedString))
        self.can_controller_activation_2.setChecked(can_controller_activation_2)
        self.can_wakeup_support_2.setChecked(can_wakeup_support_2)
        self.can_wakeup_API_2.setChecked(can_wakeup_API_2)

        ########################## show in Can BauseRate Config 2 #####################################

        self.BaudRate_config_ID_2.setText(BaudRate_config_ID_2)
        self.BaudRate_2.setText(BaudRate_2)
        self.Prop_seg_2.setText(Prop_seg_2)
        self.Prop_seg1_2.setText(Prop_seg1_2)
        self.Prop_seg2_2.setText(Prop_seg2_2)
        self.Sync_jumpwidth_2.setText(Sync_jumpwidth_2)

        ########################## show Can Hardware object 1 #########################################

        self.Can_Object_Id_1.setText(Can_Object_Id_1)
        self.Can_Fd_Padding_Value_1.setText(Can_Fd_Padding_Value_1)
        self.Can_Object_Type_1.setCurrentIndex(self.Can_Object_Type_1.findText(Can_Object_Type_1,QtCore.Qt.MatchFixedString))
        self.Can_HandleType_1.setCurrentIndex(self.Can_HandleType_1.findText(Can_HandleType_1,QtCore.Qt.MatchFixedString))
        self.Can_Id_Type_1.setCurrentIndex(self.Can_Id_Type_1.findText(Can_Id_Type_1,QtCore.Qt.MatchFixedString))
        self.Can_Trigger_Transmit_Enable_1.setChecked(Can_Trigger_Transmit_Enable_1)
        self.Can_Controller_ref_1.setCurrentIndex(self.Can_Controller_ref_1.findText(CanControllerRef_1,QtCore.Qt.MatchFixedString))

        ########################## show Can Hardware filter 1 #########################################
        self.Can_Hw_Filter_Mask_1.setText(Can_Hw_Filter_Mask_1)
        self.Can_Hw_Filter_Code_1.setText(Can_Hw_Filter_Code_1)

        ########################## show Can Hardware object 2 #########################################

        self.Can_Object_Id_2.setText(Can_Object_Id_2)
        self.Can_Fd_Padding_Value_2.setText(Can_Fd_Padding_Value_2)
        self.Can_Object_Type_2.setCurrentIndex(self.Can_Object_Type_2.findText(Can_Object_Type_2,QtCore.Qt.MatchFixedString))
        self.Can_HandleType_2.setCurrentIndex(self.Can_HandleType_2.findText(Can_HandleType_2,QtCore.Qt.MatchFixedString))
        self.Can_Id_Type_2.setCurrentIndex(self.Can_Id_Type_2.findText(Can_Id_Type_2,QtCore.Qt.MatchFixedString))
        self.Can_Trigger_Transmit_Enable_2.setChecked(Can_Trigger_Transmit_Enable_2)
        self.Can_Controller_ref_2.setCurrentIndex(self.Can_Controller_ref_2.findText(CanControllerRef_2,QtCore.Qt.MatchFixedString))


        ########################## show Can Hardware filter 2 #########################################
        self.Can_Hw_Filter_Mask_2.setText(Can_Hw_Filter_Mask_2)
        self.Can_Hw_Filter_Code_2.setText(Can_Hw_Filter_Code_2)

        ########################## show Can Hardware object 3 #########################################

        self.Can_Object_Id_3.setText(Can_Object_Id_3)
        self.Can_Fd_Padding_Value_3.setText(Can_Fd_Padding_Value_3)
        self.Can_Object_Type_3.setCurrentIndex(self.Can_Object_Type_3.findText(Can_Object_Type_3,QtCore.Qt.MatchFixedString))
        self.Can_HandleType_3.setCurrentIndex(self.Can_HandleType_3.findText(Can_HandleType_3,QtCore.Qt.MatchFixedString))
        self.Can_Id_Type_3.setCurrentIndex(self.Can_Id_Type_3.findText(Can_Id_Type_3,QtCore.Qt.MatchFixedString))
        self.Can_Trigger_Transmit_Enable_3.setChecked(Can_Trigger_Transmit_Enable_3)
        self.Can_Controller_ref_3.setCurrentIndex(self.Can_Controller_ref_3.findText(CanControllerRef_3,QtCore.Qt.MatchFixedString))


        ########################## show Can Hardware filter 3 #########################################
        self.Can_Hw_Filter_Mask_3.setText(Can_Hw_Filter_Mask_3)
        self.Can_Hw_Filter_Code_3.setText(Can_Hw_Filter_Code_3)

        ########################## show Can Hardware object 4 #########################################

        self.Can_Object_Id_4.setText(Can_Object_Id_4)
        self.Can_Fd_Padding_Value_4.setText(Can_Fd_Padding_Value_4)
        self.Can_Object_Type_4.setCurrentIndex(self.Can_Object_Type_4.findText(Can_Object_Type_4,QtCore.Qt.MatchFixedString))
        self.Can_HandleType_4.setCurrentIndex(self.Can_HandleType_4.findText(Can_HandleType_4,QtCore.Qt.MatchFixedString))
        self.Can_Id_Type_4.setCurrentIndex(self.Can_Id_Type_4.findText(Can_Id_Type_4,QtCore.Qt.MatchFixedString))
        self.Can_Trigger_Transmit_Enable_4.setChecked(Can_Trigger_Transmit_Enable_4)
        self.Can_Controller_ref_4.setCurrentIndex(self.Can_Controller_ref_4.findText(CanControllerRef_4,QtCore.Qt.MatchFixedString))


        ########################## show Can Hardware filter 4 #########################################
        self.Can_Hw_Filter_Mask_4.setText(Can_Hw_Filter_Mask_4)
        self.Can_Hw_Filter_Code_4.setText(Can_Hw_Filter_Code_4)


    def save_xml(self):
        parser = Module(self.path_1)
        parser.Modify("CanIndex",str(self.Can_Index.text()))
        parser.Modify("CanMainFunctionModePeriod",str(self.Can_main_fn_Mode_period.text()))
        parser.Modify("CanTimeoutDuration",str(self.Can_Timeout_Duration.text()))
        parser.Modify("CanMainFunctionWakeupPeriod",str(self.Can_Main_Fn_Wakeup.text()))
        parser.Modify("CanMultiplexedTransmission",str(self.Can_mul_transmission.isChecked()))
        parser.Modify("CanPublicIcomSupport",str(self.Can_Public_icom_support.isChecked()))
        parser.Modify("CanSetBaudrateApi",str(self.Can_Set_baudrate_API.isChecked()))
        parser.Modify("CanVersionInfoApi",str(self.Can_version_info.isChecked()))
        parser.Modify("CanDevErrorDetect",str(self.Can_Dev_error.isChecked()))

        ########################## save in Can controller_1_XML_region ################################
        parser.Modify("CanControllerId_1",str(self.Can_Controller_ID.text()))
        parser.Modify("CanControllerActivation_1",str(self.can_controller_activation.isChecked()))
        parser.Modify("CanControllerBaseAddress_1",str(self.Can_Controller_Base_Address.text()))
        parser.Modify("CanWakeupSupport_1",str(self.can_wakeup_support.isChecked()))
        parser.Modify("CanWakeupFunctionalityAPI_1",str(self.can_wakeup_API.isChecked()))
        parser.Modify("CanTxProcessing_1",str(self.Can_Tx_Processing.currentText()))
        parser.Modify("CanRxProcessing_1",str(self.Can_Rx_Processing.currentText()))
        parser.Modify("CanBusoffProcessing_1",str(self.can_bus_off.currentText()))
        parser.Modify("CanWakeupProcessing_1",str(self.can_wakeup.currentText()))

        ##########################save in CanContollerBaudRate_1_XML_region#################################
        parser.Modify("CanControllerBaudRate_1",str(self.BaudRate.text()))
        parser.Modify("CanControllerPropSeg_1",str(self.Prop_seg.text()))
        parser.Modify("CanControllerSeg1_1",str(self.Prop_seg1.text()))
        parser.Modify("CanControllerSeg2_1",str(self.Prop_seg2.text()))
        parser.Modify("CanControllerSyncJumpWidth_1",str(self.Sync_jumpwidth.text()))
        parser.Modify("CanControllerBaudRateConfigID_1",str(self.BaudRate_config_ID.text()))

        ########################## save in Can controller_2_XML_region ####################################
        parser.Modify("CanControllerId_2",str(self.Can_Controller_ID_2.text()))
        parser.Modify("CanControllerActivation_2",str(self.can_controller_activation_2.isChecked()))
        parser.Modify("CanControllerBaseAddress_2",str(self.Can_Controller_Base_Address_2.text()))
        parser.Modify("CanWakeupSupport_2",str(self.can_wakeup_support_2.isChecked()))
        parser.Modify("CanWakeupFunctionalityAPI_2",str(self.can_wakeup_API_2.isChecked()))
        parser.Modify("CanTxProcessing_2",str(self.Can_Tx_Processing_2.currentText()))
        parser.Modify("CanRxProcessing_2",str(self.Can_Rx_Processing_2.currentText()))
        parser.Modify("CanBusoffProcessing_2",str(self.can_bus_off_2.currentText()))
        parser.Modify("CanWakeupProcessing_2",str(self.can_wakeup.currentText()))

        ##########################save in CanContollerBaudRate_2_XML_region#################################
        parser.Modify("CanControllerBaudRate_2",str(self.BaudRate_2.text()))
        parser.Modify("CanControllerPropSeg_2",str(self.Prop_seg_2.text()))
        parser.Modify("CanControllerSeg1_2",str(self.Prop_seg1_2.text()))
        parser.Modify("CanControllerSeg2_2",str(self.Prop_seg2_2.text()))
        parser.Modify("CanControllerSyncJumpWidth_2",str(self.Sync_jumpwidth_2.text()))
        parser.Modify("CanControllerBaudRateConfigID_2",str(self.BaudRate_config_ID_2.text()))

        ##########################save in CanHWObject_1_XML_region##########################################
        parser.Modify("CanHandleType_1",str(self.Can_HandleType_1.currentText()))
        parser.Modify("CanObjectType_1",str(self.Can_Object_Type_1.currentText()))
        parser.Modify("CanIdType_1",str(self.Can_Id_Type_1.currentText()))
        parser.Modify("CanObjectId_1",str(self.Can_Object_Id_1.text()))
        parser.Modify("CanFdPaddingValue_1",str(self.Can_Fd_Padding_Value_1.text()))
        parser.Modify("CanTriggerTransmitEnable_1",str(self.Can_Trigger_Transmit_Enable_1.isChecked()))
        parser.Modify('CanControllerRef_1',str(self.Can_Controller_ref_1.currentText()))

        ##########################save in CanHWFilter_1_XML_region##########################################
        parser.Modify("CanHwFilterMask_1",str(self.Can_Hw_Filter_Mask_1.text()))
        parser.Modify("CanHwFilterCode_1",str(self.Can_Hw_Filter_Code_1.text()))

        ##########################save in CanHWObject_2_XML_region##########################################
        parser.Modify("CanHandleType_2",str(self.Can_HandleType_2.currentText()))
        parser.Modify("CanObjectType_2",str(self.Can_Object_Type_2.currentText()))
        parser.Modify("CanIdType_2",str(self.Can_Id_Type_2.currentText()))
        parser.Modify("CanObjectId_2",str(self.Can_Object_Id_2.text()))
        parser.Modify("CanFdPaddingValue_2",str(self.Can_Fd_Padding_Value_2.text()))
        parser.Modify("CanTriggerTransmitEnable_2",str(self.Can_Trigger_Transmit_Enable_2.isChecked()))
        parser.Modify('CanControllerRef_2',str(self.Can_Controller_ref_2.currentText()))


        ##########################save in CanHWFilter_2_XML_region##########################################
        parser.Modify("CanHwFilterMask_2",str(self.Can_Hw_Filter_Mask_2.text()))
        parser.Modify("CanHwFilterCode_2",str(self.Can_Hw_Filter_Code_2.text()))

        ##########################save in CanHWObject_3_XML_region##########################################
        parser.Modify("CanHandleType_3",str(self.Can_HandleType_3.currentText()))
        parser.Modify("CanObjectType_3",str(self.Can_Object_Type_3.currentText()))
        parser.Modify("CanIdType_3",str(self.Can_Id_Type_3.currentText()))
        parser.Modify("CanObjectId_3",str(self.Can_Object_Id_3.text()))
        parser.Modify("CanFdPaddingValue_3",str(self.Can_Fd_Padding_Value_3.text()))
        parser.Modify("CanTriggerTransmitEnable_3",str(self.Can_Trigger_Transmit_Enable_3.isChecked()))
        parser.Modify('CanControllerRef_3',str(self.Can_Controller_ref_3.currentText()))

        ##########################save in CanHWFilter_3_XML_region##########################################
        parser.Modify("CanHwFilterMask_3",str(self.Can_Hw_Filter_Mask_3.text()))
        parser.Modify("CanHwFilterCode_3",str(self.Can_Hw_Filter_Code_3.text()))

        ##########################save in CanHWObject_4_XML_region##########################################
        parser.Modify("CanHandleType_4",str(self.Can_HandleType_4.currentText()))
        parser.Modify("CanObjectType_4",str(self.Can_Object_Type_4.currentText()))
        parser.Modify("CanIdType_4",str(self.Can_Id_Type_4.currentText()))
        parser.Modify("CanObjectId_4",str(self.Can_Object_Id_4.text()))
        parser.Modify("CanFdPaddingValue_4",str(self.Can_Fd_Padding_Value_4.text()))
        parser.Modify("CanTriggerTransmitEnable_4",str(self.Can_Trigger_Transmit_Enable_4.isChecked()))
        parser.Modify('CanControllerRef_4',str(self.Can_Controller_ref_4.currentText()))

        ##########################save in CanHWFilter_4_XML_region##########################################
        parser.Modify("CanHwFilterMask_4",str(self.Can_Hw_Filter_Mask_4.text()))
        parser.Modify("CanHwFilterCode_4",str(self.Can_Hw_Filter_Code_4.text()))

    
################################################ Generation ########################################################

    def Generate(self):
        self.dlg.exec_()
        parser= Module(self.path_1)
        paramters = parser.GetParamName("CanGeneral")
        Generated_file = open("Can_Cgf.h",'w',newline='')
        print("#define " + paramters[5] + " " + parser.GetValue(paramters[5])+'U',file=Generated_file)
        print("#define " + paramters[4] + " " + parser.GetValue(paramters[4])+'U',file=Generated_file)
        print("#define " + paramters[2] + " " + parser.GetValue(paramters[2])+'U',file=Generated_file)
        print("#define " + paramters[3] + " " + parser.GetValue(paramters[3])+'U',file=Generated_file)
        print("#define " + paramters[1] + " " + parser.GetValue(paramters[1]),file=Generated_file)
        print("#define " + paramters[8] + " " + parser.GetValue(paramters[8]),file=Generated_file)
        print("#define " + paramters[7] + " " + parser.GetValue(paramters[7]),file=Generated_file)
        print("#define " + paramters[6] + " " + parser.GetValue(paramters[6]),file=Generated_file)
        print("#define " + paramters[0] + " " + parser.GetValue(paramters[0]),file=Generated_file)
        print("\n\n",file=Generated_file)
        print("#define NUM_OF_CanControllers "+ str(parser.Subcontainer_no('CanController'))+'U',file=Generated_file)
        print("#define NUM_OF_HTH "+ str(parser.no_HTH_HRH('TRANSMIT'))+'U',file=Generated_file)
        print("#define NUM_OF_HRH "+ str(parser.no_HTH_HRH('RECEIVE'))+'U',file=Generated_file)
        print("#define size_MAP_HOH_2_CANObj "+ str(parser.Subcontainer_no('CanHardwareObject'))+'U',file=Generated_file)
        print('\n\n\n\n',file=Generated_file)
        print("#define UserCANCfg \\",file=Generated_file)
        print("{.CanConfigSet.CanController =\\"+"\n"+"    {\\" + "\n" + "        {\\",file=Generated_file)


        #printing ""  .CanConfigSet.CanController  ""
        for i in range(1,parser.Subcontainer_no('CanController')+1):
            Controllerparams=parser.Subcontainer_param('CanController'+"_"+str(i))
            BRparams=parser.Subsubcontainer_param('CanControllerBaudrateConfig'+"_"+str(i))

            # printing can controller parameters
            for j in Controllerparams:
                if(j[:-2]=='CanControllerBaseAddress'):
                    print("        ." + j[:-2] + " = 0x" + parser.GetValue(j) + ",\\",file=Generated_file)
                else:
                    print("        ." + j[:-2] + " = " + parser.GetValue(j) + ",\\",file=Generated_file)
            print("\n",file=Generated_file)
            #print can controller Default badurate
            print("        .CanControllerDefaultBaudrate = &"+self.dlg.textValue()+".CanConfigSet.CanController["+str(i-1)+"].CanControllerBaudrateConfig,\\",file=Generated_file)
            print("\n",file=Generated_file)
            #printing can controller baudrate config
            for k in BRparams:
                print("        .CanControllerBaudrateConfig." + k[:-2] + " = " + parser.GetValue(k) + ",\\",file=Generated_file)

            if(i == parser.Subcontainer_no('CanController')):
                print("        }\\" + "\n" + "    }\\" + "\n" +"};" ,file=Generated_file )
            else:
                print("        },\\" + "\n" + "        {\\",file=Generated_file)

        print('\n\n\n\n',file=Generated_file)

        #printing "CanConfigSet.CanHWObjects"
        #print(parser.Subcontainer_no('CanHardwareObject'))
        print("#define hthMap \\",file=Generated_file)
        print("{.CanConfigSet.CanHardwareObject =\\"+"\n"+"    {\\" + "\n" + "        {\\",file=Generated_file)
        for i in range(1,parser.Subcontainer_no('CanHardwareObject')+1):
            HardwareObj_param=parser.Subcontainer_param('CanHardwareObject'+"_"+str(i))
            HWFilter_param=parser.Subsubcontainer_param('CanHwFilter'+"_"+str(i))
            HardwareObj_type=parser.HW_object_Type('CanHardwareObject'+"_"+str(i))

            if(HardwareObj_type=='TRANSMIT'):
                for j in HardwareObj_param:
                    if(j[:-2] == "CanControllerRef"):
                        print("           ." + j[:-2] + " = &"+ self.dlg.textValue() + ".CanConfigSet.CanController[" + parser.GetValue(j)[-1:]+"]" + ",\\",file=Generated_file)
                    else:
                        print("           ." + j[:-2] + " = " + parser.GetValue(j) + ",\\",file=Generated_file)
                print("\n",file=Generated_file)
                for k in HWFilter_param:
                    if(k[:-2]=='CanHwFilterMask'):
                        print("           .CanHwFilter." + k[:-2] + " = 0x" + parser.GetValue(k) + ",\\",file=Generated_file)
                    else:
                        print("           .CanHwFilter." + k[:-2] + " = " + parser.GetValue(k) + ",\\",file=Generated_file)

                if(i == parser.Subcontainer_no('CanHardwareObject')):
                    print("        }\\" +"\n"+ "    }\\"+"\n" +"};" ,file=Generated_file )
                else:
                    print("        },\\" + "\n" + "        {\\",file=Generated_file)

        print("#define hrhMap \\",file=Generated_file)
        print("{.CanConfigSet.CanHardwareObject =\\"+"\n"+"    {\\" + "\n" + "        {\\",file=Generated_file)
        for i in range(1,parser.Subcontainer_no('CanHardwareObject')+1):
            HardwareObj_param=parser.Subcontainer_param('CanHardwareObject'+"_"+str(i))
            HWFilter_param=parser.Subsubcontainer_param('CanHwFilter'+"_"+str(i))
            HardwareObj_type=parser.HW_object_Type('CanHardwareObject'+"_"+str(i))
            
            if(HardwareObj_type=='RECEIVE'):
                for j in HardwareObj_param:
                    if(j[:-2] == "CanControllerRef"):
                        print("           ." + j[:-2] + " = &"+ self.dlg.textValue() + ".CanConfigSet.CanController[" + parser.GetValue(j)[-1:]+"]" + ",\\",file=Generated_file)
                    else:
                        print("           ." + j[:-2] + " = " + parser.GetValue(j) + ",\\",file=Generated_file)
                print("\n",file=Generated_file)
                for k in HWFilter_param:
                    if(k[:-2]=='CanHwFilterMask'):
                        print("           .CanHwFilter." + k[:-2] + " = 0x" + parser.GetValue(k) + ",\\",file=Generated_file)
                    else:
                        print("           .CanHwFilter." + k[:-2] + " = " + parser.GetValue(k) + ",\\",file=Generated_file)

                if(i == parser.Subcontainer_no('CanHardwareObject')):
                    print("        }\\" + "\n" + "    }\\" + "\n" +"};" ,file=Generated_file )
                else:
                    print("        },\\" + "\n" + "        {\\",file=Generated_file)
                
                    


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    CanTool = QtGui.QMainWindow()
    CanTool.setWindowIcon(QIcon('icon.png'))
    splash_pix = QtGui.QPixmap('dodge.jpg')
    splash = QtGui.QSplashScreen(splash_pix, Qt.WindowStaysOnTopHint)
    progressBar = QtGui.QProgressBar(splash)
    progressBar.setGeometry(0, splash_pix.height() - 50, splash_pix.width(), 20)
    splash.setMask(splash_pix.mask())
    splash.show()
    splash.showMessage("<h1><font color='black'>Can Configuration Tool</font></h1>", Qt.AlignTop | Qt.AlignCenter, Qt.black)
    for i in range(0, 100):
        progressBar.setValue(i)
        t = time.time()
        while time.time() < t + 0.1:
            app.processEvents()
    time.sleep(1)

    
    ui = Ui_CanTool()
    ui.setupUi(CanTool)
    CanTool.show()
    splash.finish(CanTool)
    sys.exit(app.exec_())
    

