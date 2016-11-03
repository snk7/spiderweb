# coding: utf-8
import urlparse


class filteurl:
    def __init__(self, url):
        self.url = url

    def judgetype(self, strs):
        try:
            int(strs)
            return 'int'
        except:
            return 'str'

    def json_filte(self):
        urls = urlparse.urlparse(self.url)
        liststr = []
        try:
            for i in urls.query.split('&'):
                para = i.split('=')
                length_int = len(para[1])
                if self.judgetype(para[1]) == 'int':
                    para[1] = 'int[%s]' % length_int
                else:
                    para[1] = 'str[%s]' % length_int
                para = '='.join(para)
                liststr.append(para)
            url_paras = '&'.join(liststr)
            return urls.scheme + '://' + urls.netloc + urls.path + '?' + url_paras
        except:
            length_int = len(urls.query)
            url_paras = self.judgetype(urls.query) + '[%s]' % length_int
            return urls.scheme + '://' + urls.netloc + urls.path + '?' + url_paras

    def Pseudo_static_filte(self):
        url = self.url
        urls = urlparse.urlparse(url)
        if urls.query != '':
            url = self.json_filte()
        urls = urlparse.urlparse(url)
        pathlist = urls.path
        pathlisted = []
        for i in pathlist:
            if i == '/':
                pathlisted.append(i)
            pathlisted.append(self.judgetype(i))
        # print pathlisted
        # print ''.join(pathlisted)
        if urls.query != '':
            return urls.scheme + '://' + urls.netloc + ','.join(pathlisted) + '?' + urls.query
        else:
            return urls.scheme + '://' + urls.netloc + ','.join(pathlisted)


if __name__ == '__main__':
    urlss = 'http://www.mianxian.gov.cn/zxft/20483.htm?dsdsa'
    p = filteurl(urlss)
    print p.Pseudo_static_filte()
