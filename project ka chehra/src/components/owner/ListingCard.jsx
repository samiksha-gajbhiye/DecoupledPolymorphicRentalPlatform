import { Star, MapPin, Eye, Calendar } from 'lucide-react';

const ListingCard = ({ listing }) => {
  const statusVariants = {
    active: { bg: 'bg-green-100 dark:bg-green-900/20', text: 'text-green-800 dark:text-green-200' },
    inactive: { bg: 'bg-gray-100 dark:bg-gray-800/20', text: 'text-gray-800 dark:text-gray-200' },
    maintenance: { bg: 'bg-yellow-100 dark:bg-yellow-900/20', text: 'text-yellow-800 dark:text-yellow-200' }
  };

  const variant = statusVariants[listing.status] || statusVariants.active;

  return (
    <div className="flex items-start space-x-4 p-4 border-b border-gray-200 dark:border-gray-700 last:border-0">
      <img
        src={listing.image}
        alt={listing.name}
        className="w-16 h-16 object-cover rounded-md"
      />
      <div className="flex-1 space-y-2">
        <div className="flex justify-between items-start">
          <h3 className="font-medium text-gray-900 dark:text-white">{listing.name}</h3>
          <span className={`px-2 py-1 text-xs rounded-full ${variant.bg} ${variant.text}`}>
            {listing.status.charAt(0).toUpperCase() + listing.status.slice(1)}
          </span>
        </div>
        <div className="flex items-center space-x-2 text-sm text-gray-500 dark:text-gray-400">
          <MapPin className="h-4 w-4" />
          <span>{listing.category}</span>
        </div>
        <div className="flex items-center space-x-2 text-sm text-gray-500 dark:text-gray-400">
          <Eye className="h-4 w-4" />
          <span>{listing.views} views</span>
        </div>
        <div className="flex items-center space-x-2 text-sm text-gray-500 dark:text-gray-400">
          <Calendar className="h-4 w-4" />
          <span>{listing.bookings} bookings</span>
        </div>
        <div className="flex items-center space-x-2 text-sm text-gray-500 dark:text-gray-400 mt-1">
          <Star className="h-4 w-4 text-yellow-400" />
          <span>4.8 avg rating</span>
        </div>
      </div>
    </div>
  );
};

export default ListingCard;