def calculate_charges(vehicle_type, hours_parked):
    """
    Calculate parking charges based on vehicle type and duration
    Pricing:
    - Bike: ₹10/hour
    - Car: ₹20/hour
    - EV: ₹15/hour (discounted)
    - Heavy Vehicle: ₹40/hour
    
    Special: First 2 hours flat rate, then hourly
    """
    rates = {
        'Bike': 10,
        'Car': 20,
        'EV': 15,
        'Heavy Vehicle': 40
    }
    rate_per_hour = rates.get(vehicle_type, 20) 
    if hours_parked <= 2:
        charges = rate_per_hour * 2
    else:
        base_charge = rate_per_hour * 2
        additional_hours = hours_parked - 2
        additional_charge = additional_hours * rate_per_hour
        charges = base_charge + additional_charge
    if charges < rate_per_hour:
        charges = rate_per_hour
    
    return round(charges, 2)