# coding:utf-8
# NWSUAF_EMS.py
"""
Grab Northwest A&F University educational management system
"""
import urllib2, urllib
import cookielib
import re
import sys

# login url
base_url = 'http://jwgl.nwsuaf.edu.cn/academic/j_acegi_security_check'
# captcha url
captcha_url = 'http://jwgl.nwsuaf.edu.cn/academic/getCaptcha.do'
# score url
score_url = 'http://jwgl.nwsuaf.edu.cn/academic/manager/score/studentOwnScore.do?groupId=&moduleId=2020'
# this is not strictly necessary but it is safer
headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36",
        "Host": "jwgl.nwsuaf.edu.cn",
        "Referer": "http://jwgl.nwsuaf.edu.cn/academic/index.html"
     }

class NWSUAF_EMS(object):
    """
    Grab educational management system.
    """
    def __init__(self):
        # login url
        self.url = base_url
        # captcha url
        self.captcha_url = captcha_url
        # CookieJar object
        self.cookies = cookielib.CookieJar()
        # construct opener
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookies))
        # score page
        self.score_page = None
        # construct login post data
        self.postdata = {
            'j_username': '',
            'j_password': '',
            'j_captcha': '',
        }
        # construct get score post data
        self.score_data = {
            "year": 36,
            "term": 1,
            "para": 0,
            "sortColumn": "",
            "Submit": "查询"
        }

    def set_data(self, username, password):
        """
        Set postdata of j_username and j_password
        :param username: string
        :param password: string
        :return:
        """
        self.postdata['j_username'] = username
        self.postdata['j_password'] = password

    def set_captcha(self, captcha):
        """
        :param captcha: string
        :return:
        """
        self.postdata['j_captcha'] = captcha

    def write_captcha(self, content):
        """
        :param content: string
        :return:
        """
        try:
            f = open('captcah', 'wb')
            f.write(content)
            f.close()
        except IOError:
            print 'write file error!'

    def get_captcha(self):
        """
        Using captcha url to attain captcha that store in current captcha file.
        :return:
        """
        try:
            # construct request
            request = urllib2.Request(self.captcha_url)
            # get response
            response = self.opener.open(request)
            # to store captcha
            self.write_captcha(response.read())
        except urllib2.URLError, e:
            if hasattr(e, 'reason'):
                print 'Get captcha error!', e.reason

    def get_index_page(self, captcha):
        """
        Using post data to login.
        :param captcha: string
        :return:
        """
        # set captcha
        self.set_captcha(captcha)
        # login
        try:
            # post data
            data = urllib.urlencode(self.postdata)
            # construct request
            request = urllib2.Request(url=self.url, data=data, headers=headers)
            # get response
            response = self.opener.open(request)
        except urllib2.URLError, e:
            if hasattr(e, 'reason'):
                print 'login error!', e.reason

    def get_score_page(self):
        """
        :return:
        """
        # score post data
        data = urllib.urlencode(self.score_data)
        # construct request
        request = urllib2.Request(url=score_url, data=data)
        try:
            response = self.opener.open(request)
            self.score_page = response.read()
        except urllib2.URLError as e:
            if hasattr(e, 'reason'):
                print 'Get score page error!', e.reason

    def get_score_page_item(self):
        """
        :return:
        """
        # re
        pattern = r'<tr>(.*?)</tr>'
        pattern = re.compile(pattern, re.S)
        # get match
        result = re.findall(pattern, self.score_page)
        if len(result) == 0:
            return None
        else:
            result.pop(0)
        # get title
        if len(result) == 0:
            return None
        pattern = r'<th>(.*?)</th>'
        pattern = re.compile(pattern, re.S)
        title_result = re.findall(pattern, result[0])
        for item in title_result:
            print item.strip()
        # get subject
        pattern = r'<td>(.*?)</td>'
        pattern = re.compile(pattern, re.S)
        # subject from result[1:]
        subject = result[1:]
        result = []
        for item in subject:
            # get subject item
            subject_item = re.findall(pattern, item)
            temp = []
            for index in subject_item:
                temp.append(index.strip())
            result.append(temp)
        return result


if __name__ == '__main__':
    splider = NWSUAF_EMS()
    # set username and password
    splider.set_data('2014012623', '132237')
    # get captcha
    splider.get_captcha()
    # input captcha
    captcha = raw_input("Input Captcha: ")
    # login
    splider.get_index_page(captcha)
    # score page
    splider.get_score_page()
    # get subject item
    for items in splider.get_score_page_item():
        for item in items:
            print item
        break
