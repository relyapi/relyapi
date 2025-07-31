'use client';

import { useState } from 'react';

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

interface CardProps {
  data: CardData;
  onLike?: (cardId: string) => void;
  onShare?: (cardId: string) => void;
}

// 平台图标组件
const PlatformIcon = ({ platform }: { platform: string }) => {
  const iconMap = {
    taobao: '🛒',
    facebook: '📘',
    instagram: '📷',
    twitter: '🐦',
    youtube: '📺'
  };
  
  return (
    <span className="text-lg">
      {iconMap[platform as keyof typeof iconMap] || '🌐'}
    </span>
  );
};

// 格式化时间
const formatTimestamp = (timestamp: string) => {
  const date = new Date(timestamp);
  const now = new Date();
  const diffInHours = Math.floor((now.getTime() - date.getTime()) / (1000 * 60 * 60));
  
  if (diffInHours < 1) {
    return '刚刚';
  } else if (diffInHours < 24) {
    return `${diffInHours}小时前`;
  } else {
    const diffInDays = Math.floor(diffInHours / 24);
    return `${diffInDays}天前`;
  }
};

export default function Card({ data, onLike, onShare }: CardProps) {
  const [isLiked, setIsLiked] = useState(false);
  const [likeCount, setLikeCount] = useState(data.likes || 0);
  const [isLoading, setIsLoading] = useState(false);

  const platformColors = {
    taobao: 'bg-orange-500',
    facebook: 'bg-blue-600',
    instagram: 'bg-gradient-to-r from-purple-500 to-pink-500',
    twitter: 'bg-blue-400',
    youtube: 'bg-red-600'
  };

  const handleLike = async () => {
    if (isLoading) return;
    
    setIsLoading(true);
    try {
      const response = await fetch('/api/cards', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          action: 'like',
          cardId: data.id
        })
      });

      if (response.ok) {
        setIsLiked(!isLiked);
        setLikeCount(prev => isLiked ? prev - 1 : prev + 1);
        onLike?.(data.id);
      }
    } catch (error) {
      console.error('Failed to like:', error);
    } finally {
      setIsLoading(false);
    }
  };

  const handleShare = async () => {
    if (isLoading) return;
    
    setIsLoading(true);
    try {
      const response = await fetch('/api/cards', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          action: 'share',
          cardId: data.id
        })
      });

      if (response.ok) {
        onShare?.(data.id);
        // 可以添加分享成功的提示
      }
    } catch (error) {
      console.error('Failed to share:', error);
    } finally {
      setIsLoading(false);
    }
  };

  const handleViewDetails = () => {
    // 在新窗口打开原始链接
    window.open(data.url, '_blank', 'noopener,noreferrer');
  };

  return (
    <div className="bg-white rounded-lg shadow-md hover:shadow-lg transition-all duration-300 overflow-hidden group">
      {/* 平台标识 */}
      <div className={`${platformColors[data.platform]} text-white px-3 py-2 flex items-center gap-2`}>
        <PlatformIcon platform={data.platform} />
        <span className="font-medium capitalize">{data.platform}</span>
      </div>
      
      {/* 图片 */}
      <div className="relative h-48 bg-gray-200 overflow-hidden">
        <div className="absolute inset-0 flex items-center justify-center text-gray-500">
          <span>图片占位符</span>
        </div>
        {/* 悬停效果 */}
        <div className="absolute inset-0 bg-black bg-opacity-0 group-hover:bg-opacity-10 transition-all duration-300"></div>
      </div>
      
      {/* 内容 */}
      <div className="p-4">
        <h3 className="font-bold text-lg mb-2 line-clamp-2 group-hover:text-blue-600 transition-colors duration-200">
          {data.title}
        </h3>
        <p className="text-gray-600 text-sm mb-3 line-clamp-3">{data.description}</p>
        
        {/* 作者和时间 */}
        <div className="flex items-center justify-between text-sm text-gray-500 mb-3">
          <span className="font-medium">{data.author}</span>
          <span>{formatTimestamp(data.timestamp)}</span>
        </div>
        
        {/* 交互按钮 */}
        <div className="flex items-center justify-between mb-3">
          <div className="flex items-center gap-4">
            <button
              onClick={handleLike}
              disabled={isLoading}
              className={`flex items-center gap-1 text-sm transition-colors duration-200 ${
                isLiked ? 'text-red-500' : 'text-gray-600 hover:text-red-500'
              } ${isLoading ? 'opacity-50 cursor-not-allowed' : ''}`}
            >
              <span>{isLiked ? '❤️' : '🤍'}</span>
              <span>{likeCount}</span>
            </button>
            
            {data.shares !== undefined && (
              <button
                onClick={handleShare}
                disabled={isLoading}
                className={`flex items-center gap-1 text-sm text-gray-600 hover:text-blue-500 transition-colors duration-200 ${
                  isLoading ? 'opacity-50 cursor-not-allowed' : ''
                }`}
              >
                <span>🔄</span>
                <span>{data.shares}</span>
              </button>
            )}
          </div>
          
          {data.price && (
            <span className="text-lg font-bold text-orange-600">{data.price}</span>
          )}
        </div>
        
        {/* 查看详情按钮 */}
        <button
          onClick={handleViewDetails}
          className="w-full bg-blue-500 hover:bg-blue-600 text-white py-2 px-4 rounded transition-colors duration-200 font-medium"
        >
          查看详情
        </button>
      </div>
    </div>
  );
}
