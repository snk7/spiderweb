import socket

import psutil
from browsermobproxy import Server
from selenium import webdriver


class webbrowser:
    def __init__(self, path, url, cookie):
        socket.setdefaulttimeout(10)
        self.url = url
        self.cookie = cookie
        self.path = path
        self.server = Server('browsermob-proxy-2.1.2\\bin\\browsermob-proxy')
        self.server.start()
        self.proxy = self.server.create_proxy()
        cap = webdriver.DesiredCapabilities.PHANTOMJS
        cap["phantomjs.page.settings.resourceTimeout"] = 2000
        cap["phantomjs.page.settings.loadImages"] = False
        cap["phantomjs.page.settings.localToRemoteUrlAccessEnabled"] = True
        cap["phantomjs.page.settings.userAgent"] = (
            "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36")
        service_args = ["--proxy=%s" % self.proxy.proxy, '--ignore-ssl-errors=yes']
        self.driver = webdriver.PhantomJS(service_args=service_args, desired_capabilities=cap)
        self.proxy.new_har(options={'captureContent': True})
        self.driver.get('http://192.168.0.107/xssting/get.html')
        if self.cookie != None:
            for i in self.cookie.split(';'):
                self.driver.execute_script("document.cookie = \"%s\"" % i)

    def gethtml(self, url):
        self.driver.get(url)
        return self.driver.page_source

    def get_network(self):
        all_requests = [entry['request']['url'] for entry in self.proxy.har['log']['entries'] if
                        entry['request']['method'] == 'GET' and entry['response']['status'] == 200]
        for i in self.proxy.har['log']['entries']:
            if i['request']['method'] == 'POST' and entry['response']['status'] == 200:
                postdata = []
                for j in i['request']['postData']['params']:
                    postdata.append(j['name'] + '=' + j['value'])
                data = "&".join(postdata)
                all_requests.append(i['request']['url'] + '||post||' + data)
        print list(set(all_requests))

    def close(self):
        self.driver.quit()
        for process in psutil.process_iter():
            try:
                process_info = process.as_dict(attrs=['name', 'cmdline'])
                if process_info.get('name') in ('java', 'java.exe'):
                    for cmd_info in process_info.get('cmdline'):
                        if cmd_info == '-Dapp.name=browsermob-proxy':
                            process.kill()
            except psutil.NoSuchProcess:
                pass


if __name__ == '__main__':
    p = webbrowser('result/www.tencent.com/', 'http://www.tencent.com/dasdasdas/', 'aaaaa')
    list_url = ['http://www.tencent.com/zh-cn/', 'http://www.tencent.com/zh-cn/ps/ieg.shtml',
                'http://www.tencent.com/zh-cn/ps/ieg.shtml', 'http://www.tencent.com/zh-cn/ir/news/', \
                'http://www.tencent.com/zh-cn/ir/govern.shtml', ' https://www.baidu.com']
    for i in list_url:
        p.gethtml(i)
    p.get_network()
    p.close()
