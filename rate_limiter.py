def create_rate_limiter(max_tokens, refill_interval_ms):
    buckets = {}
    
    def is_rate_limited(user_id, current_time_ms):
        if user_id not in buckets:
            buckets[user_id] = {"tokens": max_tokens,
                               "last_refill_time": current_time_ms}
        
        
        bucket = buckets[user_id]
        
        elapsed = current_time_ms - bucket["last_refill_time"]
        
        completed_intervals = elapsed // refill_interval_ms
        
        if completed_intervals > 0:
            bucket["tokens"] = min(bucket["tokens"] + completed_intervals, max_tokens)
            
            bucket["last_refill_time"] += (completed_intervals * refill_interval_ms)
        
        if bucket["tokens"] == 0:
            return True 
        
        bucket["tokens"] -= 1
        return False   
    
    return is_rate_limited

limiter = create_rate_limiter(2, 100)

print(limiter("sam", 0))    # False
print(limiter("sam", 0))    # False
print(limiter("sam", 0))    # True

print(limiter("sam", 100))  # False
print(limiter("sam", 100))  # True

print(limiter("sam", 200))  # False