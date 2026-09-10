import { useAuth } from '../../context/AuthContext';
import { Sun } from 'lucide-react';
import { useState, useEffect } from 'react';

const WelcomeCard = () => {
  const { user } = useAuth();
  const [greeting, setGreeting] = useState('Good morning');

  // Set greeting based on time of day
  useEffect(() => {
    const hour = new Date().getHours();
    if (hour < 12) setGreeting('Good morning');
    else if (hour < 18) setGreeting('Good afternoon');
    else setGreeting('Good evening');
  }, []);

  return (
    <div className="bg-white dark:bg-gray-800 rounded-xl shadow-sm p-6 mb-6">
      <div className="flex items-center space-x-4 mb-4">
        <div className="flex items-center justify-center w-10 h-10 bg-blue-500 text-white rounded-full">
          <Sun className="h-5 w-5" />
        </div>
        <div>
          <p className="text-sm text-gray-500 dark:text-gray-400">
            {greeting},
          </p>
          <p className="text-xl font-bold text-gray-900 dark:text-white">
            {user?.name || 'User'}!
          </p>
        </div>
      </div>
      <p className="text-gray-600 dark:text-gray-300">
        Here's a quick overview of your rental activity. Keep track of your bookings, earnings, and more.
      </p>
    </div>
  );
};

export default WelcomeCard;