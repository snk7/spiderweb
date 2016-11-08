class filter_main:
    def __init__(self,list_url):
        self.list_url=list_url
    def scheduler(self):
        for i in self.list_url:
            print i
if __name__ == '__main__':
    liststr=[u'http://imgcache.qq.com/ac/www_tencent/zh-cn/scripts/menu.js', u'http://www.tencent.com/styles/ps.css',
     u'http://www.tencent.com/zh-cn/', u'http://www.tencent.com/styles/homepage.css',
     u'http://imgcache.qq.com/ac/www_tencent/public/scripts/menu/steffie.js',
     u'http://www.tencent.com/scripts/breadcrumb.js', u'http://www.tencent.com/zh-cn/ps/ieg.shtml',
     u'http://imgcache.qq.com/ac/www_tencent/public/scripts/menu/stmenu.js',
     u'http://jqmt.qq.com/cdn_dianjiliu.js?a=0.7674563738983124', u'http://www.tencent.com/styles/global.css',
     u'http://www.tencent.com/zh-cn/ir/news/', u'http://www.tencent.com/styles/ir.css',
     u'http://jsqmt.qq.com/cdn_djl.js', u'http://www.tencent.com/zh-cn/ir/news/2016.shtml',
     u'http://www.tencent.com/scripts/local.js', u'http://imgcache.qq.com/ac/www_tencent/public/scripts/menu/stcode.js',
     u'http://pingjs.qq.com/tcss.ping.js', u'http://jqmt.qq.com/cdn_dianjiliu.js?a=0.5768777495250106',
     u'http://imgcache.qq.com/ac/www_tencent/public/scripts/menu/steffslip.js',
     u'http://jqmt.qq.com/cdn_dianjiliu.js?a=0.31197135196998715', u'http://www.tencent.com/zh-cn/ir/govern.shtml',
     u'http://imgcache.qq.com/ac/www_tencent/public/scripts/menu/steffrect.js',
     u'http://imgcache.qq.com/ac/www_tencent/public/scripts/MSIE.PNG.js']
    p1=filter_main(liststr)
    p1.scheduler()