import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';

const RevenueOverview = () => {
  // Sample monthly revenue data for admin overview
  const monthlyData = [
    { month: 'Jan', revenue: 8500, profit: 4200 },
    { month: 'Feb', revenue: 9200, profit: 4600 },
    { month: 'Mar', revenue: 7800, profit: 3900 },
    { month: 'Apr', revenue: 11000, profit: 5500 },
    { month: 'May', revenue: 9500, profit: 4750 },
    { month: 'Jun', revenue: 12500, profit: 6250 },
    { month: 'Jul', revenue: 10800, profit: 5400 },
    { month: 'Aug', revenue: 13200, profit: 6600 }
  ];

  return (
    <div className="bg-white dark:bg-gray-800 rounded-xl shadow-sm p-6">
      <div className="flex items-center justify-between mb-4">
        <h3 className="text-lg font-medium text-gray-900 dark:text-white">
          Platform Revenue
        </h3>
        <a href="/admin/reports" className="text-sm text-blue-600 hover:text-blue-500 dark:hover:text-blue-400 font-medium">
          View Detailed Reports
        </a>
      </div>
      <div className="h-48">
        <ResponsiveContainer width="100%" height="100%">
          <BarChart data={monthlyData}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="month" tick={{ fontSize: 12 }} />
            <YAxis tick={{ fontSize: 12 }} />
            <Tooltip />
            <Legend verticalAlign="top" height={36} />
            <Bar dataKey="revenue" fill="#3b82f6" radius={[4, 4, 0, 0]} />
            <Bar dataKey="profit" fill="#10b981" radius={[4, 4, 0, 0]} />
          </BarChart>
        </ResponsiveContainer>
      </div>
      <div className="mt-4 text-sm text-gray-500 dark:text-gray-400 flex justify-between">
        <span>Total Revenue: $82,500</span>
        <span>Total Profit: $41,250</span>
        <span>Profit Margin: 50%</span>
      </div>
    </div>
  );
};

export default RevenueOverview;