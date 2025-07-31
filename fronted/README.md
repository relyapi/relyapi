# API聚合服务前端

这是一个基于Next.js开发的API聚合服务前端应用，用于展示来自淘宝、Facebook、Instagram等多个平台的内容卡片。

## 功能特性

- 🎨 现代化的卡片展示界面
- 🔍 平台过滤功能（支持淘宝、Facebook、Instagram、Twitter、YouTube）
- ❤️ 交互功能（点赞、分享、查看详情）
- 📱 响应式设计，支持多种设备
- 🚀 基于Next.js 15和Tailwind CSS v4
- 🐳 Docker容器化部署

## 技术栈

- **前端框架**: Next.js 15 with App Router
- **样式**: Tailwind CSS v4
- **语言**: TypeScript
- **API**: Next.js API Routes
- **容器化**: Docker & Docker Compose

## 快速开始

### 本地开发

1. 安装依赖：
```bash
npm install
```

2. 启动开发服务器：
```bash
npm run dev
```

3. 打开浏览器访问 [http://localhost:3000](http://localhost:3000)

### Docker部署

#### 方式一：使用Docker Compose（推荐）

1. 构建并启动服务：
```bash
docker-compose up -d --build
```

2. 访问应用：
```bash
open http://localhost:3000
```

3. 查看日志：
```bash
docker-compose logs -f frontend
```

4. 停止服务：
```bash
docker-compose down
```

#### 方式二：直接使用Docker

1. 构建镜像：
```bash
docker build -t api-aggregator-frontend .
```

2. 运行容器：
```bash
docker run -p 3000:3000 --name api-frontend api-aggregator-frontend
```

3. 查看容器日志：
```bash
docker logs -f api-frontend
```

4. 停止容器：
```bash
docker stop api-frontend
docker rm api-frontend
```

### 生产环境部署

1. 构建生产镜像：
```bash
docker build -t api-aggregator-frontend:latest .
```

2. 推送到镜像仓库（可选）：
```bash
docker tag api-aggregator-frontend:latest your-registry/api-aggregator-frontend:latest
docker push your-registry/api-aggregator-frontend:latest
```

3. 在生产服务器上运行：
```bash
docker run -d \
  --name api-aggregator-frontend \
  -p 3000:3000 \
  --restart unless-stopped \
  api-aggregator-frontend:latest
```

## 项目结构

```
├── src/
│   ├── app/
│   │   ├── page.tsx          # 主页面
│   │   ├── layout.tsx        # 根布局
│   │   ├── globals.css       # 全局样式
│   │   └── api/cards/        # API路由
│   └── components/
│       ├── Card.tsx          # 卡片组件
│       └── LoadingSpinner.tsx # 加载组件
├── Dockerfile                # Docker构建文件
├── docker-compose.yml        # Docker Compose配置
├── .dockerignore            # Docker忽略文件
└── next.config.ts           # Next.js配置
```

## API接口

### 获取卡片数据
```
GET /api/cards?platform={platform}&limit={limit}
```

参数：
- `platform`: 平台名称（all, taobao, facebook, instagram, twitter, youtube）
- `limit`: 返回数量限制（默认10）

### 用户交互
```
POST /api/cards
```

请求体：
```json
{
  "action": "like|share",
  "cardId": "card_id"
}
```

## 环境变量

| 变量名 | 描述 | 默认值 |
|--------|------|--------|
| `NODE_ENV` | 运行环境 | `production` |
| `PORT` | 服务端口 | `3000` |
| `NEXT_TELEMETRY_DISABLED` | 禁用遥测 | `1` |

## 开发指南

### 添加新平台

1. 在 `src/app/api/cards/route.ts` 中添加新平台的模拟数据
2. 在 `src/components/Card.tsx` 中添加平台图标和颜色
3. 在 `src/app/page.tsx` 中添加过滤选项

### 集成真实API

将 `src/app/api/cards/route.ts` 中的模拟数据替换为对您实际代理服务的调用：

```typescript
async function fetchFromPlatform(platform: string): Promise<ApiCard[]> {
  const response = await fetch(`${process.env.API_BASE_URL}/${platform}`);
  return response.json();
}
```

## 性能优化

- 使用Next.js的Image组件优化图片加载
- 实现数据缓存机制
- 添加服务端渲染（SSR）或静态生成（SSG）
- 使用CDN加速静态资源

## 监控和日志

建议在生产环境中添加：
- 应用性能监控（APM）
- 错误追踪
- 访问日志分析
- 健康检查端点

## 故障排除

### Docker构建失败

如果遇到构建错误，请尝试以下解决方案：

1. **清理Docker缓存**：
```bash
docker system prune -a
```

2. **重新构建镜像**：
```bash
docker-compose build --no-cache
```

3. **检查Node.js版本兼容性**：
确保使用Node.js 18+版本

4. **检查依赖安装**：
```bash
# 本地测试构建
npm ci
npm run build
```

### 常见问题

**Q: 应用启动后无法访问**
A: 检查端口是否被占用，或尝试使用不同端口：
```bash
docker run -p 3001:3000 api-aggregator-frontend
```

**Q: CSS样式不生效**
A: 确保Tailwind CSS配置正确，重新构建镜像

**Q: API调用失败**
A: 检查网络连接和API端点配置

## 许可证

MIT License

## 贡献

欢迎提交Issue和Pull Request来改进这个项目。
