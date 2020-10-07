# Pulumi

## Web Server Using Azure Virtual Machine

1. Installing Pulumi on Linux
> curl -fsSL https://get.pulumi.com | sh

2. Configuring Azure (this assumes you aleady have the Azure CLI installed)
> az login

3. Move to the configuration's folder

> cd azure-py-webserver-stack

4. Create a new stack

> pulumi stack init azure-py-webserver

5. Set the environment in the configuration:

> pulumi config set environment public

6. Specify the location:

> pulumi config set location EastUS

7. Set the username and password

> pulumi config set username a10o

> pulumi config set --secret password PulumiPulumi10#

8. Preview and Deploy the changes

> pulumi up

**Note**: You will see an IP address in the output where the web server will be available.

9. [Optional] Destroy the resources previously created

> pulumi destroy

