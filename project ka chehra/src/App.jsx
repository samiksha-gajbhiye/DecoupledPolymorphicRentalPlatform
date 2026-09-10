import React from 'react';
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import { AuthProvider } from './context/AuthContext';
import { ThemeProvider } from './context/ThemeContext';
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import LandingPage from './pages/public/LandingPage.jsx';
import BrowseRentals from './pages/public/BrowseRentals.jsx';
import SearchResults from './pages/public/SearchResults.jsx';
import ProductDetails from './pages/public/ProductDetails.jsx';
import Categories from './pages/public/Categories.jsx';
import About from './pages/public/About.jsx';
import Login from './pages/public/Login.jsx';
import Register from './pages/public/Register.jsx';
// Customer Dashboard
import CustomerDashboard from './pages/customer/Dashboard.jsx';
import MyBookings from './pages/customer/MyBookings.jsx';
import BookingDetails from './pages/customer/BookingDetails.jsx';
import Wishlist from './pages/customer/Wishlist.jsx';
import Recommendations from './pages/customer/Recommendations.jsx';
import MessagesNotifications from './pages/customer/MessagesNotifications.jsx';
import Profile from './pages/customer/Profile.jsx';
import Payments from './pages/customer/Payments.jsx';
import Reviews from './pages/customer/Reviews.jsx';
import Settings from './pages/customer/Settings.jsx';
// Owner Dashboard
import OwnerOverview from './pages/owner/Overview.jsx';
import MyListings from './pages/owner/MyListings.jsx';
import AddListing from './pages/owner/AddListing.jsx';
import EditListing from './pages/owner/EditListing.jsx';
import BookingRequests from './pages/owner/BookingRequests.jsx';
import ActiveRentals from './pages/owner/ActiveRentals.jsx';
import Revenue from './pages/owner/Revenue.jsx';
import PricingIntelligence from './pages/owner/PricingIntelligence.jsx';
import ListingAnalytics from './pages/owner/ListingAnalytics.jsx';
import OwnerReviews from './pages/owner/Reviews.jsx';
import CustomerInsights from './pages/owner/CustomerInsights.jsx';
// Admin Dashboard
import AdminOverview from './pages/admin/Overview.jsx';
import AdminUsers from './pages/admin/Users.jsx';
import AdminListings from './pages/admin/Listings.jsx';
import AdminBookings from './pages/admin/Bookings.jsx';
import AdminPayments from './pages/admin/Payments.jsx';
import FraudDetection from './pages/admin/FraudDetection.jsx';
import AIAnalytics from './pages/admin/AIAnalytics.jsx';
import PlatformAnalytics from './pages/admin/PlatformAnalytics.jsx';
import AdminCategories from './pages/admin/Categories.jsx';
import AdminReports from './pages/admin/Reports.jsx';
import SystemHealth from './pages/admin/SystemHealth.jsx';
import AdminSettings from './pages/admin/Settings.jsx';
// Layout components
import Navbar from './components/Navbar';
import Footer from './components/Footer';
import PrivateRoute from './components/PrivateRoute';
import RoleRoute from './components/RoleRoute';

// Create a query client for react-query
const queryClient = new QueryClient();

function App() {
  return (
    <ThemeProvider>
      <AuthProvider>
        <QueryClientProvider client={queryClient}>
          <BrowserRouter>
            <div className="app-shell min-h-screen bg-gray-50 dark:bg-gray-900 transition-colors">
              <Navbar />
              <main className="pb-16">
                <Routes>
                  {/* Public Routes */}
                  <Route path="/" element={<LandingPage />} />
                  <Route path="/browse" element={<BrowseRentals />} />
                  <Route path="/search" element={<SearchResults />} />
                  <Route path="/product/:id" element={<ProductDetails />} />
                  <Route path="/categories" element={<Categories />} />
                  <Route path="/about" element={<About />} />
                  <Route path="/login" element={<Login />} />
                  <Route path="/register" element={<Register />} />

                  {/* Protected Routes - Customer */}
                  <Route
                    path="/customer/*"
                    element={
                      <PrivateRoute>
                        <RoleRoute role="USER">
                          <Routes>
                            <Route path="dashboard" element={<CustomerDashboard />} />
                            <Route path="bookings" element={<MyBookings />} />
                            <Route path="bookings/:id" element={<BookingDetails />} />
                            <Route path="wishlist" element={<Wishlist />} />
                            <Route path="recommendations" element={<Recommendations />} />
                            <Route path="messages" element={<MessagesNotifications />} />
                            <Route path="profile" element={<Profile />} />
                            <Route path="payments" element={<Payments />} />
                            <Route path="reviews" element={<Reviews />} />
                            <Route path="settings" element={<Settings />} />
                          </Routes>
                        </RoleRoute>
                      </PrivateRoute>
                    }
                  />

                  {/* Protected Routes - Owner */}
                  <Route
                    path="/owner/*"
                    element={
                      <PrivateRoute>
                        <RoleRoute role="OWNER">
                          <Routes>
                            <Route path="dashboard" element={<OwnerOverview />} />
                            <Route path="listings" element={<MyListings />} />
                            <Route path="listings/add" element={<AddListing />} />
                            <Route path="listings/edit/:id" element={<EditListing />} />
                            <Route path="booking-requests" element={<BookingRequests />} />
                            <Route path="active-rentals" element={<ActiveRentals />} />
                            <Route path="revenue" element={<Revenue />} />
                            <Route path="pricing" element={<PricingIntelligence />} />
                            <Route path="analytics" element={<ListingAnalytics />} />
                            <Route path="reviews" element={<OwnerReviews />} />
                            <Route path="insights" element={<CustomerInsights />} />
                          </Routes>
                        </RoleRoute>
                      </PrivateRoute>
                    }
                  />

                  {/* Protected Routes - Admin */}
                  <Route
                    path="/admin/*"
                    element={
                      <PrivateRoute>
                        <RoleRoute role="ADMIN">
                          <Routes>
                            <Route path="dashboard" element={<AdminOverview />} />
                            <Route path="users" element={<AdminUsers />} />
                            <Route path="listings" element={<AdminListings />} />
                            <Route path="bookings" element={<AdminBookings />} />
                            <Route path="payments" element={<AdminPayments />} />
                            <Route path="fraud" element={<FraudDetection />} />
                            <Route path="ai-analytics" element={<AIAnalytics />} />
                            <Route path="platform-analytics" element={<PlatformAnalytics />} />
                            <Route path="categories" element={<AdminCategories />} />
                            <Route path="reports" element={<AdminReports />} />
                            <Route path="system-health" element={<SystemHealth />} />
                            <Route path="settings" element={<AdminSettings />} />
                          </Routes>
                        </RoleRoute>
                      </PrivateRoute>
                    }
                  />

                  {/* Redirect to login if not authenticated and trying to access protected routes */}
                  <Route path="*" element={<Navigate to="/" replace />} />
                </Routes>
              </main>
              <Footer />
            </div>
          </BrowserRouter>
        </QueryClientProvider>
      </AuthProvider>
    </ThemeProvider>
  );
}

export default App;