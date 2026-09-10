import { DollarSign, Calendar, Users, TrendingUp } from 'lucide-react';

const RevenueCard = () => {
  const stats = [
    {
      label: 'Total Earnings',
      value: '$12,450',
      icon: <DollarSign className="h-5 w-5 text-green-500" />,
      color: 'green'
    },
    {
      label: 'This Month',
      value: '$2,450',
      icon: <Calendar className="h-5 w-5 text-blue-500" />,
      color: 'blue'
    },
    {
      label: 'Active Rentals',
      value: '3',
      icon: <Users className="h-5 w-5 text-purple-500" />,
      color: 'purple'
    },
    {
      label: 'Growth Rate',
      value: '+23%',
      icon: <TrendingUp className="h-5 w-5 text-yellow-500" />,
      color: 'yellow'
    }
  ];

  return (
    <div className="bg-white dark:bg-gray-800 rounded-xl shadow-sm p-6">
      <h3 className="text-lg font-medium text-gray-900 dark:text-white mb-4">
        Overview
      </h3>
      <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-4">
        {stats.map((stat, index) => (
          <div
            key={index}
            className="p-3 bg-gray-50 dark:bg-gray-900/50 rounded-lg"
          >
            <div className="flex items-center space-x-3 mb-2">
              <div className={`flex items-center justify-center w-8 h-8 bg-${stat.color}-100 text-${stat.color}-500 dark:bg-${stat.color}-900 dark:text-${stat.color}-400 rounded-full`}>
                {stat.icon}
              </div>
              <div>
                <p className="text-sm font-medium text-gray-700 dark:text-gray-300">
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
    </div>
  );
};

export default RevenueCard;