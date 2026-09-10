import { Star, MapPin, Calendar, User, ShieldCheck } from 'lucide-react';

const RentalDetails = ({ product }) => {
  return (
    <div className="space-y-6">
      {/* Basic Info */}
      <div className="space-y-4">
        <div className="flex items-center text-sm text-gray-600 dark:text-gray-400">
          <MapPin className="h-4 w-4 mr-2" />
          <span>{product.location}</span>
        </div>
        <div className="flex items-center text-sm text-gray-600 dark:text-gray-400">
          <Calendar className="h-4 w-4 mr-2" />
          <span>{product.availability.nextAvailable} • {product.availability.minimumDays}-{product.availability.maximumDays} days</span>
        </div>
      </div>

      {/* Owner Info */}
      <div className="border-t border-gray-200 dark:border-gray-700 pt-5">
        <h3 className="text-lg font-medium text-gray-900 dark:text-white mb-3">
          About the Owner
        </h3>
        <div className="flex items-center space-x-3">
          <img
            src={product.owner.avatar}
            alt={product.owner.name}
            className="h-10 w-10 rounded-full border-2 border-blue-500"
          />
          <div className="flex-1">
            <p className="font-medium text-gray-900 dark:text-white">{product.owner.name}</p>
            <div className="flex items-center space-x-2 text-sm">
              <Star className="h-4 w-4 text-yellow-400" />
              <span>{product.owner.rating}</span>
              {product.owner.verified && (
                <span className="ml-2">
                  <ShieldCheck className="h-4 w-4 text-green-500" />
                </span>
              )}
            </div>
            <p className="text-sm text-gray-500 dark:text-gray-400 mt-1">
              {product.owner.listings} listings
            </p>
          </div>
        </div>
      </div>

      {/* Policies */}
      <div className="border-t border-gray-200 dark:border-gray-700 pt-5">
        <h3 className="text-lg font-medium text-gray-900 dark:text-white mb-3">
          Rental Policies
        </h3>
        <div className="space-y-3">
          <p className="text-sm text-gray-600 dark:text-gray-400">
            <strong>Cancellation:</strong> {product.policies.cancellation}
          </p>
          <p className="text-sm text-gray-600 dark:text-gray-400">
            <strong>Deposit:</strong> {product.policies.deposit}
          </p>
          <p className="text-sm text-gray-600 dark:text-gray-400">
            <strong>Late Return:</strong> {product.policies.lateReturn}
          </p>
        </div>
      </div>
    </div>
  );
};

export default RentalDetails;