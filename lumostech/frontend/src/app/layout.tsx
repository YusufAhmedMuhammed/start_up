import './globals.css';
import type { Metadata } from 'next';
import LeadForm from '@/components/forms/LeadForm';

export const metadata: Metadata = {
  title: 'LumosTech - Digital Innovation Agency',
  description: 'Transform your business with cutting-edge digital solutions',
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}

export function ContactPage() {
  return (
    <div className="py-12">
      <h1 className="text-3xl font-bold text-center mb-8">Contact Us</h1>
      <LeadForm />
    </div>
  );
} 