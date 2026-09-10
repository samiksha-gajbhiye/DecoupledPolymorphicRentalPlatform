import { Calendar, Truck, MapPin } from 'lucide-react';

const ActiveRentalsCard = () => {
  const activeRentals = [
    {
      id: 1,
      name: "Professional DSLR Camera Kit",
      image: "https://images.unsplash.com/photo-1526170375885-4d8ecf77b99f?w=400",
      startDate: "2026-08-20",
      endDate: "2026-08-25",
      location: "New York, NY",
      status: "active"
    },
    {
      id: 2,
      name: "Electric Scooter",
      image: "https://images.unsplash.com/photo-1544538461-8b8a5ee303f6?w=400",
      startDate: "2026-08-22",
      endDate: "2026-08-24",
      location: "Los Angeles, CA",
      status: "active"
    }
  ];

  return (
    <div className="bg-white dark:bg-gray-800 rounded-xl shadow-sm p-6">
      <div className="flex items-center justify-between mb-4">
        <h3 className="text-lg font-medium text-gray-900 dark:text-white">
          Active Rentals
        </h3>
        <a href="/customer/bookings" className="text-sm text-blue-600 hover:text-blue-500 dark:hover:text-blue-400 font-medium">
          View All
        </a>
      </div>
      <div className="space-y-4">
        {activeRentals.map(rental => (
          <div key={rental.id} className="border-b border-gray-200 dark:border-gray-700 pb-3 last:border-0">
            <div className="flex items-start">
              <img
                src={rental.image}
                alt={rental.name}
                className="w-16 h-16 object-cover rounded-md mr-3"
              />
              <div className="flex-1">
                <p className="font-medium text-gray-900 dark:text-white">{rental.name}</p>
                <div className="flex items-center space-x-2 text-sm text-gray-500 dark:text-gray-400 mt-1">
                  <MapPin className="h-4 w-4" />
                  <span>{rental.location}</span>
                </div>
                <div className="flex items-center space-x-2 text-sm text-gray-500 dark:text-gray-400 mt-1">
                  <Calendar className="h-4 w-4" />
                  <span>{rental.startDate} to {rental.endDate}</span>
                </div>
                <span className="px-2 py-1 text-xs rounded-full bg-green-100 text-green-800 dark:bg-green-900 dark:text-green-200">
                  Active
                </span>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default ActiveRentalsCard;