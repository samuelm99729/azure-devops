# Deployment Plan for Student Feedback Portal to Azure AKS

## Phase 1: Source Code and Version Control
- [ ] Update requirements.txt to add gunicorn
- [ ] Execute git add .
- [ ] Execute git commit -m "Phase 1: Add gunicorn, requirements.txt, and update app.py for containerization"
- [ ] Execute git push origin main

## Phase 2: Containerization
- [ ] Create Dockerfile
- [ ] Execute docker build -t feedback-app:latest .
- [ ] Execute docker run -d -p 8080:8080 --name feedback-test feedback-app:latest
- [ ] Execute docker logs feedback-test
- [ ] Execute docker ps
- [ ] Execute docker stop feedback-test
- [ ] Execute docker rm feedback-test

## Phase 3: Infrastructure Provisioning (IaC)
- [ ] Execute mkdir terraform
- [ ] Execute cd terraform
- [ ] Create terraform/variables.tf
- [ ] Create terraform/main.tf
- [ ] Create terraform/outputs.tf
- [ ] Execute az login
- [ ] Execute terraform init
- [ ] Execute terraform plan
- [ ] Execute terraform apply --auto-approve
- [ ] Execute cd ..
- [ ] Execute az acr login --name samuelmdevopsacr
- [ ] Execute docker tag feedback-app:latest samuelmdevopsacr.azurecr.io/feedback-app:latest
- [ ] Execute docker push samuelmdevopsacr.azurecr.io/feedback-app:latest

## Phase 4: Configuration Management
- [ ] Execute mkdir k8s
- [ ] Execute mkdir ansible
- [ ] Create k8s/deployment.yaml
- [ ] Create k8s/service.yaml
- [ ] Create ansible/deploy.yml

## Phase 5: CI/CD Pipeline Setup (GitHub Actions)
- [ ] Execute mkdir -p .github/workflows
- [ ] Create .github/workflows/main.yml
- [ ] Execute git add .
- [ ] Execute git commit -m "Phase 5: Add Terraform output, K8s manifests, Ansible playbook, and GitHub Actions CI/CD"
- [ ] Execute git push origin main

## Phase 6: Deployment and Validation
- [ ] Monitor GitHub Actions pipeline
- [ ] Execute az aks get-credentials --resource-group rg-devops-project-iac --name aks-devops-project --overwrite-existing
- [ ] Execute kubectl get pods -l app=feedback-app
- [ ] Execute kubectl get svc feedback-app-service
- [ ] Execute echo "Application URL: http://$(kubectl get svc feedback-app-service -o jsonpath='{.status.loadBalancer.ingress[0].ip}')"

## Phase 7: Documentation & Destruction
- [ ] Gather screenshots and create documentation
- [ ] Execute cd terraform
- [ ] Execute terraform destroy --auto-approve
