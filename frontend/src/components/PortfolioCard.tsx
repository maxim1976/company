import { ImageWithFallback } from './figma/ImageWithFallback';

interface PortfolioCardProps {
  image: string;
  title: string;
  category: string;
  description: string;
}

export function PortfolioCard({ image, title, category, description }: PortfolioCardProps) {
  return (
    <div className="bg-white rounded-2xl overflow-hidden shadow-sm hover:shadow-md transition-shadow">
      <div className="aspect-[4/3] overflow-hidden">
        <ImageWithFallback
          src={image}
          alt={title}
          className="w-full h-full object-cover hover:scale-105 transition-transform duration-300"
        />
      </div>
      <div className="p-6">
        <div className="text-sm text-[#2563EB] mb-2">
          {category}
        </div>
        <h3 className="text-[#0F172A] mb-2">
          {title}
        </h3>
        <p className="text-[#475569] text-sm">
          {description}
        </p>
      </div>
    </div>
  );
}
