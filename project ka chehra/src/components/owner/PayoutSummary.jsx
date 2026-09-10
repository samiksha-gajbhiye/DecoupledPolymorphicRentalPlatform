import { CreditCard, Calendar, CheckCircle } from 'lucide-react';

const PayoutSummary = () => {
  const recentPayouts = [
    {
      id: 1,
      date: "2026-08-20",
      amount: 375,
      status: "completed",
      method: "Bank Transfer"
    },
    {
      id: 2,
      date: "2026-08-18",
      amount: 240,
      status: "completed",
      method: "Bank Transfer"
    },
    {
      id: 3,
      date: "2026-08-15",
      amount: 70,
      status: "pending",
      method: "Bank Transfer"
    },
    {
      id: 4,
      date: "2026-08-10",
      amount: 150,
      status: "completed",
      method: "PayPal"
    }
  ];

  return (
    <div className="bg-white dark:bg-gray-800 rounded-xl shadow-sm p-6">
      <div className="flex items-center justify-between mb-4">
        <h3 className="text-lg font-medium text-gray-900 dark:text-white">
          Recent Payouts
        </h3>
        <a href="/owner/revenue" className="text-sm text-blue-600 hover:text-blue-500 dark:hover:text-blue-400 font-medium">
          View All
        </a>
      </div>
      <div className="space-y-4">
        {recentPayouts.map(payout => (
          <div key={payout.id} className="p-3 bg-gray-50 dark:bg-gray-900/50 rounded-lg">
            <div className="flex justify-between items-start">
              <div className="space-y-1">
                <p className="text-sm font-medium text-gray-900 dark:text-white">
                  ₹{payout.amount}
                </p>
                <p className="text-xs text-gray-500 dark:text-gray-400">
                  {new Date(payout.date).toLocaleDateString('en-GB', {
                    day: '2-digit',
                    month: '2-digit',
                    year: 'numeric'
                  })} • {payout.method}
                </p>
              </div>
              <div className="flex items-center space-x-2">
                <div className={`flex items-center justify-center w-5 h-5
                  ${payout.status === 'completed' ? 'bg-green-100 text-green-500 dark:bg-green-900 dark:text-green-400' :
                    payout.status === 'pending' ? 'bg-yellow-100 text-yellow-500 dark:bg-yellow-900 dark:text-yellow-400' :
                    'bg-red-100 text-red-500 dark:bg-red-900 dark:text-red-400'} rounded-full`}>
                  {payout.status === 'completed' && (
                    <CheckCircle className="h-3 w-3" />
                  )}
                  {payout.status === 'pending' && (
                    <Calendar className="h-3 w-3" />
                  )}
                </div>
                <span className="text-xs text-gray-600 dark:text-gray-300">
                  {payout.status.charAt(0).toUpperCase() + payout.status.slice(1)}
                </span>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default PayoutSummary;