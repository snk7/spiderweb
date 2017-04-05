# coding: utf-8
import os,webbrowser,psutil,re
from urlparse import urlparse
from BeautifulSoup import BeautifulSoup
from publicsuffix import PublicSuffixList,fetch
class main:
    def __init__(self, domian,cookie):
        self.url = domian
        domain = urlparse(domian)
        self.new_path = os.path.join('result', domain.netloc)
        if not os.path.isdir(self.new_path):
            os.makedirs(self.new_path)
        domain = domain.netloc.split('.')
        self.domain = domain[-2] + '.' + domain[-1]
        self.cookie=cookie
    def find_url(self,htmlsoruce):
        #抽取url
        liststr=[]
        soup = BeautifulSoup(htmlsoruce)
        for a in soup.findAll('a',href=True):
            if  (a['href']):
                liststr.append(a['href'])
        return liststr
    def screenurl(self,liststr,url):
        #过滤url
        listurl=[]
        for i in liststr:
            cr = re.compile(r'^((?!.*://|javascript.*|\#.*|mailto:.*|//.*).)*$',re.I)
            j=''.join(i.split())
            if re.search("^%s"%self.domain, j):
                listurl.append(j)
            elif cr.search(j):
                listurl.append(urlparse.urljoin(url,j))
    def find_domian(self,list_url):
        psl_file = fetch()
        psl = PublicSuffixList(psl_file)
        list_urls=[]
        for i in list_url:
            j=urlparse(i).netloc
            if psl.get_public_suffix(j)==self.domain:
                list_urls.append(j)
        return list_urls
    def Dispatch(self,list_urla):
        try:
            list_url_a=[]
            p = webbrowser.webbrowser(self.url, self.cookie)
            list_url = ['http://www.tencent.com/zh-cn/', 'http://www.tencent.com/zh-cn/ps/ieg.shtml',
                        'http://www.tencent.com/zh-cn/ps/ieg.shtml', 'http://www.tencent.com/zh-cn/ir/news/', \
                        'http://www.tencent.com/zh-cn/ir/govern.shtml']
            for i in list_url:
                j=self.find_url(p.gethtml(i))
                print j
            #print list(set(list_url_a))
            for l in list(set(p.get_network())):    print l
            p.close()
        finally:
            pass
                
    def start(self):
        try:
            self.Dispatch('A')
            '''list_url_a=[]
            p = webbrowser.webbrowser(self.new_path, self.url, 'aaaaa')
            list_url = ['http://www.tencent.com/zh-cn/', 'http://www.tencent.com/zh-cn/ps/ieg.shtml', 
                        'http://www.tencent.com/zh-cn/ps/ieg.shtml', 'http://www.tencent.com/zh-cn/ir/news/', \
                        'http://www.tencent.com/zh-cn/ir/govern.shtml']
            for i in list_url:
                self.find_url(p.gethtml(i))
            print list(set(list_url_a))
            print p.get_network()'''
        except Exception, e:
            print e
        finally:
            self.kill_proxy()
    def kill_proxy(self):
        for process in psutil.process_iter():
            try:
                process_info = process.as_dict(attrs=['name', 'cmdline'])
                if process_info.get('name') in ('java', 'java.exe'):
                    for cmd_info in process_info.get('cmdline'):
                        if cmd_info == '-Dapp.name=browsermob-proxy':
                            process.kill()
            except psutil.NoSuchProcess:
                pass
if __name__=='__main__':
    try:
        itm = main('http://www.tencent.com/dasdasdas/',None)
        itm.start()
    except Exception,e:
        print e
