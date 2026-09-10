import { Star, Users, Calendar, DollarSign } from 'lucide-react';

const OwnerStatsGrid = () => {
  const stats = [
    {
      label: 'Active Listings',
      value: '8',
      icon: <Users className="h-5 w-5 text-blue-500" />,
      color: 'blue'
    },
    {
      label: 'This Month Revenue',
      value: '₹2,450',
      icon: <DollarSign className="h-5 w-5 text-green-500" />,
      color: 'green'
    },
    {
      label: 'Booking Requests',
      value: '3',
      icon: <Calendar className="h-5 w-5 text-purple-500" />,
      color: 'purple'
    },
    {
      label: 'Avg. Rating',
      value: '4.8',
      icon: <Statistics className="h-5 w-5 text-yellow-500" />,
      color: 'yellow'
    }
  ];

  return (
    <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-4 mb-6">
      {stats.map((stat, index) => (
        <div
          key={index}
          className={`bg-white dark:bg-gray-800 rounded-xl shadow-sm p-4 transition-all hover:shadow-md`}
        >
          <div className="flex items-center space-x-3 mb-3">
            <div className={`flex items-center justify-center w-8 h-8 bg-${stat.color}-100 text-${stat.color}-500 dark:bg-${stat.color}-900 dark:text-${stat.color}-400 rounded-full`}>
              {stat.icon}
            </div>
            <div>
              <p className="text-sm font-medium text-gray-900 dark:text-white">
                {stat.label}
              </p>
              <p className="text-2xl font-bold text-gray-900 dark:text-white">
                {stat.value}
              </p>
            </div>
          </div>
        </div>
      ))}
    </div>
  );
};

export default OwnerStatsGrid;