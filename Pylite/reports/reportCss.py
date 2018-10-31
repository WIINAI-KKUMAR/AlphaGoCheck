import xlsxwriter
from _pytest import unittest
global Css_Main,Css_Testresult,Css_Header,Css_Status_True,Css_Status_Fail
global workbook
import datetime
import Pylite.reports.reportsFormat as css

summary_report=[['Sno','Testcase_Name','Status']]


report_path= r'C:\Users\vinaykumar_puppala\Desktop\finaltestresults.xlsx'



class report:	
	
	def intiate_result_workbook(self):
		self.workbook = xlsxwriter.Workbook(report_path)
	def close_result_excel_book(self):
		self.workbook.close()
		
	def add_steps_to_excel_report(self,test_case_result,test_case_name,worksheet):
		summay_sublist = []
		TcNumber=+1
		summay_sublist.append(TcNumber)
		summay_sublist.append(test_case_name)
		
		Style_format_TESTRESULT=self.workbook.add_format(css.Css_Testresult)
		Style_format           = self.workbook.add_format(css.Css_Main)
		Css_Header_Format      = self.workbook.add_format(css.Css_Header)
		
		worksheet.merge_range('A1:E1', 'Test result', Style_format_TESTRESULT)
		
		worksheet.merge_range('A2:B2', 'TestCase : ', Style_format)
		worksheet.merge_range('C2:E2', test_case_name,Style_format)
		
		worksheet.write(2, 0, "SNo",             Css_Header_Format)
		worksheet.write(2, 1, "Description",     Css_Header_Format)
		worksheet.write(2, 2, "Expected_Result", Css_Header_Format)
		worksheet.write(2, 3, "Actuall_Result",  Css_Header_Format)
		worksheet.write(2, 4, "Status",  		 Css_Header_Format)	
		
		Row=3
		for sublist in test_case_result:
			#print(sublist)			
			print("row number :" + str(Row))			
			worksheet.write(Row,0,Row-2)
			Col = 1
			for itemvalue in sublist:
				print(itemvalue)							
				worksheet.write(Row,Col,itemvalue)	
				Col = Col + 1		
				if itemvalue == "FAIL"	:
					tc_status_out= 1
			print(" -- -- -- -- ")
			Row = Row + 1
		
		if tc_status_out==1 : summay_sublist.append("FAIL")
		else:summay_sublist.append("PASS") 
		
		
		
		summary_report.append(summay_sublist)
		summay_sublist=None		
		Row = None
		Col = None

	def add_testcase_result(self,testcase_name,Test_steps):
		worksheet= self.workbook.add_worksheet(testcase_name)
		self.add_steps_to_excel_report(Test_steps,testcase_name,worksheet)
		

class email :
	
	#Sending email
	def fn_TosentEmailConfirmation(self,DB_Record_count,Attachment_Report,Message_Json):
	
		Str_html=self.Html_body_Report(self,DB_Record_count,Message_Json)
		
		import win32com.client as win32
		outlook = win32.Dispatch('outlook.application')
		mail = outlook.CreateItem(0)
		#mail.To ='michelle.antrum@spglobal.com'
		mail.To ='vinaykumar.puppala@spglobal.com'
		mail.CC='vinaykumar.puppala@spglobal.com'
		#mail.bcc = 'jshankar@spglobal.com;michelle.antrum@spglobal.com'
		mail.Subject = 'Automation Notification Email @QAAutomationCommunity.'
		mail.Body    = 'Notification - Automation Notification Email .'
		mail.HTMLBody = Str_html
		
		# To attach a file to the email (optional):
		for attach in Attachment_Report :mail.Attachments.Add(attach) #attachment  = "Path to the attachment"
		mail.Send()
		print("Email notification sent successfully")
	
	def Html_body_Report(self,RecordS,Message_Json):		
		#MessgaStr=str(Message_Json[2])
		#print (MessgaStr)
		now = datetime.datetime.now()
		currentTime = now.strftime("%Y-%m-%d %H:%M:%S")
		Input_Html='<head><style>table, th, td {border: 1px solid black; border-collapse: collapse;}</style></head>\
		            <body><img src = C:\\Users\\vinaykumar_puppala\\Downloads\\QA_automationCommunity_png.png' 'alt = "logo_Image" width = "1330"  height = "200"  border="3" align = "Center"/>\
		            <h1 style="color:red;"><center> Automation Report(Python)<center></h1>\
		            <h2><center>Application Name : USPF DATA LINKING </h2></center><br>\
		            <P style="font-size:10px;"><center>'+str(currentTime)+'</center></p>\
		            <table style="width:100%">\
		            <tr><th>Source_RecordCount</th><th>Target_RecordCount</th><th>No Of records mismatched</th></tr> \
		            <tr><center><td>'+str(RecordS[0])+'</td><td>'+str(RecordS[1])+'</td><td style="color:red;">'+str(RecordS[2]) + '</td>\
		            </center></tr> </table><br>\
	 	            <P style="font-size:15px;">'+str(Message_Json)+'</P>\
		            <P style="font-size:10px;">Any Queries/clarification on result. Please reach us on : Vinaykumar.puppala@spglobal.com </P>\
		            </body>'
		return (Input_Html)


# 
# 	            <P>Please find the attached fetched and compared DB files </P>\
# # 	        <P style="font-size:15px;"><a href='+str(Message_Json[0])+'> Source DB </P>\
# # 	        <P style="font-size:15px;"><a href='+str(Message_Json[1])+'> DB feched report For WFM JOB ID</P>\

# #for i in range(2,6):
# 
# intiate_result_workbook()
# resultList_1=[['1','b','c','d','Pass'],['2','b','c','d','Fail'],['3','b','c','d','Inprogress']]
# worksheet= workbook.add_worksheet('TC_03')
# add_steps_to_excel_report(resultList_1,'TC_03',worksheet)
# worksheet= workbook.add_worksheet('TC_02')
# add_steps_to_excel_report(resultList_1,'TC_02',worksheet)
# close_result_excel_book()
# workbook.close()






	








