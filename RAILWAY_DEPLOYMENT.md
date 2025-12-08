# Railway Deployment Guide

## Project Overview
Django 6.0 + Django Templates landing page for Studio web design business.

## Prerequisites
- Railway account with PostgreSQL database provisioned
- GitHub repository connected to Railway
- Environment variables configured in Railway dashboard

## Required Environment Variables

Set these in Railway's dashboard under **Variables**:

```
SECRET_KEY=<generate-with-django-command>
DEBUG=False
ALLOWED_HOSTS=your-app.up.railway.app
DATABASE_URL=<auto-provided-by-railway-postgresql>
```

To generate a secure `SECRET_KEY`:
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

## Project Structure

```
studio/
├── backend/
│   ├── core/              # Django settings
│   ├── landing_page/      # Main app
│   ├── static/           # CSS, JS
│   ├── templates/        # Django templates
│   └── manage.py
├── pyproject.toml        # Dependencies (Railway auto-detects this)
├── railway.toml          # Railway configuration
├── Procfile              # Process definition (backup)
└── .env.example          # Environment variable template
```

## Deployment Configuration

### railway.toml
```toml
[deploy]
startCommand = "cd backend && python manage.py migrate && python manage.py collectstatic --noinput && gunicorn core.wsgi --bind 0.0.0.0:$PORT"
```

**Key points:**
- Railway auto-detects Python from `pyproject.toml`
- No `nixpacks.toml` needed (causes conflicts)
- Migrations run on startup (database available)
- Static files collected on startup
- Gunicorn binds to Railway's `$PORT`

### Procfile (backup method)
```
web: cd backend && gunicorn core.wsgi --bind 0.0.0.0:$PORT
```

## Common Issues & Solutions

### Issue 1: "ModuleNotFoundError: No module named 'django'"
**Cause:** Virtual environment not activated or dependencies not installed

**Solution:** 
- Railway auto-installs from `pyproject.toml`
- Ensure `railway.toml` doesn't override install phase
- Remove `nixpacks.toml` if present

### Issue 2: "TemplateDoesNotExist: index.html"
**Cause:** Static files not collected or TEMPLATES path misconfigured

**Solution:**
- Add `collectstatic --noinput` to start command
- Verify `TEMPLATES['DIRS']` in `settings.py`:
  ```python
  TEMPLATES = [{
      'DIRS': [BACKEND_DIR / 'templates'],
  }]
  ```

### Issue 3: "pip: command not found" or "uv: command not found"
**Cause:** Trying to manually install package managers in build phase

**Solution:**
- **DO NOT** create `nixpacks.toml`
- Let Railway auto-detect Python and use its built-in pip
- Railway handles dependency installation automatically

### Issue 4: Build succeeds but app crashes on startup
**Cause:** Database not available during migrations

**Solution:**
- Migrations should run in `startCommand`, not build phase
- Ensure PostgreSQL service is linked to your app
- Check DATABASE_URL is set correctly

### Issue 5: Static files not loading
**Cause:** Whitenoise not configured or collectstatic not run

**Solution:**
- Ensure in `settings.py`:
  ```python
  MIDDLEWARE = [
      'whitenoise.middleware.WhiteNoiseMiddleware',  # After SecurityMiddleware
      ...
  ]
  STATIC_ROOT = BACKEND_DIR / 'staticfiles'
  STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
  ```
- Run collectstatic in start command

## Deployment Steps

1. **Push to GitHub**
   ```bash
   git add .
   git commit -m "Deploy to Railway"
   git push
   ```

2. **Railway auto-deploys** when it detects changes on `main` branch

3. **Monitor logs** in Railway dashboard:
   - Build Logs: Check dependency installation
   - Deploy Logs: Check migrations and startup
   - HTTP Logs: Check requests and errors

4. **First deployment only:** Seed data and create superuser
   ```bash
   # Run in Railway's shell or locally connected to Railway DB
   python backend/seed_data.py
   python backend/manage.py createsuperuser
   ```

## Database Connection

### Production (Railway)
DATABASE_URL is automatically set by Railway PostgreSQL service.

### Local Development (Connected to Railway DB)
Get the public connection URL from Railway PostgreSQL variables and add to `.env`:
```
DATABASE_URL=postgresql://postgres:password@host.railway.app:port/railway
```

## Verifying Deployment

1. **Check homepage:** `https://your-app.up.railway.app/`
2. **Check admin:** `https://your-app.up.railway.app/admin/`
3. **Test contact form:** Submit from homepage
4. **Check admin logs:** View submissions in admin panel

## Troubleshooting Commands

Run these in Railway's shell (Settings → Deploy → Shell):

```bash
# Check Django installation
python -c "import django; print(django.VERSION)"

# Check database connection
python backend/manage.py dbshell

# Run migrations manually
python backend/manage.py migrate

# Collect static files manually
python backend/manage.py collectstatic --noinput

# Create superuser
python backend/manage.py createsuperuser
```

## Best Practices

✅ **DO:**
- Use Railway's auto-detection (no custom buildpacks)
- Keep `railway.toml` minimal
- Run migrations in start command
- Use environment variables for secrets
- Use Whitenoise for static files
- Monitor Railway logs regularly

❌ **DON'T:**
- Create `nixpacks.toml` (causes conflicts)
- Hardcode SECRET_KEY or DATABASE_URL
- Run migrations in build phase
- Use custom Python installation scripts
- Ignore Railway's build warnings

## Support Resources

- [Railway Docs](https://docs.railway.app/)
- [Django Deployment Checklist](https://docs.djangoproject.com/en/6.0/howto/deployment/checklist/)
- [Whitenoise Documentation](http://whitenoise.evans.io/)

---

Last updated: December 8, 2025
