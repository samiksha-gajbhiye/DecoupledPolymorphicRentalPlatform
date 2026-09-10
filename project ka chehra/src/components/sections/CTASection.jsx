const CTASection = () => {
  return (
    <section className="py-16 bg-blue-600 text-white">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
        <h2 className="text-3xl font-bold mb-6">Start Renting Today</h2>
        <p className="text-lg mb-8">
          Join thousands of satisfied users who are discovering, renting, and managing products with ease.
        </p>
        <div className="flex flex-col sm:flex-row sm:justify-center sm:space-x-4">
          <a href="/login" className="bg-white text-blue-600 px-6 py-3 rounded-md font-medium hover:bg-gray-100 transition-colors flex-1 sm:flex-none sm:w-48">
            Login
          </a>
          <a href="/register" className="bg-white/20 hover:bg-white/30 text-white px-6 py-3 rounded-md font-medium transition-colors flex-1 sm:flex-none sm:w-48 border border-white/20">
            Register
          </a>
        </div>
      </div>
    </section>
  );
};

export default CTASection;