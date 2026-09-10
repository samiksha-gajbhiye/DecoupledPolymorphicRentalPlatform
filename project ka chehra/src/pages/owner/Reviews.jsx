import ReviewCard from '../../components/owner/ReviewCard';

const OwnerReviews = () => {
  const reviews = [
    {
      id: 1,
      renterName: "John Doe",
      renterAvatar: "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=100",
      rating: 5,
      date: "2026-08-15",
      comment: "Great experience! The camera kit was in perfect condition and exactly as described. Pickup and drop-off were smooth.",
      itemName: "Professional DSLR Camera Kit"
    },
    {
      id: 2,
      renterName: "Jane Smith",
      renterAvatar: "https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=100",
      rating: 4,
      date: "2026-08-10",
      comment: "The scooter worked well for our weekend trip. Would rent again!",
      itemName: "Electric Scooter"
    },
    {
      id: 3,
      renterName: "Mike Johnson",
      renterAvatar: "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=100",
      rating: 5,
      date: "2026-08-05",
      comment: "Excellent communication and the sofa set was very comfortable. Highly recommend!",
      itemName: "Modern Sofa Set"
    }
  ];

  return (
    <div className="min-h-screen bg-gray-50 dark:bg-gray-900">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <div className="mb-6">
          <h1 className="text-2xl font-bold text-gray-900 dark:text-white">
            Reviews
          </h1>
          <div className="mt-2 flex items-center space-x-4 text-sm text-gray-500 dark:text-gray-400">
            <span>Total Reviews: {reviews.length}</span>
            <span className="mx-2">•</span>
            <span>Average Rating: 4.7/5.0</span>
          </div>
        </div>

        <div className="space-y-4">
          {reviews.map(review => (
            <ReviewCard key={review.id} review={review} />
          ))}
        </div>
      </div>
    </div>
  );
};

export default OwnerReviews;