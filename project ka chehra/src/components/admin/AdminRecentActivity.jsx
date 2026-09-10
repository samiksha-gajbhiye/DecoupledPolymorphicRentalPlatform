import { MessageSquare, UserPlus, Calendar, Truck, CreditCard, ShieldCheck } from 'lucide-react';

const AdminRecentActivity = () => {
  const activities = [
    {
      id: 1,
      type: 'user',
      title: 'New user registered',
      description: 'Alex Johnson signed up as a customer',
      time: '2 minutes ago',
      icon: <UserPlus className="h-4 w-4 text-blue-500" />
    },
    {
      id: 2,
      type: 'listing',
      title: 'New listing approved',
      description: 'Professional Drone Kit (Electronics)',
      time: '5 minutes ago',
      icon: <MessageSquare className="h-4 w-4 text-green-500" />
    },
    {
      id: 3,
      type: 'booking',
      title: 'Booking completed',
      description: 'Electric Scooter rental completed',
      time: '12 minutes ago',
      icon: <Truck className="h-4 w-4 text-purple-500" />
    },
    {
      id: 4,
      type: 'payment',
      title: 'Payment processed',
      description: '₹85.50 paid for Camera Lens rental',
      time: '20 minutes ago',
      icon: <CreditCard className="h-4 w-4 text-yellow-500" />
    },
    {
      id: 5,
      type: 'security',
      title: 'Fraud detected',
      description: 'Suspicious login attempt blocked',
      time: '35 minutes ago',
      icon: <ShieldCheck className="h-4 w-4 text-red-500" />
    }
  ];

  return (
    <div className="bg-white dark:bg-gray-800 rounded-xl shadow-sm p-6">
      <div className="flex items-center justify-between mb-4">
        <h3 className="text-lg font-medium text-gray-900 dark:text-white">
          Recent Activity
        </h3>
        <a href="/admin/reports" className="text-sm text-blue-600 hover:text-blue-500 dark:hover:text-blue-400 font-medium">
          View All
        </a>
      </div>
      <div className="space-y-4">
        {activities.map(activity => (
          <div key={activity.id} className="flex items-start space-x-3 p-3 bg-gray-50 dark:bg-gray-900/50 rounded">
            <div className="flex-shrink-0">
              {activity.icon}
            </div>
            <div className="flex-1 space-y-1">
              <h3 className="font-medium text-gray-900 dark:text-white">{activity.title}</h3>
              <p className="text-sm text-gray-600 dark:text-gray-400">
                {activity.description}
              </p>
              <p className="text-xs text-gray-500 dark:text-gray-300">
                {activity.time}
              </p>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default AdminRecentActivity;