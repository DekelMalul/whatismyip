# WhatIsMyIp?

This repo contains simple flask application, helm chart and eksctl config file. 

## Flask application

The flask application is a simple python project which returns the ipv4 of the remote client. 

### Dockerfile

The source code are provided with Dockerfile for building the image and use privately. 

## Helm chart

The helm directory deploy the whatismyip helm chart and ingress controller helm chart (as dependency).

* https://kubernetes.github.io/ingress-nginx/deploy/#using-helm

# Installtion guide

## Prerequisites

* Connection to dockerhub.

* EKS cluster.

Sample eks cluster to be deployed

```console
eksctl create cluster -f cluster.yaml
```

## Installtion Process


```console
cd helm
helm install whatismyip . -f values.yaml
```

Find the loadbalancer ip

```console
lb_dns=$(kubectl get service | grep nginx-ingress | awk '{print $4}')
loadbalancer_ip=$(ping $lb_dns | head -n 1 | cut -d "(" -f2 | cut -d ")" -f1)
echo $loadbalancer_ip
```

Map the hosts field to our local hosts file or route 53

# Parameters

| Parameter                              | Description                                     | Default                                                 |
|----------------------------------------|-------------------------------------------------|---------------------------------------------------------|
| `image.registry`                       | Docker image registry                           | `Null`                                                  |
| `image.repository`                     | Docker image repository name                    | `keeperdekel/whatismyip`                                |
| `image.pullPolicy`                     | Image pull policy                               | `IfNotPresent`                                          |
| `image.pullSecrets`                    | Docker registry secret names as an              | `{}`                                                    |
| `image.tag`                            | Docker image tag                                | `0.0.2`                                                 |
| `nameOverride`                         | Overide the resources names                     | `coolname`                                              |
| `replicaCount`                         | Number of replicas pods                         | `1`                                                     |
| `PodAnnotations`                       | Custom pod annotaions                           | `{}`                                                    |
| `commonlabels`                         | Custom labels that want to be added             | `environment: dev`                                      |
| `resources.requests.memory`            | Memory requests                                 | `128Mi`                                                 |
| `resources.requests.cpu`               | Cpu requests                                    | `128m`                                                  |
| `resources.limits.memory`              | Memory limits                                   | `1024Mi`                                                |
| `resources.limits.cpu`                 | Cpu limits                                      | `512m`                                                  |
| `service.type`                         | Service type                                    | `ClusterIP`                                             |
| `service.port`                         | The port that need to be used for the app       | `5000`                                                  |
| `service.annotations`                  | Custom annotaions on the service                | `{}`                                                    |
| `readinessProbe.initialDelaySeconds`   | Delay before first check if app is ready        | `5`                                                     |
| `readinessProbe.periodSeconds`         | period before the next check                    | `10`                                                    |
| `readinessProbe.failureThreshold`      | number of failures                              | `10`                                                    |
| `livenessProbe.initialDelaySeconds`    | Delay before first check if app is up           | `5`                                                     |
| `livenessProbe.periodSeconds`          | period before the next check                    | `10`                                                    |
| `livenessProbe.failureThreshold`       | number of failures                              | `10`                                                    |
| `ingress.enabled`                      | Check if you want to use ingress or not         | `true`                                                  | 
| `ingress.host`                         | DNS name for the ingress rules                  | `sisence.dekel.com`                                     | 
