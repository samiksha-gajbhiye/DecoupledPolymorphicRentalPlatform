import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';

const PriceRecommendations = () => {
  // Sample pricing recommendation data
  const pricingData = [
    { day: 'Mon', price: 70 },
    { day: 'Tue', price: 72 },
    { day: 'Wed', price: 75 },
    { day: 'Thu', price: 78 },
    { day: 'Fri', price: 85 },
    { day: 'Sat', price: 95 },
    { day: 'Sun', price: 90 }
  ];

  return (
    <div className="bg-white dark:bg-gray-800 rounded-xl shadow-sm p-6">
      <div className="flex items-center justify-between mb-4">
        <h3 className="text-lg font-medium text-gray-900 dark:text-white">
          Daily Price Recommendations
        </h3>
        <a href="/owner/pricing" className="text-sm text-blue-600 hover:text-blue-500 dark:hover:text-blue-400 font-medium">
          View Details
        </a>
      </div>
      <div className="h-48">
        <ResponsiveContainer width="100%" height="100%">
          <BarChart data={pricingData}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="day" tick={{ fontSize: 12 }} />
            <YAxis tick={{ fontSize: 12 }} />
            <Tooltip />
            <Legend />
            <Bar dataKey="price" fill="#10b981" radius={[4, 4, 0, 0]} />
          </BarChart>
        </ResponsiveContainer>
      </div>
      <div className="mt-4 text-sm text-gray-500 dark:text-gray-400">
        Based on market demand, day of week, and seasonal trends
      </div>
    </div>
  );
};

export default PriceRecommendations;