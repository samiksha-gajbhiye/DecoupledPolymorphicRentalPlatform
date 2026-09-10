import { useParams } from 'react-router-dom';
import ImageGallery from '../../components/ImageGallery';
import RentalDetails from '../../components/RentalDetails';
import BookingForm from '../../components/BookingForm';
import RelatedItems from '../../components/RelatedItems';

const ProductDetails = () => {
  const { id } = useParams();

  // Sample product data - in real app this would come from API
  const product = {
    id: parseInt(id),
    name: "Professional DSLR Camera Kit",
    category: "Cameras",
    location: "New York, NY",
    rating: 4.9,
    reviewCount: 128,
    price: 75,
    images: [
      "https://images.unsplash.com/photo-1526170375885-4d8ecf77b99f?w=800",
      "https://images.unsplash.com/photo-1516035069371-2901b265cc26?w=800",
      "https://images.unsplash.com/photo-1502920947138-1931412dd77c?w=800"
    ],
    description: "Professional-grade DSLR camera kit including camera body, multiple lenses, tripod, and accessories. Perfect for photography enthusiasts and professionals.",
    specifications: {
      "Camera Body": "Full-frame DSLR",
      "Lenses": "24-70mm f/2.8, 70-200mm f/2.8",
      "Resolution": "24.2 MP",
      "Video": "4K UHD",
      "Battery Life": "1200 shots",
      "Weight": "1.5 lbs"
    },
    availability: {
      "nextAvailable": "Tomorrow",
      "minimumDays": 1,
      "maximumDays": 30
    },
    owner: {
      name: "Alex Johnson",
      avatar: "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=100",
      rating: 4.9,
      verified: true,
      listings: 12
    },
    policies: {
      cancellation: "Free cancellation up to 24 hours before pickup",
      deposit: "Security deposit required: ₹200",
      lateReturn: "Late returns incur additional daily fee"
    }
  };

  return (
    <div className="min-h-screen bg-gray-50 dark:bg-gray-900">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        <div className="mb-8">
          <div className="flex items-center space-x-4">
            <button onClick={() => window.history.back()} className="text-gray-500 hover:text-gray-700 dark:hover:text-gray-200">
              ← Back to Search
            </button>
            <h1 className="text-2xl font-bold text-gray-900 dark:text-white flex-1">
              {product.name}
            </h1>
          </div>
        </div>

        <div className="grid gap-8 lg:grid-cols-3">
          {/* Main Image Gallery */}
          <div className="lg:col-span-2">
            <ImageGallery images={product.images} />
          </div>

          {/* Details Sidebar */}
          <div className="lg:col-span-1 space-y-6">
            <RentalDetails product={product} />
            <BookingForm product={product} />
          </div>
        </div>

        {/* Description and Specs */}
        <div className="mt-12">
          <RelatedItems product={product} />
        </div>
      </div>
    </div>
  );
};

export default ProductDetails;