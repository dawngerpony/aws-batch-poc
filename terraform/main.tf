terraform {
  required_version = ">=0.11.2"
}

provider "aws" {
  region = "eu-west-1"
  profile = "default"
}
