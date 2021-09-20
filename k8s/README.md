# Kubernetes
### After the instructions followed, this is the output of `kubectl get pods,svc` command


| Name      | Ready | Status     | Restarts | Age |
| :---        |    :----:   |    :----:   |    :----:   |          ---: |
| pod/nginx-deployment-66b6c48dd5-ktk9q      | 1/1        | Running   | 0 | 86s|
| pod/nginx-deployment-66b6c48dd5-w2c5w   | 1/1         | Running      | 0 | 86s|
| pod/nginx-deployment-66b6c48dd5-zlqkm | 1/1  | Running| 0 | 86s |


| Name      | Type | Cluster-IP     | External-IP | Port(s) | Age|
| :---        |    :----:   |    :----:   |    :----:  |    :----: |          ---: | 
| service/kubernetes      | ClusterIP        |  10.96.0.1     | \<none>  | 443/TCP|63m |
| service/my-service   | ClusterIP        | 10.105.42.238      | \<none>  | 80/TCP|22s |