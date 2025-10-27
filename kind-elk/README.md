ELK stack for kind (practice)

This folder contains minimal manifests to run a single-node ELK stack (Elasticsearch, Logstash, Kibana) on a local kind cluster for practice and learning.

Files:
- namespace.yaml            - Namespace definition (`logging`)
- elasticsearch.yaml       - ConfigMap (elasticsearch.yml), StatefulSet, Service
- kibana.yaml              - Deployment + Service for Kibana
- logstash.yaml            - ConfigMap (pipeline), Deployment + Service for Logstash

Quick start (assumes `kubectl` can talk to your kind cluster):

1) Create the namespace and apply manifests

```bash
kubectl apply -f kind-elk/namespace.yaml
kubectl apply -f kind-elk/elasticsearch.yaml
kubectl apply -f kind-elk/kibana.yaml
kubectl apply -f kind-elk/logstash.yaml
```

2) Wait for pods to be ready

```bash
kubectl get pods -n logging -w
# or wait for each to be ready
kubectl wait --for=condition=ready pod -l app=elasticsearch -n logging --timeout=120s
kubectl wait --for=condition=ready pod -l app=kibana -n logging --timeout=120s
kubectl wait --for=condition=ready pod -l app=logstash -n logging --timeout=120s
```

3) Access Kibana

Use port-forward to access Kibana locally:

```bash
kubectl port-forward svc/kibana 5601:5601 -n logging
# then open http://localhost:5601 in your browser
```

4) Test Elasticsearch from inside cluster

```bash
kubectl exec -n logging deploy/elasticsearch -- curl -s http://localhost:9200 | jq .
```

Notes & caveats
- This is intentionally minimal for local practice and uses `emptyDir` volumes. Do not use this configuration in production.
- Security (xpack security) is disabled for convenience. If you enable security, you will need to configure Kibana and Logstash credentials.
- If you want Filebeat/Metricbeat, add additional manifests.

Cleanup

```bash
kubectl delete -f kind-elk/ --ignore-not-found
kubectl delete ns logging --ignore-not-found
```

If you want, I can:
- (A) apply these manifests to your current cluster now,
- (B) run verification checks (pods/services/logs), or
- (C) add Filebeat and example data ingestion pipelines.

Reply with A, B, or C (or both) and I'll proceed.
