import { Link } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import { useTheme } from '../context/ThemeContext';
import { Bell, Moon, Sun, Menu } from 'lucide-react';

const Navbar = () => {
  const { user } = useAuth();
  const { theme, toggleTheme } = useTheme();

  return (
    <nav className="site-nav">
      <div className="nav-inner">
          <div className="flex items-center">
            <Link to="/" className="flex-shrink-0">
              <span className="brand-mark"><b>d</b> demorental.</span>
            </Link>
          </div>
          <div className="nav-links">
            <Link to="/browse">Explore</Link>
            <Link to="/categories">Categories</Link>
            <Link to="/customer/recommendations">Recommendations</Link>
            <Link to="/owner/listings/add">Become a Host</Link>
          </div>
          <div className="nav-actions">
            <div className="nav-search"><input type="search" placeholder="Search rentals..." aria-label="Search rentals" /></div>
            <button aria-label="Notifications" className="notification-toggle"><Bell size={19} /><i /></button>
            <button aria-label="Toggle theme" onClick={toggleTheme} className="theme-toggle">
              {theme === 'light' ? <Moon size={17} /> : <Sun size={17} />}
            </button>
            {/* User Menu */}
            {user ? (
              <div className="relative">
                <button className="flex items-center space-x-2 p-2 rounded hover:bg-gray-100 dark:hover:bg-gray-700 transition-colors">
                  <img
                    src={user.avatar || 'https://ui-avatars.com/api/?name=' + encodeURIComponent(user.name)}
                    alt="Avatar"
                    className="h-8 w-8 rounded-full"
                  />
                  <span className="hidden md:block">{user.name}</span>
                  <span className="ml-2">▼</span>
                </button>
                <div className="absolute right-0 mt-2 w-48 bg-white dark:bg-gray-800 rounded-md shadow-lg py-1 z-20 hidden">
                  <a href="#" className="block px-4 py-2 text-sm text-gray-700 dark:text-gray-200 hover:bg-gray-100 dark:hover:bg-gray-700">Profile</a>
                  <a href="#" className="block px-4 py-2 text-sm text-gray-700 dark:text-gray-200 hover:bg-gray-100 dark:hover:bg-gray-700">Settings</a>
                  <button onClick={() => { /* logout logic */ }} className="block w-full text-left px-4 py-2 text-sm text-gray-700 dark:text-gray-200 hover:bg-gray-100 dark:hover:bg-gray-700">Logout</button>
                </div>
              </div>
            ) : (
              <>
                <Link to="/login" className="login-link">Log in</Link>
                <Link to="/register" className="get-started">Get started <span>-&gt;</span></Link>
              </>
            )}
          </div>
          {/* Mobile Menu Button */}
          <button className="mobile-menu" id="mobile-menu-button" aria-label="Open menu">
            <Menu size={20} />
          </button>
        </div>
    </nav>
  );
};

export default Navbar;