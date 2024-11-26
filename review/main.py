# Implement a function that removes the email from a string.
# Return an empty string if an empty string is provided or
# if an email without a root is provided. Return -1 if
# an improper data type is provided.
def remove_domain(email: str) -> str:
    """
    A function to remove the email domain from the input string

    Args:
        email (str): the email string
    Returns:
        str: The root of the email without the domain address
    """
    if email != str(email):
        return -1
    elif "@" in email:
        email = email.split("@").pop(0)
        return email
    elif email == '':
        return ''
   

        
    

    
    


# Implement a function that calculates the area of a cube.
# Return -1 if an improper data-type is provided in the args.
# Return -1 if a negative number is provided.
def cube(side: int) -> int:
    ...


# Implement a function which sums the first and the last element
#  of the list together
# Return 0 if the list is empty. Return -1 if an improper data
# type is provided.
def sum_first(nums: list) -> int:
    ...
