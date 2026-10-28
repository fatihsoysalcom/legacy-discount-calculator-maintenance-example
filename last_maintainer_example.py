# This script simulates a "legacy" system function that calculates a customer discount.
# It's designed to illustrate the challenges faced by a "Last Maintainer" due to:
# - Obscure variable names
# - Lack of initial documentation (comments added later by the maintainer)
# - Magic numbers and strings
# - Complex, intertwined business logic that evolved over time
# - Criticality (small changes can have large impacts)

def calculate_legacy_discount(customer_info):
    """
    Calculates a customer's discount percentage based on various, often obscure, rules.
    This function represents a piece of critical legacy code.
    """
    # Initial state: No comments, just code.
    # The comments below are added by "The Last Maintainer" after significant effort
    # to understand the original, undocumented business logic.

    # Initialize base discount. This is the starting point for all customers.
    # (Maintainer's Note: This '5' is a magic number representing a universal 5% base discount.)
    d = 5.0

    # Check for specific customer ID with a special, undocumented bonus.
    # (Maintainer's Note: Customer ID '1001' receives an additional 7% due to an old,
    # possibly forgotten, promotional campaign or a key partner agreement.)
    if customer_info.get('id') == 1001:
        d += 7.0 # Special customer bonus

    # Evaluate loyalty tier bonuses.
    # (Maintainer's Note: These 'GOLD' and 'SILVER' strings are hardcoded tier identifiers.
    # The '10' and '5' are magic numbers for their respective bonus percentages.)
    tier = customer_info.get('loyalty_tier', 'NONE')
    if tier == 'GOLD':
        d += 10.0 # Gold tier bonus
    elif tier == 'SILVER':
        d += 5.0  # Silver tier bonus

    # Apply first purchase bonus if applicable and purchase amount meets a threshold.
    # (Maintainer's Note: The 'True' check and '100' threshold are for a first-time
    # buyer promotion that applies only if their initial purchase exceeds $100.)
    if customer_info.get('is_first_purchase') and customer_info.get('total_purchase') > 100:
        d += 2.0 # First purchase bonus

    # Apply volume discount for high-value purchases.
    # (Maintainer's Note: '500' is the threshold for a bulk purchase discount.
    # The '3' is the additional percentage for this discount.)
    if customer_info.get('total_purchase') > 500:
        d += 3.0 # High volume purchase bonus

    # Cap the maximum possible discount.
    # (Maintainer's Note: The '20.0' is a hardcoded maximum discount percentage
    # to prevent excessive discounts, likely a business rule from years ago.)
    if d > 20.0:
        d = 20.0 # Maximum discount cap

    return d

def main():
    print("--- Legacy Discount Calculator Example ---")
    print("Simulating a critical system function that requires maintenance.")
    print("The inline comments represent the effort of a 'Last Maintainer' to decipher this code.\n")

    # Example customer data
    customer1 = {
        'id': 123,
        'loyalty_tier': 'NONE',
        'total_purchase': 75.0,
        'is_first_purchase': True
    }
    customer2 = {
        'id': 456,
        'loyalty_tier': 'GOLD',
        'total_purchase': 600.0,
        'is_first_purchase': False
    }
    customer3 = {
        'id': 1001, # Special customer ID
        'loyalty_tier': 'SILVER',
        'total_purchase': 150.0,
        'is_first_purchase': True
    }
    customer4 = {
        'id': 789,
        'loyalty_tier': 'PLATINUM', # Unknown tier, should not affect discount
        'total_purchase': 1000.0,
        'is_first_purchase': False
    }

    customers = [customer1, customer2, customer3, customer4]

    for i, customer in enumerate(customers):
        print(f"Customer {i+1} (ID: {customer['id']}):")
        print(f"  Loyalty Tier: {customer['loyalty_tier']}")
        print(f"  Total Purchase: ${customer['total_purchase']:.2f}")
        print(f"  First Purchase: {customer['is_first_purchase']}")
        
        discount = calculate_legacy_discount(customer)
        print(f"  Calculated Discount: {discount:.2f}%\n")

if __name__ == "__main__":
    main()
