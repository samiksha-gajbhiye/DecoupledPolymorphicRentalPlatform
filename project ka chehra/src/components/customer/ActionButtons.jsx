import { MessageSquare, Phone, Truck } from 'lucide-react';

const ActionButtons = ({ booking }) => {
  return (
    <div className="py-4">
      <div className="border-t border-gray-200 dark:border-gray-700 pt-4">
        <h3 className="text-lg font-medium text-gray-900 dark:text-white mb-3">
          Need Help?
        </h3>
        <div className="grid gap-3 sm:grid-cols-2">
          <button className="w-full bg-blue-50 dark:bg-blue-900/10 border border-blue-200 dark:border-blue-800 rounded-lg p-4 text-left hover:bg-blue-100 dark:hover:bg-blue-800/10 transition-colors flex items-center space-x-3">
            <MessageSquare className="h-5 w-5 text-blue-600" />
            <div>
              <p className="text-sm font-medium text-gray-900 dark:text-white">Contact Owner</p>
              <p className="text-xs text-gray-500 dark:text-gray-400">
                Send a message to the owner about your booking
              </p>
            </div>
          </button>
          <button className="w-full bg-blue-50 dark:bg-blue-900/10 border border-blue-200 dark:border-blue-800 rounded-lg p-4 text-left hover:bg-blue-100 dark:hover:bg-blue-800/10 transition-colors flex items-center space-x-3">
            <Phone className="h-5 w-5 text-blue-600" />
            <div>
              <p className="text-sm font-medium text-gray-900 dark:text-white">Customer Support</p>
              <p className="text-xs text-gray-500 dark:text-gray-400">
                Get help from our support team
              </p>
            </div>
          </button>
          <button className="w-full bg-blue-50 dark:bg-blue-900/10 border border-blue-200 dark:border-blue-800 rounded-lg p-4 text-left hover:bg-blue-100 dark:hover:bg-blue-800/10 transition-colors flex items-center space-x-3">
            <Truck className="h-5 w-5 text-blue-600" />
            <div>
              <p className="text-sm font-medium text-gray-900 dark:text-white">Delivery Options</p>
              <p className="text-xs text-gray-500 dark:text-gray-400">
                Arrange for item delivery or pickup
              </p>
            </div>
          </button>
          <button className="w-full bg-blue-50 dark:bg-blue-900/10 border border-blue-200 dark:border-blue-800 rounded-lg p-4 text-left hover:bg-blue-100 dark:hover:bg-blue-800/10 transition-colors flex items-center space-x-3">
            <MessageSquare className="h-5 w-5 text-blue-600" />
            <div>
              <p className="text-sm font-medium text-gray-900 dark:text-white">Leave a Review</p>
              <p className="text-xs text-gray-500 dark:text-gray-400">
                Share your experience after the rental ends
              </p>
            </div>
          </button>
        </div>
      </div>
    </div>
  );
};

export default ActionButtons;