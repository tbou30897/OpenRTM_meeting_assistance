#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-

"""
 @file WebScraping1.py
 @brief ModuleDescription
 @date $Date$


"""
import sys
import time
sys.path.append(".")
#import関係はここに
from selenium import webdriver
import time
# Import RTM module
import RTC
import OpenRTM_aist


# Import Service implementation class
# <rtc-template block="service_impl">

# </rtc-template>

# Import Service stub modules
# <rtc-template block="consumer_import">
# </rtc-template>


# This module's spesification
# <rtc-template block="module_spec">
webscraping1_spec = ["implementation_id", "WebScraping1",
		 "type_name",         "WebScraping1",
		 "description",       "ModuleDescription",
		 "version",           "1.0.0",
		 "vendor",            "VenderName",
		 "category",          "Category",
		 "activity_type",     "UNIQUE",
		 "max_instance",      "1",
		 "language",          "Python",
		 "lang_type",         "SCRIPT",
		 "conf.default.URL", "https://distracted-chandrasekhar-3c01ee.netlify.app/",
		 "conf.default.attribute", "id",
		 "conf.default.element", "result_text",
		 "conf.default.FileStorageLocation", "C:/RT/chromedriver.exe",

		 "conf.__widget__.URL", "text",
		 "conf.__widget__.attribute", "text",
		 "conf.__widget__.element", "text",
		 "conf.__widget__.FileStorageLocation", "text",

         "conf.__type__.URL", "string",
         "conf.__type__.attribute", "string",
         "conf.__type__.element", "string",
         "conf.__type__.FileStorageLocation", "string",

		 ""]
# </rtc-template>

