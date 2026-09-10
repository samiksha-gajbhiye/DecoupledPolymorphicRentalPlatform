import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';

const RevenueTrends = () => {
  // Sample monthly revenue data for the last 12 months
  const revenueData = [
    { month: 'Jan', revenue: 1200 },
    { month: 'Feb', revenue: 1350 },
    { month: 'Mar', revenue: 1200 },
    { month: 'Apr', revenue: 1800 },
    { month: 'May', revenue: 1500 },
    { month: 'Jun', revenue: 2200 },
    { month: 'Jul', revenue: 1900 },
    { month: 'Aug', revenue: 2450 },
    { month: 'Sep', revenue: 2100 },
    { month: 'Oct', revenue: 2300 },
    { month: 'Nov', revenue: 2000 },
    { month: 'Dec', revenue: 2600 }
  ];

  return (
    <div className="bg-white dark:bg-gray-800 rounded-xl shadow-sm p-6">
      <div className="flex items-center justify-between mb-4">
        <h3 className="text-lg font-medium text-gray-900 dark:text-white">
          Revenue Trends
        </h3>
        <a href="/owner/revenue" className="text-sm text-blue-600 hover:text-blue-500 dark:hover:text-blue-400 font-medium">
          View Details
        </a>
      </div>
      <div className="h-48">
        <ResponsiveContainer width="100%" height="100%">
          <LineChart data={revenueData}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="month" tick={{ fontSize: 12 }} />
            <YAxis tick={{ fontSize: 12 }} />
            <Tooltip />
            <Legend />
            <Line type="monotone" dataKey="revenue" stroke="#3b82f6" strokeWidth={2} point={false} />
          </LineChart>
        </ResponsiveContainer>
      </div>
    </div>
  );
};

export default RevenueTrends;