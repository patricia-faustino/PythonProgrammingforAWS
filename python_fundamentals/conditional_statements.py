"""Determine the appropriate AWS service based on the user's requirement"""
def main():
    # Define the user's requirement: file_storage, serveless_computing, virtual_server, other
    user_requirement = 'serveless_computing'

    # If none of the above conditions match, seth the service as 'Unknown'
    if user_requirement == 'file_storage':
        aws_service = 'S3'
    elif user_requirement == 'virtual_server':
        aws_service = 'EC2'
    elif user_requirement == 'serveless_computing':
        aws_service = 'Lambda'
    else:
        aws_service = 'Unknown'

    # Print the recommended AWS service based on the user's requirement
    if user_requirement != 'Unknown':
        print(f"The AWS service required is {aws_service}")
    else:
        print(f"Errot: The AWS service is {aws_service}")

    # Check if the service is not 'Unknown'
    print("Unknown service")

if __name__ == '__main__':
    main()