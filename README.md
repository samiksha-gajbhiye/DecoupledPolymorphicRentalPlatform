#Decoupled Polymorphic Rental Platform
A scalable, AI-enabled rental platform designed to support multiple categories of rental products through a decoupled, polymorphic,
and service-oriented architecture.
The platform combines a Java Spring Boot backend for core rental operations with a dedicated Python AI/ML service for intelligent search,
recommendations, fraud detection, image processing, dynamic pricing, and analytics.

#Overview
The Decoupled Polymorphic Rental Platform is designed as an extensible rental ecosystem capable of supporting different categories of rental products through a common platform.
The system separates core business operations from AI-driven capabilities. The primary backend manages users, authentication, rental operations, persistence, and business workflows, 
while a dedicated Python service provides machine-learning and data-intensive capabilities.
This separation allows AI/ML components to evolve independently from the core application and provides a foundation for scaling individual services according to their workloads.

#Core Objectives
Build a flexible rental platform supporting multiple rental categories
Apply polymorphism to the rental domain
Decouple core business logic from AI/ML workloads
Provide secure JWT-based authentication
Improve performance using Redis caching
Enable intelligent semantic search and recommendations
Detect fraudulent listings and suspicious activity
Analyze rental data for insights and forecasting
Process and validate uploaded rental images
Support intelligent pricing and ranking
Maintain independently deployable application components

System Architecture
                                      ┌───────────────────────┐
                                      │       Frontend        │
                                      │    Web Application     │
                                      └───────────┬───────────┘
                                                  │
                                                  │ REST / HTTP
                                                  ▼
                         ┌─────────────────────────────────────────┐
                         │          Spring Boot Backend            │
                         │                                         │
                         │  Authentication                         │
                         │  User Management                         │
                         │  Rental Management                        │
                         │  Business Logic                          │
                         │  REST APIs                               │
                         └───────────────┬─────────────────────────┘
                                         │
                       ┌─────────────────┼──────────────────┐
                       │                 │                  │
                       ▼                 ▼                  ▼
                ┌─────────────┐   ┌─────────────┐   ┌─────────────┐
                │    MySQL    │   │    Redis    │   │    Email    │
                │  Database   │   │    Cache    │   │   Service   │
                └─────────────┘   └─────────────┘   └─────────────┘
                                         
                                         │
                                         │ AI / ML Requests
                                         ▼
                         ┌─────────────────────────────────────────┐
                         │          Python AI/ML Service           │
                         │              DemoRental                │
                         │                                         │
                         │  Recommendation                         │
                         │  Semantic Search                         │
                         │  Fraud Detection                         │
                         │  Image Processing                        │
                         │  Dynamic Pricing                         │
                         │  Analytics & Forecasting                 │
                         └───────────────┬─────────────────────────┘
                                         │
                     ┌───────────────────┼───────────────────┐
                     │                   │                   │
                     ▼                   ▼                   ▼
               ┌───────────┐       ┌───────────┐       ┌───────────┐
               │   FAISS   │       │ ML Models │       │  Vector   │
               │  Index    │       │  YOLO/CLIP│       │ Database  │
               └───────────┘       └───────────┘       └───────────┘

               
