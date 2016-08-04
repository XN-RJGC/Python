# BDTB.py
# coding:utf-8
"""
a simple crawler of baidutieba
"""
import urllib2, urllib
import re

def get_params(see_lz, pn):
    """
    Using urllib to get params.
    :param see_lz: int
    :param pn: int
    :return: string
    """
    params = {
        "see_lz": str(see_lz),
        "pn": str(pn)
    }
    return '?' + urllib.urlencode(params)

class handle_content(object):
    """
    a class to deal with content, by this you can get waht you want to see.
    """
    # re
    remove_img = re.compile('<img.*?>')
    remove_a_href = re.compile('<a href=.*?>|</a>')
    remove_br = re.compile('(<br>)+')
    remove_space_2 = re.compile('( ){4,7}')

    def replace(self, content):
        # deal with img tag.
        content = re.sub(self.remove_img, "", content)
        # deal with href tag.
        content = re.sub(self.remove_a_href, "", content)
        # deal with br tag.
        content = re.sub(self.remove_br, "\n", content)
        # deal with space that at least than 2
        content = re.sub(self.remove_space_2, "", content)

        return content.strip()

class bdtb(object):
    """
    a class of cralwler to crab baidutieba.
    """
    def __init__(self, base_url, is_see_lz):
        """
        Init.
        :rtype: object
        """
        self.base_url = base_url
        self.is_see_lz = is_see_lz
        # a sistance of class handle_conntent
        self.tool = handle_content()
        # file name
        self.file = None
        # default flie name
        self.default_title = u"百度贴吧"

    def get_page(self, index):
        """
        Get page'html of index.
        :param index: int
        :return: string
        """
        try:
            url = self.base_url + get_params(self.is_see_lz, index)
            # construct a request of using url
            request = urllib2.Request(url)
            # get response
            response = urllib2.urlopen(request)
            return response.read()
        except urllib2.URLError, e:
            if hasattr(e, 'reason'):
                print 'get_page:', e.reason
                return None

    @property
    def get_title(self):
        """
        Get page title.
        :return: string or None
        """
        page = self.get_page(1)
        # re
        pattern = r'<h3 class="core_title_txt.*?>(.*?)</h3>'
        pattern = re.compile(pattern, re.S)
        result = re.search(pattern, page)
        if result:
            return result.group(1).strip()
        else:
            return None

    @property
    def get_page_num(self):
        """
        Get page number.
        :return: string or None
        """
        page = self.get_page(1)
        # re
        pattern = r'<li class="l_reply_num.*?</span>.*?<span.*?>(.*?)</span>.*?</li>'
        pattern = re.compile(pattern, re.S)
        result = re.search(pattern, page)
        if result:
            return result.group(1).strip()
        else:
            return None

    def get_page_content(self, page):
        """
        Get page content that you want to attain.
        :param page: string
        :return: list
        """
        # re
        pattern = r'<div id="post_content_.*?>(.*?)</div>'
        pattern = re.compile(pattern, re.S)
        items = re.findall(pattern, page)
        # to store after handle
        content_list = []
        for item in items:
            content_list.append(self.tool.replace(item))
        return content_list

if __name__ == '__main__':
    base_url = 'http://tieba.baidu.com/p/3138733512'
    splider = bdtb(base_url, 1)
    for item in splider.get_page_content(splider.get_page(1)):
        print item
