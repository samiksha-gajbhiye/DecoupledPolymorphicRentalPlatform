import { useEffect, useMemo, useState } from 'react';
import { useSearchParams } from 'react-router-dom';
import ProductCard from '../../components/ProductCard';
import SearchBar from '../../components/SearchBar';
import SortSelector from '../../components/SortSelector';
import FiltersSidebar from '../../components/FiltersSidebar';
import { getAllProducts, resolveImageUrl } from '../../api/productApi';
import { rankProducts } from '../../utils/search';

const toCardModel = (product) => ({
  id: product.productId,
  name: product.title,
  description: product.description,
  category: product.category?.name || 'Uncategorized',
  location: product.location,
  rating: product.rating ?? 0,
  price: product.pricePerDay,
  image: resolveImageUrl(product.images?.[0]?.imageUrl) || 'https://images.unsplash.com/photo-1526170375885-4d8ecf77b99f?w=400',
  availability: product.availability,
  verified: product.verified,
});

const SearchResults = () => {
  const [params] = useSearchParams();
  const query = params.get('q') || '';
  const location = params.get('location') || '';

  const [products, setProducts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    getAllProducts()
      .then(setProducts)
      .catch(() => setError('Could not load rentals. Is the backend running on port 8080?'))
      .finally(() => setLoading(false));
  }, []);

  const { matches, similar } = useMemo(
    () => rankProducts(query, products, location),
    [query, location, products]
  );

  const label = [query && `"${query}"`, location && `in ${location}`].filter(Boolean).join(' ');

  return (
    <div className="min-h-screen bg-gray-50 dark:bg-gray-900">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        <div className="mb-8">
          <h1 className="text-2xl font-bold text-gray-900 dark:text-white">
            Search Results
          </h1>
          <p className="text-gray-600 dark:text-gray-300 mt-2">
            {loading
              ? 'Searching...'
              : `Found ${matches.length} item${matches.length === 1 ? '' : 's'}${label ? ` for ${label}` : ''}`}
          </p>
        </div>
        <SearchBar />

        {error && (
          <div className="mt-6 bg-red-50 dark:bg-red-900/20 text-red-500 dark:text-red-400 px-4 py-3 rounded-md">
            {error}
          </div>
        )}

        <div className="mt-8 flex flex-col lg:flex-row lg:gap-8">
          <FiltersSidebar className="lg:w-64" />

          <div className="flex-1">
            <div className="mb-6 flex flex-col sm:flex-row sm:items-center sm:justify-between">
              <div className="mb-4 sm:mb-0">
                <p className="text-gray-500 dark:text-gray-400">
                  Showing {matches.length} results
                </p>
              </div>
              <SortSelector />
            </div>

            {!loading && !error && matches.length === 0 && (
              <p className="text-gray-500 dark:text-gray-400 mb-6">
                No exact matches{similar.length > 0 ? ' — here are some similar items.' : ' found. Try a different word.'}
              </p>
            )}

            <div className="grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
              {matches.map((item) => (
                <ProductCard key={item.productId} product={toCardModel(item)} />
              ))}
            </div>

            {similar.length > 0 && (
              <div className="mt-12">
                <h2 className="text-xl font-bold text-gray-900 dark:text-white mb-4">
                  Similar items you may like
                </h2>
                <div className="grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
                  {similar.map((item) => (
                    <ProductCard key={item.productId} product={toCardModel(item)} />
                  ))}
                </div>
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  );
};

export default SearchResults;