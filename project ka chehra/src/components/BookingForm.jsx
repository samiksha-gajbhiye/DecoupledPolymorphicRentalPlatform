import { useState } from 'react';
import { Calendar, MapPin, CreditCard } from 'lucide-react';
import DateInput from './DateInput';

const BookingForm = ({ product }) => {
  const [checkIn, setCheckIn] = useState('');
  const [checkOut, setCheckOut] = useState('');
  const [guests, setGuests] = useState(1);
  const [loading, setLoading] = useState(false);

  const handleSubmit = (e) => {
    e.preventDefault();
    setLoading(true);
    // In a real app, this would send a request to the backend
    setTimeout(() => {
      setLoading(false);
      alert('Booking request sent!'); // Placeholder for actual booking logic
    }, 1000);
  };

  // Calculate total price
  const nights = checkIn && checkOut ?
    Math.ceil((new Date(checkOut) - new Date(checkIn)) / (1000 * 60 * 60 * 24)) : 0;
  const totalPrice = nights * product.price;

  return (
    <div className="border-t border-gray-200 dark:border-gray-700 pt-5">
      <h3 className="text-lg font-medium text-gray-900 dark:text-white mb-4">
        Book This Item
      </h3>
      <form onSubmit={handleSubmit} className="space-y-4">
        <div className="grid gap-4 sm:grid-cols-2">
          <div>
            <label htmlFor="check-in" className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">
              Check-in Date
            </label>
            <DateInput
              id="check-in"
              value={checkIn}
              onChange={(e) => setCheckIn(e.target.value)}
              min={new Date().toISOString().split('T')[0]}
              className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:text-white dark:focus:ring-blue-400"
            />
          </div>
          <div>
            <label htmlFor="check-out" className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">
              Check-out Date
            </label>
            <DateInput
              id="check-out"
              value={checkOut}
              onChange={(e) => setCheckOut(e.target.value)}
              min={new Date().toISOString().split('T')[0]}
              className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:text-white dark:focus:ring-blue-400"
            />
          </div>
        </div>

        <div className="flex items-center space-x-4">
          <MapPin className="h-4 w-4 text-gray-500" />
          <div className="flex-1">
            <p className="text-sm text-gray-600 dark:text-gray-400">
              {product.location}
            </p>
          </div>
        </div>

        <div>
          <label htmlFor="guests" className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">
            Guests
          </label>
          <input
            type="number"
            id="guests"
            value={guests}
            onChange={(e) => setGuests(parseInt(e.target.value) || 1)}
            min={1}
            className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:text-white dark:focus:ring-blue-400"
          />
        </div>

        {/* Price Summary */}
        {checkIn && checkOut && (
          <div className="border-t border-gray-200 dark:border-gray-700 pt-4">
            <div className="flex justify-between text-sm text-gray-600 dark:text-gray-400">
              <span>Base Price (₹{product.price}/day × {nights} nights)</span>
              <span>₹{totalPrice}</span>
            </div>
            <div className="flex justify-between text-sm text-gray-500 dark:text-gray-400 mt-1">
              <span>Estimated Taxes & Fees</span>
              <span>₹{Math.round(totalPrice * 0.15)}</span>
            </div>
            <div className="flex justify-between pt-2 border-t border-gray-200 dark:border-gray-700 text-lg font-medium">
              <span>Total Estimated</span>
              <span>₹{Math.round(totalPrice * 1.15)}</span>
            </div>
          </div>
        )}

        <button
          type="submit"
          disabled={loading || !(checkIn && checkOut)}
          className="w-full bg-blue-600 text-white py-2 px-4 rounded-md hover:bg-blue-700 dark:hover:bg-blue-800 transition-colors disabled:opacity-50 disabled:cursor-not-allowed text-sm font-medium"
        >
          {loading ? 'Processing...' : 'Request to Book'}
        </button>
      </form>
    </div>
  );
};

export default BookingForm;