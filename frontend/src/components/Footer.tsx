import { Mail, Instagram, MessageCircle } from 'lucide-react';

export function Footer() {
  return (
    <footer className="py-12 px-6 lg:px-16 bg-[#0F172A]">
      <div className="max-w-[1440px] mx-auto">
        <div className="flex flex-col md:flex-row justify-between items-center gap-6">
          {/* Logo and Description */}
          <div className="text-center md:text-left">
            <div className="text-xl font-semibold text-white mb-2">
              Max 網頁工作室 Web Studio
            </div>
            <p className="text-gray-400 text-sm">
              網站 • 網路商店 • AI 自動化
              <span className="block">Websites • Online Stores • AI Automation</span>
            </p>
          </div>

          {/* Social Links */}
          <div className="flex gap-4">
            <a
              href="mailto:contact@maxwebstudio.com"
              className="w-10 h-10 bg-white/10 hover:bg-white/20 rounded-full flex items-center justify-center transition-colors"
              aria-label="Email"
            >
              <Mail className="text-white" size={20} />
            </a>
            <a
              href="#"
              className="w-10 h-10 bg-white/10 hover:bg-white/20 rounded-full flex items-center justify-center transition-colors"
              aria-label="Line"
            >
              <MessageCircle className="text-white" size={20} />
            </a>
            <a
              href="#"
              className="w-10 h-10 bg-white/10 hover:bg-white/20 rounded-full flex items-center justify-center transition-colors"
              aria-label="Instagram"
            >
              <Instagram className="text-white" size={20} />
            </a>
          </div>
        </div>

        {/* Copyright */}
        <div className="mt-8 pt-8 border-t border-white/10 text-center text-gray-400 text-sm">
          © 2025 Max 網頁工作室 Web Studio. 版權所有 All rights reserved.
        </div>
      </div>
    </footer>
  );
}
