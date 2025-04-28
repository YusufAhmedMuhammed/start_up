# SaaS Agency Platform

A professional SaaS agency platform built with Next.js, FastAPI, and PostgreSQL.

## Project Structure

```
├── frontend/                 # Next.js frontend application
│   ├── src/
│   │   ├── components/      # Reusable UI components
│   │   ├── pages/          # Next.js pages and API routes
│   │   ├── styles/         # Global styles and Tailwind config
│   │   ├── utils/          # Utility functions
│   │   ├── types/          # TypeScript type definitions
│   │   ├── hooks/          # Custom React hooks
│   │   ├── context/        # React context providers
│   │   └── config/         # Frontend configuration
│   ├── public/             # Static assets
│   └── package.json        # Frontend dependencies
│
├── backend/                # FastAPI backend application
│   ├── app/
│   │   ├── api/           # API routes and endpoints
│   │   ├── core/          # Core application logic
│   │   ├── models/        # Database models
│   │   ├── schemas/       # Pydantic schemas
│   │   ├── services/      # Business logic
│   │   ├── utils/         # Utility functions
│   │   └── config/        # Backend configuration
│   ├── tests/             # Backend tests
│   └── requirements.txt   # Python dependencies
│
├── shared/                # Shared code between frontend and backend
│   ├── types/            # Shared TypeScript types
│   └── constants/        # Shared constants
│
└── docker/               # Docker configuration
    ├── frontend/
    ├── backend/
    └── database/
```

## Getting Started

### Prerequisites

- Node.js (v18 or higher)
- Python (v3.9 or higher)
- PostgreSQL (v14 or higher)
- Docker (optional)

### Installation

1. Clone the repository
2. Install frontend dependencies:
   ```bash
   cd frontend
   npm install
   ```
3. Install backend dependencies:
   ```bash
   cd backend
   pip install -r requirements.txt
   ```
4. Set up environment variables (see .env.example files)
5. Start the development servers:
   - Frontend: `npm run dev`
   - Backend: `uvicorn app.main:app --reload`

## Development

- Frontend runs on http://localhost:3000
- Backend runs on http://localhost:8000
- API documentation available at http://localhost:8000/docs

## License

MIT 