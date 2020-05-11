def extract_info(hospital_list):
    result = []
    for hospital in hospital_list:
        hospital_city = hospital.select_one('tr > td:nth-child(2)').string
        hospital_district = hospital.select_one('tr > td:nth-child(3)').string
        hospital_name =  hospital.select_one('tr > td:nth-child(4)').text
        parsed_hname = ''
        if '*' in hospital_name : 
            parsed_hname = hospital_name.split('\t')[0]
            # print(idx)
            # p = hospital_name.split()[:idx][0]
        # p = hospital_name[0,str(hospital_name).find('*')]

        hospital_telephone = hospital.select_one('tr > td:nth-child(5)').string

        hospital_info = {
            "district" : hospital_city,
            "city" : hospital_district,
            "name" : parsed_hname,
            "telephone" : hospital_telephone,
        }
        result.append(hospital_info)
    
    print(result)
    return result

        # 이제부터 시도, 시군구, 선별진료소(이름), 전화번호 크롤링 후 csv 파일에 저장하시면 됩니다!