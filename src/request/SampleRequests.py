import Boarding
import Credit
import Check
import Services
from Model import *

def sampleCreditAuthorization() :
        authorizationRequest = Credit.Authorization()

        credentials = Credentials();
        credentials.AcceptorID = "1147003"
        authorizationRequest.Credentials = credentials

        reports = Reports();
        reports.ReportGroup = "1243"
        authorizationRequest.Reports = reports

        transaction = Transaction();
        transaction.ReferenceNumber = "1"
        transaction.TransactionAmount = "10.00"
        transaction.OrderSource = (Transaction.OrderSourceEnum.ECOMMERCE)
        authorizationRequest.Transaction = transaction

        card = Card();
        card.CardNumber = "4457010000000009"
        card.ExpirationMonth = "01"
        card.ExpirationYear = "16"
        card.CVV = "349"
        card.Type = (Card.TypeEnum.VI)
        authorizationRequest.Card = card

        application = Application();
        application.ApplicationID = "1234"
        authorizationRequest.Application = application

        return authorizationRequest

def sampleCreditReversal(transactionID) :
        reversalRequest = Credit.Reversal()

        credentials = Credentials();
        credentials.AcceptorID = "1147003"
        reversalRequest.Credentials = credentials

        reports = Reports();
        reports.ReportGroup = "1243"
        reversalRequest.Reports = reports

        transaction = Transaction();
        transaction.TransactionID = transactionID
        reversalRequest.Transaction = transaction

        application = Application();
        application.ApplicationID = "1234"
        reversalRequest.Application = application

        return reversalRequest

def sampleCreditAuthorizationCompletion(transactionID) :
        authorizationCompletionRequest = Credit.AuthorizationCompletion()

        credentials = Credentials();
        credentials.AcceptorID = "1147003"
        authorizationCompletionRequest.Credentials = credentials

        reports = Reports();
        reports.ReportGroup = "1243"
        authorizationCompletionRequest.Reports = reports

        transaction = Transaction();
        transaction.TransactionID = transactionID
        authorizationCompletionRequest.Transaction = transaction

        application = Application();
        application.ApplicationID = "1234"
        authorizationCompletionRequest.Application = application

        return authorizationCompletionRequest

def sampleCreditCaptureGivenAuth() :
        captureGivenAuthRequest = Credit.CaptureGivenAuth()

        credentials = Credentials();
        credentials.AcceptorID = "1147003"
        captureGivenAuthRequest.Credentials = credentials

        reports = Reports();
        reports.ReportGroup = "1243"
        captureGivenAuthRequest.Reports = reports

        transaction = Transaction();
        transaction.ReferenceNumber = "1"
        transaction.TransactionAmount = "100.10"
        transaction.AuthorizationDate = "1111-11-11"
        transaction.ApprovalNumber = "1234"
        transaction.OrderSource = (Transaction.OrderSourceEnum.ECOMMERCE)
        captureGivenAuthRequest.Transaction = transaction

        card = Card();
        card.CardNumber = "4457010000000009"
        card.ExpirationMonth = "01"
        card.ExpirationYear = "16"
        card.CVV = "349"
        card.Type = (Card.TypeEnum.VI)
        captureGivenAuthRequest.Card = card

        application = Application();
        application.ApplicationID = "1234"
        captureGivenAuthRequest.Application = application

        return captureGivenAuthRequest

def sampleCreditCredit(transactionID) :
        creditRequest = Credit.Credit()

        credentials = Credentials();
        credentials.AcceptorID = "1147003"
        creditRequest.Credentials = credentials

        reports = Reports();
        reports.ReportGroup = "1243"
        creditRequest.Reports = reports

        transaction = Transaction();
        transaction.TransactionID = transactionID
        creditRequest.Transaction = transaction

        application = Application();
        application.ApplicationID = "1234"
        creditRequest.Application = application

        return creditRequest

