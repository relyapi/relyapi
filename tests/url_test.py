import tldextract

host = 'https://h5api.m.taobao.com/h5/mtop.tmall.kangaroo.core.service.route.aldlampservicefixedresv2/1.0/?jsv=2.7.5&appKey=12574478&t=1753276697714&sign=3d97061d619adc402348e798eddf78d2&type=originaljson&v=1.0&api=mtop.tmall.kangaroo.core.service.route.aldlampservicefixedresv2&dataType=jsonp'
result = tldextract.extract(host)
print(result.__dict__)
