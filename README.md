# AI Agent Organization

A Hermes-style organization agent platform with:
- backend orchestration service
- API gateway
- MCP tool server
- Postgres + Redis state
- Ollama LLM integration
- lightweight frontend dashboard
- operating documents for SOUL and SKILL

## Architecture

- `backend/` orchestrates planning, task routing, and LLM reasoning.
- `api/` exposes HTTP access for the organization and dashboard.
- `mcp-server/` exposes MCP-compatible tool functions and execution endpoints.
- `frontend/` provides a simple dashboard for goals, tasks, and service health.
- `database/` contains initialization scripts for Postgres.

## Features

- Hermes-inspired operating identity
- Task planning and execution workflow
- MCP tool registry
- Ollama-based reasoning for agent responses
- Postgres persistence for organization state
- Redis for caching and fast coordination
- dashboard UI for monitoring agent health and tasks

## Quick start

```bash
docker compose up --build
```

Then open:
- API: http://localhost:8000
- Backend: http://localhost:8001/docs
- MCP Server: http://localhost:9000/docs
- Dashboard: http://localhost:5173

## Service health checks

```bash
curl http://localhost:8000/health
curl http://localhost:8001/health
curl http://localhost:9000/health
```

## Ollama setup

```bash
ollama pull llama3.1
```

## Notes

This project is intended as a strong starter foundation for a company-grade AI orchestration layer. It can be extended with authentication, workflows, multi-agent team roles, and production observability.
