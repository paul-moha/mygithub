### 创建vSmart Device 模板（vSmart1）
Configuration --- Templates --- Device

+ Create Template(CLI Template)

Device Model: vSmart
Template Name: vSmart1_Template
Description: vSmart1_Template

Load Running Config from reachable device: 2.2.2.1-vSmart1

====自动获取配置====

点击: Add

### Attach 模板到vSmart
vSmart_Template ----> Attach Device


### 创建vSmart Device 模板（vSmart2）
Configuration --- Templates --- Device --- vSmart1

+ Create Template(CLI Template)

Device Model: vSmart
Template Name: vSmart2_Template
Description: vSmart2_Template

Load Running Config from reachable device: 2.2.2.2-vSmart2

====自动获取配置====

点击: Add

### Attach 模板到vSmart
vSmart_Template ----> Attach Device --- vSmart2
