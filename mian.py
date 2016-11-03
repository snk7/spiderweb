# coding: utf-8
import os
from urlparse import urlparse


class main:
    def __init__(self, domian):
        self.url = domian
        domain = urlparse(domian)
        self.new_path = os.path.join('result', domain.netloc)
        if not os.path.isdir(self.new_path):
            os.makedirs(self.new_path)
        domain = domain.netloc.split('.')
        self.domain = domain[-2] + '.' + domain[-1]

    def start(self):
        print self.url
        print self.get_domain()

    def get_domain(self):
        # domain=urlparse(self.domain).netloc.split('.')
        # domain.netloc.split('.')
        return self.domain


if __name__ == '__main__':
    itm = main('http://www.tencent.com/dasdasdas/')
    itm.start()
