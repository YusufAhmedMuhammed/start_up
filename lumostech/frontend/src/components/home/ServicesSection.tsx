import { CodeBracketIcon, DevicePhoneMobileIcon, PaintBrushIcon, CloudIcon } from '@heroicons/react/24/outline';

const services = [
  {
    name: 'Web Development',
    description: 'Custom web applications and websites built with modern technologies and best practices.',
    icon: CodeBracketIcon,
  },
  {
    name: 'Mobile Apps',
    description: 'Native and cross-platform mobile applications for iOS and Android devices.',
    icon: DevicePhoneMobileIcon,
  },
  {
    name: 'UI/UX Design',
    description: 'Beautiful and intuitive user interfaces designed for optimal user experience.',
    icon: PaintBrushIcon,
  },
  {
    name: 'Cloud Solutions',
    description: 'Scalable cloud infrastructure and services to power your digital transformation.',
    icon: CloudIcon,
  },
];

export default function ServicesSection() {
  return (
    <section className="py-24 bg-gray-50">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center mb-16">
          <h2 className="text-3xl font-bold text-gray-900 sm:text-4xl">
            Our Services
          </h2>
          <p className="mt-4 text-lg text-gray-600">
            Comprehensive digital solutions to help your business grow
          </p>
        </div>

        <div className="grid grid-cols-1 gap-8 sm:grid-cols-2 lg:grid-cols-4">
          {services.map((service) => (
            <div
              key={service.name}
              className="bg-white rounded-lg shadow-lg p-6 hover:shadow-xl transition-shadow duration-200"
            >
              <div className="flex items-center justify-center h-12 w-12 rounded-md bg-primary-100 text-primary-600 mb-4">
                <service.icon className="h-6 w-6" aria-hidden="true" />
              </div>
              <h3 className="text-lg font-medium text-gray-900 mb-2">
                {service.name}
              </h3>
              <p className="text-gray-600">{service.description}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
} 