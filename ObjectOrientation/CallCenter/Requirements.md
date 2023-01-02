# Design Call Center

# CallCenterSystem
- Maintains a queue of calls and workers
- Accepts or puts calls on hold depending on worker availabilty
- Whenever a call is available, next available worker will pick up call

# Caller
- Caller is entered into the call queue if no worker is available
- Caller is picked up whenever worker is available

# Worker
- Worker will be maintained in a worker queue
- Worker will wait in queue if no calls available
- Worker will take next call if all workers are busy