import ProductCard from '../ProductCard';

const PopularRentals = () => {
  // Sample data for popular rentals
  const popularItems = [
    {
      id: 1,
      name: "Professional DSLR Camera Kit",
      category: "Cameras",
      location: "New York, NY",
      rating: 4.9,
      price: 75,
      image: "https://images.unsplash.com/photo-1526170375885-4d8ecf77b99f?w=400",
      availability: "Available",
      verified: true
    },
    {
      id: 2,
      name: "Electric Scooter",
      category: "Vehicles",
      location: "Los Angeles, CA",
      rating: 4.7,
      price: 35,
      image: "https://images.unsplash.com/photo-1544538461-8b8a5ee303f6?w=400",
      availability: "Available",
      verified: true
    },
    {
      id: 3,
      name: "Modern Sofa Set",
      category: "Furniture",
      location: "Chicago, IL",
      rating: 4.8,
      price: 60,
      image: "https://images.unsplash.com/photo-1555041469-a586c61ea9bc?w=400",
      availability: "Available",
      verified: false
    },
    {
      id: 4,
      name: "Power Tool Kit",
      category: "Tools",
      location: "Houston, TX",
      rating: 4.6,
      price: 45,
      image: "https://images.unsplash.com/photo-1581091853897-d36451e25e44?w=400",
      availability: "Available",
      verified: true
    }
  ];

  return (
    <section className="py-16 bg-white dark:bg-gray-900">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <h2 className="text-2xl font-bold text-gray-900 dark:text-white mb-8">
          Popular Rentals
        </h2>
        <div className="grid gap-6 sm:grid-cols-2 lg:grid-cols-4">
          {popularItems.map(item => (
            <ProductCard key={item.id} product={item} />
          ))}
        </div>
      </div>
    </section>
  );
};

export default PopularRentals;