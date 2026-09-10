import { useState } from 'react';
import { useParams } from 'react-router-dom';
import { Form, FormField, FormItem, FormLabel, FormControl, FormDescription, FormMessage } from '../../components/ui/form';
import { Input } from '../../components/ui/input';
import { Textarea } from '../../components/ui/textarea';
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from '../../components/ui/select';
import { Checkbox } from '../../components/ui/checkbox';
import { Button } from '../../components/ui/button';
import { DollarSign, MapPin, BatteryCharging, Clock, Image, Truck, ShieldCheck } from 'lucide-react';
import DateInput from '../../components/DateInput';

const EditListing = () => {
  const { id } = useParams();
  const [formData, setFormData] = useState({
    title: '',
    category: '',
    description: '',
    pricePerDay: '',
    location: '',
    availability: {
      startDate: '',
      endDate: ''
    },
    requirements: [],
    features: [],
    images: []
  });

  const [previewImage, setPreviewImage] = useState(null);
  const categories = [
    'Electronics',
    'Vehicles',
    'Furniture',
    'Tools',
    'Cameras',
    'Sports Equipment',
    'Appliances',
    'Event Equipment',
    'Other'
  ];

  const featuresOptions = [
    { label: 'Delivery Available', value: 'delivery' },
    { label: 'Pickup Available', value: 'pickup' },
    { label: 'Shipping Available', value: 'shipping' },
    { label: 'Cleaning Included', value: 'cleaning' },
    { label: 'Setup Assistance', value: 'setup' },
    { label: '24/7 Support', value: 'support' }
  ];

  const requirementsOptions = [
    { label: 'ID Verification Required', value: 'id-verification' },
    { label: 'Security Deposit Required', value: 'security-deposit' },
    { label: 'Minimum Age 21+', value: 'min-age-21' },
    { label: 'Minimum Age 25+', value: 'min-age-25' },
    { label: 'Positive Reviews Required', value: 'positive-reviews' },
    { label: 'Verified Only', value: 'verified-only' }
  ];

  // Simulate loading existing listing data
  // In a real app, this would come from an API call
  const loadListingData = () => {
    // Mock data for demonstration
    setFormData({
      title: "Professional DSLR Camera Kit",
      category: "Cameras",
      description: "Professional-grade DSLR camera kit including camera body, multiple lenses, tripod, and accessories. Perfect for photography enthusiasts and professionals.",
      pricePerDay: "75",
      location: "New York, NY",
      availability: {
        startDate: new Date().toISOString().split('T')[0],
        endDate: new Date(Date.now() + 30 * 24 * 60 * 60 * 1000).toISOString().split('T')[0]
      },
      requirements: ['id-verification', 'security-deposit'],
      features: ['delivery', 'setup'],
      images: [
        "https://images.unsplash.com/photo-1526170375885-4d8ecf77b99f?w=400",
        "https://images.unsplash.com/photo-1516035069371-2901b265cc26?w=400"
      ]
    });
  };

  if (formData.images.length > 0) {
    setPreviewImage(formData.images[0]);
  }

  // Load data on mount
  // useEffect(() => {
  //   loadListingData();
  // }, []);

  const handleChange = (e) => {
    const { name, value, type, checked } = e.target;
    if (type === 'checkbox') {
      setFormData(prev => ({
        ...prev,
        [name]: checked ? [...prev[name], value] : prev[name].filter(item => item !== value)
      }));
    } else if (name === 'pricePerDay') {
      setFormData(prev => ({
        ...prev,
        [name]: value.replace(/[^0-9.]/g, '')
      }));
    } else {
      setFormData(prev => ({
        ...prev,
        [name]: value
      }));
    }
  };

  const handleImageChange = (e) => {
    const file = e.target.files[0];
    if (file) {
      const reader = new FileReader();
      reader.onloadend = () => {
        setPreviewImage(reader.result);
        // In a real app, you would upload the image to a server and store the URL
        setFormData(prev => ({
          ...prev,
          images: [...prev.images.filter(img => img !== previewImage), reader.result]
        }));
      };
      reader.readAsDataURL(file);
    }
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    // In a real app, this would send a PUT/PATCH request to your backend API
    console.log('Updating listing:', formData);
    alert('Listing updated successfully! (This is a demo)');
  };

  return (
    <div className="min-h-screen bg-gray-50 dark:bg-gray-900">
      <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <div className="mb-6">
          <h1 className="text-2xl font-bold text-gray-900 dark:text-white">
            Edit Listing
          </h1>
          <p className="text-gray-600 dark:text-gray-300">
            Update your rental listing details
          </p>
        </div>

        <div className="bg-white dark:bg-gray-800 rounded-xl shadow-sm">
          <form onSubmit={handleSubmit} className="p-6 space-y-6">
            <div className="grid gap-4 sm:grid-cols-2">
              <Form>
                <FormField
                  control={{
                    value: formData.title,
                    onChange: (e) => handleChange({ target: { name: 'title', value: e.target.value } })
                  }}
                  render={({ field }) => (
                    <>
                      <FormLabel>Listing Title</FormLabel>
                      <FormControl>
                        <Input
                          placeholder="e.g., Professional DSLR Camera Kit"
                          {...field}
                        />
                      </FormControl>
                      <FormDescription>
                        Be descriptive and specific about what you're offering
                      </FormDescription>
                    </>
                  )}
                />

                <FormField
                  control={{
                    value: formData.category,
                    onChange: (e) => handleChange({ target: { name: 'category', value: e.target.value } })
                  }}
                  render={({ field }) => (
                    <div>
                      <FormLabel>Category</FormLabel>
                      <FormControl>
                        <Select>
                          <SelectTrigger placeholder="Select a category" {...field}>
                            <SelectValue placeholder="Select a category" />
                          </SelectTrigger>
                          <SelectContent>
                            {categories.map(category => (
                              <SelectItem key={category} value={category}>
                                {category}
                              </SelectItem>
                            ))}
                          </SelectContent>
                        </Select>
                      </FormControl>
                      <FormDescription>
                        Choose the best category for your item
                      </FormDescription>
                    </div>
                  )}
                />
              </Form>
            </div>

            <FormField
              control={{
                value: formData.description,
                onChange: (e) => handleChange({ target: { name: 'description', value: e.target.value } })
              }}
              render={({ field }) => (
                <>
                  <FormLabel>Description</FormLabel>
                  <FormControl>
                    <Textarea
                      placeholder="Describe your item in detail, including condition, specifications, and any special features..."
                      rows={4}
                      {...field}
                    />
                  </FormControl>
                  <FormDescription>
                    The more details you provide, the more likely renters will book your item
                  </FormDescription>
                </>
              )} />

            <div className="grid gap-4 sm:grid-cols-2">
              <FormField
                control={{
                  value: formData.pricePerDay,
                  onChange: (e) => handleChange({ target: { name: 'pricePerDay', value: e.target.value } })
                }}
                render={({ field }) => (
                  <>
                    <FormLabel>Price Per Day (₹)</FormLabel>
                    <FormControl>
                      <Input
                        type="text"
                        placeholder="e.g., 75.00"
                        prefix="₹"
                        {...field}
                      />
                    </FormControl>
                    <FormDescription>
                      Set your daily rental rate
                    </FormDescription>
                  </>
                )} />

              <FormField
                control={{
                  value: formData.location,
                  onChange: (e) => handleChange({ target: { name: 'location', value: e.target.value } })
                }}
                render={({ field }) => (
                  <>
                    <FormLabel>Location</FormLabel>
                    <FormControl>
                      <Input
                        placeholder="e.g., New York, NY"
                        {...field}
                      />
                    </FormControl>
                    <FormDescription>
                      Where your item is located for pickup
                    </FormDescription>
                  </>
                )} />
            </div>

            <div className="grid gap-4 sm:grid-cols-2">
              <FormField
                control={{
                  value: formData.availability.startDate,
                  onChange: (e) => handleChange({ target: { name: 'availability.startDate', value: e.target.value } })
                }}
                render={({ field }) => (
                  <>
                    <FormLabel>Available From</FormLabel>
                    <FormControl>
                      <DateInput
                        min={new Date().toISOString().split('T')[0]}
                        className="w-full px-3 py-2 border border-gray-300 rounded-md"
                        {...field}
                      />
                    </FormControl>
                  </>
                )} />

              <FormField
                control={{
                  value: formData.availability.endDate,
                  onChange: (e) => handleChange({ target: { name: 'availability.endDate', value: e.target.value } })
                }}
                render={({ field }) => (
                  <>
                    <FormLabel>Available Until</FormLabel>
                    <FormControl>
                      <DateInput
                        min={new Date().toISOString().split('T')[0]}
                        className="w-full px-3 py-2 border border-gray-300 rounded-md"
                        {...field}
                      />
                    </FormControl>
                  </>
                )} />
            </div>

            <div className="space-y-4">
              <div>
                <FormLabel>Features</FormLabel>
                <div className="flex flex-wrap gap-2">
                  {featuresOptions.map(option => (
                    <label key={option.value} className="flex items-center text-sm">
                      <Checkbox
                        checked={formData.features.includes(option.value)}
                        onChange={(e) => handleChange({
                          target: {
                            name: 'features',
                            type: 'checkbox',
                            checked: e.target.checked,
                            value: option.value
                          }
                        })}
                      />
                      <span className="ml-2">{option.label}</span>
                    </label>
                  ))}
                </div>
              </div>

              <div>
                <FormLabel>Requirements</FormLabel>
                <div className="flex flex-wrap gap-2">
                  {requirementsOptions.map(option => (
                    <label key={option.value} className="flex items-center text-sm">
                      <Checkbox
                        checked={formData.requirements.includes(option.value)}
                        onChange={(e) => handleChange({
                          target: {
                            name: 'requirements',
                            type: 'checkbox',
                            checked: e.target.checked,
                            value: option.value
                          }
                        })}
                      />
                      <span className="ml-2">{option.label}</span>
                    </label>
                  ))}
                </div>
              </div>
            </div>

            <div className="border-t border-gray-200 dark:border-gray-700 pt-5">
              <div className="flex items-center space-x-3">
                <Image className="h-5 w-5" />
                <h3 className="text-lg font-medium text-gray-900 dark:text-white">Photos</h3>
              </div>
              <div className="mt-4 space-x-3">
                <input
                  type="file"
                  accept="image/*"
                  onChange={handleImageChange}
                  className="hidden"
                  id="image-upload"
                />
                <label
                  htmlFor="image-upload"
                  className="flex items-center justify-center w-36 h-36 border-2 border-dashed border-gray-300 dark:border-gray-600 rounded-lg hover:border-gray-400 dark:hover:border-gray-400 cursor-pointer transition-colors"
                >
                  {previewImage ? (
                    <img
                      src={previewImage}
                      alt="Preview"
                      className="w-full h-full object-cover rounded"
                    />
                  ) : (
                    <>
                      <Image className="h-4 w-4 mr-2" />
                      <span className="text-sm text-gray-500 dark:text-gray-400">
                        Click to upload photos
                      </span>
                    </>
                  )}
                </label>
                <p className="text-sm text-gray-500 dark:text-gray-400 mt-2">
                  Upload clear, well-lit photos of your item from multiple angles
                </p>
              </div>
            </div>

            <div className="flex items-center justify-between">
              <Button variant="outline" type="button">
                Cancel
              </Button>
              <Button type="submit">
                Update Listing
              </Button>
            </div>
          </form>
        </div>
      </div>
    </div>
  );
};

export default EditListing;