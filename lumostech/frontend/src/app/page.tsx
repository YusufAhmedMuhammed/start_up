import React from 'react';
import HeroSection from '../components/home/HeroSection';
import ServicesSection from '../components/home/ServicesSection';
import IndustriesSection from '../components/home/IndustriesSection';
import AboutSection from '../components/home/AboutSection';
import Footer from '../components/home/Footer';

export default function Home() {
  return (
    <main className="min-h-screen">
      <HeroSection />
      <ServicesSection />
      <IndustriesSection />
      <AboutSection />
      <Footer />
    </main>
  );
} 