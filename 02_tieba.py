import requests
#https://tieba.baidu.com/f?kw=%E6%9D%8E%E6%AF%85&ie=utf-8&pn=50
class Web_Spider(object):

    def __init__(self,name):
        self.name = name
        self.header = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36"}
        self.first_url = "https://tieba.baidu.com/f?kw=" + "%s"%name +"&ie=utf-8&pn={}"

    def url_list(self):
        self.url_lists = []
        num = 0
        for i in range(10):
            num+=50
            self.url_lists.append(self.first_url.format(num))
        return self.url_lists



    def save_webpage(self,data,i):

        new_webpage = "{}吧的第{}个网页.html".format(self.name,i)
        with open (new_webpage,'w',encoding="utf-8") as f:
            f.write(data)
            f.close()



    def run_spider(self):
        #读取url的列表
        heard_list = self.url_list()
        #打开url

        #爬下网页
        for i in range(10):
            responese = requests.get(self.first_url,heard_list[i])
            data = responese.content.decode()
            #print(data)
            self.save_webpage(data,i)
        #保存网页



        pass

def test_one():
    one = Web_Spider("李毅")
    one.run_spider()
def test_two():
    pass

def test_three():
    print("1")
if __name__ == "__main__":
    test_one()
