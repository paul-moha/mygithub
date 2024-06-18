### 查看默认的SLA Class
Configuration --- Policies --- Custom Options --- Centralized Policy --- Lists --- SLA Class

### 创建Application-Aware Routing Policies

Configuration --- Policies --- Custom Options --- Centralized Policy --- Traffic Policy

Appliciation Aware Routing Policy

+ Add Policy

Name:           Branch1_AAR_Policy
Description:    Branch1_AAR_Policy

=================APP Route=====================
Match Conditions
Application/Application Family List:       Audio_Video_APPS

Actions:
SLA Class                   : Voice-And-Video
Preferred Color             : public-internet
strict:                     不勾

------------------------------------------
Default Action
None    Enabled





