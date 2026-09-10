import { PieChart, Pie, Cell, Tooltip, Legend, ResponsiveContainer } from 'recharts';

const MarketAnalysis = () => {
  // Sample market analysis data
  const demandData = [
    { name: 'Weekends', value: 40 },
    { name: 'Weekdays', value: 25 },
    { name: 'Events', value: 20 },
    { name: 'Holidays', value: 15 }
  ];

  const seasonalData = [
    { name: 'Summer', value: 35 },
    { name: 'Winter', value: 20 },
    { name: 'Spring', value: 25 },
    { name: 'Fall', value: 20 }
  ];

  return (
    <div className="bg-white dark:bg-gray-800 rounded-xl shadow-sm p-6 space-y-6">
      <div className="flex items-center justify-between mb-4">
        <h3 className="text-lg font-medium text-gray-900 dark:text-white">
          Market Insights
        </h3>
        <a href="/owner/pricing" className="text-sm text-blue-600 hover:text-blue-500 dark:hover:text-blue-400 font-medium">
          View Details
        </a>
      </div>

      <div className="grid gap-6 sm:grid-cols-2">
        <div>
          <h4 className="text-sm font-medium text-gray-900 dark:text-white mb-2">
            Demand by Time Period
          </h4>
          <div className="h-32">
            <ResponsiveContainer width="100%" height="100%">
              <PieChart>
                <Pie data={demandData} dataKey="value" nameKey="name" cx="50%" cy="50%" innerRadius="60%" outerRadius="80%" labelLine={false} label={false}>
                  {demandData.map((entry, index) => (
                    <Cell key={`cell-${index}`} fill={['#3b82f6', '#10b981', '#f59e0b', '#ef4444'][index]} />
                  ))}
                </Pie>
                <Tooltip />
                <Legend verticalAlign="top" height={36} />
              </PieChart>
            </ResponsiveContainer>
          </div>
        </div>

        <div>
          <h4 className="text-sm font-medium text-gray-900 dark:text-white mb-2">
            Seasonal Trends
          </h4>
          <div className="h-32">
            <ResponsiveContainer width="100%" height="100%">
              <PieChart>
                <Pie data={seasonalData} dataKey="value" nameKey="name" cx="50%" cy="50%" innerRadius="60%" outerRadius="80%" labelLine={false} label={false}>
                  {seasonalData.map((entry, index) => (
                    <Cell key={`cell-${index}`} fill={['#8b5cf6', '#ec4899', '#06b6d4', '#84cc16'][index]} />
                  ))}
                </Pie>
                <Tooltip />
                <Legend verticalAlign="top" height={36} />
              </PieChart>
            </ResponsiveContainer>
          </div>
        </div>
      </div>
    </div>
  );
};

export default MarketAnalysis;