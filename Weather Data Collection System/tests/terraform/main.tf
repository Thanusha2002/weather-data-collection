terraform {
}
resource "aws_iam_user" "ci_user" {
  name = "weather-ci-user"
}
resource "aws_iam_access_key" "ci_keys" {
  user = aws_iam_user.ci_user.name
}
resource "aws_iam_policy" "s3_write_only" {
  name = "weather-s3-write-only"
  policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Action = [
          "s3:PutObject",
          "s3:PutObjectAcl",
          "s3:ListBucket"
        ],
        Effect   = "Allow",
        Resource = [
          aws_s3_bucket.weather_data.arn,
          "${aws_s3_bucket.weather_data.arn}/*"
        ]
      }
    ]
  })
}
resource "aws_iam_user_policy_attachment" "attach_policy" {
  user       = aws_iam_user.ci_user.name
  policy_arn = aws_iam_policy.s3_write_only.arn
}
output "s3_bucket" {
  value = aws_s3_bucket.weather_data.id
}
output "ci_access_key_id" {
  value = aws_iam_access_key.ci_keys.id
}
output "ci_secret_access_key" {
  value     = aws_iam_access_key.ci_keys.secret
  sensitive = true
}
 