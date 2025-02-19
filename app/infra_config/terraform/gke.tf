terraform {
  required_providers {
    google = {
      source = "hashicorp/google"
    }
  }
}

provider "google" {
  credentials = file("~/projects/.std/oraculoTf.json")

  project = "oraculo-346203"
  region = "us-central1"
  zone = "us-central1-c"
}

resource "google_container_cluster" "oraculo_gke" {
  name = "oraculo-gke"
  location = "us-central1"
  ip_allocation_policy {
    
  }
  enable_autopilot = true
  
  network = google_compute_network.vpc_oraculo.self_link
  subnetwork = google_compute_subnetwork.oraculo_gke_subnet.self_link

}