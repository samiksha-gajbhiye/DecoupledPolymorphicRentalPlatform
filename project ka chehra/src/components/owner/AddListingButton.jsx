import { Link } from 'react-router-dom';
import { Plus } from 'lucide-react';

const AddListingButton = () => {
  return (
    <Link to="/owner/listings/add" className="bg-blue-600 text-white px-4 py-2 rounded-md hover:bg-blue-700 dark:hover:bg-blue-800 transition-colors text-sm font-medium flex items-center space-x-2">
      <Plus className="h-4 w-4" />
      Add Listing
    </Link>
  );
};

export default AddListingButton;