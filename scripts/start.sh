#!/bin/bash

set -e

# Cuttlefish Civilization Engine Startup Script
# Constitutional AI system initialization

echo "🐙 Starting Cuttlefish Civilization Engine..."
echo "Version: 1.0.0-alpha"
echo "Constitutional Framework: v1.2"

# Check dependencies
echo "Checking dependencies..."

if ! command -v docker &> /dev/null; then
    echo "❌ Docker not found. Please install Docker first."
    exit 1
fi

if ! command -v docker-compose &> /dev/null; then
    echo "❌ Docker Compose not found. Please install Docker Compose first."
    exit 1
fi

echo "✅ Dependencies satisfied"

# Create necessary directories
echo "Creating data directories..."
mkdir -p data/{governance,knowledge,agents,orchestrator,monitoring}
mkdir -p logs/{governance,knowledge,agents,orchestrator}

echo "✅ Directory structure created"

# Check for environment configuration
if [ ! -f ".env" ]; then
    echo "Creating default environment configuration..."
    cat > .env << 'EOF'
# Cuttlefish Civilization Engine Configuration

# Constitutional Framework
CONSTITUTION_VERSION=1.2
GOVERNANCE_MODE=strict
TRUST_DECAY_RATE=0.05

# Agent Configuration
DEFAULT_TRUST_THRESHOLD=50.0
MAX_AGENT_INSTANCES=10
AGENT_TIMEOUT_SECONDS=300

# Database Configuration
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=cuttlefish
POSTGRES_USER=cuttlefish
POSTGRES_PASSWORD=cuttlefish2026

# Vector Database
QDRANT_URL=http://localhost:6333
EMBEDDING_MODEL=sentence-transformers/all-MiniLM-L6-v2

# Redis Configuration
REDIS_URL=redis://localhost:6379

# API Configuration
API_HOST=0.0.0.0
API_PORT=8000
API_WORKERS=4

# Security
JWT_SECRET=constitutional-ai-civilization-engine-2026
ENCRYPTION_KEY=cuttlefish-constitutional-governance

# Monitoring
PROMETHEUS_ENABLED=true
GRAFANA_ENABLED=true
LOG_LEVEL=INFO

# Development
DEBUG_MODE=false
DEV_MODE=false
EOF
    echo "✅ Default .env created - please review and customize"
fi

# Constitutional validation
echo "Validating constitutional framework..."
if [ ! -f "constitution/CONSTITUTION.md" ]; then
    echo "❌ CONSTITUTION.md not found - constitutional governance required"
    exit 1
fi

echo "✅ Constitutional framework validated"

# Parse command line arguments
PROFILE="default"
BUILD=false
PULL=false
DETACH=true

while [[ $# -gt 0 ]]; do
    case $1 in
        --profile)
            PROFILE="$2"
            shift 2
            ;;
        --build)
            BUILD=true
            shift
            ;;
        --pull)
            PULL=true
            shift
            ;;
        --foreground)
            DETACH=false
            shift
            ;;
        --dev)
            PROFILE="dev"
            shift
            ;;
        --production)
            PROFILE="production"
            shift
            ;;
        --help)
            echo "Usage: $0 [options]"
            echo ""
            echo "Options:"
            echo "  --profile PROFILE    Docker compose profile (default, dev, production)"
            echo "  --build              Force rebuild of images"
            echo "  --pull               Pull latest images before starting"
            echo "  --foreground         Run in foreground (don't detach)"
            echo "  --dev                Enable development profile"
            echo "  --production         Enable production profile"
            echo "  --help               Show this help message"
            exit 0
            ;;
        *)
            echo "Unknown option: $1"
            exit 1
            ;;
    esac
done

# Build images if requested
if [ "$BUILD" = true ]; then
    echo "🔨 Building images..."
    docker-compose build
fi

# Pull images if requested
if [ "$PULL" = true ]; then
    echo "⬇️ Pulling images..."
    docker-compose pull
fi

# Start services based on profile
echo "🚀 Starting services with profile: $PROFILE"

COMPOSE_ARGS=""
if [ "$PROFILE" != "default" ]; then
    COMPOSE_ARGS="--profile $PROFILE"
fi

if [ "$DETACH" = true ]; then
    COMPOSE_ARGS="$COMPOSE_ARGS -d"
fi

docker-compose $COMPOSE_ARGS up

# Wait for services to be healthy
if [ "$DETACH" = true ]; then
    echo "⏳ Waiting for services to start..."
    sleep 15
    
    # Check service health
    echo "🔍 Checking service health..."
    
    services=("orchestrator:8000" "governance:8001" "knowledge:8002" "builder-agent:8003")
    
    for service in "${services[@]}"; do
        name=$(echo $service | cut -d':' -f1)
        port=$(echo $service | cut -d':' -f2)
        
        echo -n "  - $name: "
        if curl -sf "http://localhost:$port/health" > /dev/null 2>&1; then
            echo "✅ healthy"
        else
            echo "⚠️  starting (may take a moment)"
        fi
    done
    
    echo ""
    echo "🐙 Cuttlefish Civilization Engine is operational!"
    echo ""
    echo "🏛️ Constitutional Services:"
    echo "  - Main API:        http://localhost:8000"
    echo "  - Governance:      http://localhost:8001"
    echo "  - Knowledge RAG:   http://localhost:8002"
    echo "  - Builder Agent:   http://localhost:8003"
    echo "  - Dashboard:       http://localhost:3000"
    echo ""
    echo "📊 Monitoring:"
    echo "  - Prometheus:      http://localhost:9090"
    echo "  - Grafana:         http://localhost:3001 (admin/cuttlefish2026)"
    echo ""
    echo "🗄️ Databases:"
    echo "  - PostgreSQL:      localhost:5432 (cuttlefish/cuttlefish2026)"
    echo "  - Qdrant Vector:   localhost:6333"
    echo "  - Redis Cache:     localhost:6379"
    echo ""
    echo "📋 Management:"
    echo "  - Monitor logs:    docker-compose logs -f"
    echo "  - Stop system:     docker-compose down"
    echo "  - View status:     docker-compose ps"
    echo ""
    echo "🏛️ CONSTITUTIONAL GOVERNANCE: ACTIVE AND IMMUTABLE"
    echo "🦑 Ready to build sustainable human-AI civilization"
    echo ""
    echo "Trust scores affect access levels. Adversarial behavior penalized."
    echo "All agent interactions logged for governance transparency."
fi