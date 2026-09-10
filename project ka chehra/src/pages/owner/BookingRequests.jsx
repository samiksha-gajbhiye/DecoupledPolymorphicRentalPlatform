import BookingRequestCard from '../../components/owner/BookingRequestCard';

const BookingRequests = () => {
  const requests = [
    {
      id: 1,
      itemName: "Professional DSLR Camera Kit",
      itemImage: "https://images.unsplash.com/photo-1526170375885-4d8ecf77b99f?w=400",
      renterName: "John Doe",
      renterAvatar: "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=100",
      startDate: "2026-08-25",
      endDate: "2026-08-28",
      totalPrice: 225,
      status: "pending",
      message: "Hey! Is the camera kit still available for the weekend? I'll take good care of it."
    },
    {
      id: 2,
      itemName: "Electric Scooter",
      itemImage: "https://images.unsplash.com/photo-1544538461-8b8a5ee303f6?w=400",
      renterName: "Jane Smith",
      renterAvatar: "https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=100",
      startDate: "2026-08-27",
      endDate: "2026-08-29",
      totalPrice: 70,
      status: "pending",
      message: "Looking to rent this for a weekend trip to the beach."
    },
    {
      id: 3,
      itemName: "Modern Sofa Set",
      itemImage: "https://images.unsplash.com/photo-1555041469-a586c61ea9bc?w=400",
      renterName: "Mike Johnson",
      renterAvatar: "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=100",
      startDate: "2026-08-30",
      endDate: "2026-09-02",
      totalPrice: 240,
      status: "approved",
      message: "Need this for my new apartment move-in."
    }
  ];

  return (
    <div className="min-h-screen bg-gray-50 dark:bg-gray-900">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <div className="mb-6">
          <h1 className="text-2xl font-bold text-gray-900 dark:text-white">
            Booking Requests
          </h1>
          <div className="mt-2 flex items-center space-x-4 text-sm text-gray-500 dark:text-gray-400">
            <span>Total Requests: {requests.length}</span>
            <span className="mx-2">•</span>
            <span>Pending: {requests.filter(r => r.status === 'pending').length}</span>
            <span className="mx-2">•</span>
            <span>Approved: {requests.filter(r => r.status === 'approved').length}</span>
          </div>
        </div>

        <div className="space-y-4">
          {requests.map(request => (
            <BookingRequestCard key={request.id} request={request} />
          ))}
        </div>
      </div>
    </div>
  );
};

export default BookingRequests;