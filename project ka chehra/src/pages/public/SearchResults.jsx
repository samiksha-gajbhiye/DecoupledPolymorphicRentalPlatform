import ProductCard from '../../components/ProductCard';
import SearchBar from '../../components/SearchBar';
import SortSelector from '../../components/SortSelector';
import FiltersSidebar from '../../components/FiltersSidebar';

const SearchResults = () => {
  // Sample search results data
  const results = [
    {
      id: 201,
      name: "GoPro Hero 11 Bundle",
      category: "Cameras",
      location: "San Diego, CA",
      rating: 4.8,
      price: 50,
      image: "https://images.unsplash.com/photo-1526170375885-4d8ecf77b99f?w=400",
      availability: "Available",
      verified: true
    },
    {
      id: 202,
      name: "Mountain Bike",
      category: "Sports Equipment",
      location: "Portland, OR",
      rating: 4.6,
      price: 40,
      image: "https://images.unsplash.com/photo-1518248125592-2b67025e5d83?w=400",
      availability: "Available",
      verified: true
    },
    {
      id: 203,
      name: "Nintendo Switch Console",
      category: "Electronics",
      location: "Boston, MA",
      rating: 4.9,
      price: 35,
      image: "https://images.unsplash.com/photo-1601233272723-31d34574b9cb?w=400",
      availability: "Available",
      verified: false
    }
  ];

  return (
    <div className="min-h-screen bg-gray-50 dark:bg-gray-900">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        <div className="mb-8">
          <h1 className="text-2xl font-bold text-gray-900 dark:text-white">
            Search Results
          </h1>
          <p className="text-gray-600 dark:text-gray-300 mt-2">
            Found {results.length} items for your search
          </p>
        </div>
        <SearchBar />

        <div className="mt-8 flex flex-col lg:flex-row lg:gap-8">
          {/* Filters Sidebar */}
          <FiltersSidebar className="lg:w-64" />

          {/* Results */}
          <div className="flex-1">
            <div className="mb-6 flex flex-col sm:flex-row sm:items-center sm:justify-between">
              <div className="mb-4 sm:mb-0">
                <p className="text-gray-500 dark:text-gray-400">
                  Showing {results.length} results
                </p>
              </div>
              <SortSelector />
            </div>

            <div className="grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
              {results.map(item => (
                <ProductCard key={item.id} product={item} />
              ))}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default SearchResults;