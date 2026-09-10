import { useParams } from 'react-router-dom';
import BookingDetailsHeader from '../../components/customer/BookingDetailsHeader';
import BookingTimeline from '../../components/customer/BookingTimeline';
import BookingSummary from '../../components/customer/BookingSummary';
import ActionButtons from '../../components/customer/ActionButtons';

const BookingDetails = () => {
  const { id } = useParams();

  // Sample booking data - in real app this would come from API
  const booking = {
    id: parseInt(id),
    item: {
      name: "Professional DSLR Camera Kit",
      image: "https://images.unsplash.com/photo-1526170375885-4d8ecf77b99f?w=800",
      category: "Cameras",
      location: "New York, NY"
    },
    dates: {
      start: "2026-08-20",
      end: "2026-08-25",
      totalDays: 5
    },
    pricing: {
      dailyRate: 75,
      subtotal: 375,
      taxes: 56,
      fees: 25,
      total: 456
    },
    status: "active",
    paymentStatus: "paid",
    owner: {
      name: "Alex Johnson",
      avatar: "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=100",
      rating: 4.9,
      verified: true
    },
    timeline: [
      {
        date: "2026-08-15",
        time: "10:30 AM",
        title: "Booking Created",
        description: "Your booking request was submitted and is pending owner approval.",
        status: "completed"
      },
      {
        date: "2026-08-15",
        time: "11:15 AM",
        title: "Booking Confirmed",
        description: "The owner has approved your booking request.",
        status: "completed"
      },
      {
        date: "2026-08-20",
        time: "9:00 AM",
        title: "Pickup Scheduled",
        description: "Item is ready for pickup at the agreed location.",
        status: "upcoming"
      },
      {
        date: "2026-08-25",
        time: "6:00 PM",
        title: "Return Due",
        description: "Please return the item by this time to avoid late fees.",
        status: "upcoming"
      }
    ]
  };

  return (
    <div className="min-h-screen bg-gray-50 dark:bg-gray-900">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <div className="mb-6">
          <h1 className="text-2xl font-bold text-gray-900 dark:text-white">
            Booking Details
          </h1>
          <div className="mt-2 flex items-center space-x-3 text-sm text-gray-500 dark:text-gray-400">
            <span>Booking ID: #{booking.id}</span>
            <span className="mx-2">•</span>
            <span className={`px-2 py-0.5 text-xs rounded-full bg-${booking.status === 'active' ? 'green' : booking.status === 'completed' ? 'gray' : 'red'}-100 text-${booking.status === 'active' ? 'green' : booking.status === 'completed' ? 'gray' : 'red'}-800 dark:bg-${booking.status === 'active' ? 'green' : booking.status === 'completed' ? 'gray' : 'red'}-900/20 dark:text-${booking.status === 'active' ? 'green' : booking.status === 'completed' ? 'gray' : 'red'}-200`}>
              {booking.status.charAt(0).toUpperCase() + booking.status.slice(1)}
            </span>
          </div>
        </div>

        <div className="bg-white dark:bg-gray-800 rounded-xl shadow-sm">
          <BookingDetailsHeader booking={booking} />
          <div className="divide-y divide-gray-200 dark:divide-gray-700">
            <BookingTimeline timeline={booking.timeline} />
            <BookingSummary booking={booking} />
            <ActionButtons booking={booking} />
          </div>
        </div>
      </div>
    </div>
  );
};

export default BookingDetails;