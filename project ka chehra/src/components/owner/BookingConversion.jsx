import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';

const BookingConversion = () => {
  // Sample conversion data (views vs bookings)
  const conversionData = [];
  for (let i = 6; i >= 0; i--) {
    const date = new Date();
    date.setDate(date.getDate() - i);
    conversionData.push({
      date: date.toLocaleDateString('en-GB', { day: '2-digit', month: '2-digit', year: 'numeric' }),
      views: Math.floor(Math.random() * 100) + 20,
      bookings: Math.floor(Math.random() * 15) + 2
    });
  }

  return (
    <div className="bg-white dark:bg-gray-800 rounded-xl shadow-sm p-6">
      <div className="flex items-center justify-between mb-4">
        <h3 className="text-lg font-medium text-gray-900 dark:text-white">
          Booking Conversion
        </h3>
        <a href="/owner/analytics" className="text-sm text-blue-600 hover:text-blue-500 dark:hover:text-blue-400 font-medium">
          View Details
        </a>
      </div>
      <div className="h-48">
        <ResponsiveContainer width="100%" height="100%">
          <BarChart data={conversionData}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="date" tick={{ fontSize: 12 }} />
            <YAxis tick={{ fontSize: 12 }} />
            <Tooltip />
            <Legend verticalAlign="top" height={36} />
            <Bar dataKey="views" fill="#3b82f6" radius={[4, 4, 0, 0]} />
            <Bar dataKey="bookings" fill="#10b981" radius={[4, 4, 0, 0]} />
          </BarChart>
        </ResponsiveContainer>
      </div>
      <div className="mt-3 text-sm text-gray-500 dark:text-gray-400 flex justify-between">
        <span>Views: 420</span>
        <span>Bookings: 52</span>
        <span>Conversion Rate: 12.4%</span>
      </div>
    </div>
  );
};

export default BookingConversion;