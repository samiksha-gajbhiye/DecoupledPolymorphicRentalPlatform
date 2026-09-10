import { Calendar, User, CheckCircle, XCircle, MessageSquare, Phone } from 'lucide-react';

const BookingRequestCard = ({ request }) => {
  const statusVariants = {
    pending: { bg: 'bg-yellow-100 dark:bg-yellow-900/20', text: 'text-yellow-800 dark:text-yellow-200' },
    approved: { bg: 'bg-green-100 dark:bg-green-900/20', text: 'text-green-800 dark:text-green-200' },
    rejected: { bg: 'bg-red-100 dark:bg-red-900/20', text: 'text-red-800 dark:text-red-200' }
  };

  const variant = statusVariants[request.status] || statusVariants.pending;

  return (
    <div className="bg-white dark:bg-gray-800 rounded-xl shadow-sm p-6">
      <div className="flex items-start space-x-4">
        <img
          src={request.itemImage}
          alt={request.itemName}
          className="w-16 h-16 object-cover rounded-md"
        />
        <div className="flex-1 space-y-3">
          <div className="flex justify-between items-start">
            <h3 className="font-medium text-gray-900 dark:text-white">{request.itemName}</h3>
            <span className={`px-2 py-1 text-xs rounded-full ${variant.bg} ${variant.text}`}>
              {request.status.charAt(0).toUpperCase() + request.status.slice(1)}
            </span>
          </div>
          <div className="flex items-center space-x-2 text-sm text-gray-500 dark:text-gray-400">
            <User className="h-4 w-4" />
            <span>{request.renterName}</span>
          </div>
          <div className="flex items-center space-x-2 text-sm text-gray-500 dark:text-gray-400">
            <Calendar className="h-4 w-4" />
            <span>{request.startDate} to {request.endDate}</span>
          </div>
          <div className="text-right text-sm font-medium text-gray-900 dark:text-white">
            <span>${request.totalPrice}</span>
          </div>
          <p className="text-sm text-gray-600 dark:text-gray-400 mt-1">
            "{request.message}"
          </p>
        </div>
      </div>
      <div className="mt-4 pt-3 border-t border-gray-200 dark:border-gray-700">
        <div className="flex justify-end space-x-3">
          {request.status === 'pending' && (
            <>
              <button
                onClick={() => { /* approve logic */ }}
                className="px-3 py-1 text-xs font-medium bg-green-100 text-green-800 rounded hover:bg-green-200 dark:hover:bg-green-800/20"
              >
                Approve
              </button>
              <button
                onClick={() => { /* reject logic */ }}
                className="px-3 py-1 text-xs font-medium bg-red-100 text-red-800 rounded hover:bg-red-200 dark:hover:bg-red-800/20 ml-2"
              >
                Reject
              </button>
            </>
          )}
          {request.status !== 'pending' && (
            <>
              <button
                onClick={() => { /* message logic */ }}
                className="px-3 py-1 text-xs font-medium bg-blue-100 text-blue-800 rounded hover:bg-blue-200 dark:hover:bg-blue-800/20"
              >
                Message
              </button>
              <button
                onClick={() => { /* call logic */ }}
                className="px-3 py-1 text-xs font-medium bg-green-100 text-green-800 rounded hover:bg-green-200 dark:hover:bg-green-800/20 ml-2"
              >
                Call
              </button>
            </>
          )}
        </div>
      </div>
    </div>
  );
};

export default BookingRequestCard;