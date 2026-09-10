import ListingCard from './ListingCard';

const RecentListings = () => {
  const listings = [
    {
      id: 1,
      name: "Professional DSLR Camera Kit",
      image: "https://images.unsplash.com/photo-1526170375885-4d8ecf77b99f?w=400",
      category: "Cameras",
      price: 75,
      status: "active",
      views: 124,
      bookings: 8
    },
    {
      id: 2,
      name: "Electric Scooter",
      image: "https://images.unsplash.com/photo-1544538461-8b8a5ee303f6?w=400",
      category: "Vehicles",
      price: 35,
      status: "active",
      views: 89,
      bookings: 5
    },
    {
      id: 3,
      name: "Modern Sofa Set",
      image: "https://images.unsplash.com/photo-1555041469-a586c61ea9bc?w=400",
      category: "Furniture",
      price: 60,
      status: "active",
      views: 156,
      bookings: 12
    }
  ];

  return (
    <div className="bg-white dark:bg-gray-800 rounded-xl shadow-sm p-6">
      <div className="flex items-center justify-between mb-4">
        <h3 className="text-lg font-medium text-gray-900 dark:text-white">
          Recent Listings
        </h3>
        <a href="/owner/listings" className="text-sm text-blue-600 hover:text-blue-500 dark:hover:text-blue-400 font-medium">
          View All
        </a>
      </div>
      <div className="space-y-4">
        {listings.map(listing => (
          <ListingCard key={listing.id} listing={listing} />
        ))}
      </div>
    </div>
  );
};

export default RecentListings;