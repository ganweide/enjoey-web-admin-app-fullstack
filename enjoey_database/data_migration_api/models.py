from django.db import models
from .storagebackend import ImageStorage

class ChildrenTempTable(models.Model):
    no = models.CharField(max_length=250, null=True)
    name = models.CharField(max_length=250, null=True)
    foreignName = models.CharField(max_length=250, null=True)
    studentID = models.CharField(max_length=250, null=True)
    gender = models.CharField(max_length=250, null=True)
    dob = models.CharField(max_length=250, null=True)
    age = models.CharField(max_length=250, null=True)
    race = models.CharField(max_length=250, null=True)
    citizenship = models.CharField(max_length=250, null=True)
    residentialStatus = models.CharField(max_length=250, null=True)
    religion = models.CharField(max_length=250, null=True)
    motherTonguelanguage = models.CharField(max_length=250, null=True)
    childOfStaff = models.BooleanField(default=False)
    householdIncome = models.CharField(max_length=250, null=True)
    subsidyType = models.CharField(max_length=250, null=True)
    otherResidentialRemarks = models.CharField(max_length=250, null=True)
    siblings1 = models.CharField(max_length=250, null=True)
    siblingsRelationship1 = models.CharField(max_length=250, null=True)
    siblings2 = models.CharField(max_length=250, null=True)
    siblingsRelationship2 = models.CharField(max_length=250, null=True)
    siblings3 = models.CharField(max_length=250, null=True)
    siblingsRelationship3 = models.CharField(max_length=250, null=True)
    siblings4 = models.CharField(max_length=250, null=True)
    siblingsRelationship4 = models.CharField(max_length=250, null=True)
    medicalConditions = models.CharField(max_length=250, null=True)
    vaccinationHistory = models.CharField(max_length=250, null=True)
    allergyHistory = models.CharField(max_length=250, null=True)
    specialDiet = models.CharField(max_length=250, null=True)
    specialNeeds = models.CharField(max_length=250, null=True)
    familyDoctorNum = models.CharField(max_length=250, null=True)
    admissionDate = models.CharField(max_length=250, null=True)
    withdrawalDate = models.CharField(max_length=250, null=True)
    programType = models.CharField(max_length=250, null=True)
    className = models.CharField(max_length=250, null=True)
    classSession = models.CharField(max_length=250, null=True)
    classLevel = models.CharField(max_length=250, null=True)
    transportationNum = models.CharField(max_length=250, null=True)
    paymentMethod1 = models.CharField(max_length=250, null=True)
    bankName1 = models.CharField(max_length=250, null=True)
    bankAccountHolder1 = models.CharField(max_length=250, null=True)
    bankAccountCode1 = models.CharField(max_length=250, null=True)
    branchCode1 = models.CharField(max_length=250, null=True)
    bankAccountNumber1 = models.CharField(max_length=250, null=True)
    paymentMethodApprovalDate1 = models.CharField(max_length=250, null=True)
    attentionTo1 = models.CharField(max_length=250, null=True)
    payeeID = models.CharField(max_length=250, null=True)
    amount = models.CharField(max_length=250, null=True)
    paymentMethod2 = models.CharField(max_length=250, null=True)
    bankName2 = models.CharField(max_length=250, null=True)
    bankAccountHolder2 = models.CharField(max_length=250, null=True)
    bankAccountCode2 = models.CharField(max_length=250, null=True)
    branchCode2 = models.CharField(max_length=250, null=True)
    bankAccountNumber2 = models.CharField(max_length=250, null=True)
    secondaryPayeeID = models.CharField(max_length=250, null=True)
    paymentMethodApprovalDate2 = models.CharField(max_length=250, null=True)
    attentionTo2 = models.CharField(max_length=250, null=True)
    paymentMethod3 = models.CharField(max_length=250, null=True)
    bankName3 = models.CharField(max_length=250, null=True)
    bankAccountHolder3 = models.CharField(max_length=250, null=True)
    bankAccountCode3 = models.CharField(max_length=250, null=True)
    branchCode3 = models.CharField(max_length=250, null=True)
    bankAccountNo = models.CharField(max_length=250, null=True)
    paymentMethodApprovalReference = models.CharField(max_length=250, null=True)
    paymentMethodApprovalDate3 = models.CharField(max_length=250, null=True)
    depositOption = models.CharField(max_length=250, null=True)
    parentRelationship1 = models.CharField(max_length=250, null=True)
    name1 = models.CharField(max_length=250, null=True)
    email1 = models.CharField(max_length=250, null=True)
    mobileNo1 = models.CharField(max_length=250, null=True)
    phoneNo1 = models.CharField(max_length=250, null=True)
    NRIC1 = models.CharField(max_length=250, null=True)
    race1 = models.CharField(max_length=250, null=True)
    citizenship1 = models.CharField(max_length=250, null=True)
    occupation1 = models.CharField(max_length=250, null=True)
    mainContact1 = models.BooleanField(default=False)
    authorisedPickUpPerson1 = models.BooleanField(default=False)
    emailInvoiceReceipt1 = models.BooleanField(default=False)
    emailCheckin1 = models.BooleanField(default=False)
    parentRelationship2 = models.CharField(max_length=250, null=True)
    name2 = models.CharField(max_length=250, null=True)
    email2 = models.CharField(max_length=250, null=True)
    mobileNo2 = models.CharField(max_length=250, null=True)
    phoneNo2 = models.CharField(max_length=250, null=True)
    NRIC2 = models.CharField(max_length=250, null=True)
    race2 = models.CharField(max_length=250, null=True)
    citizenship2 = models.CharField(max_length=250, null=True)
    occupation2 = models.CharField(max_length=250, null=True)
    mainContact2 = models.BooleanField(default=False)
    authorisedPickUpPerson2 = models.BooleanField(default=False)
    emailInvoiceReceipt2 = models.BooleanField(default=False)
    emailCheckin2 = models.BooleanField(default=False)
    parentRelationship3 = models.CharField(max_length=250, null=True)
    name3 = models.CharField(max_length=250, null=True)
    email3 = models.CharField(max_length=250, null=True)
    mobileNo3 = models.CharField(max_length=250, null=True)
    phoneNo3 = models.CharField(max_length=250, null=True)
    NRIC3 = models.CharField(max_length=250, null=True)
    race3 = models.CharField(max_length=250, null=True)
    citizenship3 = models.CharField(max_length=250, null=True)
    occupation3 = models.CharField(max_length=250, null=True)
    mainContact3 = models.BooleanField(default=False)
    authorisedPickUpPerson3 = models.BooleanField(default=False)
    emailInvoiceReceipt3 = models.BooleanField(default=False)
    emailCheckin3 = models.BooleanField(default=False)
    blocknoM = models.CharField(max_length=250, null=True)
    buildingM = models.CharField(max_length=250, null=True)
    streetM = models.CharField(max_length=250, null=True)
    unitM = models.CharField(max_length=250, null=True)
    postalCodeM = models.CharField(max_length=250, null=True)
    transportOptionM = models.CharField(max_length=250, null=True)
    blocknoF = models.CharField(max_length=250, null=True)
    buildingF = models.CharField(max_length=250, null=True)
    streetF = models.CharField(max_length=250, null=True)
    unitF = models.CharField(max_length=250, null=True)
    postalCodeF = models.CharField(max_length=250, null=True)
    transportOptionF = models.CharField(max_length=250, null=True)
    addressLine1 = models.CharField(max_length=250, null=True)
    addressLine2 = models.CharField(max_length=250, null=True)
    postalCodeRA1 = models.CharField(max_length=250, null=True)
    transportOptionRA1 = models.CharField(max_length=250, null=True)
    relationship1EC = models.CharField(max_length=250, null=True)
    name1EC = models.CharField(max_length=250, null=True)
    mobileNumber1EC = models.CharField(max_length=250, null=True)
    phoneNumber1EC = models.CharField(max_length=250, null=True)
    email1EC = models.CharField(max_length=250, null=True)
    badgeNo = models.CharField(max_length=250, null=True)
    migrationStatus = models.CharField(max_length=250, null=True)
    migrationRemark = models.CharField(max_length=250, null=True)

