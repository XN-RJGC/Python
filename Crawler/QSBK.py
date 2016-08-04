# QSBK.py
"""
a simple crawler of qsbk
"""
import urllib2
import re

url = 'http://www.qiushibaike.com/hot/page/'
headers = {
    "Host": 'www.qiushibaike.com',
    "User-Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36'
    #"Referer": ''
}

class qsbk:
    """
    a crawler of qsbk
    """
    def __init__(self):
        # page index
        self.page = 1
        # default url
        self.url = url
        # header
        self.header = headers
        self.enable = False
        # store story
        self.stories = []

    def get_page(self, page_index):
        """
        Using page_index to get this page of html.
        :param page_index: int
        :return: int
        """
        try:
            global url
            current_url = url + str(page_index)
            # create a request
            request = urllib2.Request(current_url, headers=self.header)
            # get page of page_index
            response = urllib2.urlopen(request)
            # coding to utf-8
            return response.read()
        except urllib2.URLError, e:
            if hasattr(e, 'reason'):
                print 'connect to qsbk error', e.reason
                return None

    def get_page_item(self, page_index):
        """
        Using get_page to get page items of storing a list.
        :param page_index: int
        :return: list
        """
        # get page from self.get_page(page_index)
        page = self.get_page(page_index)
        # check return value
        if not page:
            print 'page is None'
            return None
        # regular expression matching
        pattern = r'<div class="author clearfix">.*?<h2>(.*?)</h2>.*?' \
                  r'<div class="content">(.*?)</div>.*?<span.*?class="number">(.*?)</i>'
        pattern = re.compile(pattern, re.S)
        items = re.findall(pattern, page)

        page_stories = []
        for item in items:
            replace_br = re.compile('<br/>')
            text = re.sub(replace_br, "\n", item[1])
            # item[0] is author item[1] is content item[2] is vote
            page_stories.append([item[0].strip(), text.strip(), item[2].strip()])

        return page_stories

    def load_page(self):
        """
        Loading a page with storing a list.
        :return:
        """
        if self.enable == True:
            if len(self.stories) < 2:
                # get a page stories
                page_stories = self.get_page_item(self.page)
                if page_stories:
                    self.stories.append(page_stories)
                    self.page += 1

    def print_one_story(self, page_story, now_page):
        """
        Print one story with special format.
        :param page_story: list
        :param now_page: int
        :return:
        """
        for story in page_story:
            # waiting for input.
            input = raw_input()
            # load a page stories
            self.load_page()
            # whether or not quit
            if input == 'Q' or input == 'q':
                self.enable = False
                return
            print 'page:%d\tauthor:%s\tvote:%s\n\t%s' %(now_page, story[0], story[2], story[1])

    def start(self):
        """
        Starting to crawler page.
        :return:
        """
        print "starting to crawler qsbk's page(Enter Q or q to quit)"
        print
        self.enable = True
        self.load_page()
        # a variabel to control counts
        nowpage = 0
        while self.enable:
            if len(self.stories) > 0:
                # get a page stories
                page_stories = self.stories[0]
                nowpage += 1
                del self.stories[0]
                # print stories
                self.print_one_story(page_stories, nowpage)

if __name__ == '__main__':
    spider = qsbk()
    spider.start()
