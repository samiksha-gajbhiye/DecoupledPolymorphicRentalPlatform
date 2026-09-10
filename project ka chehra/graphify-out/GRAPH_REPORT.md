# Graph Report - project ka chehra  (2026-08-26)

## Corpus Check
- Corpus is ~21,760 words - fits in a single context window. You may not need a graph.

## Summary
- 385 nodes · 630 edges · 41 communities (27 shown, 14 thin omitted)
- Extraction: 100% EXTRACTED · 0% INFERRED · 0% AMBIGUOUS · INFERRED: 3 edges (avg confidence: 0.85)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- Frontend Dependencies
- Authentication Components
- Booking Inputs
- API Data Services
- Build Tooling
- Rental Components
- Application Pages
- Project Documentation
- Owner Listings
- Admin Overview
- Booking Details
- Customer Dashboard
- Lint Configuration
- Icon Sprite
- Owner Analytics
- Pricing Intelligence
- Revenue Reporting
- Hero Artwork
- Vite Branding
- Favicon Branding
- React Branding
- HTML Entry Point
- Admin Users
- Customer Bookings
- Active Rentals
- Booking Requests
- Owner Reviews
- Site Footer
- Admin Categories
- Admin Listings
- Platform Analytics
- Admin Reports
- Messages Notifications
- Customer Payments
- Customer Reviews
- Customer Settings

## God Nodes (most connected - your core abstractions)
1. `react` - 43 edges
2. `useAuth()` - 21 edges
3. `DemoRental README` - 17 edges
4. `ProductCard()` - 8 edges
5. `DateInput()` - 7 edges
6. `scripts` - 5 edges
7. `client` - 5 edges
8. `AuthProvider()` - 5 edges
9. `useTheme()` - 5 edges
10. `stacked platform` - 5 edges

## Surprising Connections (you probably didn't know these)
- `AuthProvider()` --calls--> `loginRequest()`  [EXTRACTED]
  src/context/AuthContext.jsx → src/api/authApi.js
- `AuthProvider()` --calls--> `registerRequest()`  [EXTRACTED]
  src/context/AuthContext.jsx → src/api/authApi.js
- `BrowseRentals()` --calls--> `getAllProducts()`  [EXTRACTED]
  src/pages/public/BrowseRentals.jsx → src/api/productApi.js
- `toCardModel()` --calls--> `resolveImageUrl()`  [EXTRACTED]
  src/pages/public/BrowseRentals.jsx → src/api/productApi.js
- `AuthProvider()` --calls--> `getCurrentUser()`  [EXTRACTED]
  src/context/AuthContext.jsx → src/api/userApi.js

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **** — public_icons_svg_bluesky_icon, public_icons_svg_discord_icon, public_icons_svg_github_icon, public_icons_svg_x_icon [INFERRED 0.85]
- **React atom composition** — src_assets_react_react_mark, src_assets_react_orbital_paths, src_assets_react_central_nucleus [EXTRACTED 1.00]

## Communities (41 total, 14 thin omitted)

### Community 0 - "Frontend Dependencies"
Cohesion: 0.05
Nodes (39): axios, @headlessui/react, @heroicons/react, lucide-react, dependencies, axios, @headlessui/react, @heroicons/react (+31 more)

### Community 1 - "Authentication Components"
Cohesion: 0.12
Nodes (20): loginRequest(), registerRequest(), getCurrentUser(), WelcomeCard(), MobileNavDrawer(), Navbar(), WelcomeCard(), PrivateRoute() (+12 more)

### Community 2 - "Booking Inputs"
Cohesion: 0.18
Nodes (21): react, DateInput(), getParts(), toDisplayDate(), toIsoDate(), Button, Checkbox, Form (+13 more)

### Community 3 - "API Data Services"
Cohesion: 0.10
Nodes (12): BASE_URL, client, getAllProducts(), resolveImageUrl(), CategorySelector(), FiltersSidebar(), SearchBar(), HeroSection() (+4 more)

### Community 4 - "Build Tooling"
Cohesion: 0.07
Nodes (28): autoprefixer, oxlint, devDependencies, autoprefixer, oxlint, postcss, tailwindcss, tailwindcss-animate (+20 more)

### Community 5 - "Rental Components"
Cohesion: 0.11
Nodes (14): BookingForm(), ImageGallery(), ProductCard(), RelatedItems(), RentalDetails(), AIRecommendations(), CTASection(), HowItWorks() (+6 more)

### Community 6 - "Application Pages"
Cohesion: 0.13
Nodes (12): App(), queryClient, AIAnalytics(), AdminBookings(), FraudDetection(), AdminPayments(), AdminSettings(), SystemHealth() (+4 more)