def sampleCreditForce() :
        forceRequest = Credit.Force()

        credentials = Credentials();
        credentials.AcceptorID = "1147003"
        forceRequest.Credentials = credentials

        reports = Reports();
        reports.ReportGroup = "1243"
        forceRequest.Reports = reports

        transaction = Transaction();
        transaction.ReferenceNumber = "1"
        transaction.TransactionAmount = "100.10"
        transaction.OrderSource = (Transaction.OrderSourceEnum.ECOMMERCE)
        forceRequest.Transaction = transaction

        card = Card();
        card.CardNumber = "4457010000000009"
        card.ExpirationMonth = "01"
        card.ExpirationYear = "16"
        card.CVV = "349"
        card.Type = (Card.TypeEnum.VI)
        forceRequest.Card = card

        application = Application();
        application.ApplicationID = "1234"
        forceRequest.Application = application

        return forceRequest

def sampleCreditReturn() :
        returnRequest = Credit.Return()

        credentials = Credentials();
        credentials.AcceptorID = "1147003"
        returnRequest.Credentials = credentials

        reports = Reports();
        reports.ReportGroup = "1243"
        returnRequest.Reports = reports

        transaction = Transaction();
        transaction.ReferenceNumber = "123"
        transaction.TransactionAmount = "10.00"
        transaction.OrderSource = (Transaction.OrderSourceEnum.ECOMMERCE)
        returnRequest.Transaction = transaction

        card = Card();
        card.CardNumber = "4457010000000009"
        card.ExpirationMonth = "01"
        card.ExpirationYear = "16"
        card.CVV = "349"
        card.Type = (Card.TypeEnum.VI)
        returnRequest.Card = card

        application = Application();
        application.ApplicationID = "1234"
        returnRequest.Application = application

        return returnRequest

def sampleCreditSale() :
        saleRequest = Credit.Sale()

        credentials = Credentials();
        credentials.AcceptorID = "1147003"
        saleRequest.Credentials = credentials

        reports = Reports();
        reports.ReportGroup = "1243"
        saleRequest.Reports = reports

        transaction = Transaction();
        transaction.ReferenceNumber = "1"
        transaction.TransactionAmount = "100.10"
        transaction.OrderSource = (Transaction.OrderSourceEnum.ECOMMERCE)
        saleRequest.Transaction = transaction

        card = Card();
        card.CardNumber = "4457010000000009"
        card.ExpirationMonth = "01"
        card.ExpirationYear = "16"
        card.CVV = "349"
        card.Type = (Card.TypeEnum.VI)
        saleRequest.Card = card

        application = Application();
        application.ApplicationID = "1234"
        saleRequest.Application = application

        return saleRequest

def sampleCreditVoid(transactionID) :
        voidRequest = Credit.Void()

        credentials = Credentials();
        credentials.AcceptorID = "1147003"
        voidRequest.Credentials = credentials

        reports = Reports();
        reports.ReportGroup = "1243"
        voidRequest.Reports = reports

        transaction = Transaction();
        transaction.TransactionID = transactionID
        voidRequest.Transaction = transaction

        application = Application();
        application.ApplicationID = "1234"
        voidRequest.Application = application

        return voidRequest


def sampleCheckCredit(transactionID) :
        creditRequest = Check.Credit()

        credentials = Credentials();
        credentials.AcceptorID = "1147003"
        creditRequest.Credentials = credentials

        transaction = Transaction();
        transaction.TransactionID = transactionID
        creditRequest.Transaction = transaction

        reports = Reports();
        reports.ReportGroup = "1243"
        creditRequest.Reports = reports

        application = Application();
        application.ApplicationID = "1234"
        creditRequest.Application = application

        return creditRequest

def sampleCheckReturn() :
        returnRequest = Check.Return()

        credentials = Credentials();
        credentials.AcceptorID = "1147003"
        returnRequest.Credentials = credentials

        transaction = Transaction();
        transaction.ReferenceNumber = "708388073320126000"
        transaction.TransactionAmount = "12.56"
        transaction.OrderSource = (Transaction.OrderSourceEnum.ECOMMERCE)
        returnRequest.Transaction = transaction

        demandDepositAccount = DemandDepositAccount();
        demandDepositAccount.DDAAccountType = "Checking"
        demandDepositAccount.AccountNumber = "234"
        demandDepositAccount.RoutingNumber = "123234345"
        demandDepositAccount.CheckNumber = "456"
        demandDepositAccount.CCDPaymentInformation = "567"
        returnRequest.DemandDepositAccount = demandDepositAccount

        address = Address();
        address.BillingName = "John Smith"
        address.BillingAddress1 = "1 Main St."
        address.BillingCity = "Burlington"
        address.BillingState = "MA"
        address.BillingZipcode = "01803-3747"
        address.BillingEmail = "jdoe@litle.com"
        address.BillingPhone = "978-551-0040"
        address.BillingCountry = (Address.BillingCountryEnum.USA)
        returnRequest.Address = address

        reports = Reports();
        reports.ReportGroup = "1243"
        returnRequest.Reports = reports

        application = Application();
        application.ApplicationID = "1234"
        returnRequest.Application = application

        return returnRequest

