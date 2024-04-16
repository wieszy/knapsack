read.table(text=s, sep="\t", header = TRUE) %>%
  tibble() %>%
  pivot_longer(cols=starts_with("value_other"), names_prefix="value_other_") %>%
  rename(control_group=name, value_other=value) %>%
  mutate(endowment=case_match(control_group, "mixed" ~ endowment_mixed, "damage" ~ endowment_damage, .default = 0)) %>%
  select(-starts_with("endowment_"))