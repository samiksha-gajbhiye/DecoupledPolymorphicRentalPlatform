import BookingCard from '../../components/customer/BookingCard';

const MyBookings = () => {
  const bookings = [
    {
      id: 1001,
      itemName: "Professional DSLR Camera Kit",
      itemImage: "https://images.unsplash.com/photo-1526170375885-4d8ecf77b99f?w=400",
      startDate: "2026-08-20",
      endDate: "2026-08-25",
      totalCost: 375,
      status: "active",
      location: "New York, NY"
    },
    {
      id: 1002,
      itemName: "Electric Scooter",
      itemImage: "https://images.unsplash.com/photo-1544538461-8b8a5ee303f6?w=400",
      startDate: "2026-08-22",
      endDate: "2026-08-24",
      totalCost: 70,
      status: "upcoming",
      location: "Los Angeles, CA"
    },
    {
      id: 1003,
      itemName: "Modern Sofa Set",
      itemImage: "https://images.unsplash.com/photo-1555041469-a586c61ea9bc?w=400",
      startDate: "2026-08-10",
      endDate: "2026-08-15",
      totalCost: 300,
      status: "completed",
      location: "Chicago, IL"
    }
  ];

  return (
    <div className="min-h-screen bg-gray-50 dark:bg-gray-900">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <div className="mb-6">
          <h1 className="text-2xl font-bold text-gray-900 dark:text-white">
            My Bookings
          </h1>
          <div className="mt-2 flex space-x-4 text-sm text-gray-500 dark:text-gray-400">
            <span>Total Bookings: {bookings.length}</span>
            <span className="mx-2">•</span>
            <span>Active: {bookings.filter(b => b.status === 'active').length}</span>
          </div>
        </div>

        <div className="space-y-6">
          {bookings.map(booking => (
            <BookingCard key={booking.id} booking={booking} />
          ))}
        </div>
      </div>
    </div>
  );
};

export default MyBookings;