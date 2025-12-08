import { useEffect, useState } from 'react';
import { Globe, Zap, Bot, LucideIcon } from 'lucide-react';
import { ServiceCard } from './ServiceCard';
import { api, Service } from '@/lib/api';

// Map icon names from API to Lucide components
const iconMap: Record<string, LucideIcon> = {
  Globe,
  Zap,
  Bot,
};

export function Services() {
  const [services, setServices] = useState<Service[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    api.getServices()
      .then(setServices)
      .catch(console.error)
      .finally(() => setLoading(false));
  }, []);

  if (loading) {
    return (
      <section id="services" className="py-20 px-6 lg:px-16 bg-[#F8FAFC]">
        <div className="max-w-[1440px] mx-auto text-center">載入中... Loading...</div>
      </section>
    );
  }

  return (
    <section id="services" className="py-20 px-6 lg:px-16 bg-[#F8FAFC]">
      <div className="max-w-[1440px] mx-auto">
        <h2 className="text-center text-[#0F172A] mb-12">
          我提供的服務 Services I Provide
        </h2>
        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
          {services.map((service) => (
            <ServiceCard
              key={service.id}
              icon={iconMap[service.icon] || Globe}
              title={service.title}
              description={service.description}
            />
          ))}
        </div>
      </div>
    </section>
  );
}
