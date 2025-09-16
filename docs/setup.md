# Template Setup Guide

This guide will help you set up and customize the SaaS Automation Platform template for your project.

## 🚀 Quick Start

### 1. Clone the Template

```bash
git clone <template-repository-url> my-saas-project
cd my-saas-project
```

### 2. Run the Initialization Script

```bash
chmod +x scripts/init-template.sh
./scripts/init-template.sh
```

This script will:
- Update package names and project information
- Generate secure secret keys
- Create environment files
- Install dependencies
- Initialize git repository

### 3. Manual Configuration

After running the initialization script, review and update:

#### Environment Variables (`.env`)
- Database connection strings
- API keys (OpenAI, Anthropic, etc.)
- SAP system endpoints
- Email configuration
- Monitoring services (Sentry, etc.)

#### Project Customization
- Update `README.md` with your project details
- Modify the landing page content in `apps/frontend/src/app/page.tsx`
- Update the project logo and branding
- Configure authentication providers

## 🏗️ Development Setup

### Prerequisites

- Node.js 18+
- Python 3.11+
- Docker & Docker Compose
- PostgreSQL 15+
- Redis 7+

### Local Development

1. **Start all services:**
   ```bash
   npm run dev
   ```

2. **Access the application:**
   - Frontend: http://localhost:3004
   - Backend API: http://localhost:8000
   - API Documentation: http://localhost:8000/docs

### Database Setup

1. **Run migrations:**
   ```bash
   npm run db:migrate
   ```

2. **Seed initial data:**
   ```bash
   npm run db:seed
   ```

## 📦 Project Structure Customization

### Adding New Packages

1. Create a new package directory in `packages/`
2. Add `package.json` with workspace configuration
3. Update root `package.json` workspaces array
4. Add build scripts to `turbo.json`

### Adding New Apps

1. Create a new app directory in `apps/`
2. Configure build and dev scripts
3. Update Docker Compose if needed
4. Add CI/CD configuration

## 🔧 Configuration

### Turborepo

The template uses Turborepo for monorepo management. Key files:
- `turbo.json` - Build pipeline configuration
- `package.json` - Workspace configuration

### TypeScript

Shared TypeScript configuration:
- Root `tsconfig.json` for references
- Package-specific configs extend base config
- Shared types in `packages/shared-types`

### Linting & Formatting

- ESLint configuration in `.eslintrc.json`
- Prettier configuration in `.prettierrc.json`
- Husky pre-commit hooks
- Lint-staged for staged files only

## 🧪 Testing

### Frontend Testing
```bash
npm run test
```

### Backend Testing
```bash
cd apps/backend
pytest
```

### End-to-End Testing
```bash
npm run test:e2e
```

## 🚢 Deployment

### Environment Setup

1. **Staging:**
   ```bash
   npm run build
   npm run deploy:staging
   ```

2. **Production:**
   ```bash
   git tag v1.0.0
   git push origin v1.0.0
   ```

### Docker Deployment

```bash
docker-compose -f docker-compose.prod.yml up -d
```

### Kubernetes Deployment

Update the manifests in `infra/kubernetes/` and apply:

```bash
kubectl apply -f infra/kubernetes/
```

## 🔐 Security

### Environment Secrets

Never commit sensitive data. Use:
- Environment variables for configuration
- Secret management systems for production
- `.env.example` as a template

### Security Checklist

- [ ] Update default secret keys
- [ ] Configure CORS origins
- [ ] Set up authentication
- [ ] Enable HTTPS in production
- [ ] Configure security headers
- [ ] Set up monitoring and alerting

## 📚 Additional Resources

- [API Documentation](./api.md)
- [Frontend Development](./frontend.md)
- [Backend Development](./backend.md)
- [Agent Development](./agents.md)
- [Deployment Guide](./deployment.md)
- [Contributing Guidelines](./contributing.md)

## 🆘 Troubleshooting

### Common Issues

1. **Port conflicts:**
   - The dev server automatically finds available ports
   - Check for processes using ports 3000-3004, 8000

2. **TypeScript errors:**
   - Run `npm run type-check` to identify issues
   - Ensure all packages are built: `npm run build`

3. **Database connection:**
   - Verify PostgreSQL is running
   - Check DATABASE_URL in `.env`
   - Run migrations: `npm run db:migrate`

4. **Package resolution:**
   - Clear node_modules: `rm -rf node_modules && npm install`
   - Clear Turbo cache: `npx turbo clean`

## 📞 Support

- Create issues in the repository
- Check existing documentation
- Review the example implementations
