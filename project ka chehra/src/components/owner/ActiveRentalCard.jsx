import { Calendar, User, MapPin, CheckCircle, RefreshCw } from 'lucide-react';

const ActiveRentalCard = ({ rental }) => {
  return (
    <div className="bg-white dark:bg-gray-800 rounded-xl shadow-sm p-6">
      <div className="flex items-start space-x-4">
        <img
          src={rental.itemImage}
          alt={rental.itemName}
          className="w-16 h-16 object-cover rounded-md"
        />
        <div className="flex-1 space-y-3">
          <div className="flex justify-between items-start">
            <h3 className="font-medium text-gray-900 dark:text-white">{rental.itemName}</h3>
            <span className="px-2 py-1 text-xs rounded-full bg-green-100 text-green-800 dark:bg-green-900 dark:text-green-200">
              Active
            </span>
          </div>
          <div className="flex items-center space-x-2 text-sm text-gray-500 dark:text-gray-400">
            <User className="h-4 w-4" />
            <span>{rental.renterName}</span>
          </div>
          <div className="flex items-center space-x-2 text-sm text-gray-500 dark:text-gray-400">
            <MapPin className="h-4 w-4" />
            <span>{rental.location}</span>
          </div>
          <div className="flex items-center space-x-2 text-sm text-gray-500 dark:text-gray-400">
            <Calendar className="h-4 w-4" />
            <span>{rental.startDate} to {rental.endDate}</span>
          </div>
          <div className="flex items-center space-x-2 text-sm text-gray-500 dark:text-gray-400 mt-1">
            <Calendar className="h-4 w-4" />
            <span>{rental.daysRemaining} days remaining</span>
          </div>
          <div className="text-right text-sm font-medium text-gray-900 dark:text-white">
            <span>${rental.totalPrice}</span>
          </div>
        </div>
      </div>
      <div className="mt-4 pt-3 border-t border-gray-200 dark:border-gray-700">
        <div className="flex justify-end space-x-3">
          <button
            onClick={() => { /* extend rental logic */ }}
            className="px-3 py-1 text-xs font-medium bg-blue-100 text-blue-800 rounded hover:bg-blue-200 dark:hover:bg-blue-800/20"
          >
            Extend
          </button>
          <button
            onClick={() => { /* modify rental logic */ }}
            className="px-3 py-1 text-xs font-medium bg-green-100 text-green-800 rounded hover:bg-green-200 dark:hover:bg-green-800/20 ml-2"
          >
            Modify
          </button>
          <button
            onClick={() => { /* end rental early logic */ }}
            className="px-3 py-1 text-xs font-medium bg-red-100 text-red-800 rounded hover:bg-red-200 dark:hover:bg-red-800/20 ml-2"
          >
            End Early
          </button>
        </div>
      </div>
    </div>
  );
};

export default ActiveRentalCard;