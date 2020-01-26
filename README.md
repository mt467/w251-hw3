# HW3-Internet of Things 101

##How to set up Jetson TX2
__ Build Docker Images for Face Detection and MQTT__

__Build 

##How to set up ibm cloud server
__Create a new ibm cloud virtual server__

Create a VSI using the gui (using the ssh key imported from HW2)

    Staying in the "Classic" section, navigate to Devices -> Device List
    Select the blue "Order Devices" button at the top right
    Select "Virtual Server" from the list, then "Public Virtual Server"
    Accept the default for Quantity (1) and Billing (Hourly)
    Choose a hostname and domain. You can literally use any domain name you choose, it will not be registered in DNS
    Choose San Jose as a location 
    Select the Compute C1.1x1 profile (2 CPU, 4GB of RAM)
    Select your SSH Key from the dropdown list
    Choose Ubuntu 18.04 Minimal as your Image
    Accept the rest of the defaults
    Read and Accept the Service Agreements (if you agree with them) and click the Create button
    Your Virtual Machine (also called a Virtual Server Instance) will appear in the portal
    
__Create an object storage bucket__
First created a cloud storage object using the default setting via gui, then created "w205-hw3" (please don't mind w205, lol)  bucket inside it following by creating credentials for the bucket. Set the bucket access to public. 

__Mount Object Storage to VSI

__Install Docker on VSI__

__Build and Run a Docker for Image processing__



