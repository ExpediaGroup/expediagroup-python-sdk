[index](index.md) / [expediagroup.sdk.fraudpreventionv2.model](expediagroup.sdk.fraudpreventionv2.model.md) / [LoginTransactionDetails](LoginTransactionDetails.md)
# class `expediagroup.sdk.fraudpreventionv2.model.LoginTransactionDetails`
```
LoginTransactionDetails(
    authentication_type: AuthenticationType,
    authentication_sub_type: Optional[AuthenticationSubType],
    successful_login_flag: bool,
    failed_login_reason: Optional[FailedLoginReason],
    type: Literal["LOGIN"],
)
```

pydantic model LoginTransactionDetails



## Attributes
    
    
        
    
        
    
        
    
        
    
        
    

|           Name          |                             Type                            | Required |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|-------------------------|-------------------------------------------------------------|----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| authentication_sub_type | Optional[[AuthenticationSubType](AuthenticationSubType.md)] |  False   | The sub type of login authentication method used by a user.<br/>For `authentication_sub_type` ensure attributes mentioned in dictionary below are set to corresponding values only.<br/>`authentication_sub_type` is an enum value with the following mapping with `authentication_type` attribute:<br/>*       authentication_sub_type   :     authentication_type<br/>* -------------------------------------------------------------------------------<br/>* `EMAIL`                               : `CREDENTIALS`<br/>* `EMAIL`                               : `PASSWORD_RESET`<br/>* `EMAIL`                               : `SINGLE_SIGN_ON`<br/>* `EMAIL`                               : `MULTI_FACTOR_AUTHENTICATION`<br/>* `PHONE`                               : `MULTI_FACTOR_AUTHENTICATION`<br/>* `GOOGLE`                              : `SOCIAL`<br/>* `FACEBOOK`                            : `SOCIAL`<br/>* `APPLE`                               : `SOCIAL`<br/>*                                       : `CREDENTIALS` |
|   authentication_type   |         [AuthenticationType](AuthenticationType.md)         |   True   |                                           The type of login authentication method used by a user.<br/>For `authentication_type` ensure attributes mentioned in dictionary below are set to corresponding values only.<br/>`authentication_type` is an enum value with the following mapping with `authentication_sub_type` attribute:<br/>*       authentication_type       :     authentication_sub_type<br/>* -------------------------------------------------------------------------------<br/>* `CREDENTIALS`                         : `EMAIL`<br/>* `CREDENTIALS`                         :<br/>* `PASSWORD_RESET`                      : `EMAIL`<br/>* `SINGLE_SIGN_ON`                      : `EMAIL`<br/>* `MULTI_FACTOR_AUTHENTICATION`         : `EMAIL`<br/>* `MULTI_FACTOR_AUTHENTICATION`         : `PHONE`<br/>* `SOCIAL`                              : `GOOGLE`<br/>* `SOCIAL`                              : `FACEBOOK`<br/>* `SOCIAL`                              : `APPLE`                                            |
|   failed_login_reason   |     Optional[[FailedLoginReason](FailedLoginReason.md)]     |  False   |                                                                                                                                                                                                     The reason for the failed login attempt in the Partner''s system, related to user failure or Partner''s system failure.<br/>- `INVALID_CREDENTIALS` - Applicable if the user provided invalid login credentials for this login attempt.<br/>- `ACCOUNT_NOT_FOUND` - Applicable if the user attempted to login to an account that doesn't exist.<br/>- `VERIFICATION_FAILED` - Applicable if the user failed the verification for this login, or any authentication exception occured in the Partner system for this login attempt.<br/>- `ACCOUNT_LOCKED` - Applicable if the user attempted to login to an account that is locked.                                                                                                                                                                                                      |
|  successful_login_flag  |                             bool                            |   True   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        Identifies if a login attempt by a user was successful or not.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|           type          |                       Literal["LOGIN"]                      |   True   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      The categorized type of account event related to a user's action.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |










# Inheritance
object > [AccountTakeoverTransactionDetailsGeneric](AccountTakeoverTransactionDetailsGeneric.md) > LoginTransactionDetails