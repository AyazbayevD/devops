# Logging
## Launching
1. Create `monitoring` directory and create there `docker-compose.yml`, `prometheus.yml` and `promtail.yml` files
2. Specify your image name and ports which are needed by your app. Also specify ports for monitoring services.
3. Run `docker-compose` pull
4. Run `docker-compose` up
5. Open `localhost:3000` to check if `Grafana` works. There you can see the metrics.
## Best practices
1. The amount of logs for docker-compose should be limited
2. Not to use the default network
3. Use static labels 