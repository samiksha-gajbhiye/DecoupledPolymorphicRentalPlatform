const About = () => {
  return (
    <div className="min-h-screen bg-gray-50 dark:bg-gray-900">
      <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-16">
        <h1 className="text-3xl font-bold text-gray-900 dark:text-white mb-8">
          About DemoRental
        </h1>
        <div className="prose dark:prose-invert max-w-none">
          <p>DemoRental is a modern AI-powered rental platform built to make discovering, renting, and managing products simple. Our mission is to democratize access to products by making it easy for anyone to rent anything they need, when they need it.</p>
          <h2 className="text-2xl font-semibold text-gray-900 dark:text-white mt-8 mb-4">Our Story</h2>
          <p>Founded in 2024, DemoRental started with a simple idea: why buy when you can rent? We noticed that many products sit idle most of the time while people struggle to access them when needed. Our platform bridges this gap by connecting product owners with renters in a secure, efficient marketplace.</p>
          <h2 className="text-2xl font-semibold text-gray-900 dark:text-white mt-8 mb-4">Our Vision</h2>
          <p>We envision a world where access outweighs ownership, where products are utilized to their fullest potential, and where everyone can enjoy the things they need without the burden of ownership. Through AI-powered recommendations, secure transactions, and trusted community verification, we're building the future of collaborative consumption.</p>
          <h2 className="text-2xl font-semibold text-gray-900 dark:text-white mt-8 mb-4">Our Values</h2>
          <ul className="list-disc list-inside space-y-2 mt-4">
            <li><strong>Trust:</strong> We build trust through verified identities, secure payments, and transparent processes.</li>
            <li><strong>Innovation:</strong> We leverage AI and machine learning to create personalized experiences and detect fraud.</li>
            <li><strong>Community:</strong> We foster a community of responsible owners and respectful renters.</li>
            <li><strong>Sustainability:</strong> We promote sustainable consumption by maximizing product utilization.</li>
            <li><strong>Accessibility:</strong> We strive to make our platform accessible to everyone, regardless of technical expertise.</li>
          </ul>
        </div>
      </div>
    </div>
  );
};

export default About;