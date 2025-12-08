import { Button } from './ui/button';
import { ImageWithFallback } from './figma/ImageWithFallback';

export function Hero() {
  const scrollToSection = (sectionId: string) => {
    const element = document.getElementById(sectionId);
    if (element) {
      element.scrollIntoView({ behavior: 'smooth' });
    }
  };

  return (
    <section className="pt-32 pb-20 px-6 lg:px-16">
      <div className="max-w-[1440px] mx-auto">
        <div className="grid lg:grid-cols-2 gap-12 items-center">
          {/* Left Content */}
          <div className="space-y-6">
            <h1 className="text-[#0F172A]">
              為您的企業打造現代網站與 AI 解決方案
              <span className="block text-2xl lg:text-3xl mt-2 text-[#475569] font-normal">
                Modern Websites & AI Solutions for Your Business
              </span>
            </h1>
            <p className="text-[#475569] text-lg">
              我專門製作著陸頁、網路商店和 AI 助理 — 快速、實惠、專業。
              <span className="block mt-1 text-base">
                I build landing pages, online stores, and AI assistants — fast, affordable, and professional.
              </span>
            </p>
            <div className="flex flex-col sm:flex-row gap-4">
              <Button
                onClick={() => scrollToSection('contact')}
                className="bg-[#2563EB] hover:bg-[#3B82F6] text-white px-4 py-4 rounded-[10px]"
              >
                預約免費諮詢 Book a Free Consultation
              </Button>
              <Button
                onClick={() => scrollToSection('portfolio')}
                variant="outline"
                className="border border-[#2563EB] text-[#2563EB] bg-white hover:bg-[#F8FAFC] px-4 py-4 rounded-[10px]"
              >
                查看作品集 View Portfolio
              </Button>
            </div>
          </div>

          {/* Right Illustration */}
          <div className="relative">
            <ImageWithFallback
              src="https://images.unsplash.com/photo-1630522790545-67ad2cb700fe?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w3Nzg4Nzd8MHwxfHNlYXJjaHwxfHxtb2Rlcm4lMjB3ZWJzaXRlJTIwbW9ja3VwfGVufDF8fHx8MTc2MzY5NDA3NHww&ixlib=rb-4.1.0&q=80&w=1080&utm_source=figma&utm_medium=referral"
              alt="Website mockups"
              className="w-full h-auto rounded-2xl shadow-lg"
            />
          </div>
        </div>
      </div>
    </section>
  );
}
