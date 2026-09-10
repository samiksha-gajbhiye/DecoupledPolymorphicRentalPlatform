import { useState } from 'react';

const CategorySelector = ({ categories }) => {
  const [selectedCategory, setSelectedCategory] = useState('All');

  return (
    <div className="flex flex-wrap gap-2">
      <button
        onClick={() => setSelectedCategory('All')}
        className={`px-4 py-2 text-sm font-medium ${selectedCategory === 'All' ? 'bg-blue-600 text-white' : 'bg-gray-200 hover:bg-gray-300 dark:bg-gray-700 dark:hover:bg-gray-600 dark:text-white'} rounded-full transition-colors`}
      >
        All Categories
      </button>
      {categories.map((category) => (
        <button
          key={category}
          onClick={() => setSelectedCategory(category)}
          className={`px-4 py-2 text-sm font-medium ${selectedCategory === category ? 'bg-blue-600 text-white' : 'bg-gray-200 hover:bg-gray-300 dark:bg-gray-700 dark:hover:bg-gray-600 dark:text-white'} rounded-full transition-colors`}
        >
          {category}
        </button>
      ))}
    </div>
  );
};

export default CategorySelector;