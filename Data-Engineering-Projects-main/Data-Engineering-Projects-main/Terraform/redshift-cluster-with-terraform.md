🚀 Step-by-Step: Create a Redshift Cluster with Terraform

📁 Step 1: Create Terraform Project Folder

```hcl
mkdir terraform-redshift
cd terraform-redshift
```

📝 Step 2: Create Terraform Files

1️⃣ main.tf

```hcl
provider "aws" {
  region = "us-west-2"
}

resource "aws_redshift_cluster" "bita_redshift" {
  cluster_identifier = "bita-redshift-cluster"
  node_type          = "dc2.large"
  number_of_nodes    = 1

  database_name      = "bitadb"
  master_username    = "adminuser"
  master_password    = "SuperSecret123!"

  skip_final_snapshot = true
}

resource "aws_security_group" "redshift_sg" {
  name        = "redshift-security-group"
  description = "Allow Redshift access"

  ingress {
    from_port   = 5439
    to_port     = 5439
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
```

2️⃣ variables.tf (optional)

```hcl
variable "region" {
  default = "us-west-2"
}
```

3️⃣ outputs.tf

```hcl
output "redshift_endpoint" {
  value = aws_redshift_cluster.bita_redshift.endpoint
}
```

🔄 Step 3: Initialize Terraform

```hcl
terraform init
```

✅ Step 4: Review the Plan

```hcl
terraform plan
```

🚀 Step 5: Apply the Configuration

```hcl
terraform apply
```

🔍 Step 6: Check the Redshift Endpoint

```hcl
Outputs:
redshift_endpoint = bita-redshift-cluster.cdxvxyzabc123.us-west-2.redshift.amazonaws.com:5439
```

🧹 Step 7: Clean Up

```hcl
terraform destroy
```

📝 Tips:

• Change node type for real production workloads.

• Keep your master password in a secrets manager.

• Define VPC and subnet group for more control (advanced).

• Add IAM roles if you want Redshift to access S3 directly.