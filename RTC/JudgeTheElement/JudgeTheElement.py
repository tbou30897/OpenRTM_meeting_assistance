#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-

"""
 @file JudgeTheElement.py
 @brief ModuleDescription
 @date $Date$


"""
import sys
import time
sys.path.append(".")

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
judgetheelement_spec = ["implementation_id", "JudgeTheElement",
		 "type_name",         "JudgeTheElement",
		 "description",       "ModuleDescription",
		 "version",           "1.0.0",
		 "vendor",            "VenderName",
		 "category",          "Category",
		 "activity_type",     "STATIC",
		 "max_instance",      "1",
		 "language",          "Python",
		 "lang_type",         "SCRIPT",
		 ""]
# </rtc-template>

##
# @class JudgeTheElement
# @brief ModuleDescription
#
#
class JudgeTheElement(OpenRTM_aist.DataFlowComponentBase):

	##
	# @brief constructor
	# @param manager Maneger Object
	#
	def __init__(self, manager):
		OpenRTM_aist.DataFlowComponentBase.__init__(self, manager)

		self._d_name = OpenRTM_aist.instantiateDataType(RTC.TimedWString)
		"""
		"""
		self._nameIn = OpenRTM_aist.InPort("name", self._d_name)
		self._d_textin1 = OpenRTM_aist.instantiateDataType(RTC.TimedWString)
		"""
		"""
		self._textin1In = OpenRTM_aist.InPort("textin1", self._d_textin1)
		self._d_textin2 = OpenRTM_aist.instantiateDataType(RTC.TimedWString)
		"""
		"""
		self._textin2In = OpenRTM_aist.InPort("textin2", self._d_textin2)
		self._d_recordout = OpenRTM_aist.instantiateDataType(RTC.TimedWString)
		"""
		"""
		self._recordoutOut = OpenRTM_aist.OutPort("recordout", self._d_recordout)
		self._d_textout = OpenRTM_aist.instantiateDataType(RTC.TimedWString)
		"""
		"""
		self._textoutOut = OpenRTM_aist.OutPort("textout", self._d_textout)





		# initialize of configuration-data.
		# <rtc-template block="init_conf_param">

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

		# Set InPort buffers
		self.addInPort("name",self._nameIn)
		self.addInPort("textin1",self._textin1In)
		self.addInPort("textin2",self._textin2In)

		# Set OutPort buffers
		self.addOutPort("recordout",self._recordoutOut)
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
		self.judge = 0
		self.element1 = ""
		self.element2 = ""
		self.name = "氏名未入力"
		self.t = ""
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
		if self._textin1In.isNew(): #新しいデータが来たか確認
			self._d_textin1 = self._textin1In.read() #値を読み込む
			self.element1 = self._d_textin1.data
			if self.element1.find == -1:
				pass
			else:
				num = self.element1.find(']')
				self.element1 = self.element1[ num + 1 : ]
				num2 = self.element1.find(' ')
				self.element1 = self.element1[ num2 + 1 : ]
	
		if self._textin2In.isNew(): #新しいデータが来たか確認
			self._d_textin2 = self._textin2In.read() #値を読み込む
			self.element2 = self._d_textin2.data
	
		if self._nameIn.isNew(): #新しいデータが来たか確認
			self._d_name = self._nameIn.read() #値を読み込む
			self.name = self._d_name.data

		if self.t != self.element1:
			if self.element2 == "start":
				if self.element1 != "":

				
					if self.judge == 1:
						self.judge = self.judge + 1
						
		
		
						#NAMEコンポーネントから議事録に表示する名前を取る
						if self._nameIn.isNew(): #新しいデータが来たか確認
							self._d_name = self._nameIn.read() #値を読み込む
							self.name = self._d_name.data
							print(self.name)
						else:
							pass
	
						#↓名前と音声認識結果を合わせる（名前:音声認識結果）
						rec = self.name + ":" +self.element1
						#送る
						self._d_recordout.data = rec
						self._recordoutOut.write()
						print("record" + ":" +rec)


						self.t = self.element1
	
						#↓textoutで音声認識結果のみを送る
						tex = self.element1
						#送る
						self._d_textout.data = tex
						self._textoutOut.write()
	
					
						print("text" + ":" +tex)
					else:
						pass
				else:
					pass
			else:
				self.judge = 1
		else:
			pass

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




def JudgeTheElementInit(manager):
    profile = OpenRTM_aist.Properties(defaults_str=judgetheelement_spec)
    manager.registerFactory(profile,
                            JudgeTheElement,
                            OpenRTM_aist.Delete)

def MyModuleInit(manager):
    JudgeTheElementInit(manager)

    # Create a component
    comp = manager.createComponent("JudgeTheElement")

def main():
	mgr = OpenRTM_aist.Manager.init(sys.argv)
	mgr.setModuleInitProc(MyModuleInit)
	mgr.activateManager()
	mgr.runManager()

if __name__ == "__main__":
	main()

