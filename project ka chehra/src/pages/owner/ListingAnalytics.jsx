import AnalyticsCard from '../../components/owner/AnalyticsCard';
import ViewsChart from '../../components/owner/ViewsChart';
import BookingConversion from '../../components/owner/BookingConversion';

const ListingAnalytics = () => {
  return (
    <div className="min-h-screen bg-gray-50 dark:bg-gray-900">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <div className="mb-6">
          <h1 className="text-2xl font-bold text-gray-900 dark:text-white">
            Listing Analytics
          </h1>
          <p className="text-gray-600 dark:text-gray-300">
            Detailed insights into your listing performance
          </p>
        </div>

        <AnalyticsCard />
        <div className="grid gap-6 md:grid-cols-2">
          <ViewsChart />
          <BookingConversion />
        </div>
      </div>
    </div>
  );
};

export default ListingAnalytics;