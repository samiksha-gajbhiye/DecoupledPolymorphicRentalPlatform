import ListingCard from '../../components/owner/ListingCard';
import AddListingButton from '../../components/owner/AddListingButton';

const MyListings = () => {
  const listings = [
    {
      id: 1,
      name: "Professional DSLR Camera Kit",
      image: "https://images.unsplash.com/photo-1526170375885-4d8ecf77b99f?w=400",
      category: "Cameras",
      price: 75,
      status: "active",
      views: 124,
      bookings: 8,
      rating: 4.9
    },
    {
      id: 2,
      name: "Electric Scooter",
      image: "https://images.unsplash.com/photo-1544538461-8b8a5ee303f6?w=400",
      category: "Vehicles",
      price: 35,
      status: "active",
      views: 89,
      bookings: 5,
      rating: 4.7
    },
    {
      id: 3,
      name: "Modern Sofa Set",
      image: "https://images.unsplash.com/photo-1555041469-a586c61ea9bc?w=400",
      category: "Furniture",
      price: 60,
      status: "active",
      views: 156,
      bookings: 12,
      rating: 4.8
    },
    {
      id: 4,
      name: "Power Tool Kit",
      image: "https://images.unsplash.com/photo-1581091853897-d36451e25e44?w=400",
      category: "Tools",
      price: 45,
      status: "maintenance",
      views: 45,
      bookings: 2,
      rating: 4.6
    },
    {
      id: 5,
      name: "Camping Tent 4-Person",
      image: "https://images.unsplash.com/photo-1504280390367-361c6d9f38f4?w=400",
      category: "Sports Equipment",
      price: 25,
      status: "active",
      views: 78,
      bookings: 6,
      rating: 4.5
    },
    {
      id: 6,
      name: "Projector Screen 120-inch",
      image: "https://images.unsplash.com/photo-1522850861670-9a3b0db8b859?w=400",
      category: "Event Equipment",
      price: 80,
      status: "active",
      views: 34,
      bookings: 3,
      rating: 4.6
    }
  ];

  return (
    <div className="min-h-screen bg-gray-50 dark:bg-gray-900">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <div className="mb-6">
          <h1 className="text-2xl font-bold text-gray-900 dark:text-white">
            My Listings
          </h1>
          <div className="flex items-center justify-between mt-4">
            <div className="flex items-center space-x-3 text-sm text-gray-500 dark:text-gray-400">
              <span>Total Listings: {listings.length}</span>
              <span className="mx-2">•</span>
              <span>Active: {listings.filter(l => l.status === 'active').length}</span>
            </div>
            <AddListingButton />
          </div>
        </div>

        <div className="space-y-4">
          {listings.map(listing => (
            <ListingCard key={listing.id} listing={listing} />
          ))}
        </div>
      </div>
    </div>
  );
};

export default MyListings;