"""Use a list of AWS services and demonstrate various loop operations"""

def main():
    # List of AWS services
    aws_services = ['S3', 'Lambda', 'RDS', 'EC2', 'DynamoDB']
    print(f"AWS services list: {aws_services}")

    # Use a for loop to iteratee through the list
    print(f"\nUsing a for loop to iterate through the list:")

    for service in aws_services:
        print(f"AWS service: {service}")

    # Use a while loop to iterate through the list in reverse order
    print(f"\nUsing a while loop to iterate through the list in reverse order:")

    index = len(aws_services) - 1

    while index >= 0:
        print(f"AWS service: {aws_services[index]}")
        index -= 1

    # Use enumerate() with a for loop to get both index and value
    print(f"\nUsing enumerate() with a for loop to get both index and value:")
    for index, service in enumerate(aws_services):
        print(f"Service # {index + 1}: {service}.")

if __name__ == '__main__':
    main()