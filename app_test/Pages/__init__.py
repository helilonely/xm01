#coding=utf-8
from selenium.webdriver.common.by import By

"""
---------------------------短信-----------------------------------------
"""
# 写短信按钮
new_mms_btn = (By.ID, "com.android.mms:id/action_compose_new")
# 短信接收者输入框
mms_recipients_editor = (By.ID, "com.android.mms:id/recipients_editor")
# 短信输入框
embedded_text_editor = (By.ID, "com.android.mms:id/embedded_text_editor")
# 发送短信按钮
send_button_sms = (By.ID, "com.android.mms:id/send_button_sms")
# 短信标题列表
list_sms = (By.ID, "com.android.mms:id/text_view")

"""
---------------------------设置 搜索-----------------------------------------
"""
search_btn=(By.ID, "com.android.settings:id/search")
search_input_text=(By.ID, "android:id/search_src_text")
search_result_list = (By.ID,"com.android.settings:id/title")