def sampleCheckSale() :
        saleRequest = Check.Sale()

        credentials = Credentials();
        credentials.AcceptorID = "1147003"
        saleRequest.Credentials = credentials

        transaction = Transaction();
        transaction.ReferenceNumber = "1"
        transaction.TransactionAmount = "100.10"
        transaction.OrderSource = (Transaction.OrderSourceEnum.ECOMMERCE)
        saleRequest.Transaction = transaction

        address = Address();
        address.BillingName = "John Smith"
        address.BillingAddress1 = "1 Main St."
        address.BillingCity = "Burlington"
        address.BillingState = "MA"
        address.BillingZipcode = "01803-3747"
        address.BillingEmail = "jdoe@litle.com"
        address.BillingPhone = "978-551-0040"
        address.BillingCountry = (Address.BillingCountryEnum.USA)
        saleRequest.Address = address

        demandDepositAccount = DemandDepositAccount();
        demandDepositAccount.RoutingNumber = "123234345"
        demandDepositAccount.DDAAccountType = "Checking"
        demandDepositAccount.CheckNumber = "456"
        saleRequest.DemandDepositAccount = demandDepositAccount

        paymentAccount = PaymentAccount();
        paymentAccount.PaymentAccountID = "1232343454565"
        saleRequest.PaymentAccount = paymentAccount

        reports = Reports();
        reports.ReportGroup = "1243"
        saleRequest.Reports = reports

        application = Application();
        application.ApplicationID = "1234"
        saleRequest.Application = application

        return saleRequest

def sampleCheckVerification() :
        verificationRequest = Check.Verification()

        credentials = Credentials();
        credentials.AcceptorID = "1147003"
        verificationRequest.Credentials = credentials

        transaction = Transaction();
        transaction.ReferenceNumber = "1"
        transaction.TransactionAmount = "100.10"
        transaction.OrderSource = (Transaction.OrderSourceEnum.ECOMMERCE)
        verificationRequest.Transaction = transaction

        address = Address();
        address.BillingName = "John Smith"
        address.BillingAddress1 = "1 Main St."
        address.BillingCity = "Burlington"
        address.BillingState = "MA"
        address.BillingZipcode = "01803-3747"
        address.BillingEmail = "jdoe@litle.com"
        address.BillingPhone = "978-551-0040"
        address.BillingCountry = (Address.BillingCountryEnum.USA)
        verificationRequest.Address = address

        demandDepositAccount = DemandDepositAccount();
        demandDepositAccount.DDAAccountType = "Checking"
        demandDepositAccount.AccountNumber = "234"
        demandDepositAccount.RoutingNumber = "123234345"
        demandDepositAccount.CheckNumber = "456"
        demandDepositAccount.CCDPaymentInformation = "567"
        verificationRequest.DemandDepositAccount = demandDepositAccount

        reports = Reports();
        reports.ReportGroup = "1243"
        verificationRequest.Reports = reports

        application = Application();
        application.ApplicationID = "1234"
        verificationRequest.Application = application

        return verificationRequest

def sampleCheckVoid(transactionID) :
        voidRequest = Check.Void()

        credentials = Credentials();
        credentials.AcceptorID = "1147003"
        voidRequest.Credentials = credentials

        transaction = Transaction();
        transaction.TransactionID = transactionID
        voidRequest.Transaction = transaction

        reports = Reports();
        reports.ReportGroup = "1243"
        voidRequest.Reports = reports

        application = Application();
        application.ApplicationID = "1234"
        voidRequest.Application = application

        return voidRequest


