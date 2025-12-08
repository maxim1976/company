import { useState } from 'react';
import { Menu, X } from 'lucide-react';
import { Button } from './ui/button';

export function Header() {
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);

  const scrollToSection = (sectionId: string) => {
    const element = document.getElementById(sectionId);
    if (element) {
      element.scrollIntoView({ behavior: 'smooth' });
      setMobileMenuOpen(false);
    }
  };

  return (
    <header className="fixed top-0 left-0 right-0 z-50 bg-white border-b border-gray-200">
      <div className="max-w-[1440px] mx-auto px-6 lg:px-16">
        <div className="flex items-center justify-between h-20">
          {/* Logo */}
          <div className="text-xl font-semibold text-[#0F172A]">
            花蓮網頁工作室
            <span className="text-sm font-normal text-[#475569] ml-2">Vibe Studio</span>
          </div>

          {/* Desktop Navigation */}
          <nav className="hidden md:flex items-center gap-8">
            <button
              onClick={() => scrollToSection('services')}
              className="text-[#475569] hover:text-[#2563EB] transition-colors"
            >
              服務 Services
            </button>
            <button
              onClick={() => scrollToSection('portfolio')}
              className="text-[#475569] hover:text-[#2563EB] transition-colors"
            >
              作品集 Portfolio
            </button>
            <button
              onClick={() => scrollToSection('contact')}
              className="text-[#475569] hover:text-[#2563EB] transition-colors"
            >
              聯絡 Contact
            </button>
            <Button
              onClick={() => scrollToSection('contact')}
              className="bg-[#2563EB] hover:bg-[#3B82F6] text-white px-4 py-2 rounded-[10px]"
            >
              免費報價 Get a Quote
            </Button>
          </nav>

          {/* Mobile Menu Button */}
          <button
            onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
            className="md:hidden text-[#0F172A]"
          >
            {mobileMenuOpen ? <X size={24} /> : <Menu size={24} />}
          </button>
        </div>

        {/* Mobile Menu */}
        {mobileMenuOpen && (
          <div className="md:hidden py-4 border-t border-gray-200">
            <nav className="flex flex-col gap-4">
              <button
                onClick={() => scrollToSection('services')}
                className="text-[#475569] hover:text-[#2563EB] transition-colors text-left py-2"
              >
                服務 Services
              </button>
              <button
                onClick={() => scrollToSection('portfolio')}
                className="text-[#475569] hover:text-[#2563EB] transition-colors text-left py-2"
              >
                作品集 Portfolio
              </button>
              <button
                onClick={() => scrollToSection('contact')}
                className="text-[#475569] hover:text-[#2563EB] transition-colors text-left py-2"
              >
                聯絡 Contact
              </button>
              <Button
                onClick={() => scrollToSection('contact')}
                className="bg-[#2563EB] hover:bg-[#3B82F6] text-white px-4 py-2 rounded-[10px] w-full"
              >
                免費報價 Get a Quote
              </Button>
            </nav>
          </div>
        )}
      </div>
    </header>
  );
}
