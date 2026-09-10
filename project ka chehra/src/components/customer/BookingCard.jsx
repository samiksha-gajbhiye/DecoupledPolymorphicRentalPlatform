import { Calendar, MapPin, CheckCircle, XCircle } from 'lucide-react';

const BookingCard = ({ booking }) => {
  const statusVariants = {
    active: { bg: 'bg-green-100 dark:bg-green-900/20', text: 'text-green-800 dark:text-green-200' },
    upcoming: { bg: 'bg-blue-100 dark:bg-blue-900/20', text: 'text-blue-800 dark:text-blue-200' },
    completed: { bg: 'bg-gray-100 dark:bg-gray-800/20', text: 'text-gray-800 dark:text-gray-200' },
    cancelled: { bg: 'bg-red-100 dark:bg-red-900/20', text: 'text-red-800 dark:text-red-200' }
  };

  const variant = statusVariants[booking.status] || statusVariants.completed;

  return (
    <div className="bg-white dark:bg-gray-800 rounded-xl shadow-sm p-6">
      <div className="flex items-start space-x-4">
        <img
          src={booking.itemImage}
          alt={booking.itemName}
          className="w-20 h-20 object-cover rounded-md"
        />
        <div className="flex-1 space-y-3">
          <div className="flex justify-between items-start">
            <h3 className="font-medium text-gray-900 dark:text-white">{booking.itemName}</h3>
            <span className={`px-2 py-1 text-xs rounded-full ${variant.bg} ${variant.text}`}>
              {booking.status.charAt(0).toUpperCase() + booking.status.slice(1)}
            </span>
          </div>
          <div className="flex items-center space-x-2 text-sm text-gray-500 dark:text-gray-400">
            <MapPin className="h-4 w-4" />
            <span>{booking.location}</span>
          </div>
          <div className="flex items-center space-x-2 text-sm text-gray-500 dark:text-gray-400">
            <Calendar className="h-4 w-4" />
            <span>{booking.startDate} to {booking.endDate}</span>
          </div>
          <div className="text-right text-sm font-medium text-gray-900 dark:text-white">
            <span>${booking.totalCost}</span>
          </div>
        </div>
      </div>
      <div className="mt-4 pt-3 border-t border-gray-200 dark:border-gray-700">
        <div className="flex justify-between text-sm text-gray-500 dark:text-gray-400">
          <span>Booking ID: #{booking.id}</span>
          <span>
            {booking.status === 'active' && (
              <>
                <button className="text-blue-600 hover:text-blue-500 dark:hover:text-blue-400 mr-2">
                  Modify
                </button>
                <button className="text-red-600 hover:text-red-500 dark:hover:text-red-400">
                  Cancel
                </button>
              </>
            )}
          </span>
        </div>
      </div>
    </div>
  );
};

export default BookingCard;