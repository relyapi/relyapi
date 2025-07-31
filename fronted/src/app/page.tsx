'use client';

import { useState, useEffect } from 'react';
import Card from '@/components/Card';
import LoadingSpinner from '@/components/LoadingSpinner';

// 定义卡片数据类型
interface CardData {
  id: string;
  platform: 'taobao' | 'facebook' | 'instagram' | 'twitter' | 'youtube';
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

export default function Home() {
  const [cards, setCards] = useState<CardData[]>([]);
  const [loading, setLoading] = useState(true);
  const [selectedPlatform, setSelectedPlatform] = useState<string>('all');

  // 获取数据
  const fetchData = async (platform: string = 'all') => {
    setLoading(true);
    try {
      const response = await fetch(`/api/cards?platform=${platform}&limit=20`);
      const result = await response.json();
      
      if (result.success) {
        setCards(result.data);
      } else {
        console.error('Failed to fetch data:', result.error);
      }
    } catch (error) {
      console.error('Error fetching data:', error);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchData(selectedPlatform);
  }, [selectedPlatform]);

  // 处理点赞
  const handleLike = (cardId: string) => {
    console.log('Liked card:', cardId);
  };

  // 处理分享
  const handleShare = (cardId: string) => {
    console.log('Shared card:', cardId);
  };

  // 刷新数据
  const handleRefresh = () => {
    fetchData(selectedPlatform);
  };

  // 过滤卡片
  const filteredCards = selectedPlatform === 'all' 
    ? cards 
    : cards.filter(card => card.platform === selectedPlatform);

  const platforms = ['all', 'taobao', 'facebook', 'instagram', 'twitter', 'youtube'];

  return (
    <div className="min-h-screen bg-gray-50">
      {/* 头部 */}
      <header className="bg-white shadow-sm">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6">
          <div className="flex items-center justify-between">
            <div>
              <h1 className="text-3xl font-bold text-gray-900">API聚合服务</h1>
              <p className="text-gray-600 mt-1">展示来自多个平台的精彩内容</p>
            </div>
            <div className="flex items-center gap-4">
              <button
                onClick={handleRefresh}
                disabled={loading}
                className="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600 disabled:opacity-50 disabled:cursor-not-allowed transition-colors duration-200"
              >
                {loading ? '刷新中...' : '刷新'}
              </button>
              <span className="text-sm text-gray-500">
                共 {filteredCards.length} 条内容
              </span>
            </div>
          </div>
        </div>
      </header>

      {/* 过滤器 */}
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6">
        <div className="flex flex-wrap gap-2">
          {platforms.map(platform => (
            <button
              key={platform}
              onClick={() => setSelectedPlatform(platform)}
              className={`px-4 py-2 rounded-full text-sm font-medium transition-colors duration-200 ${
                selectedPlatform === platform
                  ? 'bg-blue-500 text-white'
                  : 'bg-white text-gray-700 hover:bg-gray-100'
              }`}
            >
              {platform === 'all' ? '全部' : platform.charAt(0).toUpperCase() + platform.slice(1)}
            </button>
          ))}
        </div>
      </div>

      {/* 内容区域 */}
      <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pb-12">
        {loading ? (
          <LoadingSpinner text="正在加载内容..." />
        ) : (
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
            {filteredCards.map(card => (
              <Card 
                key={card.id} 
                data={card} 
                onLike={handleLike}
                onShare={handleShare}
              />
            ))}
          </div>
        )}

        {!loading && filteredCards.length === 0 && (
          <div className="text-center py-12">
            <p className="text-gray-500 text-lg">暂无内容</p>
          </div>
        )}
      </main>

      {/* 底部 */}
      <footer className="bg-white border-t">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6">
          <div className="text-center text-gray-500 text-sm">
            <p>© 2024 API聚合服务. 通过代理访问多平台内容.</p>
          </div>
        </div>
      </footer>
    </div>
  );
}
