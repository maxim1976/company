"""Seed initial data for landing page."""

import os
import sys

import django

# Setup Django
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

from landing_page.models import PortfolioProject, Service

# Clear existing data
Service.objects.all().delete()
PortfolioProject.objects.all().delete()

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

print("\nSeed complete!")
