import ProductCard from '../../components/ProductCard';

const Wishlist = () => {
  const wishlistItems = [
    {
      id: 501,
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
      id: 502,
      name: "Vintage Record Player",
      category: "Electronics",
      location: "Atlanta, GA",
      rating: 4.6,
      price: 25,
      image: "https://images.unsplash.com/photo-1589435580252-28c24fd24bce?w=400",
      availability: "Available",
      verified: false
    },
    {
      id: 503,
      name: "Portable Projector",
      category: "Event Equipment",
      location: "Denver, CO",
      rating: 4.7,
      price: 45,
      image: "https://images.unsplash.com/photo-1518770664339-911aa2b4f3a5?w=400",
      availability: "Available",
      verified: true
    }
  ];

  return (
    <div className="min-h-screen bg-gray-50 dark:bg-gray-900">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <div className="mb-6">
          <h1 className="text-2xl font-bold text-gray-900 dark:text-white">
            My Wishlist
          </h1>
          <p className="text-gray-600 dark:text-gray-300">
            Save items you want to rent later
          </p>
        </div>

        <div className="grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
          {wishlistItems.map(item => (
            <ProductCard key={item.id} product={item} />
          ))}
        </div>
      </div>
    </div>
  );
};

export default Wishlist;