def sampleServicesCreatePlan() :
        createPlanRequest = Services.CreatePlan()

        credentials = Credentials();
        credentials.AcceptorID = "1147003"
        createPlanRequest.Credentials = credentials

        scheduledTask = ScheduledTask();
        scheduledTask.Active = "true"
        scheduledTask.ScheduledTaskID = "12"
        scheduledTask.Name = "NewPlan"
        scheduledTask.Description = "Created New Plan"
        scheduledTask.RunFrequency = "WEEKLY"
        scheduledTask.Amount = "12.00"
        scheduledTask.RunCycles = "5"
        scheduledTask.TrialRunCycles = "7"
        scheduledTask.TrialRunFrequency = "DAY"
        createPlanRequest.ScheduledTask = scheduledTask

        return createPlanRequest

def sampleServicesFraudCheck() :
        fraudCheckRequest = Services.FraudCheck()

        credentials = Credentials();
        credentials.AcceptorID = "1147003"
        fraudCheckRequest.Credentials = credentials

        reports = Reports();
        reports.ReportGroup = "1243"
        fraudCheckRequest.Reports = reports

        advancedFraudChecks = AdvancedFraudChecks();
        advancedFraudChecks.ThreatMetrixSessionID = "123"
        fraudCheckRequest.AdvancedFraudChecks = advancedFraudChecks

        application = Application();
        application.ApplicationID = "1234"
        fraudCheckRequest.Application = application

        return fraudCheckRequest

def sampleServicesPaymentAccountCreate() :
        paymentAccountCreateRequest = Services.PaymentAccountCreate()

        credentials = Credentials();
        credentials.AcceptorID = "1147003"
        paymentAccountCreateRequest.Credentials = credentials

        reports = Reports();
        reports.ReportGroup = "1243"
        paymentAccountCreateRequest.Reports = reports

        card = Card();
        card.AccountNumber = "5454545454545454"
        paymentAccountCreateRequest.Card = card

        application = Application();
        application.ApplicationID = "1234"
        paymentAccountCreateRequest.Application = application

        return paymentAccountCreateRequest

def sampleServicesScheduledTaskDelete() :
        scheduledTaskDeleteRequest = Services.ScheduledTaskDelete()

        credentials = Credentials();
        credentials.AcceptorID = "1147003"
        scheduledTaskDeleteRequest.Credentials = credentials

        scheduledTask = ScheduledTask();
        scheduledTask.SubscriptionID = "12432463563564"
        scheduledTaskDeleteRequest.ScheduledTask = scheduledTask

        return scheduledTaskDeleteRequest

def sampleServicesScheduledTaskUpdate() :
        scheduledTaskUpdateRequest = Services.ScheduledTaskUpdate()

        credentials = Credentials();
        credentials.AcceptorID = "1147003"
        scheduledTaskUpdateRequest.Credentials = credentials

        scheduledTask = ScheduledTask();
        scheduledTask.SubscriptionID = "12432463563564"
        scheduledTask.BillingDate = "2019-10-21"
        scheduledTaskUpdateRequest.ScheduledTask = scheduledTask

        return scheduledTaskUpdateRequest

def sampleServicesPaymentAccountUpdate() :
        paymentAccountUpdateRequest = Services.PaymentAccountUpdate()

        credentials = Credentials();
        credentials.AcceptorID = "1147003"
        paymentAccountUpdateRequest.Credentials = credentials

        reports = Reports();
        reports.ReportGroup = "1243"
        paymentAccountUpdateRequest.Reports = reports

        card = Card();
        card.CVV = "123"
        paymentAccountUpdateRequest.Card = card

        application = Application();
        application.ApplicationID = "1234"
        paymentAccountUpdateRequest.Application = application

        paymentAccount = PaymentAccount();
        paymentAccount.PaymentAccountID = "1112000188575454"
        paymentAccountUpdateRequest.PaymentAccount = paymentAccount

        return paymentAccountUpdateRequest

def sampleServicesUpdatePlan() :
        updatePlanRequest = Services.UpdatePlan()

        credentials = Credentials();
        credentials.AcceptorID = "1147003"
        updatePlanRequest.Credentials = credentials

        scheduledTask = ScheduledTask();
        scheduledTask.Active = "false"
        scheduledTask.ScheduledTaskID = "12"
        updatePlanRequest.ScheduledTask = scheduledTask

        return updatePlanRequest


