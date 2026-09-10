import { useEffect, useState } from 'react';
import ProductCard from '../../components/ProductCard';
import SearchBar from '../../components/SearchBar';
import CategorySelector from '../../components/CategorySelector';
import { getAllProducts, resolveImageUrl } from '../../api/productApi';

const toCardModel = (product) => ({
  id: product.productId,
  name: product.title,
  category: product.category?.name || 'Uncategorized',
  location: product.location,
  rating: product.rating ?? 0,
  price: product.pricePerDay,
  image: resolveImageUrl(product.images?.[0]?.imageUrl) || 'https://images.unsplash.com/photo-1526170375885-4d8ecf77b99f?w=400',
  availability: product.availability,
  verified: product.verified,
});

const BrowseRentals = () => {
  const [rentals, setRentals] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    const fetchProducts = async () => {
      try {
        const data = await getAllProducts();
        setRentals(data.map(toCardModel));
      } catch (err) {
        setError('Could not load rentals. Is the backend running on port 8080?');
      } finally {
        setLoading(false);
      }
    };
    fetchProducts();
  }, []);

  return (
    <div className="min-h-screen bg-gray-50 dark:bg-gray-900">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        <h1 className="text-2xl font-bold text-gray-900 dark:text-white mb-6">
          Browse All Rentals
        </h1>
        <SearchBar />
        <div className="mt-6 flex flex-col sm:flex-row sm:items-center sm:justify-between">
          <div className="mb-4 sm:mb-0">
            <p className="text-gray-500 dark:text-gray-400">
              {loading ? 'Loading...' : `Showing ${rentals.length} items`}
            </p>
          </div>
          <CategorySelector
            categories={['All Categories','Electronics','Vehicles','Furniture','Tools','Cameras','Sports Equipment','Appliances','Event Equipment','Other']}
          />
        </div>
        {error && (
          <div className="mt-6 bg-red-50 dark:bg-red-900/20 text-red-500 dark:text-red-400 px-4 py-3 rounded-md">
            {error}
          </div>
        )}
        {!loading && !error && rentals.length === 0 && (
          <p className="mt-8 text-gray-500 dark:text-gray-400">
            No products yet — go add one from the Owner dashboard.
          </p>
        )}
        <div className="mt-8 grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
          {rentals.map(item => <ProductCard key={item.id} product={item} />)}
        </div>
      </div>
    </div>
  );
};

export default BrowseRentals;