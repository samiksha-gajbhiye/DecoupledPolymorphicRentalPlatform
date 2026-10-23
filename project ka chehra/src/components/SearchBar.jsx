import { useState } from 'react';
import { useNavigate, useSearchParams } from 'react-router-dom';
import { CalendarDays, MapPin, Search } from 'lucide-react';
import DateInput from './DateInput';

const SearchBar = () => {
  const navigate = useNavigate();
  const [params] = useSearchParams();
  const [query, setQuery] = useState(params.get('q') || '');
  const [location, setLocation] = useState(params.get('location') || '');

  const handleSubmit = (e) => {
    e.preventDefault();
    const next = new URLSearchParams();
    if (query.trim()) next.set('q', query.trim());
    if (location.trim()) next.set('location', location.trim());
    navigate(`/search?${next.toString()}`);
  };

  return (
    <div className="rental-search">
        <form onSubmit={handleSubmit}>
          <div className="search-field search-query">
            <label htmlFor="search-query" className="sr-only">Search query</label>
            <div>
              <Search size={19} />
              <span>What are you looking for?</span>
              <input
                type="text"
                id="search-query"
                placeholder="What are you looking for?"
                className="search-input"
                value={query}
                onChange={(e) => setQuery(e.target.value)}
              />
            </div>
          </div>
          <div className="search-field">
            <label htmlFor="location" className="sr-only">Location</label>
            <div>
              <MapPin size={18} />
              <span>Location</span>
              <input
                type="text"
                id="location"
                placeholder="Location"
                className="search-input"
                value={location}
                onChange={(e) => setLocation(e.target.value)}
              />
            </div>
          </div>
          <div className="search-field">
            <label htmlFor="check-in" className="sr-only">Check-in date</label>
            <div>
              <CalendarDays size={18} />
              <span>Dates</span>
              <DateInput
                id="check-in"
                className="search-input"
              />
            </div>
          </div>
          <div className="search-field search-checkout">
            <label htmlFor="check-out" className="sr-only">Check-out date</label>
            <div>
              <CalendarDays size={18} />
              <span>Return</span>
              <DateInput
                id="check-out"
                className="search-input"
              />
            </div>
          </div>
          <button type="submit" className="search-submit">
            Search rentals
          </button>
        </form>
    </div>
  );
};

export default SearchBar;