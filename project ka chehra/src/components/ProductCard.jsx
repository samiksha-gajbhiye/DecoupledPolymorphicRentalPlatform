import React from 'react';
import { Image } from 'lucide-react';

const ProductCard = ({ product, onClick }) => {
  return (
    <div
      className="bg-white dark:bg-gray-800 rounded-xl shadow-md overflow-hidden hover:shadow-lg transition-shadow cursor-pointer"
      onClick={onClick}
    >
      <div className="aspect-w-16 aspect-h-9">
        <img
          src={product.image || '/placeholder.svg'}
          alt={product.name}
          className="object-cover w-full h-full"
        />
      </div>
      <div className="p-4">
        <h3 className="text-lg font-bold text-gray-900 dark:text-white mb-2">
          {product.name}
        </h3>
        <p className="text-gray-600 dark:text-gray-400 line-clamp-2">
          {product.description || 'No description available'}
        </p>
        <div className="mt-4 flex justify-between items-center">
          <span className="text-xl font-semibold text-blue-600 dark:text-blue-400">
            ₹{product.price || 0}/day
          </span>
          <div className="flex items-center space-x-2 text-sm">
            <Image className="h-4 w-4 text-yellow-400" />
            <span className="text-gray-500 dark:text-gray-400">
              {(product.rating || 0).toFixed(1)}
            </span>
          </div>
        </div>
      </div>
    </div>
  );
};

export default ProductCard;