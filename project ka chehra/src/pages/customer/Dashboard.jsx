import WelcomeCard from '../../components/customer/WelcomeCard';
import StatsGrid from '../../components/customer/StatsGrid';
import ActiveRentalsCard from '../../components/customer/ActiveRentalsCard';
import UpcomingBookingsCard from '../../components/customer/UpcomingBookingsCard';
import RecentActivity from '../../components/customer/RecentActivity';

const CustomerDashboard = () => {
  return (
    <div className="min-h-screen bg-gray-50 dark:bg-gray-900">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <h1 className="text-2xl font-bold text-gray-900 dark:text-white mb-6">
          Dashboard
        </h1>

        <WelcomeCard />
        <StatsGrid />
        <div className="grid gap-6 md:grid-cols-2">
          <ActiveRentalsCard />
          <UpcomingBookingsCard />
        </div>
        <RecentActivity className="mt-6" />
      </div>
    </div>
  );
};

export default CustomerDashboard;