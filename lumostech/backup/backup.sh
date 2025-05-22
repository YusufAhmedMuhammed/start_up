#!/bin/bash

# Set variables
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
BACKUP_DIR="/backup"
DB_NAME="saas_agency_prod"
DB_USER="your_db_user"
DB_PASSWORD="your_secure_password"

# Create backup
PGPASSWORD=$DB_PASSWORD pg_dump -U $DB_USER -d $DB_NAME > $BACKUP_DIR/backup_$TIMESTAMP.sql

# Compress backup
gzip $BACKUP_DIR/backup_$TIMESTAMP.sql

# Keep only last 7 days of backups
find $BACKUP_DIR -name "backup_*.sql.gz" -mtime +7 -delete

# Optional: Upload to S3 (uncomment and configure if needed)
# aws s3 cp $BACKUP_DIR/backup_$TIMESTAMP.sql.gz s3://your-bucket/backups/ 