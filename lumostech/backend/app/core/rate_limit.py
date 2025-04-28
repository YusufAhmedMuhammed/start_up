from functools import wraps
from fastapi import HTTPException, Request
from datetime import datetime, timedelta
import time
from typing import Dict, Tuple

# Store rate limit data in memory (consider using Redis in production)
rate_limit_data: Dict[str, Tuple[int, datetime]] = {}

def rate_limit(limit: int = 5, period: int = 60):
    """
    Rate limiting decorator
    limit: number of requests allowed
    period: time period in seconds
    """
    def decorator(func):
        @wraps(func)
        async def wrapper(request: Request, *args, **kwargs):
            client_ip = request.client.host
            current_time = datetime.now()
            
            if client_ip in rate_limit_data:
                count, last_reset = rate_limit_data[client_ip]
                if current_time - last_reset > timedelta(seconds=period):
                    # Reset counter if period has passed
                    count = 0
                    last_reset = current_time
                
                if count >= limit:
                    # Calculate time until next allowed request
                    time_remaining = (last_reset + timedelta(seconds=period) - current_time).seconds
                    raise HTTPException(
                        status_code=429,
                        detail=f"Too many requests. Please try again in {time_remaining} seconds."
                    )
                
                count += 1
            else:
                count = 1
                last_reset = current_time
            
            rate_limit_data[client_ip] = (count, last_reset)
            return await func(request, *args, **kwargs)
        return wrapper
    return decorator 