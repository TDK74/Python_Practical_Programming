#!/usr/bin/python
# -*- coding: utf-8 -*-

from urllib.parse import *
url = urlparse("http://www.dkws.org.ua:80/index.php;st?param=value#ankor")
url
t = tuple(url)
t
url.scheme, url[0]
url.netloc, url[1]
url.hostname
url.port
url.path
url.params
url.query
url.fragment

t = ('http', 'www.dkws.org.ua', 'index.php', 'par=value', 'ankor')
urlunsplit(t)

from urllib.parse import parse_qs
from urllib.parse import parse_qsl
qs = 's=%D0%A8%D0%B8%D1%84%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B5'
parse_qs(qs, encoding = "cp1251")
parse_qs(qs, encoding = "utf-8")

qs = 'par1=val1&par2=val2'
parse_qs(qs, encoding = "utf-8")
parse_qsl(qs, encoding = "utf-8")

import xml.sax.saxutils as x
x.escape('""<>&""')

from urllib.parse import urljoin
urljoin('http://dkws.org.ua', 'index.php')
urljoin('http://dkws.org.ua', 'index.php', 'test.html')

import chardet
chardet.detect(bytes("Текст", "cp1251"))
