import { Calendar, MapPin, User, Star } from 'lucide-react';

const BookingDetailsHeader = ({ booking }) => {
  return (
    <div className="p-6">
      <div className="flex items-start space-x-4">
        <img
          src={booking.item.image}
          alt={booking.item.name}
          className="w-24 h-24 object-cover rounded-md"
        />
        <div className="flex-1 space-y-3">
          <h2 className="text-xl font-bold text-gray-900 dark:text-white">
            {booking.item.name}
          </h2>
          <div className="flex items-center space-x-2 text-sm text-gray-500 dark:text-gray-400">
            <MapPin className="h-4 w-4" />
            <span>{booking.item.location}</span>
          </div>
          <div className="flex items-center space-x-2 text-sm text-gray-500 dark:text-gray-400">
            <Calendar className="h-4 w-4" />
            <span>{booking.dates.start} to {booking.dates.end}</span>
          </div>
          <div className="flex items-center space-x-2 text-sm text-gray-500 dark:text-gray-400">
            <Star className="h-4 w-4 text-yellow-400" />
            <span>4.9 ({booking.item.category} rating)</span>
          </div>
          <div className="flex items-center space-x-2 text-sm text-gray-500 dark:text-gray-400 mt-2">
            <User className="h-4 w-4" />
            <span>Owner: {booking.owner.name}</span>
          </div>
        </div>
      </div>
    </div>
  );
};

export default BookingDetailsHeader;