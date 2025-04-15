
# 🚀 Terraform Redshift Cluster Setup

This project provides a simple way to create an Amazon Redshift cluster using Terraform. It includes security group configuration, output display, and optional variable support.

---

## 📦 Features

- Provision a single-node Redshift cluster
- Setup a security group for Redshift access
- Output Redshift endpoint after deployment
- Easy to customize via variables

---

## 🧰 Prerequisites

Before you begin, ensure you have the following installed:

- [Terraform](https://developer.hashicorp.com/terraform/downloads)
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html)
- AWS credentials configured via `aws configure`

---

## 📁 Project Structure

```
terraform-redshift/
├── main.tf           # Core infrastructure script
├── variables.tf      # (Optional) Variables for customization
├── outputs.tf        # Output Redshift endpoint
```

---

## ⚙️ How to Use

1. Clone this repository or copy the files into your project directory.

```bash
git clone https://github.com/your-username/terraform-redshift.git
cd terraform-redshift
```

2. Initialize the Terraform project:

```bash
terraform init
```

3. Preview the plan:

```bash
terraform plan
```

4. Apply the infrastructure:

```bash
terraform apply
```

5. Once created, Terraform will display your Redshift endpoint.

---

## 🧹 Cleanup

To avoid charges, destroy the infrastructure when you're done:

```bash
terraform destroy
```

---

## 🔒 Security Note

- This example allows open access to Redshift on port 5439. For production, restrict the `cidr_blocks` to trusted IP ranges.
- Never hardcode sensitive credentials (e.g., passwords) in production environments.

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---
