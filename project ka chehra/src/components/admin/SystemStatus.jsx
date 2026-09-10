import { Server, Database, Wifi, Zap } from 'lucide-react';

const SystemStatus = () => {
  const services = [
    {
      name: 'API Server',
      status: 'online',
      icon: <Server className="h-4 w-4 text-green-500" />
    },
    {
      name: 'Database',
      status: 'online',
      icon: <Database className="h-4 w-4 text-green-500" />
    },
    {
      name: 'Payment Gateway',
      status: 'online',
      icon: <Wifi className="h-4 w-4 text-green-500" />
    },
    {
      name: 'AI Services',
      status: 'online',
      icon: <Zap className="h-4 w-4 text-green-500" />
    }
  ];

  return (
    <div className="bg-white dark:bg-gray-800 rounded-xl shadow-sm p-6">
      <div className="flex items-center justify-between mb-4">
        <h3 className="text-lg font-medium text-gray-900 dark:text-white">
          System Status
        </h3>
        <a href="/admin/system-health" className="text-sm text-blue-600 hover:text-blue-500 dark:hover:text-blue-400 font-medium">
          View Details
        </a>
      </div>
      <div className="space-y-3">
        {services.map(service => (
          <div key={service.name} className="flex items-center justify-between p-2 bg-gray-50 dark:bg-gray-900/50 rounded">
            <div className="flex items-center space-x-3">
              {service.icon}
              <span className="text-sm font-medium text-gray-900 dark:text-white">
                {service.name}
              </span>
            </div>
            <span className={`px-2 py-0.5 text-xs rounded-full
              ${service.status === 'online' ? 'bg-green-100 text-green-800 dark:bg-green-900 dark:text-green-200' :
                service.status === 'degraded' ? 'bg-yellow-100 text-yellow-800 dark:bg-yellow-900 dark:text-yellow-200' :
                'bg-red-100 text-red-800 dark:bg-red-900 dark:text-red-200'}`}>
              {service.status.charAt(0).toUpperCase() + service.status.slice(1)}
            </span>
          </div>
        ))}
      </div>
    </div>
  );
};

export default SystemStatus;