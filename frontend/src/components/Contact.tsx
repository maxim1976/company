import { useState } from 'react';
import { Button } from './ui/button';
import { Input } from './ui/input';
import { Textarea } from './ui/textarea';
import { api } from '@/lib/api';

export function Contact() {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    message: '',
  });
  const [submitted, setSubmitted] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setError(null);

    try {
      await api.submitContact(formData);
      setSubmitted(true);
      setTimeout(() => {
        setSubmitted(false);
        setFormData({ name: '', email: '', message: '' });
      }, 3000);
    } catch (err) {
      setError('Failed to send message. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <section id="contact" className="py-20 px-6 lg:px-16 bg-white">
      <div className="max-w-[1440px] mx-auto">
        <div className="max-w-2xl mx-auto">
          <h2 className="text-center text-[#0F172A] mb-4">
            準備好開始您的專案了嗎？ Ready to Start Your Project?
          </h2>
          <p className="text-center text-[#475569] mb-12">
            填寫以下表格，我會在24小時內回覆您。
            <span className="block">Fill out the form below and I'll get back to you within 24 hours.</span>
          </p>
          
          {submitted ? (
            <div className="bg-green-50 border border-green-200 rounded-lg p-6 text-center">
              <p className="text-green-800">
                感謝您！您的訊息已成功傳送。
                <span className="block">Thank you! Your message has been sent successfully.</span>
              </p>
            </div>
          ) : (
            <form onSubmit={handleSubmit} className="space-y-6">
              {error && (
                <div className="bg-red-50 border border-red-200 rounded-lg p-4 text-center">
                  <p className="text-red-800">{error}</p>
                </div>
              )}
              <div>
                <label htmlFor="name" className="block mb-2 text-[#0F172A]">
                  姓名 Name
                </label>
                <Input
                  id="name"
                  type="text"
                  value={formData.name}
                  onChange={(e) => setFormData({ ...formData, name: e.target.value })}
                  required
                  className="w-full px-4 py-3 rounded-[10px] border border-gray-300 focus:border-[#2563EB] focus:outline-none focus:ring-2 focus:ring-[#2563EB]/20"
                  placeholder="您的姓名 Your name"
                />
              </div>
              
              <div>
                <label htmlFor="email" className="block mb-2 text-[#0F172A]">
                  Email / Line ID
                </label>
                <Input
                  id="email"
                  type="text"
                  value={formData.email}
                  onChange={(e) => setFormData({ ...formData, email: e.target.value })}
                  required
                  className="w-full px-4 py-3 rounded-[10px] border border-gray-300 focus:border-[#2563EB] focus:outline-none focus:ring-2 focus:ring-[#2563EB]/20"
                  placeholder="your@email.com 或 Line ID"
                />
              </div>
              
              <div>
                <label htmlFor="message" className="block mb-2 text-[#0F172A]">
                  訊息 Message
                </label>
                <Textarea
                  id="message"
                  value={formData.message}
                  onChange={(e) => setFormData({ ...formData, message: e.target.value })}
                  required
                  rows={5}
                  className="w-full px-4 py-3 rounded-[10px] border border-gray-300 focus:border-[#2563EB] focus:outline-none focus:ring-2 focus:ring-[#2563EB]/20 resize-none"
                  placeholder="請告訴我您的專案... Tell me about your project..."
                />
              </div>
              
              <Button
                type="submit"
                disabled={loading}
                className="w-full bg-[#2563EB] hover:bg-[#3B82F6] text-white px-4 py-4 rounded-[10px] disabled:opacity-50"
              >
                {loading ? '傳送中... Sending...' : '傳送訊息 Send Message'}
              </Button>
            </form>
          )}
        </div>
      </div>
    </section>
  );
}
