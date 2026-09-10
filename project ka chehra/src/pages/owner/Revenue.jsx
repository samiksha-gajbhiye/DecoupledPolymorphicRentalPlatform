import RevenueCard from '../../components/owner/RevenueCard';
import RevenueTrends from '../../components/owner/RevenueTrends';
import PayoutSummary from '../../components/owner/PayoutSummary';

const Revenue = () => {
  return (
    <div className="min-h-screen bg-gray-50 dark:bg-gray-900">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <div className="mb-6">
          <h1 className="text-2xl font-bold text-gray-900 dark:text-white">
            Revenue
          </h1>
          <p className="text-gray-600 dark:text-gray-300">
            Track your earnings, payouts, and financial performance
          </p>
        </div>

        <RevenueCard />
        <div className="grid gap-6 md:grid-cols-2">
          <RevenueTrends />
          <PayoutSummary />
        </div>
      </div>
    </div>
  );
};

export default Revenue;