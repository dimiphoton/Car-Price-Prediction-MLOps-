# main.tf
provider "aws" {
  region = "us-west-2"
}

resource "aws_ec2_instance" "example" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"
  tags = {
    Name = "example-instance"
  }
}

resource "aws_s3_bucket" "example" {
  bucket = "example-bucket"
  acl    = "private"
}
