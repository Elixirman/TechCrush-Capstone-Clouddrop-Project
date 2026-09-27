# CloudDrop architecture

```
Users --> Internet (HTTPS) --> EC2 (Nginx + Flask API, IAM role)
                                        |              \
                                        v               v
                                 S3 (file storage)   RDS PostgreSQL (metadata)

GitHub Actions --> deploys to --> EC2
```

- **Users**: access the app over HTTPS.
- **EC2**: single instance running Nginx (reverse proxy) in front of the Flask API. Uses an IAM role for AWS access — no access keys in code or `.env`.
- **S3**: stores the actual uploaded files.
- **RDS PostgreSQL**: stores file metadata (filename, owner, category, S3 key) and user accounts.
- **GitHub Actions**: builds, tests, and deploys new code to EC2 on every push to `main`.

## Security notes
- IAM role attached to the EC2 instance, scoped to only the S3 bucket and actions it needs.
- Secrets (DB URL, secret key) via environment variables, never committed.
- HTTPS terminated at Nginx (or an ALB if you add one later).
