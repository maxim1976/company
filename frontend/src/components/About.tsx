import { Check } from 'lucide-react';

export function About() {
  const highlights = [
    { zh: '5年以上經驗', en: '5+ years experience' },
    { zh: 'AI 自動化', en: 'AI automation' },
    { zh: '簡單定價', en: 'Simple pricing' },
  ];

  return (
    <section className="py-20 px-6 lg:px-16 bg-[#F8FAFC]">
      <div className="max-w-[1440px] mx-auto">
        <div className="max-w-3xl mx-auto text-center">
          <h2 className="text-[#0F172A] mb-6">
            關於我 Who I Am
          </h2>
          <p className="text-[#475569] text-lg mb-2">
            嗨，我是 Max — 一位幫助台灣小型企業在網路上成長的網頁開發者。
            我使用 Django、TailwindCSS 和 AI 工具來創建快速、實用且價格實惠的網站。
          </p>
          <p className="text-[#475569] text-base mb-8">
            Hi, I'm Maxim — a web developer helping small businesses in Taiwan grow online.
            I create fast, functional, and affordable websites using Django, TailwindCSS, and AI tools.
          </p>
          <div className="flex flex-wrap justify-center gap-6">
            {highlights.map((highlight) => (
              <div key={highlight.en} className="flex items-center gap-2">
                <div className="w-6 h-6 bg-[#2563EB] rounded-full flex items-center justify-center">
                  <Check className="text-white" size={16} />
                </div>
                <span className="text-[#0F172A]">{highlight.zh} {highlight.en}</span>
              </div>
            ))}
          </div>
        </div>
      </div>
    </section>
  );
}
