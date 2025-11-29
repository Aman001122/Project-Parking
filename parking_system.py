from datetime import datetime
from billing import calculate_charges

class ParkingLot:
    
    def __init__(self, total_slots=20):
        self.total_slots = total_slots
        self.slots = {}
        self.total_revenue = 0
        self.total_vehicles_today = 0
        self.transactions = []
        
        for slot_num in range(1, total_slots + 1):
            self.slots[slot_num] = None
    
    def find_available_slot(self):
        for slot_num, vehicle_data in self.slots.items():
            if vehicle_data is None:
                return slot_num
        return None
    
    def park_vehicle(self):
        print("\n--- VEHICLE ENTRY ---")
        
        slot_num = self.find_available_slot()
        
        if slot_num is None:
            print("❌ Sorry! Parking lot is FULL. No slots available.")
            return
        
        vehicle_number = input("Enter Vehicle Number (e.g., MH01AB1234): ").upper().strip()
        
        if not vehicle_number:
            print("❌ Vehicle number cannot be empty!")
            return
        
        for slot, data in self.slots.items():
            if data and data['vehicle_number'] == vehicle_number:
                print(f"❌ This vehicle is already parked in Slot {slot}!")
                return
        
        print("\nVehicle Types:")
        print("1. Bike/Scooter")
        print("2. Car/SUV")
        print("3. Electric Vehicle (EV)")
        print("4. Heavy Vehicle (Truck/Bus)")
        
        vehicle_type_choice = input("Select vehicle type (1-4): ")
        
        vehicle_types = {
            '1': 'Bike',
            '2': 'Car',
            '3': 'EV',
            '4': 'Heavy Vehicle'
        }
        
        vehicle_type = vehicle_types.get(vehicle_type_choice, 'Car')
        
        entry_time = datetime.now()
        
        self.slots[slot_num] = {
            'vehicle_number': vehicle_number,
            'vehicle_type': vehicle_type,
            'entry_time': entry_time
        }
        
        self.total_vehicles_today += 1
        
        print(f"\n✅ Vehicle Parked Successfully!")
        print(f"📍 Slot Number: {slot_num}")
        print(f"🚗 Vehicle: {vehicle_number}")
        print(f"🏷️  Type: {vehicle_type}")
        print(f"🕒 Entry Time: {entry_time.strftime('%I:%M %p, %d-%b-%Y')}")
    
    def exit_vehicle(self):
        print("\n--- VEHICLE EXIT ---")
        
        vehicle_number = input("Enter Vehicle Number to exit: ").upper().strip()
        
        slot_num = None
        vehicle_data = None
        
        for slot, data in self.slots.items():
            if data and data['vehicle_number'] == vehicle_number:
                slot_num = slot
                vehicle_data = data
                break
        
        if slot_num is None or vehicle_data is None:
            print(f"❌ Vehicle {vehicle_number} not found in parking lot!")
            return
        
        exit_time = datetime.now()
        entry_time = vehicle_data['entry_time']
        vehicle_type = vehicle_data['vehicle_type']
        
        duration = exit_time - entry_time
        hours_parked = duration.total_seconds() / 3600
        
        charges = calculate_charges(vehicle_type, hours_parked)
        
        print("\n" + "="*50)
        print("📄 PARKING BILL")
        print("="*50)
        print(f"Vehicle Number: {vehicle_number}")
        print(f"Vehicle Type: {vehicle_type}")
        print(f"Slot Number: {slot_num}")
        print(f"Entry Time: {entry_time.strftime('%I:%M %p, %d-%b-%Y')}")
        print(f"Exit Time: {exit_time.strftime('%I:%M %p, %d-%b-%Y')}")
        print(f"Duration: {hours_parked:.2f} hours")
        print(f"💰 Total Charges: ₹{charges:.2f}")
        print("="*50)
        
        self.total_revenue += charges
        
        self.transactions.append({
            'vehicle_number': vehicle_number,
            'vehicle_type': vehicle_type,
            'slot': slot_num,
            'entry_time': entry_time,
            'exit_time': exit_time,
            'duration_hours': hours_parked,
            'charges': charges
        })
        
        self.slots[slot_num] = None
        
        print(f"\n✅ Slot {slot_num} is now available!")
    
    def show_available_slots(self):
        print("\n--- AVAILABLE SLOTS ---")
        
        available_slots = [slot for slot, data in self.slots.items() if data is None]
        
        if available_slots:
            print(f"✅ Available Slots: {len(available_slots)}/{self.total_slots}")
            print(f"Slot Numbers: {', '.join(map(str, available_slots))}")
        else:
            print("❌ No slots available! Parking is FULL.")
    
    def show_parked_vehicles(self):
        print("\n--- CURRENTLY PARKED VEHICLES ---")
        
        parked_count = 0
        
        for slot_num, data in self.slots.items():
            if data:
                parked_count += 1
                entry_time = data['entry_time']
                duration = datetime.now() - entry_time
                hours = duration.total_seconds() / 3600
                
                print(f"\nSlot {slot_num}:")
                print(f"  🚗 Vehicle: {data['vehicle_number']}")
                print(f"  🏷️  Type: {data['vehicle_type']}")
                print(f"  🕒 Parked since: {entry_time.strftime('%I:%M %p')}")
                print(f"  ⏱️  Duration: {hours:.2f} hours")
        
        if parked_count == 0:
            print("ℹ️  No vehicles currently parked.")
        else:
            print(f"\nTotal Parked: {parked_count}/{self.total_slots} slots occupied")
    
    def show_revenue_report(self):
        print("\n" + "="*50)
        print("📊 DAILY REVENUE REPORT")
        print("="*50)
        print(f"📅 Date: {datetime.now().strftime('%d %B %Y')}")
        print(f"🚗 Total Vehicles Today: {self.total_vehicles_today}")
        print(f"💰 Total Revenue: ₹{self.total_revenue:.2f}")
        print(f"📍 Slots Occupied: {sum(1 for data in self.slots.values() if data)}/{self.total_slots}")
        print(f"📍 Slots Available: {sum(1 for data in self.slots.values() if data is None)}/{self.total_slots}")
        
        if self.transactions:
            print(f"\n📝 Total Completed Transactions: {len(self.transactions)}")
            avg_revenue = self.total_revenue / len(self.transactions)
            print(f"📈 Average Revenue per Vehicle: ₹{avg_revenue:.2f}")
        
        print("="*50)