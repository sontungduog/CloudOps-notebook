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
