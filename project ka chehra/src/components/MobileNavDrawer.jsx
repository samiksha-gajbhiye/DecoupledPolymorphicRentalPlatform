import { useState } from 'react';
import { Link } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import { useTheme } from '../context/ThemeContext';
import { X } from 'lucide-react';

const MobileNavDrawer = () => {
  const { user } = useAuth();
  const { theme } = useTheme();
  const [isOpen, setIsOpen] = useState(false);

  return (
    <>
      {/* Mobile Navigation Drawer */}
      <div className={`fixed inset-0 z-50 flex items-end bg-black/50 ${isOpen ? 'block' : 'hidden'}`} onClick={() => setIsOpen(false)}>
        <div className="relative w-full max-w-xs flex-1 flex-col bg-white dark:bg-gray-800 p-6" onClick={(e) => e.stopPropagation()}>
          <div className="flex justify-between items-start mb-6">
            <div className="flex items-center">
              <span className="text-xl font-bold text-gray-800 dark:text-gray-100">DemoRental</span>
            </div>
            <button onClick={() => setIsOpen(false)} className="p-1 rounded hover:bg-gray-100 dark:hover:bg-gray-700">
              <X className="h-5 w-5" />
            </button>
          </div>

          {/* Navigation Links */}
          <nav className="space-y-4">
            <Link to="/browse" className="block px-3 py-2 rounded text-gray-700 hover:bg-gray-100 dark:hover:bg-gray-700 transition-colors">Explore</Link>
            <Link to="/categories" className="block px-3 py-2 rounded text-gray-700 hover:bg-gray-100 dark:hover:bg-gray-700 transition-colors">Categories</Link>
            <Link to="/customer/recommendations" className="block px-3 py-2 rounded text-gray-700 hover:bg-gray-100 dark:hover:bg-gray-700 transition-colors">Recommendations</Link>
            <Link to="/owner/listings/add" className="block px-3 py-2 rounded text-gray-700 hover:bg-gray-100 dark:hover:bg-gray-700 transition-colors">Become a Host</Link>
          </nav>

          {/* User Section */}
          <div className="mt-8 pt-4 border-t border-gray-200 dark:border-gray-700">
            {user ? (
              <div className="space-y-3">
                <div className="flex items-center space-x-3">
                  <img
                    src={user.avatar || 'https://ui-avatars.com/api/?name=' + encodeURIComponent(user.name)}
                    alt="Avatar"
                    className="h-10 w-10 rounded-full"
                  />
                  <div>
                    <p className="font-medium text-gray-800 dark:text-gray-100">{user.name}</p>
                    <p className="text-sm text-gray-500 dark:text-gray-400">{user.role}</p>
                  </div>
                </div>
                <div className="space-y-2">
                  <Link to={`/customer/dashboard`} className="block px-3 py-2 rounded text-sm text-gray-700 hover:bg-gray-100 dark:hover:bg-gray-700 transition-colors">Dashboard</Link>
                  <Link to={`/customer/profile`} className="block px-3 py-2 rounded text-sm text-gray-700 hover:bg-gray-100 dark:hover:bg-gray-700 transition-colors">Profile</Link>
                  <Link to={`/customer/settings`} className="block px-3 py-2 rounded text-sm text-gray-700 hover:bg-gray-100 dark:hover:bg-gray-700 transition-colors">Settings</Link>
                  <button onClick={() => { /* logout */ }} className="block w-full text-left px-3 py-2 rounded text-sm text-gray-700 hover:bg-gray-100 dark:hover:bg-gray-700 transition-colors">Logout</button>
                </div>
              </div>
            ) : (
              <div className="space-y-3">
                <Link to="/login" className="block w-full px-3 py-2 rounded bg-blue-600 text-white text-sm font-medium hover:bg-blue-700 transition-colors">Login</Link>
                <Link to="/register" className="block w-full px-3 py-2 rounded border border-gray-300 text-sm font-medium text-gray-700 hover:bg-gray-50 dark:hover:bg-gray-700 dark:hover:text-white dark:border-gray-600 transition-colors">Register</Link>
              </div>
            )}
          </div>
        </div>
      </div>

      {/* Backdrop for closing drawer when clicking outside */}
      <div className={isOpen ? 'fixed inset-0 z-40 bg-black/50' : 'hidden'} onClick={() => setIsOpen(false)}></div>
    </>
  );
};

export default MobileNavDrawer;