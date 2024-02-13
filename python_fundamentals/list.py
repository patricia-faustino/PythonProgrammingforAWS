"""Create a lis of AWS service and modify the list appropriately"""


def main():
    # Create a list of AWS Servcices
    aws_services = ['S3', 'Lambda', 'RDS', 'EC2', 'DynamoDB']
    print(f"AWS services list: {aws_services}")

    # Access the first service in the list
    first_service = aws_services[0]
    print(f"First service: {first_service}")

    # Access the last service in the list
    last_service = aws_services[-1]
    print(f"Last service (before modification): {last_service}")

    # Modify the last service in the list
    aws_services[-1] = 'SNS'
    print(f"AWS service list: {aws_services}")

    # Add a new service to the list
    aws_services.append('SQS')
    print(f"AWS service list: {aws_services}")

    # Remove the second service from the list
    aws_services.pop(1)
    print(f"AWS service list: {aws_services}")

    # Slice the list to get services from index 1 to 3 (inclusive of 1 an exclusive of 3)
    sliced_services = aws_services[1:3]
    print(f"Sliced services: {sliced_services}")

    # Find the length of the list
    list_length = len(aws_services)
    print(f"Length of the AWS services list: {list_length}")


if __name__ == '__main__':
    main()
