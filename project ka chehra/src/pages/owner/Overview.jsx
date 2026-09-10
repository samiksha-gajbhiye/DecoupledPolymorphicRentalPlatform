import WelcomeCard from '../../components/owner/WelcomeCard';
import OwnerStatsGrid from '../../components/owner/OwnerStatsGrid';
import RecentListings from '../../components/owner/RecentListings';
import RevenueChart from '../../components/owner/RevenueChart';

const OwnerOverview = () => {
  return (
    <div className="min-h-screen bg-gray-50 dark:bg-gray-900">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <h1 className="text-2xl font-bold text-gray-900 dark:text-white mb-6">
          Owner Dashboard
        </h1>

        <WelcomeCard />
        <OwnerStatsGrid />
        <div className="grid gap-6 md:grid-cols-2">
          <RecentListings />
          <RevenueChart />
        </div>
      </div>
    </div>
  );
};

export default OwnerOverview;