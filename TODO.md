# Deployment Plan for Student Feedback Portal to Azure AKS

## Phase 1: Source Code and Version Control
- [x] Update requirements.txt to add gunicorn
- [x] Execute git add .
- [x] Execute git commit -m "Phase 1: Add gunicorn, requirements.txt, and update app.py for containerization"
- [x] Execute git push origin main

## Phase 2: Containerization
- [x] Create Dockerfile
- [x] Execute docker build -t feedback-app:latest .
- [x] Execute docker run -d -p 8080:8080 --name feedback-test feedback-app:latest
- [x] Execute docker logs feedback-test
- [x] Execute docker ps
- [x] Execute docker stop feedback-test
- [x] Execute docker rm feedback-test

## Phase 3: Infrastructure Provisioning (IaC)
- [x] Execute mkdir terraform
- [x] Execute cd terraform
- [x] Create terraform/variables.tf
- [x] Create terraform/main.tf
- [x] Create terraform/outputs.tf
- [ ] Execute az login (Azure CLI installed, waiting for login)
- [ ] Execute terraform init
- [ ] Execute terraform plan
- [ ] Execute terraform apply --auto-approve
- [ ] Execute cd ..
- [ ] Execute az acr login --name samuelmdevopsacr
- [ ] Execute docker tag feedback-app:latest samuelmdevopsacr.azurecr.io/feedback-app:latest
- [ ] Execute docker push samuelmdevopsacr.azurecr.io/feedback-app:latest

## Phase 4: Configuration Management
- [x] Execute mkdir k8s
- [x] Execute mkdir ansible
- [x] Create k8s/deployment.yaml
- [x] Create k8s/service.yaml
- [x] Create ansible/deploy.yml

## Phase 5: CI/CD Pipeline Setup (GitHub Actions)
- [x] Execute mkdir -p .github/workflows
- [x] Create .github/workflows/main.yml
- [x] Execute git add .
- [x] Execute git commit -m "Phase 5: Add Terraform output, K8s manifests, Ansible playbook, and GitHub Actions CI/CD"
- [x] Execute git push origin main

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
