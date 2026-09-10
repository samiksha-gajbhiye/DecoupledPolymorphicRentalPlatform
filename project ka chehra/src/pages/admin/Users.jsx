import UserCard from '../../components/admin/UserCard';

const AdminUsers = () => {
  const users = [
    {
      id: 1,
      name: "Alex Johnson",
      email: "alex@example.com",
      role: "CUSTOMER",
      status: "active",
      joined: "2026-01-15",
      avatar: "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=100"
    },
    {
      id: 2,
      name: "Sarah Chen",
      email: "sarah@example.com",
      role: "OWNER",
      status: "active",
      joined: "2026-02-03",
      avatar: "https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=100"
    },
    {
      id: 3,
      name: "Mike Wilson",
      email: "mike@example.com",
      role: "ADMIN",
      status: "active",
      joined: "2026-01-10",
      avatar: "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=100"
    },
    {
      id: 4,
      name: "Lisa Brown",
      email: "lisa@example.com",
      role: "CUSTOMER",
      status: "suspended",
      joined: "2026-03-22",
      avatar: "https://images.unsplash.com/photo-1526622510178-ace0b2978ff6?w=100"
    }
  ];

  return (
    <div className="min-h-screen bg-gray-50 dark:bg-gray-900">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <div className="mb-6">
          <h1 className="text-2xl font-bold text-gray-900 dark:text-white">
            Users
          </h1>
          <div className="flex items-center justify-between mt-4">
            <div className="flex items-center space-x-3 text-sm text-gray-500 dark:text-gray-400">
              <span>Total Users: {users.length}</span>
              <span className="mx-2">•</span>
              <span>Active: {users.filter(u => u.status === 'active').length}</span>
            </div>
            <input
              type="text"
              placeholder="Search users..."
              className="w-48 px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:text-white dark:focus:ring-blue-400"
            />
          </div>
        </div>

        <div className="space-y-4">
          {users.map(user => (
            <UserCard key={user.id} user={user} />
          ))}
        </div>
      </div>
    </div>
  );
};

export default AdminUsers;