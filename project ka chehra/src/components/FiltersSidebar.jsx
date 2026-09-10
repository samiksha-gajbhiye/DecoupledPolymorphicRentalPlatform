const FiltersSidebar = ({ className = '' }) => {
  return (
    <aside className={`${className} space-y-6`}>
      <div>
        <h3 className="text-lg font-medium text-gray-900 dark:text-white mb-4">
          Categories
        </h3>
        <div className="space-y-2">
          <label className="flex items-center text-sm text-gray-700 dark:text-gray-300">
            <input type="checkbox" className="h-4 w-4 text-blue-600 focus:ring-blue-500 border-gray-300 rounded" />
            Electronics
          </label>
          <label className="flex items-center text-sm text-gray-700 dark:text-gray-300">
            <input type="checkbox" className="h-4 w-4 text-blue-600 focus:ring-blue-500 border-gray-300 rounded" />
            Vehicles
          </label>
          <label className="flex items-center text-sm text-gray-700 dark:text-gray-300">
            <input type="checkbox" className="h-4 w-4 text-blue-600 focus:ring-blue-500 border-gray-300 rounded" />
            Furniture
          </label>
          <label className="flex items-center text-sm text-gray-700 dark:text-gray-300">
            <input type="checkbox" className="h-4 w-4 text-blue-600 focus:ring-blue-500 border-gray-300 rounded" />
            Tools
          </label>
          <label className="flex items-center text-sm text-gray-700 dark:text-gray-300">
            <input type="checkbox" className="h-4 w-4 text-blue-600 focus:ring-blue-500 border-gray-300 rounded" />
            Cameras
          </label>
        </div>
      </div>

      <div>
        <h3 className="text-lg font-medium text-gray-900 dark:text-white mb-4">
          Price Range
        </h3>
        <div className="space-y-3">
          <div className="flex items-center justify-between text-sm text-gray-600 dark:text-gray-400">
            <span>$0</span>
            <span>$500+</span>
          </div>
          <div className="w-full">
            <input type="range" min="0" max="500" className="w-full h-1 bg-gray-300 rounded" />
          </div>
        </div>
      </div>

      <div>
        <h3 className="text-lg font-medium text-gray-900 dark:text-white mb-4">
          Availability
        </h3>
        <div className="space-y-2">
          <label className="flex items-center text-sm text-gray-700 dark:text-gray-300">
            <input type="checkbox" className="h-4 w-4 text-blue-600 focus:ring-blue-500 border-gray-300 rounded" />
            Available Now
          </label>
          <label className="flex items-center text-sm text-gray-700 dark:text-gray-300">
            <input type="checkbox" className="h-4 w-4 text-blue-600 focus:ring-blue-500 border-gray-300 rounded" />
            Available This Week
          </label>
        </div>
      </div>

      <div className="pt-4 border-t border-gray-200 dark:border-gray-700">
        <button className="w-full bg-blue-600 text-white py-2 px-4 rounded-md hover:bg-blue-700 dark:hover:bg-blue-800 transition-colors text-sm font-medium">
          Apply Filters
        </button>
      </div>
    </aside>
  );
};

export default FiltersSidebar;