import { Eye, Calendar, CheckCircle, Users } from 'lucide-react';

const AnalyticsCard = () => {
  const stats = [
    {
      label: 'Total Views',
      value: '1,240',
      icon: <Eye className="h-5 w-5 text-blue-500" />,
      color: 'blue'
    },
    {
      label: 'Booking Rate',
      value: '12%',
      icon: <CheckCircle className="h-5 w-5 text-green-500" />,
      color: 'green'
    },
    {
      label: 'Avg. Rating',
      value: '4.8',
      icon: <Users className="h-5 w-5 text-purple-500" />,
      color: 'purple'
    },
    {
      label: 'Response Time',
      value: '2.1 hrs',
      icon: <Calendar className="h-5 w-5 text-yellow-500" />,
      color: 'yellow'
    }
  ];

  return (
    <div className="bg-white dark:bg-gray-800 rounded-xl shadow-sm p-6">
      <h3 className="text-lg font-medium text-gray-900 dark:text-white mb-4">
        Performance Overview
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

export default AnalyticsCard;