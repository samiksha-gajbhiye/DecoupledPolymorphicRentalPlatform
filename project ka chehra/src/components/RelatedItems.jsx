import ProductCard from './ProductCard';

const RelatedItems = ({ product }) => {
  // Sample related items - in real app this would come from API based on category
  const relatedItems = [
    {
      id: 301,
      name: "Mirrorless Camera Bundle",
      category: "Cameras",
      location: "New York, NY",
      rating: 4.7,
      price: 65,
      image: "https://images.unsplash.com/photo-1550583724-b2692b85b150?w=400",
      availability: "Available",
      verified: true
    },
    {
      id: 302,
      name: "GoPro Action Camera Kit",
      category: "Cameras",
      location: "Brooklyn, NY",
      rating: 4.8,
      price: 40,
      image: "https://images.unsplash.com/photo-1526170375885-4d8ecf77b99f?w=400",
      availability: "Available",
      verified: false
    },
    {
      id: 303,
      name: "Camera Lighting Kit",
      category: "Cameras",
      location: "Queens, NY",
      rating: 4.6,
      price: 30,
      image: "https://images.unsplash.com/photo-1502920947138-1931412dd77c?w=400",
      availability: "Available",
      verified: true
    }
  ];

  return (
    <div className="border-t border-gray-200 dark:border-gray-700 pt-8">
      <h2 className="text-xl font-bold text-gray-900 dark:text-white mb-6">
        You might also like
      </h2>
      <div className="grid gap-6 sm:grid-cols-2 lg:grid-cols-4">
        {relatedItems.map(item => (
          <ProductCard key={item.id} product={item} />
        ))}
      </div>
    </div>
  );
};

export default RelatedItems;