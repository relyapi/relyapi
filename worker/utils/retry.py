from tenacity import retry, stop_after_attempt, wait_exponential

retry_strategy = retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=4, max=10)
)