### Community 7 - "Project Documentation"
Cohesion: 0.11
Nodes (18): DemoRental README, Admin Dashboard, AI Services, Axios, Customer Dashboard, DemoRental, Lucide React, Owner Dashboard (+10 more)

### Community 8 - "Owner Listings"
Cohesion: 0.21
Nodes (7): AddListingButton(), ListingCard(), OwnerStatsGrid(), RecentListings(), RevenueChart(), MyListings(), OwnerOverview()

### Community 9 - "Admin Overview"
Cohesion: 0.29
Nodes (5): AdminRecentActivity(), AdminStatsGrid(), RevenueOverview(), SystemStatus(), AdminOverview()

### Community 10 - "Booking Details"
Cohesion: 0.29
Nodes (5): ActionButtons(), BookingDetailsHeader(), BookingSummary(), BookingTimeline(), BookingDetails()

### Community 11 - "Customer Dashboard"
Cohesion: 0.29
Nodes (5): ActiveRentalsCard(), RecentActivity(), StatsGrid(), UpcomingBookingsCard(), CustomerDashboard()

### Community 12 - "Lint Configuration"
Cohesion: 0.25
Nodes (7): plugins, rules, react/only-export-components, react/rules-of-hooks, $schema, oxc, warn

### Community 13 - "Icon Sprite"
Cohesion: 0.25
Nodes (7): Bluesky icon, Discord icon, Documentation icon, GitHub icon, Social account icon, Social media and utility icon sprite, X icon

### Community 14 - "Owner Analytics"
Cohesion: 0.36
Nodes (4): AnalyticsCard(), BookingConversion(), ViewsChart(), ListingAnalytics()

### Community 15 - "Pricing Intelligence"
Cohesion: 0.36
Nodes (4): MarketAnalysis(), PriceRecommendations(), PricingCard(), PricingIntelligence()

### Community 16 - "Revenue Reporting"
Cohesion: 0.36
Nodes (4): PayoutSummary(), RevenueCard(), RevenueTrends(), Revenue()

### Community 17 - "Hero Artwork"
Cohesion: 0.33
Nodes (6): hero image showing a stylized stacked platform, isometric perspective, purple illuminated lower layer, rounded rectangular layers, stacked platform, thin light outline on upper layer

### Community 18 - "Vite Branding"
Cohesion: 0.33
Nodes (5): dark-mode adaptive color, lavender highlights, parenthesis-style wordmark, purple lightning bolt, Vite logo

### Community 19 - "Favicon Branding"
Cohesion: 0.50
Nodes (5): favicon lightning-bolt mark, clipped ellipse highlights, electric energy brand symbol, lightning bolt, violet primary fill

### Community 20 - "React Branding"
Cohesion: 0.40
Nodes (5): central circular nucleus, cyan color, three elliptical orbital paths, React logo, React mark

### Community 21 - "HTML Entry Point"
Cohesion: 0.50
Nodes (4): HTML Entry Point, HTML Entry Point, Root Mount, src/main.jsx

## Knowledge Gaps
- **82 isolated node(s):** `$schema`, `oxc`, `react/rules-of-hooks`, `warn`, `name` (+77 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **14 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `react` connect `Booking Inputs` to `Admin Reports`, `Authentication Components`, `Customer Payments`, `API Data Services`, `Customer Reviews`, `Rental Components`, `Application Pages`, `Customer Settings`, `Customer Dashboard`, `Lint Configuration`, `Site Footer`, `Admin Categories`, `Admin Listings`, `Platform Analytics`?**
  _High betweenness centrality (0.076) - this node is a cross-community bridge._
- **Why does `dependencies` connect `Frontend Dependencies` to `Build Tooling`?**
  _High betweenness centrality (0.024) - this node is a cross-community bridge._
- **Why does `plugins` connect `Lint Configuration` to `Booking Inputs`?**
  _High betweenness centrality (0.024) - this node is a cross-community bridge._
- **What connects `$schema`, `oxc`, `react/rules-of-hooks` to the rest of the system?**
  _82 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Frontend Dependencies` be split into smaller, more focused modules?**
  _Cohesion score 0.05128205128205128 - nodes in this community are weakly interconnected._
- **Should `Authentication Components` be split into smaller, more focused modules?**
  _Cohesion score 0.11895161290322581 - nodes in this community are weakly interconnected._
- **Should `API Data Services` be split into smaller, more focused modules?**
  _Cohesion score 0.1010752688172043 - nodes in this community are weakly interconnected._