##
# @class WebScraping1
# @brief ModuleDescription
#
#
class WebScraping1(OpenRTM_aist.DataFlowComponentBase):

	##
	# @brief constructor
	# @param manager Maneger Object
	#
	def __init__(self, manager):
		OpenRTM_aist.DataFlowComponentBase.__init__(self, manager)

		self._d_textout = OpenRTM_aist.instantiateDataType(RTC.TimedWString)
		"""
		"""
		self._textoutOut = OpenRTM_aist.OutPort("textout", self._d_textout)





		# initialize of configuration-data.
		# <rtc-template block="init_conf_param">
		"""
		
		 - Name:  url
		 - DefaultValue: https://distracted-chandrasekhar-3c01ee.netlify.app/
		"""
		self._url = ['https://distracted-chandrasekhar-3c01ee.netlify.app/']
		"""
		↓webサイトから検索する属性を変更する際は、以下の記述に従ってコンフィグ変数を
		変更してください
		id属性で検索する場合はid
		name属性で検索する場合はname
		class属性で検索する場合はclass_name
		親子関係を持ったclass属性を検索する場合は css_selector
		 - Name:  attribute
		 - DefaultValue: id
		 - Constraint: (id,name,class_name,css_selector)
		"""
		self._attribute = ['id']
		"""
		検索したい要素の要素名を入力してください。
		id属性で検索する場合はid名
		name属性で検索する場合はname名
		class属性で検索する場合はclass名
		親子関係を持ったclass属性を検索する場合は .親要素 .子要素
		 - Name:  element
		 - DefaultValue: result_text
		"""
		self._element = ['result_text']
		"""
		chromedriver.exeの保存場所を指定します。
		 - Name:  FileStorageLocation
		 - DefaultValue: C:/RT/chromedriver.exe
		"""
		self._FileStorageLocation = ['C:/RT/chromedriver.exe']

		# </rtc-template>



	##
	#
	# The initialize action (on CREATED->ALIVE transition)
	# formaer rtc_init_entry()
	#
	# @return RTC::ReturnCode_t
	#
	#
	def onInitialize(self):
		# Bind variables and configuration variable
		self.bindParameter("URL", self._url, "https://distracted-chandrasekhar-3c01ee.netlify.app/")
		self.bindParameter("attribute", self._attribute, "self.driver.find_element_by_id('result_text')")

		# Set InPort buffers

		# Set OutPort buffers
		self.addOutPort("textout",self._textoutOut)

		# Set service provider to Ports

		# Set service consumers to Ports

		# Set CORBA Service Ports

		return RTC.RTC_OK

	###
	##
	## The finalize action (on ALIVE->END transition)
	## formaer rtc_exiting_entry()
	##
	## @return RTC::ReturnCode_t
	#
	##
	#def onFinalize(self):
	#
	#	return RTC.RTC_OK

	###
	##
	## The startup action when ExecutionContext startup
	## former rtc_starting_entry()
	##
	## @param ec_id target ExecutionContext Id
	##
	## @return RTC::ReturnCode_t
	##
	##
	#def onStartup(self, ec_id):
	#
	#	return RTC.RTC_OK

	###
	##
	## The shutdown action when ExecutionContext stop
	## former rtc_stopping_entry()
	##
	## @param ec_id target ExecutionContext Id
	##
	## @return RTC::ReturnCode_t
	##
	##
	#def onShutdown(self, ec_id):
	#
	#	return RTC.RTC_OK

	##
	#
	# The activated action (Active state entry action)
	# former rtc_active_entry()
	#
	# @param ec_id target ExecutionContext Id
	#
	# @return RTC::ReturnCode_t
	#
	#
	def onActivated(self, ec_id):

		#webdriverでChromeを開く
		self.driver = webdriver.Chrome(self._FileStorageLocation[0])
		
		#指定したURLを開く
		self.driver.get(self._url[0])
		time.sleep(1)

		#音識ボタンを押す
		self.driver.find_element_by_xpath("/html/body/input").click()
		
		return RTC.RTC_OK

	##
	#
	# The deactivated action (Active state exit action)
	# former rtc_active_exit()
	#
	# @param ec_id target ExecutionContext Id
	#
	# @return RTC::ReturnCode_t
	#
	#
	def onDeactivated(self, ec_id):

		#Chromeを閉じる
		driver.close()

		return RTC.RTC_OK

	##
	#
	# The execution action that is invoked periodically
	# former rtc_active_do()
	#
	# @param ec_id target ExecutionContext Id
	#
	# @return RTC::ReturnCode_t
	#
	#
	def onExecute(self, ec_id):
		tex = ""
		if self._attribute[0] == 'id':
			#id要素を取り出す
			element2 = self.driver.find_element_by_id(self._element[0])
			tex = element2.text
		
		elif self._attribute[0] == 'name':
			#id要素を取り出す
			element2 = self.driver.find_element_by_name(self._element[0])
			tex = element2.text

		elif self._attribute[0] == 'class_name':
			#class要素を取り出す
			element2 = self.driver.find_element_by_class_name(self._element[0])
			tex = element2.text

		elif self._attribute[0] == 'css_selector':
			#親子関係のある
			element2 = self.driver.find_element_by_class_css_selector(self._element[0])
			tex = element2.text
		else:
			pass
			
		#取り出した要素の送信
		self._d_textout.data = tex
		self._textoutOut.write()
		print(tex)

		return RTC.RTC_OK

	###
	##
	## The aborting action when main logic error occurred.
	## former rtc_aborting_entry()
	##
	## @param ec_id target ExecutionContext Id
	##
	## @return RTC::ReturnCode_t
	##
	##
	#def onAborting(self, ec_id):
	#
	#	return RTC.RTC_OK

	###
	##
	## The error action in ERROR state
	## former rtc_error_do()
	##
	## @param ec_id target ExecutionContext Id
	##
	## @return RTC::ReturnCode_t
	##
	##
	#def onError(self, ec_id):
	#
	#	return RTC.RTC_OK

	###
	##
	## The reset action that is invoked resetting
	## This is same but different the former rtc_init_entry()
	##
	## @param ec_id target ExecutionContext Id
	##
	## @return RTC::ReturnCode_t
	##
	##
	#def onReset(self, ec_id):
	#
	#	return RTC.RTC_OK

	###
	##
	## The state update action that is invoked after onExecute() action
	## no corresponding operation exists in OpenRTm-aist-0.2.0
	##
	## @param ec_id target ExecutionContext Id
	##
	## @return RTC::ReturnCode_t
	##

	##
	#def onStateUpdate(self, ec_id):
	#
	#	return RTC.RTC_OK

	###
	##
	## The action that is invoked when execution context's rate is changed
	## no corresponding operation exists in OpenRTm-aist-0.2.0
	##
	## @param ec_id target ExecutionContext Id
	##
	## @return RTC::ReturnCode_t
	##
	##
	#def onRateChanged(self, ec_id):
	#
	#	return RTC.RTC_OK




def WebScraping1Init(manager):
    profile = OpenRTM_aist.Properties(defaults_str=webscraping1_spec)
    manager.registerFactory(profile,
                            WebScraping1,
                            OpenRTM_aist.Delete)

def MyModuleInit(manager):
    WebScraping1Init(manager)

    # Create a component
    comp = manager.createComponent("WebScraping1")

def main():
	mgr = OpenRTM_aist.Manager.init(sys.argv)
	mgr.setModuleInitProc(MyModuleInit)
	mgr.activateManager()
	mgr.runManager()

if __name__ == "__main__":
	main()

