terraform {
  required_providers {
    podman = {
      source = "project0/podman"
    }
  }
}

# Per default connects to local unix socket
provider "podman" {
  // default
  uri = "unix:///run/podman/podman.sock"
}

resource "podman_pod" "nginx" {
  name = "nginx:latest"
  keep_locally = false
}

resource "docker_container" "nginx" {
  image = docker_image.nginx.latest
  name = "tutorial"
  ports {
    internel = 80
    external = 8000
  }
}