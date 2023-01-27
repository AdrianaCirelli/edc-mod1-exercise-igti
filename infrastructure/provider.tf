provider "aws" {
  region = var.aws_region
}


# Centralizar o arquivo de controle de estado do terraform
terraform {
  backend "s3" {


    #ESSE BUCKET DEVE SER CRIADO MANUALMENTE NA AWS 
    bucket = "terraform-state-igti-adri"
    key    = "state/igti/edc/mod1/terraform.tfstate"
    region = "us-east-2"
  }
}