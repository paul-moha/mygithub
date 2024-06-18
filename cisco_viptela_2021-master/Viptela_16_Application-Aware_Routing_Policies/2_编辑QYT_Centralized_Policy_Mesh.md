### 编辑QYT_Centralized_Policy_Mesh

注意: 取消Traffic Policy "QYT_Loss_Correction", 它比Application Aware Routing优先

#### 导入策略
Configuration --- Policies --- Centralized Policy

QYT_Centralized_Policy_Mesh ... Edit

Traffic Rules

Application Aware Routing

Add Policy --- Import Existing

选择: Branch1_AAR_Policy

#### 应用策略
Policy Application

Application Aware Routing

===========================================================
Branch1_AAR_Policy

Select Site List: ALL_Site_List
Select VPN List: Enterprise_VPN_10
