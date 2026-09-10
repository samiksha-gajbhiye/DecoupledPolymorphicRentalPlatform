import HeroSection from '../../components/sections/HeroSection';
import PopularRentals from '../../components/sections/PopularRentals';
import AIRecommendations from '../../components/sections/AIRecommendations';
import HowItWorks from '../../components/sections/HowItWorks';
import TrustSafety from '../../components/sections/TrustSafety';
import CTASection from '../../components/sections/CTASection';

const LandingPage = () => {
  return (
    <div>
      <HeroSection />
      <PopularRentals />
      <AIRecommendations />
      <HowItWorks />
      <TrustSafety />
      <CTASection />
    </div>
  );
};

export default LandingPage;