from replit import db

#Вставляем данные компьютеров в Replit DB



def insert_computer_information_data():
    computer_information_data = [{
        'computer_name': 'acer_aspire_5',
        'cpu': 'intel_core_i5',
        'ram': '8_gb',
        'gpu': 'ryzon_5_5600_x',
        'operating_system': 'windows_10',
        'price': '100000'
    }, {
        'computer_name': 'apple_macbook_pro',
        'cpu': 'intel_core_i5',
        'ram': '16_gb',
        'gpu': '-',
        'operating_system': 'mac_os',
        'price': '150000'
    }, {
        'computer_name': 'dell_xps_tower',
        'cpu': 'intel_core_i9',
        'ram': '32_gb',
        'gpu': 'nvidia_geforce_rtx_3080',
        'operating_system': 'windows_10',
        'price': '120000'
    }, {
        'computer_name': 'lenovo_thinkpad_x1_carbon',
        'cpu': 'intel_core_i7',
        'ram': '16_gb',
        'gpu': '-',
        'operating_system': 'windows_10_pro',
        'price': '70000'
    }, {
        'computer_name': 'asus_rog_strix_g15',
        'cpu': 'amd_ryzen_9',
        'ram': '16_gb',
        'gpu': 'nvidia_geforce_rtx_3070',
        'operating_system': 'windows_10',
        'price': '110000'
    }, {
        'computer_name': 'hp_pavilion_gaming_desktop',
        'cpu': 'amd_ryzen_7',
        'ram': '16_gb',
        'gpu': 'nvidia_geforce_rtx_3070',
        'operating_system': 'windows_10',
        'price': '95000'
    }, {
        'computer_name': 'msi_creator_z16',
        'cpu': 'intel_core_i9',
        'ram': '32_gb',
        'gpu': 'nvidia_geforce_rtx_3060',
        'operating_system': 'windows_11',
        'price': '100000'
    }, {
        'computer_name': 'razer_blade_stealth_13',
        'cpu': 'intel_core_i7',
        'ram': '16_gb',
        'gpu': 'nvidia_geforce_gtx_1650_ti',
        'operating_system': 'windows_10',
        'price': '50000'
    }, {
        'computer_name': 'alienware_aurora_r12',
        'cpu': 'intel_core_i7',
        'ram': '16_gb',
        'gpu': 'nvidia_geforce_rtx_3060_ti',
        'operating_system': 'windows_10',
        'price': '200000'
    }, {
        'computer_name': 'microsoft_surface_studio',
        'cpu': 'amd_ryzen_9',
        'ram': '16_gb',
        'gpu': '-',
        'operating_system': 'windows_10',
        'price': '60000'
    }]

    # db insertion logic here
    for idx, computer in enumerate(computer_information_data):
        if db is not None:
            db[f"computer_{idx}"] = computer

    return computer_information_data

        
#Получаем данные по компьютерам из Replit DB
def get_computer_information():
    computer_information_data = []
    if db is not None:
        for key in db.keys():
            if key.startswith("computer_"):
                computer_information_data.append(db[key])
    return computer_information_data


#Вставляем данные компьютеров в Replit DB
insert_computer_information_data()

#Получаем и выводим данные по компьютерам из Replit DB
print(get_computer_information())
