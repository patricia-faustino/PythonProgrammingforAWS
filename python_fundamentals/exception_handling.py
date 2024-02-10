""" Exceptions : Runtime errors that disrupt the normal flow of a program"""
"""Why is Exception Handling Important?
* Graceful Error Handling
* Robustness
* Maintaining Program Flow
"""


"""
This script simulates the retrieval of the operational status of various AWS services.

It demonstrates the use of Python exception handling to gracefully handle potential errors
without crashing the script. 

Handles the KeyError: This exception is raised when a key is not found in a dictionary.
""" 


def main():
    service = 'Lambda'
    
    service_status = get_service_status(service)
    
    if service_status:
        print(f"\n{service} service status: '{service_status}'")

        if service_status == "Operational":
            print(f"Performing operation on '{service}'.")
        else:
            print(f"'{service}' is NOT operational.")
    else:
        print(f"\nService status for {service} could not retrieve")

def get_service_status(service_name):
    aws_services_statuses = {
        'EC2': 'Maintenance',
        'S3': 'Operational',
        'Lambda': 'Issues Detected',
        'DynamoDB': 'Operational',
        'RDS': 'Operational'
    }

    try:
        return aws_services_statuses[service_name]
    except KeyError as ke:
        print(f"\nError: {ke}. Status for AWS service {service_name} is not available in our records.")
        return None

if __name__ == '__main__':
    main()