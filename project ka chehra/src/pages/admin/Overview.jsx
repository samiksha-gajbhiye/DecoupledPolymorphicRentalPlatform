import AdminStatsGrid from '../../components/admin/AdminStatsGrid';
import RecentActivity from '../../components/admin/AdminRecentActivity';
import SystemStatus from '../../components/admin/SystemStatus';
import RevenueOverview from '../../components/admin/RevenueOverview';

const AdminOverview = () => {
  return (
    <div className="min-h-screen bg-gray-50 dark:bg-gray-900">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <div className="mb-6">
          <h1 className="text-2xl font-bold text-gray-900 dark:text-white mb-2">
            Admin Dashboard
          </h1>
          <p className="text-gray-600 dark:text-gray-300">
            Overview of platform activity, revenue, and system health
          </p>
        </div>

        <AdminStatsGrid />
        <div className="grid gap-6 md:grid-cols-2">
          <RecentActivity />
          <SystemStatus />
        </div>
        <RevenueOverview className="mt-6" />
      </div>
    </div>
  );
};

export default AdminOverview;