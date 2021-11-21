# Graceful Shutdown

Services need to be able to stop gracefully. This means, when your service gets told that it is going to be shut down, you need to make sure that stopping is not going to cause issues. You should ensure that database transactions have completed, connections are safely closed, and work that needs to be continued later is recorded. You should also ensure your service actually stops as soon as possible.

## Why is it Important?

Graceful Shutdown is important to consider because there are many occasions where you can't control when your service will be asked to shut down. For example, if a Kubernetes Node is scaled up or down your service might be re-deployed automatically on a different Kubernetes Node. That means the old copy of your service will be stopped, and a new one will be created. Since you don't know when that will happen, you need to be able to respond at any point to a shutdown request, ensuring you don't lose too much work or data.

Gracefully shutting down your service also includes exiting properly. That means, as soon as any shutdown routine is complete, your main process should exit with an appropriate exit code (success or failure). Doing so will tell Kubernetes that the shutdown is complete, and that any operations that need to follow (deleting nodes, re-deploying your service elsewhere etc.) can begin.

If your service does not exit gracefully, that does not mean your process will continue to run. Kubernetes has a default timeout (this can be configured, but only up to approximately 60 seconds), after which it will forcefully kill the process / container if the container hasn't stopped on it's own. 

## Tips and Tricks

- Kubernetes sends `SIGTERM` to the main process (PID 1) in a container, to tell the process that it needs to shut down soon (within seconds)
- Your process should exit with exit code `0` in a Linux container to signal a successful exit
- Make sure your service stops as soon as possible, within a few seconds is preferable.
- Not handling `SIGTERM` means you will have no warning that your service is going to be killed in Kubernetes!
- For long running tasks, ensure they can be broken up into multiple steps, and continued later. Record where you are up to when your service is asked to stop, and when it starts again you can continue without too much work lost.

## See Also

- [Terminating With Grace - GKE Guide](https://cloud.google.com/blog/products/gcp/kubernetes-best-practices-terminating-with-grace)
