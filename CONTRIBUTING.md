# Contributing to SaaS Automation Platform

Thank you for your interest in contributing to our SaaS Automation Platform! This document provides guidelines and information for contributors.

## 🚀 Getting Started

### Prerequisites

- Node.js 18+ and npm
- Python 3.11+
- Docker and Docker Compose
- Git

### Development Setup

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd saas-automation-platform
   ```

2. **Install dependencies**
   ```bash
   npm install
   ```

3. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

4. **Start development servers**
   ```bash
   npm run dev
   ```

## 📝 Development Guidelines

### Code Style

- **TypeScript**: Use strict TypeScript for all frontend code
- **Python**: Follow PEP 8 guidelines for backend code
- **Formatting**: Prettier and ESLint are configured - run `npm run lint:fix`
- **Commits**: Use conventional commit messages

### Branch Strategy

- `main`: Production-ready code
- `develop`: Development branch
- `feature/*`: Feature branches
- `bugfix/*`: Bug fix branches
- `hotfix/*`: Critical fixes

### Commit Messages

Use conventional commit format:
```
type(scope): description

[optional body]

[optional footer]
```

Types: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`

Examples:
- `feat(frontend): add user authentication`
- `fix(api): resolve database connection issue`
- `docs(readme): update installation instructions`

## 🧪 Testing

### Frontend Tests
```bash
cd apps/frontend
npm test
```

### Backend Tests
```bash
cd apps/backend
python -m pytest
```

### Integration Tests
```bash
npm run test:integration
```

## 📦 Package Structure

```
apps/
├── frontend/          # Next.js application
├── backend/           # FastAPI application
└── agent-services/    # AI agent services

packages/
├── shared-types/      # Shared TypeScript types
├── ui/               # Shared UI components
├── utils/            # Shared utilities
└── sdk/              # API SDK
```

## 🔄 Pull Request Process

1. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes**
   - Write clean, documented code
   - Add tests for new functionality
   - Update documentation as needed

3. **Test your changes**
   ```bash
   npm run test
   npm run lint
   npm run build
   ```

4. **Commit and push**
   ```bash
   git add .
   git commit -m "feat: your feature description"
   git push origin feature/your-feature-name
   ```

5. **Create a Pull Request**
   - Use the PR template
   - Include screenshots for UI changes
   - Link related issues
   - Request review from maintainers

### PR Requirements

- [ ] All tests pass
- [ ] Code follows style guidelines
- [ ] Documentation is updated
- [ ] Changes are backwards compatible
- [ ] Security considerations are addressed

## 🐛 Bug Reports

When reporting bugs, please include:

- **Environment**: OS, Node.js version, browser
- **Steps to reproduce**: Clear, numbered steps
- **Expected behavior**: What should happen
- **Actual behavior**: What actually happens
- **Screenshots**: If applicable
- **Additional context**: Any other relevant information

## 💡 Feature Requests

For feature requests, please:

- Search existing issues first
- Use the feature request template
- Provide clear use cases
- Consider implementation complexity
- Discuss with maintainers before large changes

## 🏗️ Architecture Guidelines

### Frontend (Next.js)

- Use App Router for new pages
- Implement proper error boundaries
- Follow React best practices
- Use TypeScript strictly
- Optimize for performance

### Backend (FastAPI)

- Use async/await for I/O operations
- Implement proper error handling
- Follow REST API conventions
- Use Pydantic for data validation
- Document APIs with OpenAPI

### AI Agents

- Keep agents modular and focused
- Implement proper error handling
- Use structured logging
- Follow security best practices
- Document agent capabilities

## 🔒 Security

- Never commit secrets or API keys
- Use environment variables for configuration
- Follow OWASP security guidelines
- Report security issues privately
- Keep dependencies updated

## 📚 Documentation

- Update README.md for significant changes
- Document new APIs and components
- Include code examples
- Keep documentation current
- Use clear, concise language

## 🤝 Code of Conduct

- Be respectful and inclusive
- Provide constructive feedback
- Help newcomers learn
- Follow project guidelines
- Maintain professional communication

## ❓ Getting Help

- **Issues**: Create a GitHub issue
- **Discussions**: Use GitHub Discussions
- **Documentation**: Check the docs/ folder
- **Examples**: See the examples/ folder

## 🏆 Recognition

Contributors are recognized in:
- CONTRIBUTORS.md file
- Release notes
- Community highlights

Thank you for contributing to making SaaS automation better! 🚀
