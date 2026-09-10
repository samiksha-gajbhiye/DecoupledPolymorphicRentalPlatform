import { Star, Calendar, User, Reply } from 'lucide-react';

const ReviewCard = ({ review }) => {
  return (
    <div className="bg-white dark:bg-gray-800 rounded-xl shadow-sm p-6">
      <div className="flex items-start space-x-3 mb-4">
        <img
          src={review.renterAvatar}
          alt={review.renterName}
          className="w-10 h-10 rounded-full"
        />
        <div className="flex-1 space-y-2">
          <div className="flex justify-between items-start">
            <h3 className="font-medium text-gray-900 dark:text-white">
              {review.renterName}
            </h3>
            <div className="flex items-center space-x-1 text-sm text-gray-500 dark:text-gray-400">
              <Calendar className="h-3 w-3" />
              <span>{review.date}</span>
            </div>
          </div>
          <div className="flex items-center space-x-2 text-sm">
            {[1, 2, 3, 4, 5].map((star) => (
              <Star
                key={star}
                className={`h-3 w-3 ${star <= review.rating ? 'text-yellow-400' : 'text-gray-300'}`}
              />
            ))}
            <span className="ml-1 text-xs text-gray-500 dark:text-gray-400">
              ({review.rating}/5)
            </span>
          </div>
          <p className="text-sm text-gray-600 dark:text-gray-300">
            "{review.comment}"
          </p>
          <div className="mt-2 text-right">
            <button
              className="text-sm text-blue-600 hover:text-blue-500 dark:hover:text-blue-400 font-medium flex items-center space-x-1"
            >
              Reply
              <Reply className="h-3 w-3" />
            </button>
          </div>
        </div>
      </div>
      <div className="border-t border-gray-200 dark:border-gray-700 pt-4">
        <div className="flex items-center space-x-2 text-sm text-gray-500 dark:text-gray-400">
          <span>For:</span>
          <span className="font-medium text-gray-900 dark:text-white">
            {review.itemName}
          </span>
        </div>
      </div>
    </div>
  );
};

export default ReviewCard;