
# ✅ Extend Terraform Script: Redshift + S3 Integration

This guide provides a Terraform configuration snippet that:

- Attaches an **IAM role** to your Redshift cluster
- Grants necessary permissions to **query data from Amazon S3**

---

## 🔐 Step 1: Define IAM Role for Redshift

Add this to your `main.tf`:

```hcl
resource "aws_iam_role" "redshift_s3_access" {
  name = "RedshiftS3AccessRole"

  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Action = "sts:AssumeRole",
        Principal = {
          Service = "redshift.amazonaws.com"
        },
        Effect = "Allow",
        Sid = ""
      }
    ]
  })
}

resource "aws_iam_policy_attachment" "attach_s3_access" {
  name       = "attachS3ReadOnly"
  roles      = [aws_iam_role.redshift_s3_access.name]
  policy_arn = "arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess"
}
```

---

## 🛠 Step 2: Update Redshift Cluster to Use the IAM Role

Add this to your existing `aws_redshift_cluster` resource:

```hcl
iam_roles = [aws_iam_role.redshift_s3_access.arn]
```

---

## 📂 Step 3: (Optional) S3 Bucket Setup for External Tables

```hcl
resource "aws_s3_bucket" "redshift_data" {
  bucket = "bita-redshift-data-bucket"
  acl    = "private"
}
```

You can now use Amazon Redshift Spectrum or `COPY` commands to query or load data from this bucket.

---

## 📌 Notes

- Redshift Spectrum queries external data using the IAM role and must have access to the corresponding **S3 bucket** and **AWS Glue Data Catalog**.
- The role must be listed in the Redshift cluster’s `iam_roles` attribute to enable access.

---

## 🧪 Testing It

After deployment, run a SQL command like this from your Redshift SQL client:

```sql
COPY my_table
FROM 's3://bita-redshift-data-bucket/sample.csv'
IAM_ROLE 'arn:aws:iam::123456789012:role/RedshiftS3AccessRole'
FORMAT AS CSV;
```

Make sure the S3 object is in the right format and accessible.

---
