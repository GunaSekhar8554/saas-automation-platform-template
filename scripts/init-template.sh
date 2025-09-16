#!/bin/bash

# Template Initialization Script
# This script helps customize the template for a new project

set -e

echo "🚀 Initializing SaaS Automation Platform Template..."

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Check if required tools are installed
check_requirements() {
    print_status "Checking requirements..."
    
    if ! command -v node &> /dev/null; then
        print_error "Node.js is not installed. Please install Node.js 18+ and try again."
        exit 1
    fi
    
    if ! command -v python3 &> /dev/null; then
        print_error "Python 3 is not installed. Please install Python 3.11+ and try again."
        exit 1
    fi
    
    if ! command -v docker &> /dev/null; then
        print_warning "Docker is not installed. You'll need Docker for local development."
    fi
    
    print_status "Requirements check completed ✓"
}

# Collect project information
collect_project_info() {
    print_status "Let's customize your project..."
    
    read -p "Enter your project name (e.g., 'my-saas-platform'): " PROJECT_NAME
    read -p "Enter your project description: " PROJECT_DESCRIPTION
    read -p "Enter your organization/username (for Docker images): " ORG_NAME
    read -p "Enter your email: " AUTHOR_EMAIL
    read -p "Enter your name: " AUTHOR_NAME
    
    # Set defaults if empty
    PROJECT_NAME=${PROJECT_NAME:-"my-saas-platform"}
    PROJECT_DESCRIPTION=${PROJECT_DESCRIPTION:-"SaaS automation platform"}
    ORG_NAME=${ORG_NAME:-"myorg"}
    AUTHOR_EMAIL=${AUTHOR_EMAIL:-"admin@example.com"}
    AUTHOR_NAME=${AUTHOR_NAME:-"Admin"}
}

# Update package.json files
update_package_json() {
    print_status "Updating package.json files..."
    
    # Root package.json
    sed -i.bak "s/\"saas-automation-platform\"/\"$PROJECT_NAME\"/g" package.json
    sed -i.bak "s/\"SaaS automation platform for PI\/PO-to-SAP BTP Integration Suite migration using AI agents\"/\"$PROJECT_DESCRIPTION\"/g" package.json
    sed -i.bak "s/\"Your Company\"/\"$AUTHOR_NAME\"/g" package.json
    
    # Frontend package.json
    sed -i.bak "s/\"@saas-platform\/frontend\"/\"@${ORG_NAME}\/frontend\"/g" apps/frontend/package.json
    
    # Package names in other files
    find packages -name "package.json" -exec sed -i.bak "s/@saas-platform/@${ORG_NAME}/g" {} \;
    
    print_status "Package.json files updated ✓"
}

# Update README
update_readme() {
    print_status "Updating README..."
    
    sed -i.bak "s/# SaaS Automation Platform/# $PROJECT_NAME/g" README.md
    sed -i.bak "s/A comprehensive SaaS automation platform focused on PI\/PO-to-SAP BTP Integration Suite migration using AI agents and agentic stack architecture./$PROJECT_DESCRIPTION/g" README.md
    sed -i.bak "s/support@yourcompany.com/$AUTHOR_EMAIL/g" README.md
    
    print_status "README updated ✓"
}

# Update environment files
update_env_files() {
    print_status "Updating environment files..."
    
    # Generate random secret keys
    SECRET_KEY=$(openssl rand -base64 32)
    JWT_SECRET_KEY=$(openssl rand -base64 32)
    
    sed -i.bak "s/your-super-secret-key-change-in-production/$SECRET_KEY/g" .env.example
    sed -i.bak "s/your-jwt-secret-key-change-in-production/$JWT_SECRET_KEY/g" .env.example
    
    # Create actual .env file
    cp .env.example .env
    
    print_status "Environment files updated ✓"
}

# Clean up backup files
cleanup() {
    print_status "Cleaning up..."
    find . -name "*.bak" -delete
    print_status "Cleanup completed ✓"
}

# Install dependencies
install_dependencies() {
    print_status "Installing dependencies..."
    npm install
    print_status "Dependencies installed ✓"
}

# Initialize git repository
init_git() {
    if [ ! -d ".git" ]; then
        print_status "Initializing git repository..."
        git init
        git add .
        git commit -m "Initial commit from SaaS automation platform template"
        print_status "Git repository initialized ✓"
    else
        print_status "Git repository already exists, skipping initialization"
    fi
}

# Main execution
main() {
    echo -e "${BLUE}"
    echo "╔══════════════════════════════════════════════════════════════╗"
    echo "║                 SaaS Automation Platform                      ║"
    echo "║                    Template Initializer                       ║"
    echo "╚══════════════════════════════════════════════════════════════╝"
    echo -e "${NC}"
    
    check_requirements
    collect_project_info
    update_package_json
    update_readme
    update_env_files
    cleanup
    install_dependencies
    init_git
    
    echo ""
    echo -e "${GREEN}🎉 Template initialization completed successfully!${NC}"
    echo ""
    echo "Next steps:"
    echo "1. Review and update the .env file with your specific configuration"
    echo "2. Run 'npm run dev' to start the development server"
    echo "3. Visit http://localhost:3004 to see your application"
    echo "4. Start building your SaaS platform!"
    echo ""
    echo "For more information, see the README.md file."
}

# Run the script
main "$@"
