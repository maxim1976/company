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
        "description_en": "Perfect static website for small businesses",
        "price_one_time": 3500,
        "price_monthly": None,
        "billing_period": "one_time",
        "plan_type": "basic",
        "sub_note": "<strong>NT$200 / 小時</strong> · 後續更新 site updates",
        "is_highlighted": False,
        "cta_text_zh": "立即開始",
        "cta_text_en": "Get Started",
        "order": 1,
        "features": [
            {"name_zh": "HTML 靜態網站", "name_en": "Plain static HTML website", "included": True},
            {"name_zh": "GitHub Pages 託管", "name_en": "Hosted on GitHub Pages", "included": True},
            {"name_zh": "響應式設計", "name_en": "Responsive design", "included": True},
            {"name_zh": "基本 SEO 優化", "name_en": "Basic SEO optimization", "included": True},
        ],
    },
    {
        "name_zh": "標準方案",
        "name_en": "Standard Plan",
        "description_zh": "動態內容管理，適合成長中的企業",
        "description_en": "Dynamic content management for growing businesses",
        "price_one_time": 5000,
        "price_monthly": None,
        "billing_period": "one_time",
        "plan_type": "standard",
        "sub_note": "<strong>NT$200 / 小時</strong> · 設計變更 design changes",
        "is_highlighted": False,
        "cta_text_zh": "立即開始",
        "cta_text_en": "Get Started",
        "order": 2,
        "features": [
            {"name_zh": "Flask 或 Django 後端", "name_en": "Flask or Django backend", "included": True},
            {"name_zh": "後台管理面板", "name_en": "Admin panel", "included": True},
            {"name_zh": "動態內容更新", "name_en": "Dynamically update content", "included": True},
            {"name_zh": "Railway 雲端託管", "name_en": "Railway cloud hosting", "included": True},
            {"name_zh": "AWS S3 圖片儲存", "name_en": "AWS S3 image storage", "included": True},
            {"name_zh": "響應式設計", "name_en": "Responsive design", "included": True},
            {"name_zh": "基本 SEO 優化", "name_en": "Basic SEO optimization", "included": True},
        ],
    },
    {
        "name_zh": "進階方案",
        "name_en": "Advanced Plan",
        "description_zh": "全功能企業級應用，AI 整合與線上支付",
        "description_en": "Full-featured enterprise app with AI & payments",
        "price_one_time": None,
        "price_monthly": None,
        "billing_period": "both",
        "plan_type": "advanced",
        "sub_note": "月費依規模而定 · monthly fee based on scope",
        "is_highlighted": True,
        "cta_text_zh": "索取報價",
        "cta_text_en": "Get a Quote",
        "order": 3,
        "features": [
            {"name_zh": "Django 後端 + ORM", "name_en": "Django backend with ORM", "included": True},
            {"name_zh": "線上菜單系統", "name_en": "Online menu system", "included": True},
            {"name_zh": "AI 功能整合", "name_en": "AI integration", "included": True},
            {"name_zh": "線上支付系統 (ECPay / Stripe / PayPal)", "name_en": "Online payments", "included": True, "tags": ["ECPay", "Stripe", "PayPal"]},
            {"name_zh": "Railway 雲端託管", "name_en": "Railway cloud hosting", "included": True},
            {"name_zh": "AWS S3 圖片儲存", "name_en": "AWS S3 image storage", "included": True},
            {"name_zh": "後台管理系統", "name_en": "Admin management system", "included": True},
            {"name_zh": "進階 SEO 優化", "name_en": "Advanced SEO optimization", "included": True},
        ],
    },
]

for plan in pricing_plans:
    PricingPlan.objects.create(**plan)
print(f"Created {len(pricing_plans)} pricing plans")

print("\nSeed complete!")
