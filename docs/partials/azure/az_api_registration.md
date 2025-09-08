<!-- AZ CLI being a Microsoft software comes with its own Application ID

- [List of commonly used Microsoft applications ID](https://learn.microsoft.com/en-us/troubleshoot/azure/active-directory/verify-first-party-apps-sign-in#application-ids-of-commonly-used-microsoft-applications)

So in this case we can easily find the required id and add it to our API  
=== "Azure CLI application ID"
    ```
    04b07795-8ddb-461a-bbee-02f9e1bf7b46
    ```

You can then go to the App Registration of your API on your Azure Tenant and go on the `Expose an API` page.

There you can see a button `Add a client application` which will allow you to add the AZ CLI application ID as an authorized client for your api

=== "Correctly set up App Registration"
    ![Post client added screenshot](../assets/app_registration_expose_an_api.png)
Now the API will allow connections from the AZ CLI -->