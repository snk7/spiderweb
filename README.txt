# forked from https://github.com/rasca11/spiderweb

# r屌大好人，我也要开上挖掘机，挖洞赚钱，迎娶白富美！！！

# Web2.0爬虫说明:
	高效多线程基于web2.0标准url爬取,基于webkit,并且抓取post请求包。
	功能:
		爬取方式:
			带referer、cookie Html A标签多线程抽取
		三种模式:
                        深度爬取
			Json/cgi类站点爬取
			伪静态站点爬取
		Domian url去重保存
		网络请求抓取
		不抓取url黑名单
	需要环境:
		Python2.7 java mysql browsermobproxy PhantomJS
        用到技术：
		Python mysql
	数据库建表:
		*_List_url:
		id url url_re state

        CREATE TABLE data_url
                (id  integer primary key auto_increment ,
                 url TEXT NOT NULL,
	         url_re TEXT NOT NULL,
                 state INT NOT NULL)


		*_net_url
		id url url_re state method.
		
        CREATE TABLE net_url
              (id  integer primary key auto_increment ,
               url TEXT NOT NULL,
	       url_re TEXT NOT NULL,
	       method TEXT NOT NULL,
               state INT NOT NULL)


高效多线程基于web2.0标准url爬取,基于webkit,并且抓取network请求包。

爬取方式
	带referer、cookie Html A标签多线程抽取

三种爬取方式:
		深度爬取(while)
		伪静态取重爬取(re_while)
		Jsonp去重爬取(json_while)
三个结果：
	爬虫爬取页面a标记
	爬虫爬取domian
	Webkit network


# 依赖安装
sudo apt-get install python-dev
sudo pip install psutil
sudo pip install publicsuffix
sudo pip install browsermob-proxy
sudo pip install selenium
sudo pip install BeautifulSoup


Install PhantomJS:
wget https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2
tar xf  phantomjs-2.1.1-linux-x86_64.tar.bz2
sudo mv phantomjs-2.1.1-linux-x86_64 /usr/local/share
sudo ln -s /usr/local/share/phantomjs-2.1.1-linux-x86_64/bin/phantomjs /usr/bin/phantomjs
