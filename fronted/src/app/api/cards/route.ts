import { NextRequest, NextResponse } from 'next/server';

// 定义API响应类型
interface ApiCard {
  id: string;
  platform: string;
  title: string;
  description: string;
  imageUrl: string;
  url: string;
  author: string;
  timestamp: string;
  likes?: number;
  shares?: number;
  price?: string;
}

// 模拟从不同平台获取数据的函数
async function fetchFromPlatform(platform: string): Promise<ApiCard[]> {
  // 这里应该是实际的API调用逻辑
  // 通过您的代理服务访问各个平台
  
  const mockResponses: Record<string, ApiCard[]> = {
    taobao: [
      {
        id: 'tb_1',
        platform: 'taobao',
        title: '新款运动鞋',
        description: '透气舒适，适合日常运动和休闲穿着',
        imageUrl: '/api/placeholder/300/200',
        url: 'https://taobao.com/item/tb_1',
        author: '运动装备店',
        timestamp: new Date(Date.now() - 2 * 60 * 60 * 1000).toISOString(),
        likes: 156,
        price: '¥399'
      },
      {
        id: 'tb_2',
        platform: 'taobao',
        title: '智能手表',
        description: '健康监测，运动追踪，长续航',
        imageUrl: '/api/placeholder/300/200',
        url: 'https://taobao.com/item/tb_2',
        author: '智能设备专营',
        timestamp: new Date(Date.now() - 4 * 60 * 60 * 1000).toISOString(),
        likes: 89,
        price: '¥899'
      }
    ],
    facebook: [
      {
        id: 'fb_1',
        platform: 'facebook',
        title: '环保生活小贴士',
        description: '分享一些简单易行的环保生活方式，让我们一起保护地球...',
        imageUrl: '/api/placeholder/300/200',
        url: 'https://facebook.com/post/fb_1',
        author: 'Green Life',
        timestamp: new Date(Date.now() - 3 * 60 * 60 * 1000).toISOString(),
        likes: 234,
        shares: 56
      }
    ],
    instagram: [
      {
        id: 'ig_1',
        platform: 'instagram',
        title: '日落时分',
        description: '今天的日落特别美丽 🌅 #sunset #photography #nature',
        imageUrl: '/api/placeholder/300/200',
        url: 'https://instagram.com/post/ig_1',
        author: 'nature_photographer',
        timestamp: new Date(Date.now() - 1 * 60 * 60 * 1000).toISOString(),
        likes: 445
      }
    ]
  };

  // 模拟网络延迟
  await new Promise(resolve => setTimeout(resolve, 500));
  
  return mockResponses[platform] || [];
}

export async function GET(request: NextRequest) {
  try {
    const { searchParams } = new URL(request.url);
    const platform = searchParams.get('platform');
    const limit = parseInt(searchParams.get('limit') || '10');

    let allCards: ApiCard[] = [];

    if (platform && platform !== 'all') {
      // 获取特定平台的数据
      allCards = await fetchFromPlatform(platform);
    } else {
      // 获取所有平台的数据
      const platforms = ['taobao', 'facebook', 'instagram'];
      const promises = platforms.map(p => fetchFromPlatform(p));
      const results = await Promise.all(promises);
      allCards = results.flat();
    }

    // 按时间排序并限制数量
    const sortedCards = allCards
      .sort((a, b) => new Date(b.timestamp).getTime() - new Date(a.timestamp).getTime())
      .slice(0, limit);

    return NextResponse.json({
      success: true,
      data: sortedCards,
      total: sortedCards.length
    });

  } catch (error) {
    console.error('API Error:', error);
    return NextResponse.json(
      { success: false, error: 'Failed to fetch data' },
      { status: 500 }
    );
  }
}

export async function POST(request: NextRequest) {
  try {
    const body = await request.json();
    const { action, cardId } = body;

    // 处理用户交互（点赞、分享等）
    if (action === 'like') {
      // 这里应该调用您的后端API来处理点赞
      return NextResponse.json({
        success: true,
        message: 'Liked successfully'
      });
    }

    if (action === 'share') {
      // 处理分享逻辑
      return NextResponse.json({
        success: true,
        message: 'Shared successfully'
      });
    }

    return NextResponse.json(
      { success: false, error: 'Invalid action' },
      { status: 400 }
    );

  } catch (error) {
    console.error('API Error:', error);
    return NextResponse.json(
      { success: false, error: 'Failed to process request' },
      { status: 500 }
    );
  }
}
