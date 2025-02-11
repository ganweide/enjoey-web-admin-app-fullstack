from django.urls import path
from .views import UploadChildrenCSVData, MigrateIntoCoreServiceChildrenCoreServiceFamilyTable, MigrateIntoCoreServiceFamilyTable, UploadStaffCSVData, CreateTenantStaff

urlpatterns = [
    path('childrencsvupload/', UploadChildrenCSVData.as_view(), name='file-upload'),
    path('staffcsvupload/', UploadStaffCSVData.as_view(), name='staff-csv-upload'),
    path('create-tenant-staff/', CreateTenantStaff.as_view(), name='create-tenant-staff'),
    path('children-family-migration/', MigrateIntoCoreServiceChildrenCoreServiceFamilyTable.as_view(), name='children-family-migration'),
    path('family-migration/', MigrateIntoCoreServiceFamilyTable.as_view(), name='family-migration')
]

