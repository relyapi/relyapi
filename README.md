# RelyApi

## 规划

```
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

## bak

```
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