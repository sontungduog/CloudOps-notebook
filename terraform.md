
```
terraform state
Subcommands:
    list    List resources in the state
    mv      Move an item in the state
    pull    Pull current state and output to stdout
    push    Update remote state from a local state file
    rm      Remove instances from the state
    show    Show a resource in the state
```
`terraform force-unlock 209fefd8-4465-02a4-f6bf-7c8a1f1776fc`
link download terraform: https://releases.hashicorp.com/terraform/0.13.7/

Về terraform chạy mấy câu này trên dev bastion nhé:
```
cd /home/tung.ds/sinh/ipa-ops/terraform/dev/gcp
gcloud auth application-default login --no-launch-browser


terraform init
terraform plan --target=google_storage_bucket.ipa_client
terraform plan --target=module.slave0_load_balancer.google_compute_forwarding_rule.default
```


```
resource "aws_lb_target_group" "nlb-tg" {
  count = length(var.forwarding_config)
  name = "${var.lb_name}-${lookup(var.forwarding_config[count.index], "name", null)}-${random_string.target-group-suffix.result}"
  vpc_id = var.vpc_id
  port = lookup(var.forwarding_config[count.index], "port", null )
  protocol    = lookup(var.forwarding_config[count.index], "protocol", null)
  target_type = lookup(var.forwarding_config[count.index], "target_type", null)
}

resource "aws_lb_target_group_attachment" "nlb-tg-attachment" {
  count = length(var.forwarding_config)
  target_group_arn = aws_lb_target_group.nlb-tg[count.index].arn
  target_id         = var.target_id
}
```

Import
```
terraform import module.instances.aws_instance.bastion i-02c19b105********
terraform import module.instances.aws_volume_attachment.ipa-master-second-ebs /dev/sdh:vol-075267a17***:i-0dee84032****
```

Tương tác với state
```
terraform state list
terraform state rm module.instances.aws_ebs_volume.ipa-master-second-ebs[0]
```
```
Terraform import với ký tự đặc biệt

terraform import module.ecr.aws_ecr_repository.ipa-cn-ecr[\"ipa-cn\/ipa-admin\"] ipa-cn\/ipa-admin`
```

```
The for_each meta-argument accepts a map or a set of strings, and creates an instance for each item in that map or set.
In blocks where for_each is set, an additional each object is available in expressions, so you can modify the configuration of each instance. This object has two attributes:
each.key — The map key (or set member) corresponding to this instance.
each.value — The map value corresponding to this instance. (If a set was provided, this is the same as each.key.)
```

Hàm main
```
module "ecr" {
  source   = "./modules/ecr"
  for_each = local.repositories

  name                  = each.key
  project_family        = local.project_family
  environment           = each.value.environment
  image_tag_mutability  = each.value.image_tag_mutability
  scan_on_push          = each.value.scan_on_push
  expiration_after_days = each.value.expiration_after_days
  additional_tags       = each.value.tags

}

locals {
  project_family = "demoecr"
  repositories = {
    "nginx" = {
      image_tag_mutability  = "IMMUTABLE"
      scan_on_push          = true
      expiration_after_days = 7
      environment           = "dev"
      tags = {
        Project     = "ECRDemo"
        Owner       = "anotherbuginthecode"
        Purpose     = "Reverse Proxy"
        Description = "NGINX docker image"
      }
    }
variable "ecr_repositories" {
  type = map
}


```

Hàm khai báo biến, tfvar
```
ecr_repositories = [
    "ipa/admin-backend",
    "ipa/admin-frontend"
]
variable "ecr_repositories" {
  type = list(string)
}
```

