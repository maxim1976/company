// In production, use relative URL (same origin). In dev, use localhost Django server.
const API_BASE_URL = import.meta.env.PROD 
  ? '/api' 
  : (import.meta.env.VITE_API_URL || 'http://127.0.0.1:8000/api');

export interface Service {
  id: number;
  icon: string;
  title: string;
  description: string;
}

export interface PortfolioProject {
  id: number;
  title: string;
  category: string;
  description: string;
  image: string;
  link: string;
}

export interface ContactFormData {
  name: string;
  email: string;
  message: string;
}

export const api = {
  async getServices(): Promise<Service[]> {
    const response = await fetch(`${API_BASE_URL}/services/`);
    if (!response.ok) throw new Error('Failed to fetch services');
    return response.json();
  },

  async getPortfolio(): Promise<PortfolioProject[]> {
    const response = await fetch(`${API_BASE_URL}/portfolio/`);
    if (!response.ok) throw new Error('Failed to fetch portfolio');
    return response.json();
  },

  async submitContact(data: ContactFormData): Promise<{ message: string }> {
    const response = await fetch(`${API_BASE_URL}/contact/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(data),
    });
    if (!response.ok) throw new Error('Failed to submit contact form');
    return response.json();
  },
};
