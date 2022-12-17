#!/bin/bash

# create secrets
kubectl create secret generic auth-policy --from-file=../opa_configs/policy.rego
kubectl create secret generic env-file --from-env-file=../.env

# opa
kubectl create -f deployment-opa.yaml
kubectl create -f service-opa.yaml

# app
kubectl create -f deployment-app.yaml
kubectl create -f service-app.yaml

sleep 5

while true
do
    # get app pod status
    app_pod_status=$(kubectl get pods --sort-by=.metadata.creationTimestamp -o jsonpath="{.items[0].status.containerStatuses[?(@.ready)].ready}")
    
    if [ "${app_pod_status}" != "true" ]
    then
        echo "waiting for pod to be ready"
        sleep 10
    else
        break
    fi
done

# port forward app so it can be accessed from outside the cluster
app_pod_name=$(kubectl get pods --sort-by=.metadata.creationTimestamp -o jsonpath="{.items[0].metadata.name}")
kubectl port-forward $app_pod_name 8000