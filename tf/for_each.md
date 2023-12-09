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
    "ipa-cn-dev/ipa-admin-backend",
    "ipa-cn-dev/ipa-admin-frontend"
]
variable "ecr_repositories" {
  type = list(string)
}
```
