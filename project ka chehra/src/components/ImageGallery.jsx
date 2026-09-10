import { useState } from 'react';
import { ZoomOut, ZoomIn } from 'lucide-react';

const ImageGallery = ({ images }) => {
  const [currentIndex, setCurrentIndex] = useState(0);

  return (
    <div className="space-y-4">
      {/* Main Image */}
      <div className="relative aspect-w-16 aspect-h-9 w-full overflow-hidden rounded-lg bg-gray-200">
        <img
          src={images[currentIndex]}
          alt=""
          className="object-cover w-full h-full transition-transform duration-300"
        />
        {/* Navigation Arrows */}
        {images.length > 1 && (
          <>
            <button
              onClick={() => setCurrentIndex((prev) => (prev - 1 + images.length) % images.length)}
              className="absolute left-0 top-1/2 -translate-y-1/2 bg-black/50 text-white px-3 py-2 rounded-r hover:bg-black/700 transition-colors z-10"
            >
              <ZoomOut className="h-4 w-4" />
            </button>
            <button
              onClick={() => setCurrentIndex((prev) => (prev + 1) % images.length)}
              className="absolute right-0 top-1/2 -translate-y-1/2 bg-black/50 text-white px-3 py-2 rounded-l hover:bg-black/700 transition-colors z-10"
            >
              <ZoomIn className="h-4 w-4" />
            </button>
          </>
        )}
      </div>

      {/* Thumbnails */}
      {images.length > 1 && (
        <div className="flex space-x-3 overflow-x-auto py-2">
          {images.map((image, index) => (
            <button
              key={index}
              onClick={() => setCurrentIndex(index)}
              className={`flex-shrink-0 h-24 w-24 border border-transparent rounded overflow-hidden hover:border-blue-500 focus:ring-2 focus:ring-blue-500 ${currentIndex === index ? 'border-blue-500' : ''}`}
            >
              <img
                src={image}
                alt=""
                className="object-cover w-full h-full"
              />
            </button>
          ))}
        </div>
      )}
    </div>
  );
};

export default ImageGallery;