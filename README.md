# CloudDrop — Secure Cloud File Storage Platform

A file upload/storage app deployed on AWS: EC2 + Nginx (app), S3 (files), RDS PostgreSQL (metadata), IAM roles for access, GitHub Actions for CI/CD.

## Architecture
See `docs/architecture.md`.

## Tech stack
- Flask (API)
- Nginx (reverse proxy)
- AWS EC2, S3, RDS PostgreSQL, IAM
- GitHub Actions (CI/CD)

## Local setup
1. Clone the repo and create a branch (see "Git workflow" below).
2. `python -m venv venv && source venv/bin/activate`
3. `pip install -r requirements.txt`
4. Copy `.env.example` to `.env` and fill in real values.
5. `python -m app.main`
6. Visit `http://localhost:5000/health` — should return `{"status": "ok"}`.

## Environment variables
See `.env.example`. Never commit a real `.env` file (it's already git-ignored).

## Team roles
| Member | Owns | Branch |
|---|---|---|
| A | EC2 + Nginx setup | `feature/ec2-nginx-setup` |
| B | S3 upload/download logic (`app/upload.py`) | `feature/s3-upload` |
| C | RDS models + auth (`app/models.py`, `app/auth.py`) | `feature/rds-metadata-auth` |
| D | CI/CD + sharing links (`.github/workflows/deploy.yml`) | `feature/cicd-sharing-links` |

Each file with a `# TODO(Member X):` comment is that member's task. Don't edit another member's TODO file — open an issue instead if something needs to change.

## Git workflow (required for grading)
1. `git checkout -b <your-branch-name>` (from the table above)
2. Make commits as you go — small, frequent commits are better than one giant commit
3. `git push origin <your-branch-name>`
4. Open a Pull Request into `main`
5. Get it reviewed and merged

This is what generates the branch/PR/commit history the assessment checks for.

## Health check
`GET /health` → `{"status": "ok"}` — used by load balancers/monitoring and required by the assignment.

## Troubleshooting
- **App won't start**: check `.env` exists and all variables are set.
- **S3 access denied**: EC2 must have an IAM role attached (not hardcoded keys) with `s3:PutObject`/`s3:GetObject` on the bucket.
- **DB connection refused**: check RDS security group allows inbound from the EC2 security group on port 5432.
- **502 from Nginx**: confirm the Flask app is running on the port Nginx proxies to (see `nginx/clouddrop.conf`).