class CoreServiceChildren(models.Model):
    createdAt = models.DateTimeField("createdAt", auto_now_add=True)
    updatedAt = models.DateTimeField("updatedAt", auto_now=True)
    tenantId = models.CharField(max_length=250, null=True)
    branchId = models.CharField(max_length=250, null=True)
    firstName = models.CharField(max_length=250, null=True)
    lastName = models.CharField(max_length=250, null=True)
    fullName = models.CharField(max_length=250, null=True)
    birthCertNo = models.CharField(max_length=250, null=True)
    birthIC = models.CharField(max_length=250, null=True)
    birthDate = models.CharField(max_length=250, null=True)
    birthOrder = models.CharField(max_length=250, null=True)
    birthCountry = models.CharField(max_length=250, null=True)
    ethnicity = models.CharField(max_length=250, null=True)
    religion = models.CharField(max_length=250, null=True)
    siblings = models.CharField(max_length=250, null=True)
    profileImage = models.CharField(max_length=250, null=True)
    gender = models.CharField(max_length=250, null=True)
    age = models.CharField(max_length=250, null=True)
    isActive = models.BooleanField(default=False)
    isArchived = models.BooleanField(default=False)
    notes = models.CharField(max_length=250, null=True)
    isEnRolled = models.BooleanField(default=False)
    admissionId = models.CharField(max_length=250, null=True)
    isPresentToday = models.BooleanField(default=False)
    isInToday = models.BooleanField(default=False)
    isOutToday = models.BooleanField(default=False)
    isWithdraw = models.BooleanField(default=False)
    isMarkedWithdraw = models.BooleanField(default=False)
    withDrawDate = models.CharField(max_length=250, null=True)
    withDrawReason = models.CharField(max_length=250, null=True)
    isMarkedPromote = models.CharField(max_length=250, null=True)
    PromoteDate = models.CharField(max_length=250, null=True)
    PromoteReason = models.CharField(max_length=250, null=True)
    creator = models.CharField(max_length=250, null=True)

