resource "aws_ecr_repository" "sftp-client" {
  name = "sftp-client"
}

output "ecr_url" {
  value = "${aws_ecr_repository.sftp-client.repository_url}"
}
