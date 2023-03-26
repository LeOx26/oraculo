resource "google_compute_network" "vpc_oraculo" {
  name = "vpc-oraculo"
  auto_create_subnetworks = false
}

resource "google_compute_subnetwork" "oraculo_gke_subnet" {
  name = "oraculo-gke-subnet"
  ip_cidr_range = "10.10.0.0/24"
  network = google_compute_network.vpc_oraculo.self_link
  region = "us-central1"
}