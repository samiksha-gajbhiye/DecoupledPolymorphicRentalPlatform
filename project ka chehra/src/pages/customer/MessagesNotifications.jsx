import { MessageSquare, Bell, UserPlus, CheckCircle } from 'lucide-react';

const MessagesNotifications = () => {
  const notifications = [
    {
      id: 1,
      type: 'message',
      title: 'New message from Alex Johnson',
      content: 'Hey! Is the camera kit still available for the weekend?',
      time: '2 hours ago',
      unread: true
    },
    {
      id: 2,
      type: 'booking',
      title: 'Booking confirmed',
      content: 'Your booking for the Electric Scooter has been confirmed.',
      time: 'Yesterday',
      unread: false
    },
    {
      id: 3,
      type: 'system',
      title: 'New feature: AI Recommendations',
      content: 'Discover personalized rental suggestions based on your history.',
      time: '3 days ago',
      unread: false
    }
  ];

  return (
    <div className="min-h-screen bg-gray-50 dark:bg-gray-900">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <div className="mb-6">
          <h1 className="text-2xl font-bold text-gray-900 dark:text-white">
            Messages & Notifications
          </h1>
          <div className="mt-2 flex items-center space-x-4 text-sm text-gray-500 dark:text-gray-400">
            <span>Total: {notifications.length}</span>
            <span className="mx-2">•</span>
            <span>Unread: {notifications.filter(n => n.unread).length}</span>
          </div>
        </div>

        <div className="space-y-4">
          {notifications.map(notification => (
            <div
              key={notification.id}
              className={`flex items-start space-x-4 p-4 bg-white dark:bg-gray-800 rounded-xl shadow-sm ${notification.unread ? 'border-l-4 border-blue-500' : ''}`}
            >
              <div className="flex-shrink-0">
                {notification.type === 'message' && (
                  <MessageSquare className="h-5 w-5 text-blue-500" />
                )}
                {notification.type === 'booking' && (
                  <Bell className="h-5 w-5 text-blue-500" />
                )}
                {notification.type === 'system' && (
                  <UserPlus className="h-5 w-5 text-blue-500" />
                )}
              </div>
              <div className="flex-1 space-y-2">
                <div className="flex justify-between items-start">
                  <h3 className="font-medium text-gray-900 dark:text-white">{notification.title}</h3>
                  <span className="text-xs px-2 py-0.5 rounded-full
                    {notification.unread ? 'bg-blue-100 text-blue-800 dark:bg-blue-900/20 dark:text-blue-200' : 'bg-gray-100 text-gray-800 dark:bg-gray-900/20 dark:text-gray-200'}
                  ">
                    {notification.unread ? 'New' : 'Read'}
                  </span>
                </div>
                <p className="text-sm text-gray-600 dark:text-gray-400">{notification.content}</p>
                <div className="text-right text-sm text-gray-500 dark:text-gray-400">
                  {notification.time}
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default MessagesNotifications;