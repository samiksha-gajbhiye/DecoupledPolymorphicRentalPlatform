const TrustSafety = () => {
  return (
    <section className="py-16 bg-gray-50 dark:bg-gray-900">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <h2 className="text-2xl font-bold text-gray-900 dark:text-white mb-10 text-center">
          Trust & Safety
        </h2>
        <div className="grid gap-8 sm:grid-cols-2 lg:grid-cols-4">
          <div className="flex items-center space-x-4 text-center">
            <div className="flex items-center justify-center w-12 h-12 bg-blue-100 text-blue-600 dark:bg-blue-900 dark:text-blue-400 rounded-full">
              <span className="text-xl">✓</span>
            </div>
            <div>
              <h3 className="font-semibold text-gray-900 dark:text-white">Verified Owners</h3>
              <p className="text-gray-600 dark:text-gray-300 text-sm">
                All hosts undergo identity verification to ensure secure transactions.
              </p>
            </div>
          </div>
          <div className="flex items-center space-x-4 text-center">
            <div className="flex items-center justify-center w-12 h-12 bg-blue-100 text-blue-600 dark:bg-blue-900 dark:text-blue-400 rounded-full">
              <span className="text-xl">🔒</span>
            </div>
            <div>
              <h3 className="font-semibold text-gray-900 dark:text-white">Secure Payments</h3>
              <p className="text-gray-600 dark:text-gray-300 text-sm">
                Industry-standard encryption protects your financial information.
              </p>
            </div>
          </div>
          <div className="flex items-center space-x-4 text-center">
            <div className="flex items-center justify-center w-12 h-12 bg-blue-100 text-blue-600 dark:bg-blue-900 dark:text-blue-400 rounded-full">
              <span className="text-xl">🛡️</span>
            </div>
            <div>
              <h3 className="font-semibold text-gray-900 dark:text-white">Fraud Detection</h3>
              <p className="text-gray-600 dark:text-gray-300 text-sm">
                AI-powered systems monitor for suspicious activity and prevent fraud.
              </p>
            </div>
          </div>
          <div className="flex items-center space-x-4 text-center">
            <div className="flex items-center justify-center w-12 h-12 bg-blue-100 text-blue-600 dark:bg-blue-900 dark:text-blue-400 rounded-full">
              <span className="text-xl">🤖</span>
            </div>
            <div>
              <h3 className="font-semibold text-gray-900 dark:text-white">AI Validation</h3>
              <p className="text-gray-600 dark:text-gray-300 text-sm">
                Listings are validated using machine learning for accuracy and safety.
              </p>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default TrustSafety;