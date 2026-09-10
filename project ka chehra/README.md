# DemoRental - Production-Grade React Frontend

A professional, modern rental marketplace and management dashboard built with React.js, designed to connect with an existing Java Spring Boot backend and Python AI/ML services.

## Features

### 🏠 Public Website
- **Landing Page**: Premium hero section with search, categories, popular rentals, AI recommendations, and trust/safety sections
- **Browse & Search**: Advanced search with filters, sorting, and category browsing
- **Product Details**: Detailed product pages with image galleries, booking forms, and related items
- **Static Pages**: About, Login, Register pages

### 👤 Customer Dashboard
- **Overview**: Welcome message, stats grid, active rentals, and recent activity
- **My Bookings**: View and manage all bookings with status tracking
- **Wishlist**: Save favorite items for later
- **Recommendations**: AI-powered personalized suggestions
- **Messages & Notifications**: Communication center
- **Profile**: Account management and settings
- **Payments & Reviews**: Transaction history and review management

### 🏢 Owner Dashboard
- **Overview**: Business overview, stats, recent listings, and revenue charts
- **My Listings**: Manage all rental properties
- **Add/Edit Listing**: Complete listing management with photo upload
- **Booking Requests**: Approve/reject booking requests
- **Active Rentals**: Monitor current rentals
- **Revenue & Pricing Intelligence**: Financial analytics and AI-powered pricing suggestions
- **Listing Analytics**: Views, conversions, and performance metrics
- **Reviews & Customer Insights**: Feedback and renter analytics

### ⚙️ Admin Dashboard
- **Overview**: Platform statistics, recent activity, system status, and revenue
- **User Management**: View and manage all platform users
- **Listing Management**: Moderate all listings
- **Booking Oversight**: Monitor all platform bookings
- **Payment Processing**: Track all financial transactions
- **Fraud Detection**: Security monitoring and alerts
- **AI Analytics**: Platform-wide AI insights
- **Reports & System Health**: Comprehensive reporting and monitoring

## Technology Stack

- **React.js** - Frontend library
- **React Router** - Navigation and routing
- **Tailwind CSS** - Utility-first CSS framework
- **shadcn/ui** - Reusable UI components
- **Lucide React** - Icon library
- **Recharts** - Data visualization library
- **Axios** - HTTP client for API communication
- **React Hook Form** - Form handling and validation
- **Zod** - Schema validation
- **TanStack Query (React Query)** - API state management
- **JavaScript** - Programming language

## Project Structure

```
src/
├── components/
│   ├── layout/           # Navbar, footer, etc.
│   ├── sections/         # Landing page sections
│   ├── customer/         # Customer-specific components
│   ├── owner/            # Owner-specific components
│   ├── admin/            # Admin-specific components
│   └── ui/               # Reusable UI components (forms, inputs, buttons, etc.)
├── pages/
│   ├── public/           # Publicly accessible pages
│   ├── customer/         # Customer dashboard pages
│   ├── owner/            # Owner dashboard pages
│   └── admin/            # Admin dashboard pages
├── context/              # React context (Auth, Theme)
├── hooks/                # Custom React hooks
├── utils/                # Utility functions
├── assets/               # Static assets (images, icons)
└── styles/               # CSS/Tailwind configuration
```

## Design Features

- **Responsive Design**: Works on mobile, tablet, and desktop
- **Light/Dark Mode**: Theme toggle in user settings
- **Professional UI**: Clean typography, generous spacing, subtle borders, soft shadows
- **Modern Animations**: Tasteful transitions and hover effects
- **Empty States & Loading**: Thoughtful UX for all scenarios
- **Accessibility**: Proper semantic HTML and ARIA attributes
- **Performance**: Optimized components and lazy loading where applicable

## Key UI Components

- **Navbar**: Professional navigation with mobile drawer
- **Product Cards**: Consistent, informative item displays
- **Forms**: Validated, user-friendly input components
- **Data Visualization**: Charts for analytics and reporting
- **Cards**: Consistent container styling for information display
- **Badges & Tags**: Status indicators and categorization
- **Modals & Overlays**: Focused interaction patterns
- **Navigation**: Clear breadcrumbs and contextual menus

## Setup Instructions

1. Install dependencies:
   ```bash
   npm install
   ```

2. Start the development server:
   ```bash
   npm run dev
   ```

3. Build for production:
   ```bash
   npm run build
   ```

## Environment Variables

Create a `.env` file in the root directory with:

```
VITE_API_URL=https://your-backend-api-url.com/api
VITE_APP_NAME=DemoRental
```

## API Integration Points

The frontend is designed to integrate with RESTful endpoints following this pattern:

- **Auth**: `/api/auth/*` (login, register, logout)
- **Users**: `/api/users/*` (profile, settings)
- **Listings**: `/api/listings/*` (CRUD operations, search)
- **Bookings**: `/api/bookings/*` (create, retrieve, update)
- **Payments**: `/api/payments/*` (process, refund, history)
- **Reviews**: `/api/reviews/*` (create, retrieve)
- **Analytics**: `/api/analytics/*` (dashboard metrics)
- **AI Services**: `/api/ai/*` (recommendations, pricing, fraud detection)

## Future Development

To connect with the actual backend:
1. Implement API service layer using Axios
2. Add proper error handling and loading states
3. Integrate with authentication (JWT/session management)
4. Add real-time updates via WebSockets (if needed)
5. Implement form validation with Zod schemas
6. Add comprehensive unit and integration tests

## Credits

Built with modern React best practices and following professional design principles inspired by Airbnb, Stripe, Linear, and Vercel - but with original, custom UI/UX design.