class CoreServiceChildrenAllergies(models.Model):
    allergyType = models.CharField(max_length=250, null=True)
    allergies = models.CharField(max_length=250, null=True)
    allergicPrevent = models.CharField(max_length=250, null=True)
    allergicSyndrome = models.CharField(max_length=250, null=True)
    allergicAction = models.CharField(max_length=250, null=True)
    haveMedicine = models.BooleanField(default=False)
    enterBy = models.CharField(max_length=250, null=True)
    created_at = models.DateTimeField("createdAt", auto_now_add=True)
    updated_at = models.DateTimeField("updatedAt", auto_now=True)
    child_id = models.CharField(max_length=250, null=True)

class CoreServiceChildrenMedicalContact(models.Model):
    contactType = models.CharField(max_length=250)
    specialtyType = models.CharField(max_length=250)
    name = models.CharField(max_length=250)
    phone = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    state = models.CharField(max_length=250)
    country = models.CharField(max_length=250)
    postcode = models.CharField(max_length=250)
    notes = models.CharField(max_length=250)
    enterBy = models.CharField(max_length=250)
    createdAt = models.DateTimeField("createdAt", auto_now_add=True)
    updatedAt = models.DateTimeField("updatedAt", auto_now=True)
    child_id = models.CharField(max_length=250)
    isArchived = models.BooleanField()

class CoreServiceChildrenEnrollment(models.Model):
    tenantId = models.CharField(max_length=250)
    branchId = models.CharField(max_length=250)
    academyYear = models.CharField(max_length=250)
    enrollStartDate = models.CharField(max_length=250)
    enrollEndDate = models.CharField(max_length=250)
    status = models.CharField(max_length=250)
    active = models.CharField(max_length=250)
    isSpecial = models.BooleanField()
    notes = models.CharField(max_length=250)
    enrollBy = models.CharField(max_length=250)
    created_at = models.DateTimeField("createdAt", auto_now_add=True)
    updated_at = models.DateTimeField("updatedAt", auto_now=True)
    children_id = models.CharField(max_length=250)
    classroom_id = models.CharField(max_length=250)
    program_id = models.CharField(max_length=250)

