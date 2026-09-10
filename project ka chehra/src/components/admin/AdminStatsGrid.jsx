import { Users, Calendar, DollarSign, ShieldCheck } from 'lucide-react';

const AdminStatsGrid = () => {
  const stats = [
    {
      label: 'Total Users',
      value: '1,240',
      icon: <Users className="h-5 w-5 text-blue-500" />,
      color: 'blue'
    },
    {
      label: 'Active Listings',
      value: '856',
      icon: <Calendar className="h-5 w-5 text-green-500" />,
      color: 'green'
    },
    {
      label: 'Total Revenue',
      value: '₹124,500',
      icon: <DollarSign className="h-5 w-5 text-purple-500" />,
      color: 'purple'
    },
    {
      label: 'System Health',
      value: '99.8%',
      icon: <ShieldCheck className="h-5 w-5 text-yellow-500" />,
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

export default AdminStatsGrid;