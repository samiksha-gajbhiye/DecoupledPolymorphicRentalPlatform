import ProductCard from '../ProductCard';

const AIRecommendations = () => {
  // Sample data for AI recommendations
  const recommendedItems = [
    {
      id: 101,
      name: "4K Mirrorless Camera Bundle",
      category: "Cameras",
      location: "San Francisco, CA",
      rating: 4.9,
      price: 90,
      image: "https://images.unsplash.com/photo-1550583724-b2692b85b150?w=400",
      availability: "Available",
      verified: true
    },
    {
      id: 102,
      name: "Professional Drone Kit",
      category: "Electronics",
      location: "Austin, TX",
      rating: 4.8,
      price: 120,
      image: "https://images.unsplash.com/photo-1526251410205-396d62992d57?w=400",
      availability: "Available",
      verified: true
    },
    {
      id: 103,
      name: "Ergonomic Home Office Setup",
      category: "Furniture",
      location: "Seattle, WA",
      rating: 4.7,
      price: 80,
      image: "https://images.unsplash.com/photo-1586190848861-99aa4a171e90?w=400",
      availability: "Available",
      verified: false
    }
  ];

  return (
    <section className="py-16 bg-gray-50 dark:bg-gray-900">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <h2 className="text-2xl font-bold text-gray-900 dark:text-white mb-8">
          Recommended For You
        </h2>
        <p className="text-gray-600 dark:text-gray-300 mb-8 max-w-xl">
          Based on your browsing history and preferences, we think you'll love these items.
        </p>
        <div className="grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
          {recommendedItems.map(item => (
            <ProductCard key={item.id} product={item} />
          ))}
        </div>
      </div>
    </section>
  );
};

export default AIRecommendations;