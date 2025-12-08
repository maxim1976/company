import { useEffect, useState } from 'react';
import { PortfolioCard } from './PortfolioCard';
import { api, PortfolioProject } from '@/lib/api';

export function Portfolio() {
  const [projects, setProjects] = useState<PortfolioProject[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    api.getPortfolio()
      .then(setProjects)
      .catch(console.error)
      .finally(() => setLoading(false));
  }, []);

  if (loading) {
    return (
      <section id="portfolio" className="py-20 px-6 lg:px-16 bg-white">
        <div className="max-w-[1440px] mx-auto text-center">載入中... Loading...</div>
      </section>
    );
  }

  return (
    <section id="portfolio" className="py-20 px-6 lg:px-16 bg-white">
      <div className="max-w-[1440px] mx-auto">
        <h2 className="text-center text-[#0F172A] mb-12">
          最近作品 Recent Projects
        </h2>
        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
          {projects.map((project) => (
            <PortfolioCard
              key={project.id}
              image={project.image}
              title={project.title}
              category={project.category}
              description={project.description}
            />
          ))}
        </div>
      </div>
    </section>
  );
}
