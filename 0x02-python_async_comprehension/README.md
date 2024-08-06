# 0x02. Python - Async Comprehension
## Files
- **0-async_generator.py**: Holds an async coroutine that loops 10 times and yields a random number between 0 and 10.
- **1-async_comprehension.py**: Holds an async coroutine that collects 10 random numbers using an async comprehensing over async_generator, then return the 10 random numbers.
- **2-measure_runtime.py**: Holds a async coroutine that executes async_comprehension four times in parallel using asyncio.gather.
