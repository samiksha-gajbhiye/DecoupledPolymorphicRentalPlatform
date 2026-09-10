const BookingTimeline = ({ timeline }) => {
  return (
    <div className="py-4">
      <div className="space-y-4">
        {timeline.map((event, index) => (
          <div key={index} className="flex items-start space-x-3">
            <div className="flex-shrink-0">
              <div className={`w-3 h-3 rounded-full ${event.status === 'completed' ? 'bg-green-500' : event.status === 'upcoming' ? 'bg-blue-500' : 'bg-gray-500'}`} />
            </div>
            <div className="flex-1 space-y-1">
              <div className="flex justify-between text-sm">
                <h3 className="font-medium text-gray-900 dark:text-white">{event.title}</h3>
                <span className="text-xs px-2 py-0.5 rounded-full
                  ${event.status === 'completed' ? 'bg-green-100 text-green-800 dark:bg-green-900/20 dark:text-green-200' :
                     event.status === 'upcoming' ? 'bg-blue-100 text-blue-800 dark:bg-blue-900/20 dark:text-blue-200' :
                     'bg-gray-100 text-gray-800 dark:bg-gray-900/20 dark:text-gray-200'}">
                  {event.status.charAt(0).toUpperCase() + event.status.slice(1)}
                </span>
              </div>
              <p className="text-sm text-gray-600 dark:text-gray-400">
                {event.date} • {event.time}
              </p>
              <p className="text-sm text-gray-500 dark:text-gray-300">
                {event.description}
              </p>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default BookingTimeline;