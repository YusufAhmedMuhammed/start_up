import {
  BuildingOfficeIcon,
  ShoppingCartIcon,
  BanknotesIcon,
  BeakerIcon,
} from '@heroicons/react/24/outline';

const industries = [
  {
    name: 'Finance',
    description: 'Secure and compliant financial technology solutions',
    icon: BanknotesIcon,
  },
  {
    name: 'Healthcare',
    description: 'Innovative healthcare technology and patient care solutions',
    icon: BeakerIcon,
  },
  {
    name: 'Retail',
    description: 'E-commerce and retail management systems',
    icon: ShoppingCartIcon,
  },
  {
    name: 'Real Estate',
    description: 'Property management and real estate technology',
    icon: BuildingOfficeIcon,
  },
];

export default function IndustriesSection() {
  return (
    <section className="py-24 bg-white">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center mb-16">
          <h2 className="text-3xl font-bold text-gray-900 sm:text-4xl">
            Industries We Serve
          </h2>
          <p className="mt-4 text-lg text-gray-600">
            Tailored solutions for diverse business sectors
          </p>
        </div>

        <div className="grid grid-cols-1 gap-8 sm:grid-cols-2 lg:grid-cols-4">
          {industries.map((industry) => (
            <div
              key={industry.name}
              className="group relative bg-gray-50 rounded-lg p-6 hover:bg-primary-50 transition-colors duration-200"
            >
              <div className="flex items-center justify-center h-12 w-12 rounded-md bg-primary-100 text-primary-600 mb-4 group-hover:bg-primary-200 group-hover:text-primary-700 transition-colors duration-200">
                <industry.icon className="h-6 w-6" aria-hidden="true" />
              </div>
              <h3 className="text-lg font-medium text-gray-900 mb-2">
                {industry.name}
              </h3>
              <p className="text-gray-600">{industry.description}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
} 