class CoreServiceClassrooms(models.Model):
    tenantId = models.CharField(max_length=250)
    branchId = models.CharField(max_length=250)
    name = models.CharField(max_length=250)
    created_at = models.DateTimeField("createdAt", auto_now_add=True)
    updated_at = models.DateTimeField("updatedAt", auto_now=True)
    maxCapacity = models.CharField(max_length=250)
    availableCapacity = models.CharField(max_length=250)
    academyYear = models.CharField(max_length=250)
    isSpecial = models.BooleanField()
    active = models.CharField(max_length=250)
    isArchived = models.BooleanField()
    enteredBy = models.CharField(max_length=250)
    program_id = models.CharField(max_length=250)

class CoreServiceFamily(models.Model):
    userId = models.CharField(max_length=250, null=True)
    firstName = models.CharField(max_length=250)
    lastName = models.CharField(max_length=250, null=True)
    phone = models.CharField(max_length=250, null=True)
    email = models.CharField(max_length=250, null=True)
    gender = models.CharField(max_length=250, null=True)
    birthIC = models.CharField(max_length=250, null=True)
    birthCountry = models.CharField(max_length=250, null=True)
    occupation = models.CharField(max_length=250, null=True)
    relationship = models.CharField(max_length=250, null=True)
    profileImage = models.CharField(max_length=250, null=True)
    address = models.CharField(max_length=250, null=True)
    state = models.CharField(max_length=250, null=True)
    country = models.CharField(max_length=250, null=True)
    postcode = models.CharField(max_length=250, null=True)
    isArchived = models.BooleanField(default=False)
    isAllowPickup = models.BooleanField(default=False)
    isEmergencyContact = models.BooleanField(default=False)
    isBillable = models.BooleanField(default=False)
    isPrimary = models.BooleanField(default=False)
    isWebAccess = models.BooleanField(default=False)
    isMobileAccess = models.BooleanField(default=False)
    creator = models.CharField(max_length=250, null=True)
    created_at = models.DateTimeField("createdAt", auto_now_add=True)
    updated_at = models.DateTimeField("updatedAt", auto_now=True)

class StaffTempTable(models.Model):
    schoolName = models.CharField(max_length=250, null=True)
    branchName = models.CharField(max_length=250, null=True)
    firstName = models.CharField(max_length=250, null=True)
    lastName = models.CharField(max_length=250, null=True)
    email = models.CharField(max_length=250, null=True)
    phone = models.CharField(max_length=250, null=True)
    gender = models.CharField(max_length=250, null=True)
    dob = models.DateField(null=True)
    profileImage = models.ImageField(storage=ImageStorage(), null=True)
    address = models.CharField(max_length=250, null=True)
    state = models.CharField(max_length=250, null=True)
    country = models.CharField(max_length=250, null=True)
    birthCountry = models.CharField(max_length=250, null=True)
    postcode = models.CharField(max_length=250, null=True)
    role = models.CharField(max_length=250, null=True)
    isWebAccess = models.BooleanField(default=False)
    isMobileAccess = models.BooleanField(default=False)
    doj = models.DateField(null=True)
    isExternal = models.BooleanField(default=False)
    staffNRIC = models.CharField(max_length=250, null=True)
    academyYear = models.CharField(max_length=250, null=True)
    academyMonth = models.CharField(max_length=250, null=True)
    startDate = models.CharField(max_length=250, null=True)
    classroomName = models.CharField(max_length=250, null=True)
    isPrimary = models.BooleanField(default=False)
    branches = models.CharField(max_length=250, null=True)
    isFranchiseStaff = models.BooleanField(default=False)
    badgeNo = models.CharField(max_length=250, null=True)
    migrationStatus = models.CharField(max_length=250, null=True)
    migrationRemark = models.CharField(max_length=250, null=True)


