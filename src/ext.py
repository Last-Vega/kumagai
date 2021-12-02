import json
f_name = '../data/patent_parsed.json'
json_open = open(f_name, 'r')
json_data = json.load(json_open)

company_dict = {}
for itr in range(len(json_data)):
    itr = str(itr)
    # for company in json_data[itr]['term']:
    #     if company in company_dict:
    #         company_dict[company] += 1
    #     else:
    #         company_dict[company] = 1
    comp = json_data[itr]['createdBy']
    if '株式会社熊谷組' in comp:
        for c in comp:
            if c in company_dict:
                company_dict[c] += 1
            else:
                company_dict[c] = 1


company_list = sorted(company_dict.items(), key=lambda x:x[1], reverse=True)
company_dict.clear()
company_dict.update(company_list)

json_file = open('../data/relatedKumagai.json', 'w')
 
json.dump(company_dict, json_file, indent=2, ensure_ascii=False)