def sampleBoardingRetrieveMccList() :
        retrieveMccListRequest = Boarding.RetrieveMccList()

        

        return retrieveMccListRequest

def sampleBoardingCreateLegalEntity() :
        createLegalEntityRequest = Boarding.CreateLegalEntity()

        legalEntity = LegalEntity();
        legalEntity.Name = "Legal Entity Name"
        legalEntity.Type = "CORPORATION"
        legalEntity.TaxID = "12345"
        legalEntity.AnnualCreditCardSalesVolume = "80000000"
        legalEntity.HasAcceptedCreditCards = "true"
        legalEntity.YearsInBusiness = "12"
        createLegalEntityRequest.LegalEntity = legalEntity

        address = Address();
        address.Address1 = "Street Address 1"
        address.Address2 = "Street Address 2"
        address.City = "City"
        address.State = "MA"
        address.Zip = "01730"
        address.Country = "USA"
        createLegalEntityRequest.Address = address

        principal = Principal();
        principal.Title = "Chief Financial Officer"
        principal.FirstName = "p first"
        principal.LastName = "p last"
        principal.Email = "emailAddress"
        principal.SSN = "123459876"
        principal.ContactPhone = "7817659800"
        principal.DateOfBirth = "1980-10-12"
        principal.DriversLicense = "892327409832"
        principal.DriversLicenseState = "MA"
        principalAddress = Address();
        principalAddress.Address1 = "Street Address 1"
        principalAddress.Address2 = "Street Address 2"
        principalAddress.City = "Boston"
        principalAddress.State = "MA"
        principalAddress.Zip = "01890"
        principalAddress.Country = "USA"
        principal.Address = principalAddress
        createLegalEntityRequest.Principal = principal

        return createLegalEntityRequest

def sampleBoardingCreateSubMerchant() :
        createSubMerchantRequest = Boarding.CreateSubMerchant("82915251623280808")

        merchant = Merchant();
        merchant.Name = "Merchant Name"
        merchant.URL = "http://merchantUrl"
        merchant.CustomerServiceNumber = "8407809000"
        merchant.HardCodedBillingDescriptor = "billing Descriptor"
        merchant.MaxTransactionAmount = "8400"
        merchant.CategoryCode = "5074"
        merchant.BankRoutingNumber = "011103093"
        merchant.BankAccountNumber = "84012312415"
        merchant.PSPMerchantID = "123456"
        merchant.SettlementCurrency = "USD"
        merchant.FraudEnabled = "true"
        createSubMerchantRequest.Merchant = merchant

        address = Address();
        address.Address1 = "Street Address 1"
        address.Address2 = "Street Address 2"
        address.City = "City"
        address.State = "MA"
        address.Zip = "01730"
        address.Country = "USA"
        createSubMerchantRequest.Address = address

        primaryContact = PrimaryContact();
        primaryContact.FirstName = "John"
        primaryContact.LastName = "Doe"
        primaryContact.Phone = "9785552222"
        primaryContact.Email = "John.Doe@company.com"
        createSubMerchantRequest.PrimaryContact = primaryContact

        return createSubMerchantRequest

def sampleBoardingRetrieveLegalEntity() :
        retrieveLegalEntityRequest = Boarding.RetrieveLegalEntity("82915251623280808")

        

        return retrieveLegalEntityRequest

def sampleBoardingRetrieveSubMerchant() :
        retrieveSubMerchantRequest = Boarding.RetrieveSubMerchant("82915251623280808", "82915269567038420")

        

        return retrieveSubMerchantRequest

def sampleBoardingUpdateLegalEntity() :
        updateLegalEntityRequest = Boarding.UpdateLegalEntity("82915251623280808")

        address = Address();
        address.Address1 = "Street Address 1"
        address.Address2 = "Street Address 2"
        address.City = "City"
        address.State = "MA"
        address.Zip = "01730"
        address.Country = "USA"
        updateLegalEntityRequest.Address = address

        return updateLegalEntityRequest

def sampleBoardingUpdateSubMerchant() :
        updateSubMerchantRequest = Boarding.UpdateSubMerchant("82915251623280808", "82915269567038420")

        merchant = Merchant();
        merchant.FraudEnabled = "true"
        updateSubMerchantRequest.Merchant = merchant

        return updateSubMerchantRequest