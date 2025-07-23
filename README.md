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
```

## 参考

```
https://github.com/langgenius/dify-plugin-sdks/blob/main/python/examples/agent/strategies/ReAct.py
```