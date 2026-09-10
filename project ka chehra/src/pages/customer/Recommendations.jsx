import ProductCard from '../../components/ProductCard';

const Recommendations = () => {
  // Sample AI-powered recommendations
  const recommendations = [
    {
      id: 701,
      name: "4K Mirrorless Camera Bundle",
      category: "Cameras",
      location: "San Francisco, CA",
      rating: 4.9,
      price: 90,
      image: "https://images.unsplash.com/photo-1550583724-b2692b85b150?w=400",
      availability: "Available",
      verified: true,
      reason: "Based on your interest in photography equipment"
    },
    {
      id: 702,
      name: "Professional Drone Kit",
      category: "Electronics",
      location: "Austin, TX",
      rating: 4.8,
      price: 120,
      image: "https://images.unsplash.com/photo-1526251410205-396d62992d57?w=400",
      availability: "Available",
      verified: true,
      reason: "Popular with users who rented camera gear"
    },
    {
      id: 703,
      name: "Ergonomic Home Office Setup",
      category: "Furniture",
      location: "Seattle, WA",
      rating: 4.7,
      price: 80,
      image: "https://images.unsplash.com/photo-1586190848861-99aa4a171e90?w=400",
      availability: "Available",
      verified: false,
      reason: "Trending in your area"
    },
    {
      id: 704,
      name: "GoPro Action Camera Kit",
      category: "Cameras",
      location: "Miami, FL",
      rating: 4.6,
      price: 40,
      image: "https://images.unsplash.com/photo-1526170375885-4d8ecf77b99f?w=400",
      availability: "Available",
      verified: false,
      reason: "Users like you also rented this"
    }
  ];

  return (
    <div className="min-h-screen bg-gray-50 dark:bg-gray-900">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <div className="mb-6">
          <h1 className="text-2xl font-bold text-gray-900 dark:text-white">
            Recommendations
          </h1>
          <p className="text-gray-600 dark:text-gray-300">
            Personalized suggestions based on your activity and preferences
          </p>
        </div>

        <div className="grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
          {recommendations.map(item => (
            <ProductCard key={item.id} product={item} />
          ))}
        </div>
      </div>
    </div>
  );
};

export default Recommendations;