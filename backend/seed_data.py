"""Seed initial data for landing page."""

import os
import sys

import django

# Setup Django
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

from landing_page.models import PortfolioProject, PricingPlan, Service

# Clear existing data
Service.objects.all().delete()
PortfolioProject.objects.all().delete()
PricingPlan.objects.all().delete()

# Seed Services
services = [
    {
        "icon": "Globe",
        "title": "企業網站 Business Website",
        "description": "為您打造乾淨、現代化的網站，針對行動裝置和本地客戶進行優化。A clean and modern website optimized for mobile and local customers.",
        "order": 1,
    },
    {
        "icon": "Zap",
        "title": "著陸頁 Landing Page",
        "description": "高轉換率的著陸頁，適用於促銷、產品和服務。High-conversion landing pages for promotions, products, and services.",
        "order": 2,
    },
    {
        "icon": "Bot",
        "title": "AI 自動回覆 AI Auto-Responder",
        "description": "語音或聊天助理，用於訂單處理和客戶支援。Voice or chat assistant for order handling and customer support.",
        "order": 3,
    },
]

for service in services:
    Service.objects.create(**service)
print(f"Created {len(services)} services")

# Seed Portfolio Projects
projects = [
    {
        "title": "肉品店示範 Meat Shop Demo",
        "category": "網路商店 Online Store",
        "description": "產品目錄、分類、行動裝置友善介面。Product catalog, categories, mobile-ready UI.",
        "image": "https://images.unsplash.com/photo-1632154023554-c2975e9be348?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w3Nzg4Nzd8MHwxfHNlYXJjaHwxfHxidXRjaGVyJTIwbWVhdCUyMHNob3B8ZW58MXx8fHwxNzYzNzg3OTc0fDA&ixlib=rb-4.1.0&q=80&w=1080",
        "order": 1,
    },
    {
        "title": "圖瓦媒體入口 Tuvan Media Portal",
        "category": "新聞網站 News Website",
        "description": "分類、版面系統、預覽卡片。Categories, layout system, preview cards.",
        "image": "https://images.unsplash.com/photo-1722684768315-11fc753354f6?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w3Nzg4Nzd8MHwxfHNlYXJjaHwxfHxuZXdzJTIwbWVkaWElMjBwb3J0YWx8ZW58MXx8fHwxNzYzNzg3OTc0fDA&ixlib=rb-4.1.0&q=80&w=1080",
        "order": 2,
    },
    {
        "title": "AI 廚房助理 AI Kitchen Assistant",
        "category": "AI 解決方案 AI Solution",
        "description": "AI 訂餐助理示範。Demo of AI order-taking assistant.",
        "image": "https://images.unsplash.com/photo-1757310998437-b2e8a7bd2e97?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w3Nzg4Nzd8MHwxfHNlYXJjaHwxfHxBSSUyMGNoYXRib3QlMjBhc3Npc3RhbnR8ZW58MXx8fHwxNzYzNzMwNzI4fDA&ixlib=rb-4.1.0&q=80&w=1080",
        "order": 3,
    },
]

for project in projects:
    PortfolioProject.objects.create(**project)
print(f"Created {len(projects)} portfolio projects")

# Seed Pricing Plans
pricing_plans = [
    {
        "name_zh": "基礎方案",
        "name_en": "Basic Plan",
        "description_zh": "適合小型企業的靜態網站解決方案",
        "description_en": "Perfect static website solution for small businesses",
        "price_one_time": 5000,
        "price_monthly": None,
        "billing_period": "one_time",
        "is_highlighted": False,
        "cta_text_zh": "立即開始",
        "cta_text_en": "Get Started",
        "order": 1,
        "features": [
            {"name_zh": "HTML 靜態網站", "name_en": "HTML static website", "included": True},
            {"name_zh": "響應式設計", "name_en": "Responsive design", "included": True},
            {"name_zh": "聯絡表單", "name_en": "Contact form", "included": True},
            {"name_zh": "基本 SEO 優化", "name_en": "Basic SEO optimization", "included": True},
            {"name_zh": "後台管理系統", "name_en": "Admin panel", "included": False},
            {"name_zh": "資料庫整合", "name_en": "Database integration", "included": False},
            {"name_zh": "雲端主機託管", "name_en": "Cloud hosting", "included": False},
            {"name_zh": "每月維護", "name_en": "Monthly maintenance", "included": False},
        ],
    },
    {
        "name_zh": "進階方案",
        "name_en": "Advanced Plan",
        "description_zh": "全功能網站應用程式，含後台管理與雲端託管",
        "description_en": "Full-featured web application with admin panel and cloud hosting",
        "price_one_time": 15000,
        "price_monthly": 3000,
        "billing_period": "both",
        "is_highlighted": True,
        "cta_text_zh": "立即升級",
        "cta_text_en": "Get Started",
        "order": 2,
        "features": [
            {"name_zh": "Django 後端框架", "name_en": "Django backend framework", "included": True},
            {"name_zh": "PostgreSQL 資料庫", "name_en": "PostgreSQL database", "included": True},
            {"name_zh": "後台管理系統", "name_en": "Admin panel", "included": True},
            {"name_zh": "AWS 雲端主機", "name_en": "AWS cloud hosting", "included": True},
            {"name_zh": "SSL 安全憑證", "name_en": "SSL certificate", "included": True},
            {"name_zh": "每月維護與更新", "name_en": "Monthly maintenance & updates", "included": True},
            {"name_zh": "優先技術支援", "name_en": "Priority support", "included": True},
            {"name_zh": "自訂功能開發", "name_en": "Custom feature development", "included": True},
        ],
    },
]

for plan in pricing_plans:
    PricingPlan.objects.create(**plan)
print(f"Created {len(pricing_plans)} pricing plans")

print("\nSeed complete!")
