# AI Agent Organization

This repository contains a Hermes-style AI agent foundation with:
- backend orchestration service
- API layer
- MCP server
- Ollama integration
- SOUL and SKILL documents

## Architecture

- `backend/` hosts the core reasoning and LLM orchestration service.
- `api/` exposes an HTTP API for the organization-facing interface.
- `mcp-server/` provides the Model Context Protocol server tools.
- `docs/` contains the operating identity and capability definition.

## Quick start

```bash
docker compose up --build
```

Then verify:
- API: http://localhost:8000/health
- Backend: http://localhost:8001/health
- MCP: http://localhost:9000/health

## Ollama setup

Install and start Ollama locally, then pull a model:

```bash
ollama pull llama3.1
```

## Notes

This is a starter scaffold. You can extend it with:
- PostgreSQL
- Redis
- vector memory
- scheduling or workers
- auth and role management
- dashboards or admin consoles
