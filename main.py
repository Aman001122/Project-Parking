from parking_system import ParkingLot

def display_menu():
    print("\n" + "="*50)
    print("🚗 SMART PARKING MANAGEMENT SYSTEM 🚗")
    print("="*50)
    print("1. Park Vehicle (Entry)")
    print("2. Exit Vehicle")
    print("3. View Available Slots")
    print("4. View All Parked Vehicles")
    print("5. Daily Revenue Report")
    print("6. Exit System")
    print("="*50)

def main():
    parking_lot = ParkingLot(total_slots=20)
    
    while True:
        display_menu()
        
        choice = input("\nEnter your choice (1-6): ")
        
        if choice == '1':
            parking_lot.park_vehicle()
        
        elif choice == '2':
            parking_lot.exit_vehicle()
        
        elif choice == '3':
            parking_lot.show_available_slots()
        
        elif choice == '4':
            parking_lot.show_parked_vehicles()
        
        elif choice == '5':
            parking_lot.show_revenue_report()
        
        elif choice == '6':
            print("\n✅ Thank you for using Smart Parking System!")
            print(f"💰 Total Revenue Today: ₹{parking_lot.total_revenue}")
            break
        
        else:
            print("\n❌ Invalid choice! Please enter 1-6")

if __name__ == "__main__":
    main()