const HowItWorks = () => {
  return (
    <section className="py-16 bg-white dark:bg-gray-900">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <h2 className="text-2xl font-bold text-gray-900 dark:text-white mb-12 text-center">
          How DemoRental Works
        </h2>
        <div className="grid gap-8 sm:grid-cols-3">
          <div className="text-center space-y-6">
            <div className="flex items-center justify-center w-16 h-16 bg-blue-500 text-white rounded-full mb-4">
              1
            </div>
            <h3 className="font-semibold text-gray-900 dark:text-white">Discover</h3>
            <p className="text-gray-600 dark:text-gray-300">
              Browse thousands of rental items across categories or get AI-powered recommendations tailored to your needs.
            </p>
          </div>
          <div className="text-center space-y-6">
            <div className="flex items-center justify-center w-16 h-16 bg-blue-500 text-white rounded-full mb-4">
              2
            </div>
            <h3 className="font-semibold text-gray-900 dark:text-white">Book</h3>
            <p className="text-gray-600 dark:text-gray-300">
              Reserve items instantly with secure payments, flexible cancellation, and clear ownership verification.
            </p>
          </div>
          <div className="text-center space-y-6">
            <div className="flex items-center justify-center w-16 h-16 bg-blue-500 text-white rounded-full mb-4">
              3
            </div>
            <h3 className="font-semibold text-gray-900 dark:text-white">Enjoy</h3>
            <p className="text-gray-600 dark:text-gray-300">
              Pick up or get delivery, use your rental, and return it hassle-free. We handle the rest.
            </p>
          </div>
        </div>
      </div>
    </section>
  );
};

export default HowItWorks;