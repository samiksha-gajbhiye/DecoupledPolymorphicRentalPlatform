import ActiveRentalCard from '../../components/owner/ActiveRentalCard';

const ActiveRentals = () => {
  const activeRentals = [
    {
      id: 1,
      itemName: "Professional DSLR Camera Kit",
      itemImage: "https://images.unsplash.com/photo-1526170375885-4d8ecf77b99f?w=400",
      renterName: "John Doe",
      renterAvatar: "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=100",
      startDate: "2026-08-20",
      endDate: "2026-08-25",
      totalPrice: 375,
      status: "active",
      location: "New York, NY",
      daysRemaining: 2
    },
    {
      id: 2,
      itemName: "Electric Scooter",
      itemImage: "https://images.unsplash.com/photo-1544538461-8b8a5ee303f6?w=400",
      renterName: "Jane Smith",
      renterAvatar: "https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=100",
      startDate: "2026-08-22",
      endDate: "2026-08-24",
      totalPrice: 70,
      status: "active",
      location: "Los Angeles, CA",
      daysRemaining: 1
    },
    {
      id: 3,
      itemName: "Modern Sofa Set",
      itemImage: "https://images.unsplash.com/photo-1555041469-a586c61ea9bc?w=400",
      renterName: "Mike Johnson",
      renterAvatar: "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=100",
      startDate: "2026-08-18",
      endDate: "2026-08-22",
      totalPrice: 240,
      status: "active",
      location: "Chicago, IL",
      daysRemaining: 5
    }
  ];

  return (
    <div className="min-h-screen bg-gray-50 dark:bg-gray-900">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <div className="mb-6">
          <h1 className="text-2xl font-bold text-gray-900 dark:text-white">
            Active Rentals
          </h1>
          <div className="mt-2 flex items-center space-x-4 text-sm text-gray-500 dark:text-gray-400">
            <span>Total Active: {activeRentals.length}</span>
            <span className="mx-2">•</span>
            <span>Total Earnings: ${activeRentals.reduce((sum, rental) => sum + rental.totalPrice, 0)}</span>
          </div>
        </div>

        <div className="space-y-4">
          {activeRentals.map(rental => (
            <ActiveRentalCard key={rental.id} rental={rental} />
          ))}
        </div>
      </div>
    </div>
  );
};

export default ActiveRentals;