class Staff(models.Model):
    tenantId = models.CharField(max_length=250)
    branchId = models.BigIntegerField()
    firstName = models.CharField(max_length=250)
    lastName = models.CharField(max_length=250)
    email = models.EmailField(db_index=True, unique=True, max_length=254)
    phone = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    dob = models.CharField(max_length=10)
    profileImage = models.ImageField(storage=ImageStorage(), null=True)
    address = models.CharField(max_length=500, null=True)
    state = models.CharField(max_length=50, null=True)
    country = models.CharField(max_length=50, null=True)
    birthCountry = models.CharField(max_length=100, null=True)
    postcode = models.CharField(max_length=10, null=True)
    role = models.CharField(max_length=20)
    isWebAccess = models.BooleanField(default=False)
    isMobileAccess = models.BooleanField(default=False)
    doj = models.DateField()
    isExternal = models.BooleanField(default=False)
    userId = models.UUIDField(null=True)
    isActive = models.BooleanField(default=False)
    isPresentToday = models.BooleanField(default=False)
    isInToday = models.BooleanField(default=False)
    isOutToday = models.BooleanField(default=False)
    staffNRIC = models.CharField(max_length=20, null=True)
    creator = models.CharField(max_length=250, editable=False)
    isMarkedWithdraw = models.BooleanField(default=False)
    withDrawDate = models.CharField(max_length=10, null=True)
    withDrawReason = models.CharField(max_length=200, null=True)
    isArchived = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Programs(models.Model):
    tenantId = models.CharField(max_length=250)
    branchId = models.BigIntegerField()
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    startingYear = models.IntegerField(blank=True)
    startingMonth = models.IntegerField(blank=True)
    maxYear = models.IntegerField(blank=True)
    maxMonth = models.IntegerField(blank=True)
    rankMonth = models.IntegerField(blank=True)
    baseStaff = models.IntegerField(blank=True)
    baseStudent = models.IntegerField(blank=True)
    active = models.BooleanField(default=True)
    isArchived = models.BooleanField(default=False)
    isSpecial = models.BooleanField(default=False)
    creator = models.CharField(max_length=250, editable=True)
    createdAt = models.DateTimeField(editable=False)
    updatedAt = models.DateTimeField()

class ClassRooms(models.Model):
    tenantId = models.CharField(max_length=250)
    branchId = models.BigIntegerField()
    programs = models.ForeignKey(Programs, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    maxCapacity = models.IntegerField()
    availableCapacity = models.IntegerField()
    academyYear = models.CharField(max_length=4)
    isSpecial = models.BooleanField(default=False)
    active = models.BooleanField()
    isArchived = models.BooleanField(default=False)
    enteredBy = models.CharField(max_length=250, editable=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

     
class Classroom_staff(models.Model):
    tenantId = models.CharField(max_length=250)
    branchId = models.BigIntegerField()
    classroom = models.ForeignKey(ClassRooms, on_delete=models.CASCADE)
    userId = models.CharField(max_length=250, null=True)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    assignedBy = models.CharField(max_length=250)
    isPrimary = models.BooleanField(default=False)
    isActive = models.BooleanField(default=False)
    academyYear = models.CharField(max_length=4, null=True)
    academyMonth = models.CharField(max_length=2, null=True)
    startDate = models.DateField(null=True)
    endDate = models.DateField(null=True)
    isMarkedWithdraw = models.BooleanField(default=False)
    withDrawDate = models.CharField(max_length=10, null=True)
    withDrawReason = models.CharField(max_length=200, null=True)
    isMarkedTransfer = models.BooleanField(default=False)
    TransferDate = models.CharField(max_length=10, null=True)
    TransferReason = models.CharField(max_length=200, null=True)
    createdAt = models.DateTimeField(editable=False)
    updatedAt = models.DateTimeField()
    