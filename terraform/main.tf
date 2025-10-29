terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~>3.100"
    }
  }

  required_version = ">= 1.3.0"
}

provider "azurerm" {
  features {}
}

# ----------------------------
# 1️⃣ Resource Group
# ----------------------------
resource "azurerm_resource_group" "rg" {
  name     = "student-feedback-rg"
  location = "East US"
}

# ----------------------------
# 2️⃣ Azure Container Registry (ACR)
# ----------------------------
resource "azurerm_container_registry" "acr" {
  name                = "studentfeedbackacr${random_integer.suffix.result}"
  resource_group_name = azurerm_resource_group.rg.name
  location            = azurerm_resource_group.rg.location
  sku                 = "Basic"
  admin_enabled       = true
}

# Random suffix for ACR name (must be globally unique)
resource "random_integer" "suffix" {
  min = 1000
  max = 9999
}

# ----------------------------
# 3️⃣ Azure Kubernetes Service (AKS)
# ----------------------------
resource "azurerm_kubernetes_cluster" "aks" {
  name                = "student-feedback-aks"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  dns_prefix          = "studentfeedback"

  default_node_pool {
    name       = "default"
    node_count = 1
    vm_size    = "Standard_B2s"
  }

  identity {
    type = "SystemAssigned"
  }

  tags = {
    Environment = "Dev"
    Project     = "Student Feedback Portal"
  }
}

# ----------------------------
# 4️⃣ Role Assignment (AKS → ACR)
# ----------------------------
resource "azurerm_role_assignment" "aks_acr_pull" {
  principal_id         = azurerm_kubernetes_cluster.aks.kubelet_identity[0].object_id
  role_definition_name = "AcrPull"
  scope                = azurerm_container_registry.acr.id
}


