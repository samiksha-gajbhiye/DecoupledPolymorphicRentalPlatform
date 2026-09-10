import { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { Input } from '../../components/ui/input';
import { Textarea } from '../../components/ui/textarea';
import { Button } from '../../components/ui/button';
import { Image } from 'lucide-react';
import { getAllCategories } from '../../api/categoryApi';
import { addProduct } from '../../api/productApi';

const AddListing = () => {
  const navigate = useNavigate();

  const [categories, setCategories] = useState([]);
  const [imageFiles, setImageFiles] = useState([]);
  const [previewUrls, setPreviewUrls] = useState([]);
  const [submitting, setSubmitting] = useState(false);
  const [error, setError] = useState('');

  const [formData, setFormData] = useState({
    title: '',
    categoryId: '',
    description: '',
    brand: '',
    model: '',
    pricePerDay: '',
    securityDeposit: '',
    quantity: 1,
    condition: 'GOOD',
    location: '',
  });

  useEffect(() => {
    getAllCategories()
      .then(setCategories)
      .catch(() => setError('Could not load categories. Is the backend running?'));
  }, []);

  const handleChange = (e) => {
    const { name, value } = e.target;
    if (name === 'pricePerDay' || name === 'securityDeposit') {
      setFormData((prev) => ({ ...prev, [name]: value.replace(/[^0-9.]/g, '') }));
    } else {
      setFormData((prev) => ({ ...prev, [name]: value }));
    }
  };

  const handleImageChange = (e) => {
    const files = Array.from(e.target.files);
    setImageFiles((prev) => [...prev, ...files]);
    setPreviewUrls((prev) => [...prev, ...files.map((f) => URL.createObjectURL(f))]);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');

    if (!formData.categoryId) {
      setError('Please select a category');
      return;
    }
    if (imageFiles.length === 0) {
      setError('Please add at least one photo');
      return;
    }

    setSubmitting(true);

    const productPayload = {
      title: formData.title,
      description: formData.description,
      brand: formData.brand,
      model: formData.model,
      pricePerDay: formData.pricePerDay,
      securityDeposit: formData.securityDeposit || 0,
      quantity: Number(formData.quantity),
      condition: formData.condition,
      location: formData.location,
      availability: 'AVAILABLE',
      category: { categoryId: Number(formData.categoryId) },
    };

    try {
      await addProduct(productPayload, imageFiles);
      navigate('/owner/listings');
    } catch (err) {
      setError(
        err.response?.data?.message ||
        err.response?.data ||
        'Could not create listing. Please check all fields and try again.'
      );
    } finally {
      setSubmitting(false);
    }
  };

  return (
    <div className="min-h-screen bg-gray-50 dark:bg-gray-900">
      <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <div className="mb-6">
          <h1 className="text-2xl font-bold text-gray-900 dark:text-white">
            Add New Listing
          </h1>
          <p className="text-gray-600 dark:text-gray-300">
            Create a new rental listing to start earning today
          </p>
        </div>

        <div className="bg-white dark:bg-gray-800 rounded-xl shadow-sm">
          <form onSubmit={handleSubmit} className="p-6 space-y-6">
            {error && (
              <div className="bg-red-50 dark:bg-red-900/20 text-red-500 dark:text-red-400 px-4 py-3 rounded-md">
                {error}
              </div>
            )}

            <div className="grid gap-4 sm:grid-cols-2">
              <div>
                <label className="block text-sm font-medium mb-1">Listing Title</label>
                <Input
                  name="title"
                  placeholder="e.g., Professional DSLR Camera Kit"
                  value={formData.title}
                  onChange={handleChange}
                  required
                />
              </div>

              <div>
                <label className="block text-sm font-medium mb-1">Category</label>
                <select
                  name="categoryId"
                  value={formData.categoryId}
                  onChange={handleChange}
                  required
                  className="w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-md bg-white dark:bg-gray-700"
                >
                  <option value="">Select a category</option>
                  {categories.map((c) => (
                    <option key={c.categoryId} value={c.categoryId}>{c.name}</option>
                  ))}
                </select>
              </div>
            </div>

            <div className="grid gap-4 sm:grid-cols-2">
              <div>
                <label className="block text-sm font-medium mb-1">Brand</label>
                <Input name="brand" placeholder="e.g., Canon" value={formData.brand} onChange={handleChange} required />
              </div>
              <div>
                <label className="block text-sm font-medium mb-1">Model</label>
                <Input name="model" placeholder="e.g., EOS R6" value={formData.model} onChange={handleChange} required />
              </div>
            </div>

            <div>
              <label className="block text-sm font-medium mb-1">Description</label>
              <Textarea
                name="description"
                placeholder="Describe your item in detail, including condition, specifications, and any special features..."
                rows={4}
                value={formData.description}
                onChange={handleChange}
                required
              />
            </div>

            <div className="grid gap-4 sm:grid-cols-2">
              <div>
                <label className="block text-sm font-medium mb-1">Price Per Day (₹)</label>
                <Input name="pricePerDay" type="text" placeholder="e.g., 75.00" value={formData.pricePerDay} onChange={handleChange} required />
              </div>
              <div>
                <label className="block text-sm font-medium mb-1">Security Deposit (₹)</label>
                <Input name="securityDeposit" type="text" placeholder="e.g., 200.00" value={formData.securityDeposit} onChange={handleChange} />
              </div>
            </div>

            <div className="grid gap-4 sm:grid-cols-2">
              <div>
                <label className="block text-sm font-medium mb-1">Quantity Available</label>
                <Input name="quantity" type="number" min="1" value={formData.quantity} onChange={handleChange} required />
              </div>
              <div>
                <label className="block text-sm font-medium mb-1">Condition</label>
                <select
                  name="condition"
                  value={formData.condition}
                  onChange={handleChange}
                  className="w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-md bg-white dark:bg-gray-700"
                >
                  <option value="NEW">New</option>
                  <option value="LIKE_NEW">Like New</option>
                  <option value="GOOD">Good</option>
                  <option value="FAIR">Fair</option>
                  <option value="POOR">Poor</option>
                </select>
              </div>
            </div>

            <div>
              <label className="block text-sm font-medium mb-1">Location</label>
              <Input name="location" placeholder="e.g., New York, NY" value={formData.location} onChange={handleChange} />
            </div>

            <div className="border-t border-gray-200 dark:border-gray-700 pt-5">
              <div className="flex items-center space-x-3">
                <Image className="h-5 w-5" />
                <h3 className="text-lg font-medium text-gray-900 dark:text-white">Photos</h3>
              </div>
              <div className="mt-4 flex flex-wrap gap-3">
                {previewUrls.map((url, i) => (
                  <img key={i} src={url} alt={`Preview ${i}`} className="w-24 h-24 object-cover rounded-lg" />
                ))}
                <input
                  type="file"
                  accept="image/*"
                  multiple
                  onChange={handleImageChange}
                  className="hidden"
                  id="image-upload"
                />
                <label
                  htmlFor="image-upload"
                  className="flex items-center justify-center w-24 h-24 border-2 border-dashed border-gray-300 dark:border-gray-600 rounded-lg hover:border-gray-400 cursor-pointer transition-colors"
                >
                  <span className="text-sm text-gray-500 dark:text-gray-400 text-center px-1">
                    + Add photo
                  </span>
                </label>
              </div>
              <p className="text-sm text-gray-500 dark:text-gray-400 mt-2">
                Upload clear, well-lit photos of your item from multiple angles
              </p>
            </div>

            <div className="flex items-center justify-between">
              <Button variant="outline" type="button" onClick={() => navigate(-1)}>
                Cancel
              </Button>
              <Button type="submit" disabled={submitting}>
                {submitting ? 'Publishing...' : 'Publish Listing'}
              </Button>
            </div>
          </form>
        </div>
      </div>
    </div>
  );
};

export default AddListing;