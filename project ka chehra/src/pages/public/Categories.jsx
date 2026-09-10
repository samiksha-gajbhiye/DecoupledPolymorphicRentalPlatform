import { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { getAllCategories } from '../../api/categoryApi';

const Categories = () => {
  const [categories, setCategories] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const navigate = useNavigate();

  useEffect(() => {
    const fetchCategories = async () => {
      try {
        const data = await getAllCategories();
        setCategories(data);
      } catch (err) {
        setError('Could not load categories. Is the backend running on port 8080?');
      } finally {
        setLoading(false);
      }
    };
    fetchCategories();
  }, []);

  return (
    <div className="min-h-screen bg-gray-50 dark:bg-gray-900">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        <h1 className="text-2xl font-bold text-gray-900 dark:text-white mb-6">
          Browse by Category
        </h1>

        {loading && <p className="text-gray-500 dark:text-gray-400">Loading categories...</p>}

        {error && (
          <div className="bg-red-50 dark:bg-red-900/20 text-red-500 dark:text-red-400 px-4 py-3 rounded-md">
            {error}
          </div>
        )}

        {!loading && !error && categories.length === 0 && (
          <p className="text-gray-500 dark:text-gray-400">
            No categories have been set up yet.
          </p>
        )}

        <div className="mt-4 grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
          {categories.map((category) => (
            <div
              key={category.categoryId}
              onClick={() => navigate(`/browse?category=${encodeURIComponent(category.name)}`)}
              className="bg-white dark:bg-gray-800 rounded-xl shadow-md p-6 hover:shadow-lg transition-shadow cursor-pointer"
            >
              <h3 className="text-lg font-bold text-gray-900 dark:text-white mb-2">
                {category.name}
              </h3>
              <p className="text-gray-600 dark:text-gray-400 line-clamp-2">
                {category.description || 'No description available'}
              </p>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default Categories;