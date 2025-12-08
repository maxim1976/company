import { LucideIcon } from 'lucide-react';

interface ServiceCardProps {
  icon: LucideIcon;
  title: string;
  description: string;
}

export function ServiceCard({ icon: Icon, title, description }: ServiceCardProps) {
  return (
    <div className="bg-white p-8 rounded-2xl shadow-sm hover:shadow-md transition-shadow">
      <div className="w-14 h-14 bg-[#2563EB] rounded-lg flex items-center justify-center mb-6">
        <Icon className="text-white" size={28} />
      </div>
      <h3 className="text-[#0F172A] mb-3">
        {title}
      </h3>
      <p className="text-[#475569]">
        {description}
      </p>
    </div>
  );
}
