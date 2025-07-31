# RelyApi

## 支持

```
# 部分不能开headless

# 使用定制版的指纹浏览器  打包到镜像  借鉴neko镜像

# 五秒盾

# medium
https://freedium.cfd/https://medium.com/the-riff/ozzy-osbourne-legacy-of-a-madman-264a0a6c30c5

# zhihu

# 公众号
https://mp.weixin.qq.com/s/NZej8tbY6Hau6STH_xmYsQ

# 抖音

# 航空
https://www.jetblue.com/booking/flights?from=HKG&to=HBE&depart=2025-07-28&return=2025-08-27&isMultiCity=false&noOfRoute=1&adults=1&children=0&infants=0&sharedMarket=false&roundTripFaresFlag=false&usePoints=true
https://github.com/PanGuBase/cdp-navigate/blob/main/note.md
https://www.vietjetair.com/zh-tw
```

## 规划

```
geoip 判断ip归属

---
1. 统计 失败 成功  普罗米
2. 免费提供代理 按地级市
3. 插件管理

---
1. 解析器注册 拆分？ serverless
    1. 异步/同步支持  只有get/post
    2. 高性能转发
    
2. 设备管理服务
    1. socket.io 承接  如果出现验证码 自动进行滑动
    2. 账号管理 登录
    
3. 方案
    1. 使用sererless
    2. 使用类似dify的插件机制
    3. 如果遇到验证码 自动发送到 socket.io  socket.io 记录
    
4. mqtt 短信服务

5. 支持
    1. 支持tsl
    2. 自动代理服务
    3. 账号服务
    
 6. server
    1. 代理等 通过server下发到worker
```

## 思路

```
# server支持创建指纹浏览器  云手机  可以进行远程登录等  chrome android

# 提供 x-rely-city 精确地级市 免费提供带来
# 插件需要完成  签名处理和cookie替换
# 请求失败 会通知服务商  不在链接 socketio server  进行回调通知
# 可以禁用爬虫  使用 socket.io   失败上报 成功上报 使用 socket.io ?
# 管理后台配置  取那个地区的代理IP

# 走账号代理池   看是否可以借鉴 openclash 进行代理  根据域名进行自动路由
# 基于 clash 进行二次开发
# 使用隧道代理 封装隧道代理 根据用户名自行返回代理
# 不使用tls直接配置代理
# 只有 use_proxy为true 才会查询代理 如果 use_proxy为false proxy直接返回空
# 直接存储在内存 server只有一个  根据域名以及策略   domain + interface + account
# 注意 如果涉及到 cookie 和 ip 绑定的情况  如何处理
# 外部 http 指定需要那个账户  x-rely-account=xxx
# 代理ip有一定的下发策略   主动查询？？ gin提供


# 按域名配置开关 代理
# 将数据再次转发到serverless进行处理
# 提供插件 那么就是 header信息的填充
# tls统一进行处理修改 借鉴 https://curl-cffi.readthedocs.io/en/latest/impersonate.html
# https://github.com/vgavro/httpx-curl-cffi
```

## 参考

```
https://github.com/miguelgrinberg/python-socketio
https://github.com/langgenius/dify-plugin-sdks/blob/main/python/examples/agent/strategies/ReAct.py
```