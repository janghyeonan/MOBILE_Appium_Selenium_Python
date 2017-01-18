# Appium을 이용한 지스윙앱 자동화(자동화로 일부 동선으로 페이지가 잘 열리는지 확인하는 내용)
# 아직 테스트 슈트를 분리하지 않음.
import os
import unittest
import datetime
from appium import webdriver
from time import sleep
from appium.webdriver.common.touch_action import TouchAction

class AndroidTest(unittest.TestCase):
    
    def setUp(self): # 셋업
        "Setup for the test"
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = 'Android Emulator'        
        desired_caps['appPackage'] = 'com.gswing.m'
        desired_caps['appActivity'] = 'com.gswing.m.activity.Activity_Intro'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        
    def tearDown(self): # 종료
        "Tear down the test"
        self.driver.quit()
 
    def test_single_player_mode(self):

        #xpath 함수    fex("xpath", "로그/스샷명")
        def fex(aaa, ccc):  #공통합수
            sleep(3)
            print("\n" +"시작: "+ ccc)
            self.driver.find_element_by_xpath(aaa).click()
            sleep(3)
            self.driver.get_screenshot_as_file("c:/result/" +ccc+ ".png") # 스크린샷 저장
            print("\n" +"끝: "+ ccc)

        def bac():   #뒤로가기 버튼(좌측 상단에 뒤로가기 이미지 버튼 클릭
            self.driver.find_element_by_class_name("android.widget.ImageButton").click()

 	    #대기
        sleep(5)        
        #시작/ #소식
        fex("//android.widget.TextView[@text='소식']", "비로그인-소식")
        #친구
        fex("//android.widget.TextView[@text='친구']", "비로그인-친구")        
        #로그인창 / #뒤로가기
        bac()
        #나의기록실
        fex("//android.widget.TextView[@text='나의 기록실']", "비로그인-나의 기록실")        
        #로그인창 / #뒤로가기
        bac()
        #대회
        fex("//android.widget.TextView[@text='대회']", "비로그인-대회")        
        #대회목록
        fex("//android.view.View[@content-desc='대회목록']", "비로그인-대회목록")
        #대회포인트랭킹 / #나의대회
        fex("//android.view.View[@content-desc='나의 대회']", "비로그인-나의 대회")        
        #로그인창 / #뒤로가기
        bac()
        #더보기
        fex("//android.widget.TextView[@text='더보기']", "비로그인-더보기")        
        #리스트출력/ #약관 //생략 / #이용약관리스트 / #이용약관 / #로그인창/ #뒤로가기
        bac()
        #사이드메뉴
        self.driver.find_element_by_class_name("android.widget.ImageButton").click()
        sleep(5) 
        self.driver.get_screenshot_as_file("비로그인-사이드메뉴.png")        
        #스코어카드
        fex("//android.widget.TextView[@text='스코어카드']", "비로그인-스코어카드")        
        #로그인창 / #뒤로가기
        bac()
        #굿스윙
        fex("//android.widget.TextView[@text='굿스윙']", "비로그인-굿스윙")
        #세레모니 / #굿스윙 / #뒤로가기
        bac()
        #레슨
        fex("//android.widget.TextView[@text='레슨']", "비로그인-레슨")
        #뒤로가기
        bac()
        #소식지
        fex("//android.widget.TextView[@text='소식지']", "비로그인-소식지")
        bac()
        #이벤트
        fex("//android.widget.TextView[@text='이벤트']", "비로그인-이벤트")
        #이벤트 / #뒤로가기
        bac()
        #고객센터
        fex("//android.widget.TextView[@text='고객센터']", "비로그인-고객센터")
        #공지사항 /  #1:1문의 / #로그인창 /#뒤로가기
        bac()
        #매장찾기
        fex("//android.widget.TextView[@text='매장찾기']", "비로그인- 매장찾기")
        #매장찾기 / #스타매장 / #신규매장 #뒤로가기
        bac()
        #창업센터
        fex("//android.widget.TextView[@text='창업센터']", "비로그인-창업센터")
        #창업센터 웹페이지 / #뒤로가기(백키)
        self.driver.keyevent(4)
        #로그인
        fex("//android.widget.TextView[@text='로그인하기']", "로그인-로그인하기")
        self.driver.find_element_by_id("com.gswing.m:id/fragment_login__credential__edittext_member_id").send_keys("****")
        self.driver.find_element_by_id("com.gswing.m:id/fragment_login__credential__edittext_member_password").send_keys("*****")
        self.driver.find_element_by_id("com.gswing.m:id/fragment_login__credential__login_button").click()
        # 사이드메뉴
        # 토스트창 스샷
        self.driver.keyevent(4)
        self.driver.get_screenshot_as_file("종료알림_토스트 내용.png")
        #뒤로가기(백키)
        self.driver.keyevent(4)        
        #종료
 
#---START OF SCRIPT
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(AndroidTest)
    unittest.TextTestRunner(verbosity=2).run(suite)