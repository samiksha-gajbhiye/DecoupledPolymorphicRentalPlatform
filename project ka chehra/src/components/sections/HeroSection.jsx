import SearchBar from '../SearchBar';
import CategorySelector from '../CategorySelector';

const HeroSection = () => {
  return (
    <section className="hero-shell hero-centered">
      <div className="hero-grid" aria-hidden="true" />
      <div className="hero-centered-content">
        <div className="hero-centered-copy">
          <h1>Rent Anything. Smarter.</h1>
          <p>A modern AI-powered rental platform built to make discovering, renting,<br className="desktop-break" /> and managing products simple.</p>
        </div>
        <SearchBar />
        <CategorySelector categories={['Electronics', 'Vehicles', 'Furniture', 'Tools', 'Cameras', 'Sports Equipment', 'Appliances', 'Event Equipment', 'Other']} />
      </div>
    </section>
  );
};

export default HeroSection;