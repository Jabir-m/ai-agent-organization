# AI Agent Organization

A Hermes-style organization agent platform with:
- backend orchestration service
- API gateway
- MCP tool server
- Postgres + Redis state
- Ollama LLM integration
- lightweight frontend dashboard
- SOUL and SKILL documents

## Architecture

- `backend/` orchestrates planning, task routing, and LLM reasoning.
- `api/` exposes HTTP access for the organization and dashboard.
- `mcp-server/` exposes MCP-compatible tool functions and execution endpoints.
- `frontend/` provides a dashboard for goals, tasks, and service health.
- `database/` contains PostgreSQL initialization scripts.

## Quick start

```bash
docker compose up --build
```

Then open:
- API: http://localhost:8000
- Backend: http://localhost:8001/docs
- MCP Server: http://localhost:9000/docs
- Dashboard: http://localhost:5173

## Local backend flow

The API is the public entrypoint for the frontend. It proxies planning and task requests to the backend service.

## Health checks

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

This project is intentionally structured as a strong starter foundation for a multi-agent organization platform. It can be extended with authentication, role-based access, durable memory, work queues, and production observability.
