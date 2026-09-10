import { Calendar, Users, ShieldCheck, XCircle } from 'lucide-react';

const UserCard = ({ user }) => {
  const statusVariants = {
    active: { bg: 'bg-green-100 dark:bg-green-900/20', text: 'text-green-800 dark:text-green-200' },
    suspended: { bg: 'bg-red-100 dark:bg-red-900/20', text: 'text-red-800 dark:text-red-200' },
    pending: { bg: 'bg-yellow-100 dark:bg-yellow-900/20', text: 'text-yellow-800 dark:text-yellow-200' }
  };

  const variant = statusVariants[user.status] || statusVariants.active;

  return (
    <div className="flex items-start space-x-4 p-4 border-b border-gray-200 dark:border-gray-700 last:border-0">
      <img
        src={user.avatar}
        alt={user.name}
        className="w-10 h-10 rounded-full"
      />
      <div className="flex-1 space-y-2">
        <div className="flex justify-between items-start">
          <h3 className="font-medium text-gray-900 dark:text-white">{user.name}</h3>
          <span className={`px-2 py-1 text-xs rounded-full ${variant.bg} ${variant.text}`}>
            {user.status.charAt(0).toUpperCase() + user.status.slice(1)}
          </span>
        </div>
        <div className="flex items-center space-x-2 text-sm text-gray-500 dark:text-gray-400">
          <Users className="h-4 w-4" />
          <span>{user.role}</span>
        </div>
        <div className="flex items-center space-x-2 text-sm text-gray-500 dark:text-gray-400">
          <Calendar className="h-4 w-4" />
          <span>{user.joined}</span>
        </div>
      </div>
      <div className="flex items-center space-x-3 text-sm">
        <button
          onClick={() => { /* edit user logic */ }}
          className="px-3 py-1 text-xs font-medium bg-blue-100 text-blue-800 rounded hover:bg-blue-200 dark:hover:bg-blue-800/20"
        >
          Edit
        </button>
        {user.status !== 'suspended' && (
          <button
            onClick={() => { /* suspend user logic */ }}
            className="px-3 py-1 text-xs font-medium bg-red-100 text-red-800 rounded hover:bg-red-200 dark:hover:bg-red-800/20 ml-2"
          >
            Suspend
          </button>
        )}
        {user.status === 'suspended' && (
          <button
            onClick={() => { /* activate user logic */ }}
            className="px-3 py-1 text-xs font-medium bg-green-100 text-green-800 rounded hover:bg-green-200 dark:hover:bg-green-800/20 ml-2"
          >
            Activate
          </button>
        )}
      </div>
    </div>
  );
};

export default UserCard;