import PricingCard from '../../components/owner/PricingCard';
import PriceRecommendations from '../../components/owner/PriceRecommendations';
import MarketAnalysis from '../../components/owner/MarketAnalysis';

const PricingIntelligence = () => {
  return (
    <div className="min-h-screen bg-gray-50 dark:bg-gray-900">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <div className="mb-6">
          <h1 className="text-2xl font-bold text-gray-900 dark:text-white">
            Pricing Intelligence
          </h1>
          <p className="text-gray-600 dark:text-gray-300">
            AI-powered pricing recommendations to maximize your earnings
          </p>
        </div>

        <PricingCard />
        <div className="grid gap-6 md:grid-cols-2">
          <PriceRecommendations />
          <MarketAnalysis />
        </div>
      </div>
    </div>
  );
};

export default PricingIntelligence;